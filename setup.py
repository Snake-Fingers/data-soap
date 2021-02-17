import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-soap",
    version="0.0.5",
    author="Mason Fryberger / Grace Choi / Alex Angelico / Jae Young Choi / Robert Carter",
    author_email="alex.angelico@gmail.com",
    description="A CLI menu that allows users to request overall daily rating for group of websites, with other options for individual site readouts.",
    install_requires=[
        'pandas',
        'numpy',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Snake-Fingers/data-soap",
    packages=setuptools.find_packages(),
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.1',
)
