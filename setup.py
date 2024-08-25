from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openperplex",
    version="0.1.4",
    author="Yassine khazzan",
    author_email="yassine.khazzan@gmail.com",
    description="A Python client for the Openperplex API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YassKhazzan/openperplex_python_client",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx==0.26.0",
    ],
)
