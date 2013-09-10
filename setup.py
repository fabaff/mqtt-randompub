# This file is part of mqtt-randompub
#
# Copyright (c) 2013 Fabian Affolter <fabian at affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
from setuptools import setup

if __name__ == '__main__':
    setup(
        name = 'mqtt-randompub',
        version="0.1",
        description = 'Tool for generating MQTT messages on various topics',
        long_description = """For testing application and tools which are \
            handling MQTT (http://mqtt.org/) messages it's often needed to \
            send continuously messages on random topics to a broker. \
            mqtt-randompub contains options to send a single message, a \
            specific count of messages, or a constante flow of messages \
            till the tool is terminated.""",
        author = 'Fabian Affolter',
        author_email = 'fabian@affolter-engineering.ch',
        maintainer = 'Fabian Affolter',
        maintainer_email = 'fabian@affolter-engineering.ch',
        url = 'http://affolter-engineering.ch/mqtt-randompub/',
        license = 'MIT',
        platforms = 'Linux',
        packages = ['mqtt_randompub'],
        entry_points = {
            'console_scripts': ['mqtt-randompub = mqtt_randompub.mqtt_randompub:main']
        },
        include_package_data = True,
        install_requires=['mosquitto'],
        keywords = ['MQTT','System','Messages'],
        classifiers = [
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Intended Audience :: System Administrators',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Topic :: Communications',
                'Topic :: Internet',
                'Topic :: System',
                'Topic :: System :: Networking'
                ],
    )
