from setuptools import find_packages, setup

package_name = 'path_planning'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',[
            'launch/jiwon_2D_LiDAR.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cwsfa',
    maintainer_email='wldnjs0488@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'jiwon_2D_LiDAR = path_planning.jiwon_2D_LiDAR_clustering:main',
        ],
    },
)
