import sys
from pathlib import Path
from rosbags.rosbag1 import Reader
from rosbags.rosbag2 import Writer
from rosbags.serde import cdr_to_ros1, ros1_to_cdr

def convert(input_path, output_path):
    """
    Converts a ROS 1 (.bag) file to a ROS 2 (.db3) folder.
    將 ROS 1 (.bag) 文件轉換為 ROS 2 (.db3) 文件夾。
    """
    # Open the ROS 1 bag
    with Reader(input_path) as reader:
        # Create the ROS 2 bag
        with Writer(output_path) as writer:
            # Copy all topics and messages
            # 複製所有主題和消息
            conn_map = {}
            for conn in reader.connections:
                # Map ROS 1 connection to ROS 2 topic
                ext = writer.add_connection(conn.topic, conn.msgtype)
                conn_map[conn.id] = ext

            for conn, timestamp, rawdata in reader.messages():
                # Convert ROS 1 message format to ROS 2 (CDR) format
                # 將消息格式從 ROS 1 轉換為 ROS 2
                msg = ros1_to_cdr(rawdata, conn.msgtype)
                writer.write(conn_map[conn.id], timestamp, msg)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 convert_ros1_to_ros2.py <input.bag> <output_folder>")
    else:
        in_bag = Path(sys.argv[1])
        out_bag = Path(sys.argv[2])
        convert(in_bag, out_bag)
        print(f"Successfully converted {in_bag} to {out_bag}!")
