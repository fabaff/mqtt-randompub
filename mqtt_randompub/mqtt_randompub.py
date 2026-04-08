"""Main part for sending MQTT messages."""


import random
import signal
import sys
import time
from typing import Any, List, Optional, Union

from mqtt_randompub import opthandling

try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("Please install the paho-mqtt module to use mqtt-randompub")


def send(
    broker: str,
    port: Union[str, int],
    qos: Union[str, int],
    number: int,
    interval: float,
    topic: str,
    subtopic1: Union[str, List[Any]],
    subtopic2: Union[str, List[Any]],
    payload: Union[str, List[Any], None],
    random: bool,
    timestamp: bool,
    counter: bool,
) -> None:
    """Send messages to MQTT broker."""
    count = 1

    mqttclient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "mqtt-randompub")
    mqttclient.connect(broker, port=int(port))

    if number == 0:
        print(f"Messages are published on topic {topic}/#... -> CTRL + C to shutdown")
        while True:
            complete_topic = generate_topic(topic, subtopic1, subtopic2)
            message = generate_message(payload, timestamp, random)
            if counter:
                mqttclient.publish(complete_topic, "{} {}".format(str(count), message))
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
                mqttclient.publish(complete_topic, "{} {}".format(str(count), message))
            else:
                mqttclient.publish(complete_topic, message)
            count = count + 1
            time.sleep(interval)
    print(f"Message sent {count} messages to topic {complete_topic}")
    mqttclient.disconnect()


def generate_message(
    payload: Union[str, List[Any], None],
    timestamp: bool,
    random: bool
) -> Union[str, int]:
    """The generator for the messages."""
    if random:
        generated_payload = generate_random_num()
    else:
        # Always work with a list for random_subtopic
        if isinstance(payload, list):
            payload_lst = payload
        else:
            payload_lst = str2list(payload)
        gen_payload = random_subtopic(payload_lst)
        if timestamp:
            generated_payload = f"{gen_payload} {generate_timestamp()}"
        else:
            generated_payload = gen_payload
    return generated_payload


def generate_topic(
    topic: str,
    subtopic1: Union[str, List[Any]],
    subtopic2: Union[str, List[Any]]
) -> str:
    """The generator for the topic."""
    # Always work with a list for random_subtopic
    if isinstance(subtopic1, list):
        stopic1_lst = subtopic1
    else:
        stopic1_lst = str2list(subtopic1)
    stopic1 = random_subtopic(stopic1_lst)

    if isinstance(subtopic2, list):
        stopic2_lst = subtopic2
    else:
        stopic2_lst = str2list(subtopic2)
    stopic2 = random_subtopic(stopic2_lst)

    generated_topic = f"{topic}/{stopic1}/{stopic2}"
    return generated_topic


def random_subtopic(items: List[Any]) -> Any:
    """Return a random item from a list."""
    return random.choice(items)


def str2list(value: Union[str, List[Any]]) -> List[str]:
    """Return a list of strings, or the input if already a list."""
    if isinstance(value, list):
        return value
    str_lst = value.split(",")
    return [s.strip() for s in str_lst]


def generate_random_num() -> int:
    """Return a random generated number."""
    return random.randrange(0, 100, 1)


def generate_timestamp() -> int:
    """Return the current timestamp."""
    timestamp = int(time.time())
    return timestamp


def main(argv: Optional[List[str]] = None) -> None:
    """Main function for mqtt-randompub."""
    if argv is None:
        argv = sys.argv
    args = opthandling.argparsing()

    if args.number:
        send(
            args.broker,
            args.port,
            args.qos,
            int(args.number),
            float(args.interval),
            args.topic,
            args.subtopic1,
            args.subtopic2,
            args.load,
            args.random,
            args.timestamp,
            args.counter,
        )


if __name__ == "__main__":
    """Main program entry point"""
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        print("Interrupted, exiting...")
        sys.exit(1)
