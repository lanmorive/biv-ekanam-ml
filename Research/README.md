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

После такой предобработки качество NVB+TF-IDF рассмотренных моделей выросло на 7 процентных пунктов

## Наивный байесовский классификатор + TF-IDF
Решение находится в файле `Naive Bayes Classifier.ipynb`

Модель показала хорошие изначальные показатели:

- `Accuracy` = 0.875
- `F1-Score` = 0.84