from typing import List, Optional
class BaseDb:
    def __init__(self,username:str,password:str) -> None:
        self.username = username
        self.password = password

    def import_text(text:Optional[str]=None,reference:Optional[str]=None,char_splitter:str=""):
        raise NotImplemented("Abstract class")

