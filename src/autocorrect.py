from spellchecker import SpellChecker

class AutoCorrect:
    def __init__(self):
        self.spell = SpellChecker()

    def correct(self, text):
        words = text.split()
        corrected_words = []

        for w in words:
            corrected = self.spell.correction(w)
            if corrected is None:
                corrected = w
            corrected_words.append(corrected)

        return " ".join(corrected_words)