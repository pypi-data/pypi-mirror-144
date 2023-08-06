import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptlibs",
    description="Support library for penterepTools",
    author="Penterep",
    author_email="info@penterep.com",
    url="https://www.penterep.com/",
    version="0.0.6",
    license="GPLv3+",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires = '>=3.6',
    install_requires=["requests"],
    long_description=long_description,
    long_description_content_type="text/markdown"
)