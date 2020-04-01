"""Helper file to setup mqtt-randompub."""
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="mqtt-randompub",
    version="0.2.1",
    description="Tool for generating MQTT messages on various topics",
    long_description=long_description,
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    maintainer="Fabian Affolter",
    maintainer_email="fabian@affolter-engineering.ch",
    url="https://github.com/fabaff/mqtt-randompub/",
    license="MIT",
    platforms="Linux",
    packages=["mqtt_randompub"],
    entry_points={
        "console_scripts": ["mqtt-randompub = mqtt_randompub.mqtt_randompub:main"]
    },
    include_package_data=True,
    install_requires=["paho-mqtt"],
    keywords=["MQTT", "System", "Messages"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: System",
        "Topic :: System :: Networking",
    ],
)
