import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10
        )
        self.get_logger().info('Sensor Subscriber started')

    def listener_callback(self, msg):
        if msg.data > 60.0:
            self.get_logger().warn(f'High temperature detected: {msg.data}')
        else:
            self.get_logger().info(f'Temperature normal: {msg.data}')

def main():
    rclpy.init()
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
