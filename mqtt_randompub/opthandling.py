# This file is part of mqtt-randompub
#
# Copyright (c) 2013 Fabian Affolter <fabian at affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
import argparse
import ConfigParser

# Credits: Von Welch 
# http://blog.vwelch.com/2011/04/combining-configparser-and-argparse.html
def argparsing():
    """
    Handling command-line options, default values, and options provided by
    confiurations files.
    """
    conf_parser = argparse.ArgumentParser(
	    description = 'This tool send MQTT messages to random topics',
        prog = 'mqtt-randompub',
	    epilog = 'Please report all bugs and comment.',
        formatter_class = argparse.RawDescriptionHelpFormatter,
        add_help = False
        )
    conf_parser.add_argument('-f', '--config',
                             help='configuration file to use')
    args, remaining_argv = conf_parser.parse_known_args()

    if args.config:
        config = ConfigParser.SafeConfigParser()
        config.read([args.config])
        default_mqtt = dict(config.items("MQTT")) 
        default_topic = dict(config.items("Topic"))
        default_payload = dict(config.items("Payload"))
    else:
        default_mqtt = { 'broker' : '127.0.0.1',
                         'port' : '1883',
                         'qos' : '0'
                        }
        default_topic = { 'topic' : 'test',
                          'subtopic1' : ['a', 'b', 'c'],
                          'subtopic2' : [0, 1]
                        }
        default_payload = { 'load' : '#### This is a test message.' }

    parser = argparse.ArgumentParser(parents=[conf_parser])
    parser.set_defaults(**default_mqtt)
    parser.set_defaults(**default_topic)
    parser.set_defaults(**default_payload)
    parser.add_argument('-b', '--broker',
                        help='set the broker')
    parser.add_argument('-p', '--port',
                        help='set the proker port')
    parser.add_argument('-q', '--qos',
                        help='set the QoS of the messages')
    parser.add_argument('-t', '--topic',
                        help='set the main topic')
    parser.add_argument('-s', '--subtopic1',
                        help='set the first subtopic')
    parser.add_argument('-d', '--subtopic2',
                        help='set the second subtopic')
    parser.add_argument('-l', '--load',
                        help='what to use as message payload')
    parser.add_argument('-i', '--interval', default=1.0,
                        help='time in seconds between the messages')
    parser.add_argument('-n', '--number', default=1,
                        help='number of messages to send. set to 0 for running')
    parser.add_argument('-r', '--random', default=False, action='store_true',
                        help='generate random messages on the topic test/*')
    parser.add_argument('-w', '--timestamp', default=False, action='store_true',
                        help='add a timestamp to the payload message')
    parser.add_argument('-c', '--counter', default=False, action='store_true',
                        help='add a counter to the payload message')

    args = parser.parse_args(remaining_argv)
    return args
