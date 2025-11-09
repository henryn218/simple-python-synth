from synth import Synth


def main():
    print(
        "\n",
        "This simple synthesiser allows you to play sine or square wave tones using your computer keyboard.\n",
        "The z key plays the note C4 (261.63 Hz), otherwise known as middle C.\n",
        "The keys are laid out like a piano keyboard:\n",
        "s x d c v g b h n j m , l . ; / each play a semitone step up from the previous note.\n",
        "\nPress the Esc key to exit. Note you won't be able to use your keyboard while the synthesiser is running.\n",
    )

    oscillator_choice = input(
        "Choose an oscillator type by typing a number then press Enter to start...\n"
        "1. Sine Oscillator (default)\n"
        "2. Square Oscillator\n"
    )

    while oscillator_choice not in ("1", "2"):
        oscillator_choice = input("Please type 1 or 2 then press Enter: ")

    print("\nStarting synthesiser...\n")

    synth = Synth(int(oscillator_choice))
    synth.start()
    synth.stop()


if __name__ == "__main__":
    main()
