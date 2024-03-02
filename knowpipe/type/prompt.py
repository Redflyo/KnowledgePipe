from typing import List
from knowpipe.type import Document
from knowpipe.config.prompt import PROMPT_INTRODUCTION,PROMPT_NEW_REFERENCE,PROMPT_QUESTION
CHAR_SPLITTER = "\n"
class Prompt:
    def __init__(self, user_prompt:str ,document_references:List[Document], intro_prompt:str=PROMPT_INTRODUCTION) -> None:
        self.user_prompt = user_prompt
        self.references = document_references
        self.intro_prompt = intro_prompt

    def _format_references_for_prompt(self) -> str:
        return [PROMPT_NEW_REFERENCE.replace("<reference>",reference.content) for reference in self.references]
        
    def _format_question_for_prompt(self) -> str:
        return PROMPT_QUESTION.replace("<question>",self.user_prompt)

    def construct(self) -> str:
        prompt_contents = [PROMPT_INTRODUCTION]
        prompt_contents.extend(self._format_references_for_prompt())
        prompt_contents.append(self._format_question_for_prompt())

        return CHAR_SPLITTER.join(prompt_contents)
    def __str__(self) -> str:
        return self.construct()
        