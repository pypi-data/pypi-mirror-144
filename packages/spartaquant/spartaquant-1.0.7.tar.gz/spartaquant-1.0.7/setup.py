import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spartaquant", # Replace with your own username
    version="1.0.7",
    author="Benjamin Meyer",
    author_email="spartaquant@gmail.com",
    description="SpartaQuant Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://spartaquant.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)