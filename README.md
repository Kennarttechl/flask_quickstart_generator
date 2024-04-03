# flask_boilerplate_maker

The project generates boilerplate code for Flask applications.


# This project uses os and sys modules

`os module is purposely use in this project for some reasons`


1. File and Directory Management:
`Create, delete, rename, move, and check the existence of files and directories`.
**Get file/directory attributes (size, creation time, etc.).**
**List directory contents.**
**Change the current working directory.**

2. process management.
**Execute system commands and capture their output.** 
**Get information about running processes.**

3. Environment Variables:
**Get, set, and delete environment variables**

4. Path Manipulation:
**Join path components to create valid file paths across different operating systems.**
**Split paths into components.**
**Expand user's home directory in paths.**


*Functions:*

`os.getcwd(): Get the current working directory.`
`os.listdir(path): List files and directories in a directory.`
`os.mkdir(path): Create a directory.`
`os.makedirs(path, exist_ok=True): Create directories recursively, ignoring errors if they already exist (optional exist_ok argument).`
`os.remove(path): Delete a file.`
`os.rmdir(path): Delete an empty directory.`
`os.path.join(path1, path2, ...): Join path components into a valid path.`
`os.path.exists(path): Check if a file or directory exists.`
`os.system(command): Execute a system command and wait for its completion.`
`os.environ: A dictionary containing the environment variables.`



`sys moduel is purposely use for some reasons`

**Functions:**

`**sys.argv: A list containing the command-line arguments passed to the Python script when it's executed. The first element (sys.argv[0]) is always the script name itself, and subsequent elements are the arguments provided.**`

**sys.exit(exit_code=0): Exits the Python script with an optional exit code. The exit code can be used to indicate success (0) or an error condition (a non-zero value).**

**sys.getsizeof(object): Returns the approximate memory size, in bytes, of an object. This can be helpful for debugging memory usage.**

**sys.stdin: A standard input stream object, usually referring to the console from which the user can provide input.**

**sys.stdout: A standard output stream object, usually referring to the console where the program's output is displayed.**

**sys.stderr: A standard error stream object, usually referring to the console where error messages are displayed.**

**sys.version: A string containing the Python interpreter version information.**

# Attributes:

`sys.platform: A string indicating the operating system platform the script is running on (e.g., 'win32', 'linux', 'darwin').`

`sys.path: A list containing the search path for modules. This list determines where Python looks for modules when you use the import statement. You can modify sys.path to add custom directories containing modules.`

`sys.maxsize: The largest integer value a variable of data type Py_ssize_t can hold. This can be useful for understanding the limits of integer calculations.`

`sys.executable: The absolute path to the Python interpreter binary that executed the current script.`




**python -m flask_cli.main create-app my_demo_app**

pip install flask_cli-0.1.0.tar.gz
pip install flask_cli-0.1.0-py3-none-any.whl
python setup.py sdist bdist_wheel
pip install .
flask-cli create-app my_demo_app
flask-cli create-app my_demo_app
***
create_flask_app_structure()