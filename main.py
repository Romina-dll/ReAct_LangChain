from dotenv import load_dotenv

load_dotenv()

"""
Returns the length of a text by characters
"""
def get_text_length(text: str) -> int :
    print(f'get_text_length enter with {text =}')
    return len(text)

if __name__ == '__main__':
    print('Hello Reac Langchain')