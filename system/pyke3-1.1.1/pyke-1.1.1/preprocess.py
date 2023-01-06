from abc import abstractmethod
import nltk, spacy
nlp = spacy.load('es_core_news_md')


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

    @staticmethod
    def sentence_segmentation(document: str, language="spanish")->list:
        return nltk.sent_tokenize(document, language="spanish")

    @staticmethod
    def tokenize_and_tag_sent(sent:str):
        """Dada una oracion (sent:str) Devuelve una lista de tuplas de la forma (text, lemma, pos) con los tokens que formen parte de esta"""
        document = nlp(sent)

    # for token in document:
    #     print(token.text, token.lemma_, token.pos_, token.dep_)

        return [(token.text, token.lemma_, token.pos_) for token in document]

    @staticmethod
    def get_verbs_and_nouns(sent:str):
        """Dada una oracion (sent:str) Devuelve una lista de tuplas de la forma (text, lemma, pos) con los tokens que sean sustantivos o verbos"""
        targets = ["NOUN", "VERB"]
        return [(t,l,p) for (t,l,p) in PreprocessText.tokenize_and_tag_sent(sent) if p in targets]
    
    # @staticmethod
    # def process_text(text: str):
    #     return [(t,l,p) for (t,l,p) in (PreprocessText.get_verbs_and_nouns(sent) for sent in PreprocessText.sentence_segmentation(text))]