# Решение кейса

В рамках кейса мы решили сравнить 4 модели: `Naive Bayes Classifier + TF-IDF`, `FastText`, `BERT Vectorizer + biGRU` и `BERT Classifier`

## Предобработка текста

Для одинаковой предобработки датасета мы использовали следующий подход: мы удаляем из текста все кроме слов, после чего удаляем стоп-слова 

Вот код с его реализацией:

```python
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

only_text_regex = r'[^а-яА-ЯёЁ]+'
stop_words = set(stopwords.words('russian'))

def clean_text(text: str) -> str:
    return ' '.join(
        [word 
         for word in re.sub(only_text_regex, ' ', text).split() 
         if word.lower() not in stop_words]
    )
```

После такой предобработки качество NVB+TF-IDF рассмотренных моделей выросло на 4 процентных пунктов

## Результаты

|Название модели|Accuracy|F1-Score|
|---|---|---|
|NBC + TF-IDF|0.9125|0.9255|
|FastText| 0.97 | 0.97 |
|biGRU| 0.97 | 0.98 |
|RuBERT| - | - |

## Валидация моделей

Также мы оценили дискриминационные способности моделей и ее стабильность с помощью тестов индексом Джини и критерием Колмогорова-Смирнова

|Название модели|Индекс Джини|p-value критерия Колмогорова-Смирнова|Статистика критерия Колмогорова-Смирнова|
|---|---|---|---|
|NBC + TF-IDF| - | - | - |
|FastText| - | - | - |
|biGRU| 0.9983 | 0.000059 | 0.99 |
|RuBERT| - | - | - |

И с интервальной оценкой ROC-AUC построили распределения:

TODO: вставить фотку
