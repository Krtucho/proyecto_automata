class Relationship:
    def __init__(self,relationship:tuple, tags=None) -> None:
        self.relationship = relationship # 
        #self.tags = tags # tupla con el papel de cada elemento, x Cat, Rel, Term

    def __str__(self) -> str:
        return str(self.relationship)