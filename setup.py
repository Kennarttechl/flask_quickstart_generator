from setuptools import setup, find_packages


with open(file="Readme.md", encoding="utf-8", mode="r") as file:
    long_description = file.read()


# Bump version:
setup(
    name="flask_quickstart_generator",
    version="1.1.3",
    description="Flask Quickstart Generator streamlines Flask development by automatically generating a structured folder layout, expediting project setup.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kennartech",
    author_email="kennartdev@gmail.com",
    maintainer="Kennartech.Dev",
    maintainer_email="kennartdev@gmail.com",
    url="https://ktecht.pythonanywhere.com/",
    include_package_data=True,
    package_data={"": ["requirements.txt", "Readme.md", "LICENSE.txt"]},
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python Python :: 3 Python :: 3:: Only Python :: 3.10     Python :: 3.11 Python :: 3.12 Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Flask",
        "WTForms",
        "pillow",
        "psycopg2",
        "waitress",
        "Flask-WTF",
        "Flask-Login",
        "flask-babel",
        "Flask-Login",
        "Flask-Bcrypt",
        "python-dotenv",
        "Flask-Caching",
        "Flask-Limiter",
        "python-dotenv",
        "Flask-Migrate",
        "Flask-Session",
        "Flask-SQLAlchemy",
    ],
    entry_points={
        "console_scripts": [
            "flask-manage = flask_quickstart_generator:main",
        ],
    },
)

