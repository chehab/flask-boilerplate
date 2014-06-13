
Flask Application Boilerplate
=============================

A Simple Flask Application Boilerplate.

## Setup


Before setting up this boilerplate flask application. It's prepared to set it up with Python 3.x in a virtual environment `virtualenv` 

```bash
$ pip install virtualenv
```

`cd` to the Boilerplate's root Directory and create a `virtualenv`, and activate it. 

```bash
$ virtualenv env
$ source env/bin/activate
```

Next install the requirements from requirement.txt using `pip`

```bash
$ pip install -r requirement.txt
```

using `git` to get the submodules, from `.gitmodules`.

```bash
$ git submodule init
$ git submodule update
```

Now run the server `$ ./run.py` the default port is 3000, run with flag `-h` for help `$ ./run.py -h`


## Files, Folders Structure
 
 ```
    ├── flask_app/
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── assets/
    │   ├── controllers/
    │   ├── models/
    │   └── views/
    │     
    ├── requirement.txt
    └── run.py
 ```
 
 
- `requirement.txt`
    <br>&nbsp;&nbsp;&nbsp;Python required modules like `Flask` obviously.
    <br>&nbsp;&nbsp;&nbsp;Usage: `$ pip install -r requirement.txt`
 
- `run.py`
    <br>&nbsp;&nbsp;&nbsp;Imports Flask `app` instance form `flask_app` module. and runs Flask server.
    <br>&nbsp;&nbsp;&nbsp;Usage: `$ ./run.py -h` 
 
- `flask_app/`
    <br>&nbsp;&nbsp;&nbsp;flask application directory/
 
 - `flask_app/__init__.py`
    <br>&nbsp;&nbsp;&nbsp;initialize `flask_app` as Python module, also this where `flask.Flask` object is instantiated.
   
 - `flask_app/routes.py`
    <br>&nbsp;&nbsp;&nbsp;this where app URL/routes are defined.
   
 - `flask_app/assets/`
    <br>&nbsp;&nbsp;&nbsp;flask "static" directory. defined at `flask_app/__init__.py` on line 5:23 
 
 - `flask_app/views/`
    <br>&nbsp;&nbsp;&nbsp;flask "template" directory. defined at `flask_app/__init__.py` on line 5:47 
 
 - `flask_app/controllers/`
    <br>&nbsp;&nbsp;&nbsp;App view controllers should be defined here.
 
 - `flask_app/models/`
    <br>&nbsp;&nbsp;&nbsp;Application logic "models" should be defined here.
