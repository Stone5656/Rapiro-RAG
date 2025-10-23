# vector_store.py
from __future__ import annotations
from langchain_chroma import Chroma

def get_chroma(collection_name: str,
               embedding_function: object,
               persist_directory: str = "./chroma_langchain_db") -> Chroma:
    """
    Chroma の永続DBを初期化（存在すれば再利用）。
    """
    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory=persist_directory,
    )
