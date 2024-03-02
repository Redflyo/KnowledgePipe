from typing import Optional
from knowpipe.config import CHAR_VECTOR_TAG
import os
def read_file(path:str) -> Optional[str]:
    file = open(path,"r")
    content = "\n".join(file.readlines())
    file.close()
    return content

def get_content_and_reference(reference:str) -> str:
    if reference.startswith(CHAR_VECTOR_TAG):
        #TODO Implement RAG and search of document
        return ""
    else:
        #TODO Need to generate error when the RAG is implemented
        return read_file(reference), os.path.splitext(reference)[0]