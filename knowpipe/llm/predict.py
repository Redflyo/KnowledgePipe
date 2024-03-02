from typing import List,Tuple
from knowpipe.type import Prompt, Document

def predict(parameters:List[str]) -> str:
    user_prompt,references = get_prompt_and_content(parameters)
    prompt = Prompt(user_prompt,references)
    return prompt.construct()
    

def get_prompt_and_content(parameters:List[str]) -> Tuple[str,List[Document]]:

    if len(parameters) == 0:
        raise IndexError("Need a prompt to predict")

    prompt = parameters[0]
    references = [Document(reference=path) for path in parameters[1:]]
    return prompt,references

    