
import pytest
from ride_share_fare import extra_distance_fare, seats_and_bags_ok, pickup_status


# EXTRA DISTANCE FARE TESTS

def test_invalid_cab():
    with pytest.raises(ValueError):
        extra_distance_fare("bike", 10, "city", False)


def test_negative_distance():
    with pytest.raises(ValueError):
        extra_distance_fare("mini", -5, "city", False)


def test_within_included_distance():
    assert extra_distance_fare("sedan", 5, "city", False) == 0


def test_subscriber_extra_distance():
    assert extra_distance_fare("mini", 10, "city", True) == 24


def test_suv_subscriber():
    assert extra_distance_fare("suv", 15, "city", True) == 36


def test_non_city_zone():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_large_extra_distance_city():
    assert extra_distance_fare("mini", 30, "city", False) == 500


def test_large_extra_distance_outstation():
    assert extra_distance_fare("sedan", 35, "outstation", False) == 810


# SEATS AND BAGS TESTS

def test_wheelchair_with_valid_passengers():
    assert seats_and_bags_ok(2, 3, True) is True


def test_wheelchair_with_excess_passengers():
    assert seats_and_bags_ok(3, 1, True) is False


def test_excess_passengers_without_wheelchair():
    assert seats_and_bags_ok(5, 1, False) is False


def test_valid_passengers_and_bags():
    assert seats_and_bags_ok(4, 2, False) is True


def test_excess_bags():
    assert seats_and_bags_ok(3, 3, False) is False


# PICKUP STATUS TESTS

def test_scheduled_airport_on_time():
    assert pickup_status(20, True, True) == "on_time"


def test_non_scheduled_non_airport_on_time():
    assert pickup_status(5, False, False) == "on_time"


def test_delayed_pickup():
    assert pickup_status(10, True, True) == "delayed"


def test_missed_pickup():
    assert pickup_status(4, True, True) == "missed"
