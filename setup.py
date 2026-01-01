"""
Setup script for OpenAI GPT Chatbot

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from setuptools import setup, find_packages

# Author: RSK World (https://rskworld.in) - Year: 2026
setup(
    name="openai-gpt-chatbot",
    version="1.0.0",
    description="Complete chatbot project using OpenAI GPT API for intelligent conversations",
    author="RSK World",
    author_email="help@rskworld.in",
    url="https://rskworld.in",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "flask>=2.3.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

