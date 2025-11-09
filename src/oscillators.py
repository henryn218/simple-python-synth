from enum import auto, Enum
import numpy as np


class OscillatorType(Enum):
    SINE = auto()
    SQUARE = auto()


def get_oscillator(oscilllator_num):
    match oscilllator_num:
        case OscillatorType.SINE.value:
            return sine_oscillator
        case OscillatorType.SQUARE.value:
            return square_oscillator
        case _:
            return sine_oscillator


def sine_oscillator(phi):
    return np.sin(phi).astype(np.float32)


def square_oscillator(phi):
    return np.sign(np.sin(phi)).astype(np.float32)
