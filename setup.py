from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',  # corrected version
    author='Bappy Ahmed',
    author_email='entbappy73@gmail.com',
    packages=find_packages(),
    install_requires=[
        "sentence-transformers==2.2.2",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone-client[grpc]",
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental"
    ]
)