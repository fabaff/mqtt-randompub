"""Tests for opthandling module."""

import pytest

from mqtt_randompub.opthandling import argparsing


class TestArgparsing:
    """Tests for argparsing."""

    def test_defaults(self):
        args = argparsing([])
        assert args.broker == "127.0.0.1"
        assert args.port == "1883"
        assert args.qos == "0"
        assert args.topic == "test"
        assert args.number == 1
        assert args.interval == 1.0
        assert args.random is False
        assert args.timestamp is False
        assert args.counter is False

    def test_broker_option(self):
        args = argparsing(["-b", "192.168.1.1"])
        assert args.broker == "192.168.1.1"

    def test_port_option(self):
        args = argparsing(["-p", "8883"])
        assert args.port == "8883"

    def test_topic_option(self):
        args = argparsing(["-t", "sensors"])
        assert args.topic == "sensors"

    def test_number_option(self):
        args = argparsing(["-n", "5"])
        assert args.number == "5"

    def test_interval_option(self):
        args = argparsing(["-i", "2.5"])
        assert args.interval == "2.5"

    def test_random_flag(self):
        args = argparsing(["-r"])
        assert args.random is True

    def test_timestamp_flag(self):
        args = argparsing(["-w"])
        assert args.timestamp is True

    def test_counter_flag(self):
        args = argparsing(["-c"])
        assert args.counter is True

    def test_load_option(self):
        args = argparsing(["-l", "test payload"])
        assert args.load == "test payload"

    def test_subtopic1_option(self):
        args = argparsing(["-s", "room1,room2"])
        assert args.subtopic1 == "room1,room2"

    def test_subtopic2_option(self):
        args = argparsing(["-d", "sensor1,sensor2"])
        assert args.subtopic2 == "sensor1,sensor2"

    def test_qos_option(self):
        args = argparsing(["-q", "1"])
        assert args.qos == "1"
