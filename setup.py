from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mdl_scrapper",
    version="0.2",
    description="Renders results from mydramalist.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sourabh Singh Rawat",
    author_email="s.rawat3.142@live.in",
    url="https://github.com/dragneelfps/mdl_scrapper",
    license="MIT",
    packages=find_packages(),
    zip_safe=False
)
