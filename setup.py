from setuptools import setup, find_packages


with open(file="flask_boilerplate/Readme.md", mode="r") as file:
    long_description = file.read()


setup(
    license="MIT",
    version="0.1.0",
    author="Kennartech",
    include_package_data=True,
    # scripts=["manage.py"],
    package_data={"flask_boilerplate": ["manage.py"]},
    name="flask_boilerplate",
    long_description=long_description,
    package_dir={"": "flask_boilerplate"},
    url="https://ktecht.pythonanywhere.com/",
    author_email="kennarttechnologies@gmail.com",
    packages=find_packages(where="flask_boilerplate"), 
    description="Flask boilerplate is use to generate an instance boilerplate for project",
    
    
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    extras_require = {
	"dev": ["pytest>=8.2.0", "twine>=5.0.0"],
    },
    
    install_requires=[
        "Flask",
        "flask-babel",
        "Flask-Caching",
        "Flask-Session",
        "Flask-Migrate",
        "Flask-SQLAlchemy"
    ],
    # django-admin = django.core.management:execute_from_command_line
    entry_points={
        "console_scripts": [
            "manage = flask_boilerplate.manage:main"  
        ],
    },
    
    # entry_points={
    #     "console_scripts": [
    #         "flask_boilerplate = manage:main",
    #     ],
    # },
)


