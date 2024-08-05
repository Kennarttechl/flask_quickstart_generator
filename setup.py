from setuptools import setup, find_packages


with open(file="Readme.md", encoding="utf-8", mode="r") as file:
    long_description = file.read()

    
# Bump version:
setup(
    name="flask_quickstart_generator",
    version="1.1.2",
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
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Flask",
        "Flask-Assets",
        "Flask-Bcrypt",
        "flask-babel",
        "Flask-Caching",
        "Flask-Limiter",
        "Flask-Login",
        "Flask-Migrate",
        "Flask-Session",
        "Flask-Login",
        "Flask-SQLAlchemy",
        "Flask-WTF",
        "WTForms",
        "cssmin",
        "jsmin",
        "pillow",
        "rcssmin",
        "rjsmin",
    ],
    entry_points={
        "console_scripts": [
            "flask-manage = flask_quickstart_generator:main",
        ],
    },
)
