"""
This file is part of mqtt-randompub

Copyright (c) 2013-2016, Fabian Affolter <fabian@affolter-engineering.ch>
Released under the MIT license. See LICENSE file for details.
"""
import random
import time
import sys
import os
import signal
import itertools

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print('Please install the paho-mqtt module to use mqtt-randompub.')

from mqtt_randompub import opthandling


def send(broker, port, qos, number, interval, topic,
         subtopic1, subtopic2, payload, random, timestamp, counter):
    """Send messages to MQTT broker."""
    count = 1
    mqttclient = mqtt.Client("mqtt-randompub")
    mqttclient.connect(broker, port=int(port))

    if number == 0:
        print('Messages are published on topic %s/#... ',
              '->CTRL + C to shutdown', topic)
        while True:
            complete_topic = generate_topic(topic, subtopic1, subtopic2)
            message = generate_message(payload, timestamp, random)
            if counter:
                mqttclient.publish(complete_topic,
                                   '{} {}'.format(str(count), message))
            else:
                mqttclient.publish(complete_topic, message, random)
            time.sleep(interval)
            count = count + 1
    elif number == 1:
        complete_topic = generate_topic(topic, subtopic1, subtopic2)
        message = generate_message(payload, timestamp, random)
        mqttclient.publish(complete_topic, message)
    else:
        for x in range(1, number + 1):
            complete_topic = generate_topic(topic, subtopic1, subtopic2)
            message = generate_message(payload, timestamp, random)
            if counter:
                mqttclient.publish(complete_topic,
                                   '{} {}'.format(str(count), message))
            else:
                mqttclient.publish(complete_topic, message)
            count = count + 1
            time.sleep(interval)
    mqttclient.disconnect()


def generate_message(payload, timestamp, random):
    """The generator for the messages."""
    if random:
        generated_payload = generate_random_num()
    else:
        if type(payload) != list:
            payload_lst = str2list(payload)
            gen_payload = random_subtopic(payload_lst)
        else:
            gen_payload = random_subtopic(payload)
        if timestamp:
            generated_payload = gen_payload + ' ' + str(generate_timestamp())
        else:
            generated_payload = gen_payload
    return generated_payload


def generate_topic(topic, subtopic1, subtopic2):
    """The generator for the topic."""
    if type(subtopic1) != list:
        stopic1_lst = str2list(subtopic1)
        stopic1 = random_subtopic(stopic1_lst)
    else:
        stopic1 = random_subtopic(subtopic1)
    if type(subtopic2) != list:
        stopic2_lst = str2list(subtopic2)
        stopic2 = random_subtopic(stopic2_lst)
    else:
        stopic2 = random_subtopic(subtopic2)
    generated_topic = topic + '/' + str(stopic1) + '/' + str(stopic2)
    return generated_topic


def random_subtopic(list):
    """Return a random topic."""
    return random.choice(list)


def str2list(string):
    """Return a list of strings."""
    str_lst = string.split(',')
    for i, s in enumerate(str_lst):
        str_lst[i] = s.strip()
    return str_lst


def generate_random_num():
    """Return a random generated number."""
    return random.randrange(0, 100, 1)


def generate_timestamp():
    """Return the current timestamp."""
    timestamp = int(time.time())
    return timestamp


def main(argv=None):
    """Main"""
    if argv is None:
        argv = sys.argv
    args = opthandling.argparsing()

    if args.number:
        send(args.broker, args.port, args.qos, int(args.number),
             float(args.interval), args.topic, args.subtopic1, args.subtopic2,
             args.load, args.random, args.timestamp, args.counter)

if __name__ == '__main__':
    """Main program entry point"""
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        print('Interrupted, exiting...')
        sys.exit(1)
