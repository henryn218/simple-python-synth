import sys

import numpy as np
import sounddevice as sd
from pynput import keyboard

from oscillators import get_oscillator


class Synth:
    voices = {}
    amplitude = 0.2
    ref_frequency = 261.63  # set to middle C
    note_ratio = 2 ** (1 / 12)
    output_devices = sd.query_devices(None, "output")
    sample_rate = output_devices.get("default_samplerate")

    def __init__(self, oscillator_choice=None):
        self.oscillator = get_oscillator(oscillator_choice)
        self.output_stream = sd.OutputStream(
            device=None,
            channels=1,
            callback=self.audio_callback,
            samplerate=self.sample_rate,
        )

    def start(self):
        self.output_stream.start()
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release, suppress=True
        ) as listener:
            listener.join()

    def stop(self):
        self.output_stream.stop()
        self.output_stream.close()

    def map_key_to_frequency(self, key):
        key_n_map = {
            "z": -12,
            "s": -11,
            "x": -10,
            "d": -9,
            "c": -8,
            "v": -7,
            "g": -6,
            "b": -5,
            "h": -4,
            "n": -3,
            "j": -2,
            "m": -1,
            ",": 0,
            "q": 0,
            "2": 1,
            "w": 2,
            "3": 3,
            "e": 4,
            "r": 5,
            "5": 6,
            "t": 7,
            "6": 8,
            "y": 9,
            "7": 10,
            "u": 11,
            "i": 12,
        }
        n = key_n_map.get(key, None)
        if n is not None:
            return self.ref_frequency * (self.note_ratio**n)

    def audio_callback(self, outdata, frames, time, status):
        if status:
            print(status, file=sys.stderr)

        t = np.arange(frames) / self.sample_rate
        out = np.zeros(frames, dtype=np.float32)

        current_voices = {k: v.copy() for k, v in self.voices.items()}

        if not current_voices:
            outdata[:] = out.reshape(-1, 1)
            return

        for v in current_voices.values():
            freq = v["freq"]
            phase = v["phase"]
            omega = 2 * np.pi * freq
            phi = phase + omega * t
            out += self.oscillator(phi)
            new_phase = (phase + omega * frames / self.sample_rate) % (2 * np.pi)
            v["phase"] = new_phase

        n_voices = max(1, len(current_voices))
        out = (self.amplitude / n_voices) * out
        outdata[:] = out.reshape(-1, 1)

        for k in current_voices:
            try:
                self.voices[k]["phase"] = current_voices[k]["phase"]
            except KeyError:
                pass

    def on_press(self, key: keyboard.Key | keyboard.KeyCode | None) -> None:
        try:
            if isinstance(key, keyboard.KeyCode):
                freq = self.map_key_to_frequency(key.char)
                if freq is None:
                    return
                if key.char in self.voices:
                    return
                self.voices[key.char] = {
                    "freq": freq,
                    "phase": 0.0,
                }
        except AttributeError:
            pass

    def on_release(self, key: keyboard.Key | keyboard.KeyCode | None) -> None:
        try:
            if isinstance(key, keyboard.KeyCode):
                if key.char in self.voices:
                    del self.voices[key.char]
        except AttributeError:
            pass

        if key == keyboard.Key.esc:
            print("Exiting...")
            sys.exit()


if __name__ == "__main__":
    pass
