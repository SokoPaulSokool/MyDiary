# MyDairy

MyDiary is an online journal where users can pen down their thoughts and feelings.

#

[![Build Status](https://travis-ci.org/SokoPaulSokool/MyDiary.svg?branch=develop)](https://travis-ci.org/SokoPaulSokool/MyDiary)

[![Coverage Status](https://coveralls.io/repos/github/SokoPaulSokool/MyDiary/badge.svg?branch=endpoints)](https://coveralls.io/github/SokoPaulSokool/MyDiary?branch=endpoints)

[![Maintainability](https://api.codeclimate.com/v1/badges/79a0023ae3ce8ab4049e/maintainability)](https://codeclimate.com/github/SokoPaulSokool/MyDiary/maintainability)

#Easy to use Features

You can;

- Sign up to create your diary
- Login
- Add thoughts, ideas or anything to your diary
- View your records
- Delete your records
- Edit your records

These are the endpoints to test

| METHOD |      Endpoint      | Description                         |
| ------ | :----------------: | ----------------------------------- |
| GET    |  /api/v1/entries   | Get all entries                     |
| GET    | /api/v1/entries/id | Get specific entry using an id      |
| POST   |  /api/v1/entries   | Create a new entry                  |
| PUT    | /api/v1/entries/id | Modify a specific entry using an id |

## Site and api

Click [https://sokopaulsokool.github.io/MyDiary/UI](https://sokopaulsokool.github.io/MyDiary/UI) and start using the Diary

Click [https://blooming-escarpment-93743.herokuapp.com/api/v1/entries](https://blooming-escarpment-93743.herokuapp.com/api/v1/entries) for api calls

## Setting Up for Development

These are instructions for setting up MyDiary app in a development enivornment.

### Prerequisites

- Python 3.6

- Make a directory on your computer and a virtual environment

  ```
  $ mkdir myDiary
  ```

- Prepare the virtual environment

  ```
  $ pip install pipenv
  $ pipenv shell
  ```

- Clone the project repo

  ```
  $ git clone https://github.com/SokoPaulSokool/MyDiary.git
  ```

  ```
  $ cd ~/MyDiary
  ```

* Install necessary requirements

  ```
  $ pip install -r requirements.txt
  ```

* Run development server
  ```
  $ python app.py
  ```

This site should now be running at http://localhost:5000

### Run Tests

- Make sure pytest is installed

  ```
  $ py.test
  ```

### Coverage

```
$ py.test --cov-config .coveragerc  --cov=api --cov=database  tests/
```

- generated report

```
$ coverage html
```

```
$ cd ~/htmlcov
```

- open index.html in a browser
