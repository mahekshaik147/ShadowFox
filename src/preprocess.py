def load_data(path):
    with open(path, 'r') as f:
        text = f.read().lower()
    return text.split()