# deeptr.py
from mytranslationpackage.module2 import TransLate

# Демонстрація роботи функцій
text = "Bonjour, comment ça va?"
translated_text = TransLate(text, src='fr', dest='en')
print(f"Translation: {translated_text}")
