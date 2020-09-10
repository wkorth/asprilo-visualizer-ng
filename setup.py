import setuptools

with open("README.md", "r") as ld:
    long_description = ld.read()

setuptools.setup(
    name="asprilo-visualizer-ng",
    version="0.1.1",
    author="Wassily Korth",
    author_email="wkorth@uni-potsdam.de",
    description="Planned successor to the asprilo-visualizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wkorth/mapf-to-asprilo",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': [
                           'viz-ng = visualizer.__main__:main',]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.6',
)