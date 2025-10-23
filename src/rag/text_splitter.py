# text_splitter.py
from __future__ import annotations
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(docs: list[Document],
               chunk_size: int = 200,       # 小さめ
               chunk_overlap: int = 20) -> list[Document]:
    """
    再帰的文字ベース分割。段落→文→語と粒度を落として分割してくれるため、
    「小さいチャンクを大量に作る」用途でも破綻しにくい。
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )
    return splitter.split_documents(docs)
