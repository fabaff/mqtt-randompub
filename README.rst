mqtt-randompub
==============

For testing application and tools which are handling `MQTT`_ messages it's
often needed to send continuously messages on random topics to a broker. 
``mqtt-randompub`` contains options to send a single message, a specific count
of messages, or a constante flow of messages till the tool is terminated.
Configuration files can be used to store lists of topics to create repeatable
test scenarios.

.. _MQTT:http://mqtt.org/ 

Prerequisites/Installation
--------------------------

Get the files
_____________
Clone the `mqtt-randompub` [repository](https://github.com/fabaff/mqtt-randompub):

    git clone git@github.com:fabaff/mqtt-randompub.git

or use `pip`_ to make an installation.

    sudo python-pip install mqtt-randompub

.. _pip: https://pypi.python.org/pypi/mqtt-randompub

Dependencies
____________
``mqtt-randompub`` depends on a couple of additional pieces: 

- [Python](http://www.python.org)
- [mosquitto](http://mosquitto.org/)

On a Fedora system::

    sudo yum -y install mosquitto-python

On Debian and perhaps its downstream Ubuntu (not tested)::

    sudo apt-get install python-mosquitto_pub

Usage
-----
To run ``mqtt-randompub`` just type::

    $ mqtt-randompub -h
    usage: mqtt-randompub [-h] [-c CONFIG] [-b BROKER] [-p PORT] [-q QOS]
                          [-t TOPIC] [-s SUBTOPIC1] [-d SUBTOPIC2] [-l LOAD]
                          [-i INTERVAL] [-n NUMBER]

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            configuration file to use
      -b BROKER, --broker BROKER
                            set the broker
      -p PORT, --port PORT  set the proker port
      -q QOS, --qos QOS     set the QoS of the messages
      -t TOPIC, --topic TOPIC
                            set the main topic
      -s SUBTOPIC1, --subtopic1 SUBTOPIC1
                            set the first subtopic
      -d SUBTOPIC2, --subtopic2 SUBTOPIC2
                            set the second subtopic
      -l LOAD, --load LOAD  what to use as message payload
      -i INTERVAL, --interval INTERVAL
                            time in seconds between the messages
      -n NUMBER, --number NUMBER
                            number of messages to send. set to 0 for running


in a terminal to see all options. Running without any option will send a
sample message to ``test/#`` to a broker which listens on **localhost** on
port **1883**.

For local testing run a MQTT broker/server on **localhost**. 

- `mosca`_ - A multi-transport MQTT broker
  for node.js
- `mosquitto`_ - An Open Source MQTT v3.1 Broker

and subscribe to the topic ``test/#`` with a MQTT client. For example::

    mosquitto_sub -h localhost -d -t test/#

You can run ``mqtt-randompub`` with a configuration file to re-use a previous
set of topics. Check the `mqtt-randompub.example`_ file for details.

.. _mosca: http://mcollina.github.io/mosca/
.. _mosquitto: http://mosquitto.org/
.. _mqtt-randompub.example: https://github.com/fabaff/mqtt-randompub/blob/master/mqtt-randompub.example

License
-------
``mqtt-randompub`` licensed under MIT, for more details check LICENSE.
