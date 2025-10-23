from langchain_community.document_loaders import SeleniumURLLoader 

urls = [
    "https://kyoto-tech.ac.jp/",
    "https://example.com/",
]

loader = SeleniumURLLoader(urls=urls)

data = loader.load()

print(data)
