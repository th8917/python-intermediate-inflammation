"""Tests for statistics functions within the Model layer."""
import os
import numpy as np
import numpy.testing as npt
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 92792ba06e9ebf079cce99be7f5868c35d5c1605
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

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
<<<<<<< HEAD
=======
import os
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
>>>>>>> feature-std-dev
=======
>>>>>>> 92792ba06e9ebf079cce99be7f5868c35d5c1605
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

def test_load_from_json(tmpdir):
    from inflammation.models import load_json
    example_path = os.path.join(tmpdir, 'example.json')
    with open(example_path, 'w') as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 92792ba06e9ebf079cce99be7f5868c35d5c1605
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [4, 6, 9]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [4, -1, 9]),
    ])
def test_daily_max(test,expected):
    """Test max function works for zeroes, positive integers,
     mix of positive/negative integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)),np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
        ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [1, 1, 2]),
        ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [-4, -6, 2]),
    ])
def test_daily_min(test, expected):
    """Test min function works for zeroes, positive integers, mix of positive/negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise

    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
<<<<<<< HEAD
=======

@pytest.mark.parametrize('data, expected_standard_deviation', [
    ([0, 0, 0], 0.0),
    ([1.0, 1.0, 1.0], 0),
    ([0.0, 2.0], 1.0)
])
def test_daily_standard_deviation(data, expected_standard_deviation):
    from inflammation.models import s_dev
    result_data = s_dev(data)['standard deviation']
    npt.assert_approx_equal(result_data, expected_standard_deviation)
>>>>>>> feature-std-dev
=======

>>>>>>> 92792ba06e9ebf079cce99be7f5868c35d5c1605
