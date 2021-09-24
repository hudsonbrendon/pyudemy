import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyudemy",
    version="1.0.0",
    author="Hudson Brendon",
    author_email="contato.hudsonbrendon@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hudsonbrendon/pyudemy",
    project_urls={
        "Bug Tracker": "https://github.com/hudsonbrendon/pyudemy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pyudemy"},
    packages=setuptools.find_packages(where="pyudemy"),
    python_requires=">=3.8",
)
