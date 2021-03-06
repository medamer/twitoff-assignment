# web_app/services/basilica_service.py

from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = Connection(API_KEY)
# Function to return connection:
def basilica_api_client():
    connection = Connection(API_KEY)
    print(type(connection)) 
    return connection

if __name__ == "__main__":

    print("---------")
    connection = basilica_api_client()

    print("---------")
    sentence = "Hello again"
    sent_embeddings = connection.embed_sentence(sentence)
    print(list(sent_embeddings))

    print("---------")
    sentences = ["Hello world!", "How are you?"]
    print(sentences)
    # it is more efficient to make a single request for all sentences...
    embeddings = connection.embed_sentences(sentences)
    print("EMBEDDINGS...")
