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
        self.instances = cat_instances
        self.relationships = cat_relationships

class TermChunk(Chunk):
    def __init__(self, chunk, term_instances=None, cat=None) -> None:
        self.chunk = chunk
        self.chunk_type = "term"
        self.term_instances = term_instances
        self.cat = cat

class RelChunk(Chunk):
    def __init__(self, chunk, rel_instances) -> None:
        self.chunk = chunk
        self.chunk_type = "rel"
        self.rel_instances = rel_instances

class CatTermChunk(Chunk):
    def __init__(self, left_chunk, right_chunk, left_chunk_type, right_chunk_type, cat_chunk, term_chunk, cat_instances, cat_relationships, term_instances, terms_cat) -> None:
        self.cat = cat_chunk
        self.term = term_chunk
        self.chunk_type = "cat_term"

        self.left_chunk = left_chunk
        self.right_chunk = right_chunk
        self.left_chunk_type = left_chunk_type
        self.right_chunk_type = right_chunk_type
        
        self.cat_instances = cat_instances
        self.cat_relationships = cat_relationships
        self.term_instances = term_instances

        self.terms_cat = terms_cat

class RelCatTermChunk(Chunk):
    def __init__(self) -> None:
        super().__init__()