from setuptools import setup
import os
from glob import glob

package_name = 'sensor_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 👇 THIS LINE IS IMPORTANT
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='priyanshu_aryan',
    maintainer_email='priyanshu_aryan@todo.todo',
    description='ROS2 sensor monitoring package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_pub = sensor_monitor.publisher:main',
            'sensor_sub = sensor_monitor.subscriber:main',
        ],
    },
)

