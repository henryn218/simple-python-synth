from pytest import approx

from src.synth import Synth


def test_synth_map_key_to_frequency():
    synth = Synth()

    assert synth.map_key_to_frequency("z") == approx(130.8149999999999)
    assert synth.map_key_to_frequency("a") is None
    assert synth.map_key_to_frequency("q") == approx(261.63)
    assert synth.map_key_to_frequency("i") == approx(523.2600000000002)
