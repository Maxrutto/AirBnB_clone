# AirBnB Clone - The Console/Command Interpreter

## Description

This is a group project done by [Maxmillan Rutto](https://github.com/Maxrutto) and [Praise Kipngeno](https://github.com/Victorpraise5). It's the first step towards building a full web application: an AirBnB clone.
This first step consists of a custom command-line interface for data management and the base classes for the storage of this data.

## Functionalities of this command interpreter

* Create a new object (ex: a new `User` or a new `Place`)
* Retrieve an object from a file or a database (Seralization and Deserialization)
* Do operations on objects (`count`, `compute stats`, etc...)
* Update attributes of an object (`update()`)
* Destroy an object(`destroy()`)

## Console and Command Usage
The console is a `Unix` shell-like command line user interface provided by the python `CmdModule`. It prints a prompt and waits for the user for input, for our project we used (`hbnb`)

| Command | Example   |
| ------- | --------- |
|Display help command| `(hbnb) help <command>`                                                        |             
|Create object (prints its id)	      | `(hbnb) create <class>`                                        |
|Destroy object	                      | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`|
|Show object                          | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`      |
|Show "all" objects or instances class|	`(hbnb) all` or `(hbnb) all <class>`                           |
|Run console	                        | `./console.py`                                                 |
|Quit console                         | `(hbnb) quit`                                                  |

Help command example

`(hbnb) help`

## Documented commands (type help <topic>):

`EOF`  `all`  `count`  `create`  `destroy`  `help`  `quit`  `show`  `update`

## Class Models Used

|  File	            |  Description  |   Attributes  |
|-----------------  | ------------- | ------------  |
| `base_model.py`   | The `BaseModel` class is inherited by other classes | `id`, `created_at`, `updated_at`                            |
| `user.py`         | `User` class stores user-related info               | `email`, `password`, `first_name`, `last_name`              |
| `city.py`	        | `City` class stores city-specific information       | `state_id`, `name`                                          |
| `state.py`	      | `State` class stores state-specific information     |	`name`                                                      |
| `place.py`	      | `Place` class stores full detailed outline          |                                                             |
|                   | of rental unit features	                            | `city_id`, `user_id`, `name`, `description`, `number_rooms`,|  
|                   |                                                     | `number_rooms`, `number_bathrooms`, `max_guest`,            |
|                   |                                                     | `price_by_night`, `latitude`, `longitude`, `amenity_ids`    |
| `review.py`       | `Review` class stores previous customer reviews     | `place_id`, `user_id`, `text`                               |  
|                   | and opinions                                        |                                                             |
| `amenity.py`      | `Amenity` class stores highlighted amenity          | `name`                                                      |
|                   | information                                         |                                                                |

  
## Environment

This project is interpreted/tested on `Ubuntu 14.04 LTS` using `python3` (version 3.11.5)

## Installation

* Clone this repository: `git clone https://github.com/richie-oomondi/AirBnB_command_interpreter.git`
* Access AirBnb directory: `cd AirBnB_command_interpreter`
* Run hbnb(interactively): `./console.py` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Tests

All the code is tested with the unittest module. The tests for all the classes and functions are in the `tests` folder.

## Authors

* [Praise Kipngeno](https://github.com/Victorpraise5)
* [Maxmillan Rutto](https://github.com/Maxrutto)