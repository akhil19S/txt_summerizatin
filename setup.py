from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="textSummarizer",
    version="0.0.1",
    author="akhil19s",
    description="A small package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/akhil19S/txt_summerizatin.git",
    author_email="<akhilswamy77@outlook.com>",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
