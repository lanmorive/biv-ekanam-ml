import re
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from natasha import Doc, Segmenter, MorphVocab
from natasha import NewsEmbedding, NewsMorphTagger


# Инициализация компонентов Natasha
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)

# Список месяцев
months = [
    "январь", "февраль", "март", "апрель", "май", "июнь",
    "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
]

# Стоп-слова
russian_stopwords = set(stopwords.words("russian"))
russian_stopwords.discard('за')  # Убираем из стоп-слов "за"
russian_stopwords.update(['кг', 'сумма', 'тч', 'мл', 'счёт'])  # Добавляем свои слова


# Функция очистки текста
def clear(text):
    # Удаляем даты из текста
    date_pattern = r"(\d{0,4}[./-]?)"
    cleaned_text = re.sub(date_pattern, "", text)

    # Токенизация и удаление стоп-слов
    tokens = word_tokenize(cleaned_text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords]
    tokens = [token for token in tokens if token not in string.punctuation]
    cleaned_text = ' '.join(tokens)

    # Используем Natasha для морфологической обработки
    doc = Doc(cleaned_text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    # Лемматизация
    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    # Убираем месяцы и короткие слова
    lemmas = [token.lemma for token in doc.tokens if token.lemma not in months and len(token.lemma) > 1]

    return ' '.join(lemmas)