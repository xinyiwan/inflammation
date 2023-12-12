"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_integers():
    """Test that max function works for an array of positive integers."""
    from inflammation.models import daily_max

    test_input = np.array([[0, 0],
                           [0 ,0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [5, 6]),
    ])
def test_daily_max(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(test), expected)


def test_daily_min_integers():
    """Test that min function works for an array of positive integers."""
    from inflammation.models import daily_min

    test_input = np.array([[0, 0],
                           [0 ,0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [-1, -1] ], [-1, -1]),
        ([ [1, 2], [-1, 4], [5, -3] ], [-1, -3]),
    ])
def test_daily_min(test, expected):
    """Test mean function works for array of zeroes, negative integers, and a mix of positive/negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(test), expected)

def test_daily_std():
    """Test std-dev function for zeros"""
    from inflammation.models import daily_std
    
    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    npt.assert_array_equal(daily_std(test_input), test_result)


def test_daily_std_values():
    from inflammation.models import daily_std
"""This is a test function with positive integers for the std-dev function """
    test_input = np.array([[5, 3],
                           [6, 6],
                           [7, 9]])
    test_result = np.array([0.81, 2.44])

    npt.assert_array_almost_equal(daily_std(test_input), test_result, decimal=2)
