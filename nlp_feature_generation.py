import os
os.chdir(r'C:\Users\behna\OneDrive\Documents\Data Science - Projects\20210608 StackOverflow\2. Prepared Data')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from segtok.tokenizer import web_tokenizer


df = pd.read_csv(r'train.csv')

test = df['Title'][0:2]

document = test.apply(web_tokenizer)


# building counter to track every new word coming in
global_counter = []
for sentence in range(len(document)):
    for i in range(len(document[sentence])):
        if document[sentence][i] not in global_counter:
            global_counter.append(document[sentence][i])

# assigning index value to each word and adding to dictionary
s2i = {}
for i in range(len(global_counter)):
        s2i[global_counter[i]] = i
    
# =============================================================================
# alternative counting mthod!!
# s2i = {}
# for sentence in range(len(words)):
#     for i in range(len(words[sentence])):
#         if words[sentence][i] not in s2i.keys():
#             s2i[words[sentence][i]] = len(s2i)
# =============================================================================
from copy import deepcopy

documents = document.apply(deepcopy)

# vectorizing strings
vectors = []
for sentence in document:
    vectors.append(sentence)
    for index, word in enumerate(vectors[-1]):
        if vectors[-1][index] in s2i.keys():
            vectors[-1][index] = s2i[word]



def string2int(df, target: str):
    df[target] = df[target].apply(web_tokenizer)
    global_counter = []
    for sentence in range(len(df[target])):
        for i in range(len(df[target][sentence])):
            if df[target][sentence][i] not in global_counter:
                global_counter.append(df[target][sentence][i])
    
    # assigning index value to each word and adding to dictionary
    s2i = {}
    for i in range(len(global_counter)):
            s2i[global_counter[i]] = i
    return s2i

word_dict = string2int(df.iloc[:1000], 'Title')












