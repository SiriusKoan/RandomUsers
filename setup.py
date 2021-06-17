from setuptools import setup, find_packages

setup(
    name="RandomUsers",
    description="A simple tool helps you generate fake users.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="1.0",
    author="SiriusKoan",
    author_email="k.peihsun@gmail.com",
    packages=find_packages(),
    url="https://github.com/SiriusKoan/RandomUsers",
    license="MIT",
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
