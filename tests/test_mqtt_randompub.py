"""Tests for mqtt_randompub module."""

import time

from mqtt_randompub.mqtt_randompub import (generate_message,
                                           generate_random_num,
                                           generate_timestamp, generate_topic,
                                           random_subtopic, string2list)


class TestString2List:
    """Tests for string2list."""

    def test_single_item(self):
        """Tests that a single item string is converted to a list with one item."""
        assert string2list("a") == ["a"]

    def test_multiple_items(self):
        """Tests that a comma-separated string is converted to a list of items."""
        assert string2list("a,b,c") == ["a", "b", "c"]

    def test_strips_whitespace(self):
        """Tests that whitespace around items is stripped."""
        assert string2list("a, b, c") == ["a", "b", "c"]

    def test_strips_leading_and_trailing_whitespace(self):
        """Tests that leading and trailing whitespace is stripped."""
        assert string2list("  foo , bar ") == ["foo", "bar"]


class TestRandomSubtopic:
    """Tests for random_subtopic."""

    def test_returns_item_from_list(self):
        """Tests that the returned item is from the provided list."""
        items = ["a", "b", "c"]
        result = random_subtopic(items)
        assert result in items

    def test_single_item_list(self):
        """Tests that if the list has only one item, that item is returned."""
        assert random_subtopic(["only"]) == "only"

    def test_numeric_list(self):
        """Tests that it works with numeric lists."""
        items = [0, 1, 2]
        result = random_subtopic(items)
        assert result in items


class TestGenerateRandomNum:
    """Tests for generate_random_num."""

    def test_returns_integer(self):
        """Tests that the generated random number is an integer."""
        result = generate_random_num()
        assert isinstance(result, int)

    def test_value_in_range(self):
        """Tests that the generated random number is within the expected range."""
        for _ in range(50):
            result = generate_random_num()
            assert 0 <= result < 100


class TestGenerateTimestamp:
    """Tests for generate_timestamp."""

    def test_returns_integer(self):
        """Tests that the generated timestamp is an integer."""
        result = generate_timestamp()
        assert isinstance(result, int)

    def test_close_to_current_time(self):
        """Tests that the generated timestamp is close to the current time."""
        before = int(time.time())
        result = generate_timestamp()
        after = int(time.time())
        assert before <= result <= after


class TestGenerateMessage:
    """Tests for generate_message."""

    def test_random_payload_returns_int(self):
        """Tests that when random flag is set, the generated payload is an integer."""
        result = generate_message(payload=None, timestamp=False, random=True)
        assert isinstance(result, int)
        assert 0 <= result < 100

    def test_string_payload_no_timestamp(self):
        """Tests that a string payload is returned as is when timestamp and random flags are not set."""
        result = generate_message(payload="hello,world", timestamp=False, random=False)
        assert result in ["hello", "world"]

    def test_list_payload_no_timestamp(self):
        """Tests that a list payload returns a random item from the list when timestamp and random flags are not set."""
        result = generate_message(
            payload=["hello", "world"], timestamp=False, random=False
        )
        assert result in ["hello", "world"]

    def test_string_payload_with_timestamp(self):
        """Tests that a string payload is combined with a timestamp when the timestamp flag is set."""
        result = generate_message(payload="hello", timestamp=True, random=False)
        parts = result.split(" ")
        assert len(parts) == 2
        assert parts[0] == "hello"
        assert parts[1].isdigit()

    def test_random_takes_precedence_over_timestamp(self):
        """Tests that when both random and timestamp flags are set, the random payload is returned."""
        result = generate_message(payload="ignored", timestamp=True, random=True)
        assert isinstance(result, int)


class TestGenerateTopic:
    """Tests for generate_topic."""

    def test_string_subtopics(self):
        """Tests that string subtopics are split and a random one is chosen for each."""
        result = generate_topic("home", "room1,room2", "sensor1,sensor2")
        parts = result.split("/")
        assert len(parts) == 3
        assert parts[0] == "home"
        assert parts[1] in ["room1", "room2"]
        assert parts[2] in ["sensor1", "sensor2"]

    def test_list_subtopics(self):
        """Tests that list subtopics are handled correctly and a random one is chosen for each."""
        result = generate_topic("home", ["room1", "room2"], [0, 1])
        parts = result.split("/")
        assert parts[0] == "home"
        assert parts[1] in ["room1", "room2"]
        assert parts[2] in ["0", "1"]

    def test_single_subtopic_values(self):
        """Tests that if subtopics are single values, they are used directly."""
        result = generate_topic("base", "only", "sub")
        assert result == "base/only/sub"

    def test_topic_format(self):
        """Tests that the generated topic has the correct format."""
        result = generate_topic("test", "a,b", "x,y")
        assert result.startswith("test/")
        assert result.count("/") == 2
