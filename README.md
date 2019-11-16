# Uk Postcode finder and validator

A simple package to find, validate and format UK postcodes build with python.

This library use [Postcodes.io](https://postcodes.io/) API to find data regarding postcodes.

## Requirements

- Pip 3
- Python 3.6
- postcodes-io-api==0.0.4

(N.B.: postcodes-io-api will be installed following the next steps)

## Install

1. Clone this repository

```
$ git clone https://github.com/gello94/uk_postcode_finder_and_validator
```

2. Move into the library directory
```
$ cd uk_postcode_finder_and_validator
```

3. Install requirements.txt
```
$ pip install -r ./requirements.txt
```

4. Install library
```
$ pip install -e .
```

4. Go back into the main directory
```
$ cd 
```

## How to use

The app.py file present in the library main directory is an example app of how this library works.
If you want to test the library with this example app run in your terminal the command: 

1. Move into the library directory
```
$ cd uk_postcode_finder_and_validator
```

2. Run the App
```
$ python3 app.py
```

1. In your python file import the library:

```
$ from postcode.postcode import *
```

If you want to import only a specified function you can replace '*' with the name of the function.

The main functions are:

1. ```get_a_postcode(postcode)``` - To get Postcode data

2. ```postcode_is_valid(postcode)``` - To validate a Postcode

3. ```format_code(postcode)``` - To format a given Postcode in lowercase or without the spacing

4. ```get_nearest_postcode(postcode)``` - To get nearest Postcodes

## Testing

To get random postcodes I used - https://www.doogal.co.uk/PostcodeGenerator.php

Tu run the test file:

1. Move into the library directory
```
$ cd uk_postcode_finder_and_validator
```

2. Run Test.py
```
$ python3 test.py
```

You can as well test the app by running the app.py test app I created for testing and as example of how this library could be used.