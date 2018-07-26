#
# Author: Muntaser Khan
# test_inverse.py
#
import pytest

# Function to convert km to miles
def km_to_miles(km):
    return km * 0.62137

# Function to convert miles to km
def miles_to_km(miles):
    return miles * 1.60934

# Test conversion of km to miles function
def test_km_to_miles():
    assert round(km_to_miles(miles_to_km(2.3)), 2)  == 2.3

def test_km_to_miles():
    assert round(km_to_miles(miles_to_km(100.0)), 2)  == 100.0

def test_km_to_miles():
    assert round(km_to_miles(miles_to_km(55.8)), 2)  == 55.8

def test_km_to_miles():
    assert round(km_to_miles(miles_to_km(78.6)), 2)  == 78.6

def test_km_to_miles():
    assert round(km_to_miles(miles_to_km(10.4)), 2)  == 10.4

# Test conversion of miles to km function
def test_km_to_miles():
    assert round(miles_to_km(km_to_miles(2.3)), 2)  == 2.3

def test_km_to_miles():
    assert round(miles_to_km(km_to_miles(100.0)), 2)  == 100.0

def test_km_to_miles():
    assert round(miles_to_km(km_to_miles(55.8)), 2)  == 55.8

def test_km_to_miles():
    assert round(miles_to_km(km_to_miles(78.6)), 2)  == 78.6

def test_km_to_miles():
    assert round(miles_to_km(km_to_miles(10.4)), 2)  == 10.4