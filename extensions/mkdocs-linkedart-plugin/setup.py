import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdocs-linkedart-plugin", # Replace with your own username
    version="0.0.1",
    author="Rob Sanderson",
    author_email="rsanderson@example.org",
    description="Linked Art documentation support",
    url="https://github.com/linked.art/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'mkdocs',
        'requests',
        'uuid',
        'rdflib',
        'PyLD',
        'cromulent'
    ],
    entry_points={
      'mkdocs.plugins': [
        'linkedartindexing = linkedart.plugin:IndexingPlugin'
      ]
    }
)

