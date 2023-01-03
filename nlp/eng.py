import nltk

text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

# Train
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

# unigram_tagger.tag(brown_sents[2007])
# print(unigram_tagger.evaluate(brown_tagged_sents))


size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
# unigram_tagger = nltk.UnigramTagger(train_sents)
# unigram_tagger.evaluate(test_sents)

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1) # eval = 0.4521080434
# t3 = nltk.TrigramTagger(train_sents, backoff=t2) # eval = 0.433170
eval = t2.evaluate(test_sents)

# nltk.pos_tag
print(t2.tag(text))

# text = nltk.word_tokenize("En la casa hay un queso.")
# print(nltk.pos_tag(text, lang="spa"))

print(eval)


# Storing Taggers
# from cPickle import dump
# output = open('t2.pkl', 'wb')
# dump(t2, output, -1)
# output.close()

# Load Taggers
# from cPickle import load
# input = open('t2.pkl', 'rb')
# tagger = load(input)
# input.close()

# tagger.tag(tokens)


# The full process
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document, language="english") 
    sentences = [nltk.word_tokenize(sent, language="english") for sent in sentences] 
    sentences = [nltk.pos_tag(sent) for sent in sentences]

# # Chunk
# sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
# ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
# grammar = "NP: {<DT>?<JJ>*<NN>}" 
# cp = nltk.RegexpParser(grammar) 
# result = cp.parse(sentence) 

# print(result) 
# result.draw()

# 
# grammar = r"""
#  NP: {<DT|PP\$>?<JJ>*<NN>} # chunk determiner/possessive, adjectives and nouns
#  {<NNP>+} # chunk sequences of proper nouns
# """
# cp = nltk.RegexpParser(grammar)
# sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), 
#  ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
# print(cp.parse(sentence))

# Noun phrase chunking with a unigram tagger.

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
        for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence): 
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
        in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

# from nltk.corpus import conll2000
# test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
# train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
# unigram_chunker = UnigramChunker(train_sents)
# print(unigram_chunker.evaluate(test_sents))


# Sentence Segmentation
# sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
# text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
# sents = sent_tokenizer.tokenize(text)
# pprint.pprint(sents[171:181])

# Regular Exp Tokenizer
# text = 'That U.S.A. poster-print costs $12.40...'
# pattern = r'''(?x) # set flag to allow verbose regexps
# ([A-Z]\.)+ # abbreviations, e.g. U.S.A.
# | \w+(-\w+)* # words with optional internal hyphens
# | \$?\d+(\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
# | \.\.\. # ellipsis
# | [][.,;"'?():-_`] # these are separate tokens
# '''
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`] '''
print(nltk.regexp_tokenize(text, pattern))
print(nltk.word_tokenize(text))
# ['That', 'U.S.A.', 'poster-print', 'costs', '$12.40', '...']