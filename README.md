# daily_motivate

A small Python command-line app that selects a motivational quote from `quotes.json`, displays it, and reads it aloud using text-to-speech.

## How it works

- Loads the quote list from `quotes.json` in the current working directory.
- Selects a quote using the current day of the month, cycling through the list with modulo indexing. The same day number will therefore select the same quote each month, unless the quote list changes.
- Prints the date and selected quote, then speaks the quote using [`pyttsx3`](https://pypi.org/project/pyttsx3/).
- Uses the second voice available on the system when possible; otherwise, it uses the first.

## Requirements

- Python 3
- `pyttsx3`
- A supported system text-to-speech engine. The required engine and any additional setup depend on your operating system; see the [pyttsx3 documentation](https://pyttsx3.readthedocs.io/en/latest/).

## Setup

1. Clone or download this repository and open a terminal in the project directory.
2. Install the Python dependency:

   ```bash
   python -m pip install pyttsx3
   ```

3. Run the program from the project directory so it can find `quotes.json`:

   ```bash
   python announcer.py
   ```

The app prints today's date and the selected quote, then plays the spoken quote. Audio playback requires a working system voice engine.

## Project files

- `announcer.py` — loads and selects a quote, then prints and speaks it.
- `quotes.json` — the list of motivational quotes used by the app.
- `LICENSE` — MIT License.

## Customize the quotes

Add, edit, or remove strings in `quotes.json`. Keep the file as a valid JSON array of strings.

## License

This project is distributed under the MIT License. See `LICENSE` for details.
