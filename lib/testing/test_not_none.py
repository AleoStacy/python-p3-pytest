# lib/testing/test_not_none.py

from not_none_functions import some_function

def test_some_function():
    assert some_function() is not None  # Test that the function does not return None
