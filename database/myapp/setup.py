#!/usr/bin/env python3
import setuptools
from setuptools.command.develop import develop


class BuildProtos(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from grpc_tools import protoc
        protoc.main((
            '--proto_path=./',
            '--python_out=./src',
            '--grpc_python_out=./src',
            'proto/echo.proto',
        ))



def setup():
    setuptools.setup(
        name="grpc-server",
        packages=setuptools.find_packages(where="src", exclude=("test",)),
        package_dir={"": "src"},
        entry_points={
            'console_scripts': [
                'grpc-server = app:main',
            ]
        },
        cmdclass={
            'build_package_protos': BuildProtos,
            # 'develop': DevelopCmd,
        },
        setup_requires=[
            'grpcio-tools==1.33.1',
        ],
        install_requires=[
            'grpcio==1.33.1',
            'redis==3.5.3',
            'google-api-python-client==1.12.5',
            'protobuf'
        ]
    )


if __name__ == '__main__':
    setup()
