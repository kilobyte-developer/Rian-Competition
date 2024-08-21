from googletrans import Translator

def translate_text(text, target_languages):
    translator = Translator()
    translations = {}
    for lang in target_languages:
        translated = translator.translate(text, dest=lang)
        translations[lang] = translated.text
    return translations

transcript = " AI having a very busy here to talk about let's get started to make our products radically more helpful for a while which generative we are taking the next step using a combination of semantic understanding and generally where you can do much more with a new experience call magic"
target_languages = ['es'] 
translations = translate_text(transcript, target_languages)

for lang, translation in translations.items():
    print(f"Translation in {lang}: {translation}")
