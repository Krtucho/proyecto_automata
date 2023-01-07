class Relationship:
    def __init__(self,relationship:tuple, tags=None) -> None:
        self.relationship = relationship # 
        self.tags = tags    # Tupla con cada elemento como se le paso. 
                            # Puede tener un valor de la consulta o en caso de que no se le haya pasado, tendra la etiqueta de su funcion en la consulta

    def __str__(self) -> str:
        return str(self.relationship)