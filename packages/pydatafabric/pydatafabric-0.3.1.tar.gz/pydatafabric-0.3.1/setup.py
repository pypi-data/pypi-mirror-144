# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


def read(filename):
    with open(filename, "r") as file_handle:
        return file_handle.read()


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return ".".join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return ".".join(map(str, version_tuple))


init = os.path.join(os.path.dirname(__file__), "pydatafabric", "__init__.py")
version_line = list(filter(lambda l: l.startswith("VERSION"), open(init)))[0]

VERSION = get_version(eval(version_line.split("=")[-1]))
README = os.path.join(os.path.dirname(__file__), "README.md")

# Start dependencies group
emart = [
    "torch",
    "torchdiffeq",
    "tensorboard<3.0.0",
    "seaborn==0.11.2",
    "implicit==0.5.2",
    "matplotlib==3.5.1",
    "openpyxl==3.0.9",
    "xgboost==1.5.2",
    "scikit-learn==1.0.2",
    "bayesian-optimization==1.2.0",
]

install_requires = [
    "thrift-sasl==0.4.3",
    "hvac==0.11.2",
    "pyhive[hive]==0.6.5",
    "pyarrow==6.0.1",
    "pandas",
    "slackclient==2.9.3",
    "httplib2==0.20.4",
    "testresources",
    "python-dateutil>=2.8.1",
    "requests<3.0.0,>=2.26.0",
    "protobuf>=3.12.0",
    "psycopg2<3.0.0",
    "click",
    "PyGithub",
    "pycryptodome",
    "tabulate==0.8.9",
    # See: https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html#pip-requirements
    "grpcio==1.43.0",
    "grpcio-status==1.43.0",
    "sqlalchemy==1.4.31",
    "packaging",
    "tqdm==4.63.1",
    "ipywidgets",
    "hmsclient-hive-3",
    "redis",
    # Google Cloud Python SDK
    # https://github.com/googleapis/google-cloud-python
    "google-cloud-bigquery==2.34.2",
    "google-cloud-bigquery-storage==2.13.0",
    "google-cloud-bigtable==2.7.1",
    "google-cloud-monitoring==2.9.1",
    "google-cloud-vision==2.7.2",
    "google-auth==2.6.2",
    "google-auth-oauthlib<0.5,>=0.4.1",
    "google-api-core==2.7.1",
    "google-api-python-client==2.42.0",
    "google-cloud-core==2.2.3",
    "google-cloud-common==1.0.1",
    "googleapis-common-protos==1.56.0",
    # "google-resumable-media==2.2.1",
]

EXTRAS_REQUIRE = {
    "emart": emart,
}

setup(
    name="pydatafabric",
    version=VERSION,
    python_requires=">=3.8,<3.11",
    packages=find_packages("."),
    author="SHINSEGAE DataFabric",
    author_email="admin@shinsegae.ai",
    description="SHINSEGAE DataFabric Python Package",
    long_description=read(README),
    long_description_content_type="text/markdown",
    url="https://github.com/emartddt/dataplaltform-python-dist",
    install_requires=install_requires,
    extras_require=EXTRAS_REQUIRE,
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["nes = pydatafabric.nes:nescli"]},
)
