# main.py
from pprint import pprint

from rag.document_loader import load_path
from rag.text_splitter import split_docs
from rag.embedding import get_embeddings
from rag.vector_store import get_chroma

def index_corpus(data_dir: str,
                 collection_name: str = "example_collection",
                 persist_dir: str = "./chroma_langchain_db"):
    # 1) 読み込み
    raw_docs = load_path(data_dir)

    # 2) 分割
    chunked = split_docs(raw_docs, chunk_size=200, chunk_overlap=20)

    # 3) 埋め込み器
    embeddings = get_embeddings("intfloat/multilingual-e5-base")

    # 4) VectorStore（既存コレクションがあれば追記）
    vs = get_chroma(collection_name, embeddings, persist_dir)

    # 5) 追加（メタデータにchunk番号がない場合はTextSplitter側で付与済）
    #    Chromaは同一テキストの重複投入を避けたい場合、ids管理を自前でする
    ids = [f"{d.metadata.get('source','')}#{d.metadata.get('start_index',i)}" for i, d in enumerate(chunked)]
    vs.add_documents(chunked, ids=ids)

    print(f"Indexed {len(chunked)} chunks into '{collection_name}'")

def simple_query(question: str,
                 collection_name: str = "example_collection",
                 persist_dir: str = "./chroma_langchain_db",
                 k: int = 5):
    # 既存DBを開く
    embeddings = get_embeddings("intfloat/multilingual-e5-base")
    vs = get_chroma(collection_name, embeddings, persist_dir)
    retriever = vs.as_retriever(search_kwargs={"k": k})

    # ここはまずシンプルに“検索のみ”を確認（生成は後で差し込む）
    docs = retriever.invoke(question)
    print(f"Top-{k} results for: {question}")
    for i, d in enumerate(docs, 1):
        print("="*80)
        print(f"#{i} source={d.metadata.get('source')} start={d.metadata.get('start_index')}")
        print(d.page_content[:500])

if __name__ == "__main__":
    # 初回: コーパスをインデクシング
    # index_corpus("docs")

    # 確認: クエリしてみる
    simple_query("ChromaDBについて教えてください", k=1)
    pass
