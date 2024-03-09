from custom import CustomCollection
from custom_data import CustomData
from decorators import timer
import time

def test_custom_collection():
    collection = CustomCollection([1, 2, 3])
    assert list(collection) == [1, 2, 3]

def test_custom_data_equality():
    data1 = CustomData(5)
    data2 = CustomData(5)
    assert data1 == data2

def test_custom_data_truthy():
    data = CustomData(0)
    assert not data

def test_timer_decorator():
    @timer
    def wait():
        time.sleep(0.1)
    # Since `timer` prints the duration, there's no return value to assert.
    # This test ensures the decorator doesn't break the function.
    wait()
