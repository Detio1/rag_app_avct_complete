from setuptools import find_packages, setup

requirements = """
llama-index==0.10.8
streamlit
python-dotenv
llama-index-embeddings-huggingface
llama-index-llms-llama-cpp
"""

setup(
    name="advanced_chatbot",
    author="NAME_OF_YOUR_GROUP",
    description="{description}",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='==3.10.12',
    include_package_data=True,
    scripts=[],
    zip_safe=False,
)

