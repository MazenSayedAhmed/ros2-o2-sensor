from setuptools import setup

package_name = 'o2_sensor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mazen Sayed Ahmed',
    maintainer_email='mazensayedahmed88@gmail.com',
    description='ROS2 package simulating O2 sensor data',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'o2_sensor_node = o2_sensor_pkg.o2_sensor_node:main',
        ],
    },
)
