from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="plantuml_generator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A library for generating PlantUML diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/plantuml_generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "plantweb",
    ],
    extras_require={
        'dev': ['pytest', 'sphinx', 'cairosvg'],
    },
    entry_points={
        "console_scripts": [
            "plantuml_generator=plantuml_generator.core:plantuml",
        ],
    },
    test_suite='tests',
)