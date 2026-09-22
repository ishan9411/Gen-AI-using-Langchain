from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about bumrah in india"

#This is what we exactly do in RAG systems, we only store these documents embeddings
#so we dont have to create them again & again, that storage DB is know as vector DB
doc_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

vector = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, similarity = sorted(list(enumerate(vector)), key=lambda x:x[1])[-1]

print("User Query: ", query)

print("Response: ", documents[index])

print("Similarity match: ", similarity)

