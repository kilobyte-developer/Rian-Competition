from langdetect import detect

def detect_language(text):
    return detect(text)

text = "AI having a very busy here to talk about let's get started to make our products radically more helpful for a while which generative we are taking the next step using a combination of semantic understanding and generally where you can do much more with a new experience call magic"
language = detect_language(text)
print(f"Detected language: {language}")
