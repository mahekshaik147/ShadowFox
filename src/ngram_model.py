from collections import defaultdict, Counter

class NGramModel:
    def __init__(self, n=3):
        self.n = n
        self.model = defaultdict(Counter)

    def train(self, tokens):
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i+self.n-1])
            next_word = tokens[i+self.n-1]
            self.model[context][next_word] += 1

    def predict(self, text):
        words = text.split()
        context = tuple(words[-(self.n-1):])

        if context in self.model:
            return self.model[context].most_common(3)
        return []