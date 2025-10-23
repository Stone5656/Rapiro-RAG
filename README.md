# 🤖 RapiroRAG

<p align="center">
  <a href="https://github.com/Stone5656/Rapiro-RAG/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-informational?style=for-the-badge" alt="License: MIT">
  </a>
</p>

## 🧩 概要
**RapiroRAG** は、Rapiro ロボットに搭載するための軽量 RAG (Retrieval-Augmented Generation) モジュールです。  
後日、FastAPI サーバーの AI モジュールと統合されることを前提としています。  
本リポジトリは、**headless 環境（GUIなし）で動作**するシンプルな構成を目指します。

---

## 🏗️ 技術スタック

| 項目 | 使用技術 / ライブラリ |
|------|------------------------|
| フレームワーク | LangChain v1.0 |
| ベクトルDB | ChromaDB |
| パッケージ管理 | uv |
| Webスクレイピング | Selenium（学校情報取得用）|
| OS対応 | Linux / Headless 環境前提 |
| 参考ドキュメント | [LangChain Integrations](https://docs.langchain.com/oss/python/integrations) |

---

## 📁 プロジェクト構成

```bash
.
├── README.md
├── chroma_langchain_db/
│   ├── chroma.sqlite3
│   └── <永続化されたベクトルデータ>
├── docs/
│   └── <テキストまたはPDF>
├── src/
│   ├── main.py
│   └── rag/
│       ├── document_loader.py
│       ├── text_splitter.py
│       ├── embedding.py
│       └── vector_store.py
├── pyproject.toml
├── uv.lock
└── url_loader.py  # Web情報取得用 (Selenium予定)
```

---

## ⚙️ 構成モジュール

| モジュール                  | 役割                                       | 参考ドキュメント                                                                                       |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **document_loader.py** | テキスト・PDFなどを LangChain の `Document` 形式に変換 | [DocumentLoader](https://docs.langchain.com/oss/python/integrations/document_loaders)          |
| **text_splitter.py**   | テキストを小さなチャンクに再帰分割                        | [TextSplitter](https://docs.langchain.com/oss/python/integrations/splitters)                   |
| **embedding.py**       | 文書をベクトル化（E5など多言語対応モデル）                   | [Embedding](https://docs.langchain.com/oss/python/integrations/text_embedding)                 |
| **vector_store.py**    | ChromaDB による永続ベクトルストア管理                  | [VectorStore (Chroma)](https://docs.langchain.com/oss/python/integrations/vectorstores#chroma) |
| **main.py**            | 各モジュールの統合実行。index化および検索テスト用              | -                                                                                              |

---

## 🚀 実行手順

### 1️⃣ 依存関係インストール

```bash
uv sync
# または
uv add "langchain>=1.0" langchain-core langchain-community langchain-chroma \
       chromadb sentence-transformers selenium
```

### 2️⃣ ドキュメント登録（インデクシング）

```bash
uv run src/main.py
```

`docs/` 内のテキストを分割し、埋め込み生成後、`./chroma_langchain_db/` に永続保存します。

### 3️⃣ 検索実行（簡易クエリ）

```bash
uv run src/main.py
```

実行時の出力例：

```
Top-3 results for: ChromaDBについて教えてください
================================================================================
#1 source=docs/chroma_description.txt start=60
Chromaはオープンソースのベクトルデータベースで、LangChainとの統合が容易である。
...
```

---

## 🔍 今後の拡張予定

| 機能                | 説明                                                                                              | 優先度 |
| ----------------- | ----------------------------------------------------------------------------------------------- | --- |
| Retriever 実装      | [LangChain Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers) による検索戦略強化 | ★★★ |
| Chain-Build / MMR | 検索結果の圧縮・再ランキングによる精度向上                                                                           | ★★☆ |
| FastAPI統合         | Rapiroサーバー内AIモジュールへの組込み                                                                         | ★★★ |
| URLローダ            | Seleniumによる動的スクレイピング（例：学校情報など）                                                                  | ★★☆ |
| Pre-commit / ruff | 開発補助（静的解析・整形）                                                                                   | ★☆☆ |

---

## 🧠 開発ポリシー

* Headless 実行（GUI非依存）
* 環境再現性を重視（`uv.lock` に依存関係固定）
* ログ出力・LLM統合部分は後日 FastAPI モジュール側で制御
* テキストのみでの動作確認が可能

---

## 🪪 License

詳細は [LICENSE](https://github.com/Stone5656/Rapiro-RAG/main/LICENSE) を参照してください。
