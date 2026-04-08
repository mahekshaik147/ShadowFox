import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import get_prediction

print("ShadowFox Keyboard (type 'exit')")

while True:
    text = input("\nYou: ")
    if text == "exit":
        break

    corrected, suggestions = get_prediction(text)

    print("Corrected:", corrected)
    print("Suggestions:")
    
    for word, _ in suggestions:
        print("-", word)