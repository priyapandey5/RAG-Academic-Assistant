import faiss
import pickle
import numpy as np

from rag.embedder import get_model


def retrieve_chunks(query, top_k=5):

    model = get_model()

    index = faiss.read_index(
        "data/faiss_index/index.bin"
    )

    with open(
        "data/chunks.pkl",
        "rb"
    ) as f:
        chunks = pickle.load(f)

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for i in indices[0]:

        if i != -1:

            retrieved_chunks.append(
                chunks[i]
            )

    return retrieved_chunks
