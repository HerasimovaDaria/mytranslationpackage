# filetr.py
from mytranslationpackage.module1 import TransLate
from mytranslationpackage.module2 import TransLate as DeepTranslate
import os

# Демонстрація роботи функцій
input_file_path = "input.txt"  # Шлях до файлу з текстом для перекладу
output_file_path = "translated.txt"  # Шлях до файлу, де збережеться переклад

if os.path.exists(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Використовуємо функцію з першого модуля
    translated_text = TransLate(text, src='auto', dest='en')

    # Виводимо переклад на екран
    print(f"Translation: {translated_text}")

    # Зберігаємо переклад у файл
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_text)
    print(f"Translation saved to '{output_file_path}'")
else:
    print(f"Input file '{input_file_path}' not found.")
