# ShadowFox Smart Keyboard

## 🚀 Features
- Autocorrect using pyspellchecker
- Next-word prediction using N-grams
- CLI-based smart keyboard

## 🧠 Tech Stack
- Python
- NLP (N-grams)
- Spell Correction

## ▶️ How to Run
```bash
python app/keyboard_app.py
```

## 📌 Example
Input: i am goin to collge  
Output: i am going to college + suggestions

## 📁 Project Structure
ShadowFox/
│── data/           # Dataset
│── src/            # Core logic (NLP, autocorrect, prediction)
│── app/            # Main app (keyboard interface)
│── README.md
│── requirements.txt

## ⚙️ How It Works
1. User inputs text
2. Autocorrect fixes spelling errors
3. N-gram model predicts next words
4. Top suggestions are displayed

## 🔮 Future Improvements
- Add deep learning model (LSTM/RNN)
- Build web interface using Flask
- Improve dataset for better accuracy
- Add user learning capability