# import spacy

import nltk
from nltk.corpus import cess_esp

sentences = cess_esp.tagged_sents()

print(sentences[5])

# cess_esp._tagset = 'es-cast3lb'
# oraciones = cess_esp.tagged_sents(tagset='universal')
# print(oraciones[0])

# default_tagger = nltk.DefaultTagger('NOUN')
# unigram_tagger = nltk.UnigramTagger(sentences, backoff=default_tagger)
# bigram_tagger = nltk.BigramTagger(sentences, backoff=unigram_tagger)
# trigram_tagger = nltk.TrigramTagger(sentences, backoff=bigram_tagger)

document = "Este banco está ocupado por un padre y por un hijo. El padre se llama Juan y el hijo ya te lo he dicho"

# print(trigram_tagger.tag(document.split()))

sentences = nltk.sent_tokenize(document, language="spanish") 

# sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')

print(sentences)

sentences = [nltk.word_tokenize(sent, language="spanish") for sent in sentences] 

print(sentences)