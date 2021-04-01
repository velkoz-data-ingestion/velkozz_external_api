from setuptools import setup, find_namespace_packages

setup(
    name = "velkozz-developer-api",
    url = "https://github.com/velkoz-data-ingestion/velkozz_pipeline_api",
    version = "0.1.2",
    author = "Matthew Teelucksingh",
    packages = find_namespace_packages(
        include = ["vdeveloper_api.*"]
    ),
    package_dir = {"" : "vdeveloper_api"},
    install_requires = [
        "pandas", 
        "bonobo",
        "praw",
        "requests"
    ],
    license = 'MIT',
    long_description=open('README.md').read()   
    )