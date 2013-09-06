# mqtt-randompub

For testing application and tools which are handling [MQTT](http://mqtt.org/) 
messages it's often needed to send continuously messages on random topics to
a broker. `mqtt-randompub` contains options to send a single message, a
specific count of messages, or a constante flow of messages till the tool is
terminated. Configuration files can be used to store lists of topics to create
repeatable test scenarios.

## Prerequisites/Installation

### Get the files
Clone the `mqtt-randompub` [repository](https://github.com/fabaff/mqtt-randompub):
```
git clone git@github.com:fabaff/mqtt-randompub.git
```
or use [pip]() to make an installation.

```
sudo python-pip install mqtt-randompub
```

###Dependencies
`mqtt-randompub` depends on a couple of additional pieces: 

- [mosquitto](http://mosquitto.org/)

```
sudo yum -y install mosquitto
```

## Usage
To run `mqtt-randompub` just type:

```
mqtt-randompub -h
```

in a terminal to see all options. Running without any option will send a
sample message to `test/#` to a broker which listens on **localhost** on
port **1883**.

For local testing run a MQTT broker/server on **localhost**. 

- [mosca](http://mcollina.github.io/mosca/) - A multi-transport MQTT broker
  for node.js
- [mosquitto](http://mosquitto.org/) - An Open Source MQTT v3.1 Broker

and subscribe to the topic `test/#` with a MQTT client. For example:

```
$ mosquitto_sub -h localhost -d -t test/#
```

## License
`mqtt-randompub` licensed under MIT, for more details check LICENSE.
