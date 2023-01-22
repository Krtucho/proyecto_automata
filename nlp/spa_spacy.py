import spacy
# from spacy import displacy
# from collections import Counter
# import pandas as pd
# pd.set_option("max_rows", 400)
# pd.set_option("max_colwidth", 400)

import nltk.chunk as chk

print(chk)

nlp = spacy.load('es_core_news_md')

# filepath = 'es.txt'
# text = open(filepath, encoding='utf-8').read()

# text = "Este banco está ocupado por un padre y por un hijo. El padre se llama Juan y el hijo ya te lo he dicho."
text = "¿Cuáles son los síntomas que presenta el cáncer de páncreas?"
document = nlp(text)

for token in document:
    print(token.text, token.lemma_, token.pos_, token.dep_)

for chunk in document.noun_chunks:
    print(chunk)

adjs = []
for token in document:
    if token.pos_ == 'ADJ':
        adjs.append(token.lemma_)