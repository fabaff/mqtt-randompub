# This file is part of mqtt-randompub
#
# Copyright (c) 2013, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
import random
import time
import sys
import os
import itertools

import mosquitto

import opthandling
import settings

def send(broker, port, qos, number, interval, topic, subtopic1, subtopic2, payload):
    count = 1
    mqttclient = mosquitto.Mosquitto("mqtt-randompub")
    mqttclient.connect(broker, port=int(port))

    if number == 0:
        print 'Messages are published on topic %s/#... -> CTRL + C to shutdown' \
            % topic
        while True:
            complete_topic = generate_topic(topic, subtopic1, subtopic2)
            mqttclient.publish(complete_topic, payload)
            time.sleep(interval)
    elif number == 1:
        complete_topic = generate_topic(topic, subtopic1, subtopic2)
        mqttclient.publish(complete_topic, payload)
    else:
        for x in range(1, number + 1):
            complete_topic = generate_topic(topic, subtopic1, subtopic2)
            mqttclient.publish(complete_topic, (str(count) + payload))
            count = count + 1
            time.sleep(interval)
    mqttclient.disconnect()

def generate_topic(topic, subtopic1, subtopic2):
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
    return random.choice(list)

def str2list(string):
    str_lst = string.split(',')
    for i, s in enumerate(str_lst):
        str_lst[i] = s.strip()
    return str_lst

def main_run(argv=None):
    if argv is None:
        argv = sys.argv

    args = opthandling.argparsing()

    if args.number:
        send(args.broker, args.port, args.qos, int(args.number), 
            float(args.interval), args.topic, args.subtopic1, args.subtopic2, 
            args.load)

def main():
    '''Main program entry point'''
    try:
        sys.exit(main_run(sys.argv))
    except KeyboardInterrupt:
        print 'Interrupted, exiting...'
        sys.exit(1)

if __name__ == '__main__':
    main()
