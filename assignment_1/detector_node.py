import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
from ultralytics import YOLO

class VehicleDetector(Node):
    def __init__(self):
        super().__init__('vehicle_detector_node')
        self.get_logger().info('AI is starting... (AI 啟動中...)')
        
        # Load YOLO model
        self.model = YOLO('yolov8n.pt') 
        
        # Subscribe to teacher's camera channel
        self.subscription = self.create_subscription(
            CompressedImage,
            '/hikcamera/image_2/compressed',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # We use a logger to see if images are coming in
        self.get_logger().info('I see an image! (我看到圖片了！)')
        
        # Decode the compressed image
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if cv_image is not None:
            # Run AI detection
            results = self.model(cv_image)
            annotated_frame = results[0].plot()

            # Show window
            cv2.imshow("Detection Result", annotated_frame)
            cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = VehicleDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()