# from nltk.corpus import cess_esp as cess
# from nltk import UnigramTagger as ut
# from nltk import BigramTagger as bt

# # Read the corpus into a list, 
# # each entry in the list is one sentence.
# cess_sents = cess.tagged_sents()

# # Train the unigram tagger
# uni_tag = ut(cess_sents)

# sentence = "Hola , esta foo bar ."

# # Tagger reads a list of tokens.
# uni_text = uni_tag.tag(sentence.split(" "))
# print(uni_text)

# # Split corpus into training and testing set.
# train = int(len(cess_sents)*90/100) # 90%

# # Train a bigram tagger with only training data.
# bi_tag = bt(cess_sents[:train])

# # Evaluates on testing data remaining 10%
# bi_tag.evaluate(cess_sents[train+1:])

# # Using the tagger.
# bi_text = bi_tag.tag(sentence.split(" "))
# print(bi_text)

from preprocess import PreprocessText
sentences = PreprocessText.sentence_segmentation("¿Cuáles son los síntomas que presenta el cáncer de páncreas?")

result = []
for sentence in sentences:
    result.append(PreprocessText.get_verbs_and_nouns(sentence))
print(result)