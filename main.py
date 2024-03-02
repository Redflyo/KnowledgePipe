import sys
from knowpipe.command import Command_Handler

def main():
    print("Welcome in KnowledgePipe a implementation of LLM and RAG in your internal tool")
    script_handler = Command_Handler(sys.argv)
    script_answer = script_handler.execute()
    print(script_answer)
    
      
if __name__ == '__main__':
  main()