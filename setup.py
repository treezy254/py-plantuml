from setuptools import setup, find_packages, Command
import subprocess

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

class RunTests(Command):
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(['python', '-m', 'unittest', 'discover', 'tests'])

class BuildDocs(Command):
    description = 'build documentation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(['sphinx-build', '-b', 'html', 'docs/source', 'docs/build/html'])

setup(
    name="pythonplantuml",
    version="0.2.1",
    author="Kamau Samuel",
    author_email="gachungasamuel54@gmail.com",
    description="A library for generating PlantUML diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treezy254/py-plantuml.git",
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
            "pythonplantuml=pyplantuml.core:plantuml",
        ],
    },
    cmdclass={
        'test': RunTests,
        'docs': BuildDocs,
    },
)
