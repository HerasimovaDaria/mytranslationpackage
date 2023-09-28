# mytranslationpackage/module1.py
from googletrans import Translator
from langdetect import detect
from langdetect import detect_langs

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = Translator()
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_languages = detect_langs(text)
        if set == "lang":
            return detected_languages[0].lang
        elif set == "confidence":
            return str(detected_languages[0].prob)
        else:
            return f"Мова: {detected_languages[0].lang}, Коефіцієнт довіри: {detected_languages[0].prob}"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
    # Таблиця відповідності кодів мов їх назвам
    lang_codes = {
        "українська": "uk",
        "Іспанська": "es",
        "Англійська": "en",
        "Японська": "ja",
        "Польська": "pl",
        "Німецька": "de",
        "Італійська": "it",
        "Французька": "fr",
    }

    # Якщо lang є в таблиці, повертаємо відповідну назву мови
    if lang.lower() in lang_codes:
        return lang_codes[lang.lower()]

    # Якщо lang не знайдено в таблиці, то можливо це вже назва мови
    # Тоді нам потрібно знайти відповідний код мови
    for code, name in lang_codes.items():
        if lang.lower() == name.lower():
            return code

    # Якщо не вдалося знайти відповідність, повертаємо повідомлення про помилку
    return "Мова не знайдена або неправильно введена"


def LanguageList(out: str, text: str) -> str:
    # Список підтримуваних мов і кодів
    supported_languages = {
        "українська": "uk",
        "Іспанська": "es",
        "Англійська": "en",
        "Японська": "ja",
        "Польська": "pl",
        "Німецька": "de",
        "Італійська": "it",
        "Французька": "fr",
    }