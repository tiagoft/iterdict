from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iterdict",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list of package dependencies
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tiago F. Tavares",
    author_email="tiagoft@gmail.com",
    description="Use dictionaries to iterate over combinations of parameters",
    url="https://github.com/tiagoft/iterdict"
)