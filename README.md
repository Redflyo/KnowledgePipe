# KnowledgePipe
Library to implement RAG and LLM in all your internal tools
### RAG Goal
- Retrieve and merge all data
- Import define chunks associated to a document. Retrieve all chunks associated when a document is selected
### LLM Goal
- Generate prompts with many `Document`
- Chain of thought if `Document` are too big for the window context

### Usage
The Knowledge can be used with RAG system or with the definition of which `Document` to use

### Configuration
- Can be used with all LLM(Adaptative constant prompt)
- All LLM can be used, need to define: Endpoint, prompt format
- Handle different prompts