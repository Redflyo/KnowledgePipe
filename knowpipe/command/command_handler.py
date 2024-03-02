from typing import List
from knowpipe.type import CommandEnum
from knowpipe.llm.predict import predict
from knowpipe.config import CHAR_EMBEDDING_SPLITTER
from knowpipe.config.database import vectordb
class Command_Handler:
    def __init__(self,arguments:List[str]) -> None:
        assert len(arguments) > 2
        assert any(arguments[1]==c.value for c in CommandEnum)

        self.command = CommandEnum(arguments[1])
        self.parameters = arguments[2:]

    def import_texts(self,texts:List[str],char_splitter:str=CHAR_EMBEDDING_SPLITTER):
        return [vectordb.import_text(char_splitter,text=text) for text in texts]
    def import_files(self,files:List[str],char_splitter:str=CHAR_EMBEDDING_SPLITTER):
        return [vectordb.import_text(char_splitter,reference=file) for file in files]
    
    def execute(self)-> str:
        if self.command == CommandEnum.PREDICT:
            return predict(self.parameters)
        if self.command == CommandEnum.IMPORT_FILE:
            result = self.import_files(self.parameters)
            print(f"{len(result)} files imported")
            for chunks in result:
                print(f"\t-nb chunks imported: {len(chunks)}")
        if self.command == CommandEnum.IMPORT_TEXT:
            return self.import_texts(self.parameters)

