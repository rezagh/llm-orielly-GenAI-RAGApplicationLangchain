from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

import os 

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINE_CODE_API_KEY"))

index_name = "quickstart"

pc.create_index(
    name=index_name,
    dimension=8, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)