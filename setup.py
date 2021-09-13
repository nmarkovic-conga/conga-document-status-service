from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["flask>=2.0.1"]

setup(
    name="congadocumentstatusservice",
    version="0.0.1",
    author="Nikola Markovic",
    author_email="nmarkovic@conga.com",
    description="A package change document process status for Conga core app",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/nmarkovic-conga//conga-document-status-service/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)