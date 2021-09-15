import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dlomix',
    version='0.0.1',
    author="Omar Shouman",
    author_email="omar.shouman@tum.de",
    description="Deep Learning for Proteomics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wilhelm-lab/dlomix",
    packages=setuptools.find_packages(),
    package_dir={'': 'dlomix'},
    install_requires=[
        'pandas', 'numpy', 'matplotlib', 'scikit-learn', 'tensorflow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
