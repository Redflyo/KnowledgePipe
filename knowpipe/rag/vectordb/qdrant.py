from .base import BaseDb
from typing import Optional, List
from knowpipe.type import Document
from knowpipe.config import CHAR_EMBEDDING_SPLITTER
from knowpipe.rag.chunk import document_to_chunks
class QdrantDb(BaseDb):

    def __init__(self,user,password) -> None:
        super().__init__(user,password)
        

    def import_text(self,char_splitter:str,text:Optional[str]=None,reference:Optional[str]=None,):
        document = Document(text,reference)
        chunks = document_to_chunks(document,char_splitter)
        return chunks