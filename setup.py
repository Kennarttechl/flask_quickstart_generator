from setuptools import setup, find_packages


with open(file="Readme.md", encoding="utf-8", mode="r") as file:
    long_description = file.read()


setup(
    name="flask_boilerplate",
    version="1.0",
    description="Flask Boilerplate streamlines Flask development by automatically generating a structured folder layout, expediting project setup.",
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
            "flask-manage = flask_boilerplate:main",
        ],
    },
)
