# Simple python synth

This simple synthesiser allows you to play sine or square wave tones using your computer keyboard.

## Configuration, set up and running the project

After cloning the project you can optionally set up a virtual environment: 
```
python3 -m venv .venv
source .venv/bin/activate
```

The project requires several dependencies, which you can install with:
```
pip install -r requirements.txt
```

To run the project, run the `main.py` file at the command line:
```
python src/main.py
```
Press the Esc key to exit. Note you won't be able to use your keyboard while the synthesiser is running.

At the moment only 2 oscillators have been implemented, one for sine waves and the other square waves. Follow the prompts to select which you want to use when you run the program.

## Playing notes

The `q` and `,` keys play the note C4 (261.63 Hz) (middle C).

The keys are laid out like a piano keyboard and cover 2 octaves. `w` corresponds to the D above middle C, `e` to E, `r` to F, `t` to G, `y` to A, `u` to B and `i` to C an octave above middle C. For sharps and flats, `2` corresponds to C# / Db, `3` to D# / Eb, `5` to F# / Gb, `6` to G# / Ab and `7` to A# / Bb. The same layout applies for the octave below, with the C an octave below middle C mapped to the `z` key.