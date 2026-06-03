from setuptools import setup, find_packages

setup(
    name="federated-learning-framework",
    version="0.1.0",
    author="yuki-tanaka-hpc",
    description="Federated Learning Framework with Differential Privacy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yuki-tanaka-hpc/federated-learning-framework",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.0",
        "numpy>=1.24",
        "pyyaml>=6.0",
        "tqdm>=4.65",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
