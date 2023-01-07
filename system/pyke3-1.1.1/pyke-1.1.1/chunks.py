from relationship import Relationship

class Chunk:
    def __init__(self) -> None:
        self.relationships = []
        self.chunk = ""
        self.text_chunk = ""
        self.chunk_type = ""

    def __str__(self) -> str:
        output:str = f"chunk: {self.text_chunk}:\nchunk_type: {self.chunk_type}\n"
        for relationship in self.relationships:
            output += f"{relationship}\n"
        return output

class CatChunk(Chunk):
    def __init__(self, chunk, cat_instances=None, cat_relationships=None) -> None:
        self.chunk = chunk
        self.chunk_type = "cat"
        self.instances = cat_instances
        self.relationships = self.instances
        self.text_chunk = chunk
    
    def __str__(self) -> str:
        return super().__str__()

class CatCatChunk(Chunk):
    def __init__(self, left_cat:CatChunk, right_cat:CatChunk, cat_relationships: list) -> None:
        self.chunk = f"{left_cat.chunk} {right_cat.chunk}"
        self.relationships = cat_relationships
        self.text_chunk = self.chunk

    def __str__(self) -> str:
        return super().__str__()

class TermChunk(Chunk):
    def __init__(self, chunk, term_instances=None, cat=None) -> None:
        self.chunk = chunk
        self.chunk_type = "term"
        self.term_instances = term_instances
        self.cat = cat
        self.relationships = self.instances
        self.text_chunk = self.chunk

    def __str__(self) -> str:
        return super().__str__()

class RelChunk(Chunk):
    def __init__(self, chunk, rel_instances) -> None:
        self.chunk = chunk
        self.chunk_type = "rel"
        self.rel_instances = rel_instances
        self.relationships = []
        self.text_chunk = chunk

    def __str__(self) -> str:
        return super().__str__()

class CatTermChunk(Chunk):
    def __init__(self, left_chunk, right_chunk, left_chunk_type, right_chunk_type, cat_chunk, term_chunk, cat_instances, cat_relationships, term_instances, terms_cat, relationships=[]) -> None:
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

        self.text_chunk = f"{cat_chunk} {term_chunk}"
        self.relationships = []

    def __str__(self) -> str:
        return super().__str__()

class RelCatTermChunk(Chunk, ):
    def __init__(self, relationships) -> None:
        self.relationships = relationships
        self.chunk_type = "rel_cat_term"
        self.text_chunk = "rel_cat_term"
        if len(relationships) > 0:
            relationship = relationships[0]
            self.text_chunk = f"{relationship.tags[0]} {relationship.tags[1]} {relationship.tags[2]} {relationship.tags[3]} {relationship.tags[4]}"

    def __str__(self) -> str:
        return super().__str__()