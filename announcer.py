import pyttsx3
import json
import datetime

with open('quotes.json', 'r') as f:
    quotes = json.load(f)

today = datetime.date.today().day
daily_quote = quotes[today % len(quotes)]
print(f"Today's quote: {datetime.date.today()}")

full_text=f"Here is your daily motivational quote: {daily_quote}"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 1.0)

print(full_text)
engine.say(full_text)
engine.runAndWait()
