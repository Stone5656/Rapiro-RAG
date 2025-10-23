# embedding.py
from __future__ import annotations
from typing import Protocol
from langchain_huggingface import HuggingFaceEmbeddings

class SupportsEmbed(Protocol):
    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...
    def embed_query(self, text: str) -> list[float]: ...

def get_embeddings(model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> SupportsEmbed:
    """
    まずはローカル実行しやすいHuggingFaceの埋め込みを既定に。
    あとでOpenAI/Gemini等に差し替える場合も関数差し替えで対応。
    """
    return HuggingFaceEmbeddings(model_name=model_name)
