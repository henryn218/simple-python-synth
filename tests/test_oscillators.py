import numpy as np

from pytest import approx
from src.oscillators import sine_oscillator, square_oscillator, sawtooth_oscillator


def test_sin_oscillator():

    expected = np.array([0.0, 0.84147096, 0.9092974, 0.14112], dtype=np.float32)
    output = sine_oscillator(np.array([0.0, 1.0, 2.0, 3.0]))

    assert isinstance(output, np.ndarray)
    assert len(output) == 4
    assert np.all(output <= 1.0)
    assert np.all(output >= -1.0)
    assert output == approx(expected)


def test_square_oscillator():

    expected = np.array([0.0, 1.0, 1.0, 1.0], dtype=np.float32)
    output = square_oscillator(np.array([0.0, 1.0, 2.0, 3.0]))

    assert isinstance(output, np.ndarray)
    assert len(output) == 4
    assert np.all(output <= 1.0)
    assert np.all(output >= -1.0)
    assert output == approx(expected)


def test_sawtooth_oscillator():

    expected = np.array([-1.0, -0.6816901, -0.36338022, -0.04507034], dtype=np.float32)
    output = sawtooth_oscillator(np.array([0.0, 1.0, 2.0, 3.0]))

    assert isinstance(output, np.ndarray)
    assert len(output) == 4
    assert np.all(output <= 1.0)
    assert np.all(output >= -1.0)
    assert output == approx(expected)
