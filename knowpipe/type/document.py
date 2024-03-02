from typing import Callable, Optional
from knowpipe.config import CHAR_EMBEDDING_SPLITTER
from knowpipe.rag.retriever import get_content_and_reference


class Document:
    def __init__(self,content:Optional[str]=None,reference:Optional[str]=None) -> None:
        if content is not None:
            self.content = content
            self.reference = reference
        elif reference is not None:
            self.load(reference)
        else:
            raise ValueError("Document __init__ needs at least the reference or the content")
        self.tokens = []

    def __str__(self) -> str:
        return self.content

    @property
    def lines(self,char_splitter:str=CHAR_EMBEDDING_SPLITTER):
        return self.content.split(char_splitter)

    def load(self, reference:str,get_content_reference_func:Callable[[str],Optional[str]]=get_content_and_reference) -> None:
        """
        Reference object is define from a link to get the data
        The get_content function can be redefined it's depends of the use case

        Args:
            reference (str): reference used in get_content function
            get_content_func (function, optional): get_content_function. Defaults to get_content.
        """
        self.content, self.reference = get_content_reference_func(reference)
        