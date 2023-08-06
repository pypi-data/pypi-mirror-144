import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="rengine-workouts",
    version="1.0.3",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/noahsolomon0518/rengine",
    author="noahsolomon0518",
    author_email="noahsolomon0518@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={"": "rengine"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "rengine=rengine.__main__:run",
        ]
    },
)