import pickle
import numpy as np
import pandas as pd
from tqdm import tqdm

from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from clear_text import clear

df = pd.read_table('payments_main.tsv', names=['id', 'date', 'amount', 'text'])
model = load_model('bigru_model.keras')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)    

id2text = {
    0: 'TAX', 
    1: 'NON_FOOD_GOODS', 
    2: 'REALE_STATE', 
    3: 'SERVICE', 
    4: 'NOT_CLASSIFIED', 
    5: 'BANK_SERVICE', 
    6: 'LOAN', 
    7: 'FOOD_GOODS', 
    8: 'LEASING'
}


def get_label(text):
    text = clear(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=200)
    pred = model.predict(padded)
        
    return id2text[np.argmax(pred)]

result = df[['id', 'text']]
result['text'] = result['text'].apply(get_label)
result.to_csv('payment_predict.tsv', header=False, index=False)
