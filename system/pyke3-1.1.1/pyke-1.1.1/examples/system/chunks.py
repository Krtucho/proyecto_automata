from relationship import Relationship

class Chunk:
    def __init__(self) -> None:
        self.relationships = []

    def __str__(self) -> str:
        output:str = ""
        for relationship in self.relationships:
            output += f"{relationship}\n"
        return output

class CatChunk(Chunk):
    def __init__(self, chunk, cat_instances=None, cat_relationships=None) -> None:
        self.chunk = chunk
        self.chunk_type = "cat"

class TermChunk(Chunk):
    def __init__(self) -> None:
        super().__init__()

class RelChunk(Chunk):
    def __init__(self) -> None:
        self.chunk_type = "rel"

class CatTermChunk(Chunk):
    def __init__(self, left_chunk, right_chunk, left_chunk_type, right_chunk_type, cat_chunk, term_chunk, cat_instances, cat_relationships, term_instances) -> None:
        self.cat = cat_chunk
        self.term = term_chunk
        self.chunk_type = "cat_term"

class RelCatTermChunk(Chunk):
    def __init__(self) -> None:
        super().__init__()