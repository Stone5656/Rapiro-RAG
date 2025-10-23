# document_loader.py
from __future__ import annotations
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.documents import Document

def load_path(path: str | Path) -> list[Document]:
    """
    指定パス配下の .txt と .pdf を読み込み、LangChainのDocumentに統一。
    ここではシンプルに同期ロードのみ（.load）。
    """
    if type(path) == str:
        path = Path(path)

    docs: list[Document] = []

    for file in path.rglob("*"):
        if file.suffix.lower() == ".txt":
            docs.extend(TextLoader(str(file), encoding="utf-8").load())
        elif file.suffix.lower() == ".pdf":
            docs.extend(PyPDFLoader(str(file)).load())
    # メタデータの最小整形
    for doc in docs:
        doc.metadata.setdefault(
            "source", doc.metadata.get("source") or str(doc.metadata.get("file_path") or "")
        )  # loader依存の差を吸収
    return docs
