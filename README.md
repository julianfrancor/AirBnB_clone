# 0x00. AirBnB clone - The console

## Resources:books:
Read or watch:
* []()
* []()

---
## General Information and contents

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
---

#### [AirBnB clone - The console](https://intranet.hbtn.io/projects/263)
For further information, click on the previous link.

## General information

* description of the project
* description of the command interpreter:
* how to start it
* how to use it
* examples
* You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
* You should use branches and pull requests on Github - it will help you as team to organize your work

## Prerequisites

For further installation is necessary to set this program on Ubuntu 14.04 LTS using Vagrant in VirtualBox.

You need to install this software
```
1. VirtualBox - Virtual Machine
2. Vagrant
3. Emacs
4. Vim/Vi
5. VSCode
6. Usage: ./console.py
```

## Environment

This project was constructed and tested in the previous set up and debugged with GCC version 4.8.4.


## Instalation.
Follow the following instructions to get a copy of the program and run in your local machine.

- Clone the following repository.
 > `https://github.com/julianfrancor/AirBnB_clone.git`

- Run the program
 > `./console.py`



## Built with...

- Visual Studio Code - Coding and structuring.
- Clion - Debugging and testing outcomes.

---
### [0. README, AUTHORS]
* Write a README.md:
- description of the project
- description of the command interpreter:
- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
- You should use branches and pull requests on Github - it will help you as team to organize your work

### [1. Be PEP8 compliant!]
* Write beautiful code that passes the PEP8 checks.

### [2. Unittests]
* All your files, classes, functions must be tested with unit tests

### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes

### [4. Create BaseModel from dictionary](./models/base_model.py)
* Now it’s time to re-create an instance with this dictionary representation

### [5.  Store first object](./models/engine/file_storage.py)
* Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances

### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:

### [7. Console 0.1](./console.py)
* Update your console.py to have these commands:
- create
- show
- destroy
- all
- update

### [8. First User](./models/user.py)
* Write a class User that inherits from BaseModel

### [9. More classes!]
* Write all those classes that inherit from BaseModel
- State
- City
- Amenity
- Place
- Review

### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
* Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

---

##  Authors

- [GitHub - Julian Franco Rua](https://github.com/julianfrancor)

- [GitHub - Juan Pablo Yepes](https://github.com/PabloYepes27)
