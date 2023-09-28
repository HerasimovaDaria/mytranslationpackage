# gtrans.py
from mytranslationpackage.module1 import TransLate

# Зчитуємо вміст файлу "input.txt"
with open("input.txt", "r", encoding="utf-8") as input_file:
    text = input_file.read()

# Список мов, на які ви хочете перекласти текст
languages_to_translate = ['en', 'fr', 'es']  # Наприклад, англійська, французька, і іспанська

# Словник для зберігання перекладів для кожної мови
translations = {}

# Перекладаємо текст на кожну мову і зберігаємо результати
for lang in languages_to_translate:
    translated_text = TransLate(text, src='auto', dest=lang)
    translations[lang] = translated_text

# Виводимо результати перекладів
for lang, translated_text in translations.items():
    print(f"Translation to {lang}: {translated_text}")

