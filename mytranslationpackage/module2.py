# mytranslationpackage/module2.py
from deep_translator import GoogleTranslator
from langdetect import detect
from langdetect.detector_factory import detect_langs

def TransLate(text: str, src: str, dest: str) -> str:

    try:
        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:

    try:
        detected_languages = detect_langs(text)
        if set == "lang":
            return detected_languages[0].lang
        elif set == "confidence":
            return str(detected_languages[0])
        elif set == "all":
            return ", ".join([str(lang) for lang in detected_languages])
        else:
            return "Invalid 'set' parameter. Use 'lang', 'confidence', or 'all'."
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:

    try:
        detected_languages = detect_langs(lang)
        if detected_languages:
            return detected_languages[0].lang
        else:
            return "Language not detected"
    except Exception as e:
        return str(e)

