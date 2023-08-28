from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="notion-stock",
    version="1.0.0",
    author="rana421",
    author_email="u554980e@gmail.com",
    description="notionの株価データベースに現在の株価を反映する",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rana421/notion_stock_public",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)
