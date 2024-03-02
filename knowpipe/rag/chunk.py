from sentence_transformers import SentenceTransformer
from knowpipe.config import TOKENIZER_NAME, TOKENS_PER_WORD_ESTIMATION, CHAR_EMBEDDING_SPLITTER
from knowpipe.type import Document
from typing import List, Tuple, Optional
embedding_model = SentenceTransformer(TOKENIZER_NAME)

def estimate_line_tokens_length(line:str) -> int:
        words = line.split(" ")
        return TOKENS_PER_WORD_ESTIMATION * len(words)

def too_much_tokens(tokens_length):
     return embedding_model.max_seq_length < tokens_length

def compute_embedding(text:str) -> list:
    return embedding_model.encode(text)

def join_lines(lines:List[str],char_splitter:str) -> str:
    return char_splitter.join(lines)

def document_to_chunks(document:Document,char_splitter:str) -> List[Tuple[str,list]]:

    chunks = []
    tokens_length = 0
    selected_lines = []

    for line in document.lines:
        tokens_length += estimate_line_tokens_length(line)
        selected_lines.append(line)

        if not too_much_tokens(tokens_length):
            continue

        tokens_length = 0
        selected_text = join_lines(selected_lines,char_splitter)
        embeddings = compute_embedding(selected_text)

        chunks.append((selected_text,embeddings))
    return chunks
