from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="reloadly_giftcard",
    version="1.1.5",
    author="Reloadly Inc.",
    author_email="developers@reloadly.com",
    description="The Official Python library for Reloadly GiftCards APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Reloadly/reloadly-sdk-python/tree/main/giftcard",
    license="MIT",
    packages=find_namespace_packages(include=['reloadly_giftcard.*']),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        'email-validator',
        'requests',
        'jwt',
        'opentelemetry-launcher',
        'requests',
        'certifi',
        'reloadly_core',
        'reloadly_auth'
    ],
    zip_safe=False
)