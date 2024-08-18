from langdetect import detect

def detect_language(text):
    return detect(text)

text = "input transcript"
language = detect_language(text)
print(f"Detected language: {language}")
