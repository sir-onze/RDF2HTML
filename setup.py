import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rdf2html", # Replace with your own username
    version="0.0.3",
    author="Tiago Baptista",
    author_email="tiago96baptista@gmail.com",
    description="Tool that allows to visualize ontologies in HTML using python as the base to the solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sir-onze/RDF2HTML",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    package_data={'rdf2html': ['*.html','html/*.html']},
    include_package_data=True,
)