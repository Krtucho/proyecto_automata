from abc import abstractmethod
import nltk, spacy
nlp = spacy.load('es_core_news_md')


class PreprocessText():
    """Clase estatica encargada del trabajo con procesamiento del lenguaje natural"""
    @staticmethod
    def sentence_segmentation(document: str, language="spanish")->list:
        """Dado un texto con cierta cantidad de oraciones, devuelve una lista de strings donde cada elemento es una de las oraciones que fueron separadas"""
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
    
    @staticmethod
    def normalize(lista_palabras):
        """Dada una lista de palabras (lista de strings, intercambia las letras que tengan tildes por sus omologas sin tilde y las ñ por nn"""
        word_list=[]
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "nn"),
        )
        for s in lista_palabras:
            for a, b in replacements:
                s = s.replace(a, b).replace(a.upper(), b.upper())
            word_list.append(s)
        return word_list
    # @staticmethod
    # def process_text(text: str):
    #     return [(t,l,p) for (t,l,p) in (PreprocessText.get_verbs_and_nouns(sent) for sent in PreprocessText.sentence_segmentation(text))]