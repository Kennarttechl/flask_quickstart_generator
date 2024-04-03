from setuptools import setup, find_packages


setup(
    name="flask-cli",
    version="0.1.0",
    packages=find_packages(),
    scripts=["cli_startup/startup"],
    install_requires=[],
    entry_points={"console_scripts": ["cli_startup = startup"]},
)
