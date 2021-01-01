import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vitya",   # Replace with your own username
    version="0.0.3",
    author="hicebank.ru",
    author_email="levashov@hicebank.ru",
    description="validators for different russian banking values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hicebank/vitya",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
