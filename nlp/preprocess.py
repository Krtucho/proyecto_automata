import nltk

class PreprocessText():
    def __init__(self, text, sent_seg="nltk", word_tok="nltk") -> None:
        sentences = []
        if sent_seg == "nltk":  # Sentence Segmentation
            sentences = nltk.sent_tokenize(text, language="spanish")
        else:
            sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
            sentences = sent_tokenizer.tokenize(text)

        if word_tok == "nltk":  # Word Tokenizer
            sentences = [nltk.word_tokenize(sent, language="spanish") for sent in sentences] 
        else:
            pass

        # POSTag
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