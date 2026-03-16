from setuptools import find_packages, setup

package_name = 'vehicle_detector'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Liu Pui Ling',
    maintainer_email='liuliu00562@gmail.com',
    description='ROS 2 Vehicle Detection using YOLOv8',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This is the most important part! It links your code.
            # 這是最重要的部分！它連結了你的程式碼。
            'detector_node = vehicle_detector.detector_node:main'
        ],
    },
)
