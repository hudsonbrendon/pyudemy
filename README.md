# Pyudemy


[![Build Status](https://travis-ci.org/hudsonbrendon/pyudemy.svg?branch=master)](https://travis-ci.org/hudsonbrendon/pyudemy)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/pyudemy.svg?style=flat)](https://github.com/hudsonbrendon/pyudemy/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

Simple integrate of API udemy.com with python

![Logo](logo.png)

# Quick start

```bash
$ pip install pyudemy
```
or

```bash
$ python setup.py install
```

# Authentication

To make any calls to Udemy REST API, you will need to create an API client. API client consists of a bearer token, which is connected to a user account on Udemy.

If you want to create an API client, [Sign up on udemy.com](https://www.udemy.com/join/) and go to API Clients page in your user profile. Once your API client request is approved, your newly created [API client](https://www.udemy.com/user/edit-api-clients/) will be active and your bearer token will be visible on [API Clients](https://www.udemy.com/user/edit-api-clients/) page.

# Usage

With your key in hand, it's time to authenticate, so run:

```python
>>> from pyudemy import Udemy

>>> udemy = Udemy(<CLIENT_ID>, <CLIENT_SECRET>)
```

# Courses

Returns list of courses.

To see the list of accepted parameters go to:
[https://www.udemy.com/developers/methods/get-courses-list/](https://www.udemy.com/developers/methods/get-courses-list/)

```python
>>> udemy.courses()
```
or

```python
>>> udemy.courses(page=1, page_size=1, ...)
```

# Course detail

Returns course with specified id.

To see the list of accepted parameters go to:
[https://www.udemy.com/developers/methods/get-courses-detail/](https://www.udemy.com/developers/methods/get-courses-detail/)

```python
>>> udemy.course_detail(<id>)
```

# Public curriculum

Returns list of curriculum items.

To see the list of accepted parameters go to:
[https://www.udemy.com/developers/methods/get-publiccurriculum-list/](https://www.udemy.com/developers/methods/get-publiccurriculum-list/)

```python
>>> udemy.public_curriculum(<id>)
```
or

```python
>>> udemy.public_curriculum(<id>, page=1, page_size=1)
```

# Course reviews

Returns list of curriculum items.

To see the list of accepted parameters go to:
[https://www.udemy.com/developers/methods/get-coursereviews-list/](https://www.udemy.com/developers/methods/get-coursereviews-list/)

```python
>>> udemy.course_reviews(<id>)
```
or

```python
>>> udemy.course_reviews(<id>, page=1, page_size=1)
```

# Dependencies

- Python 3.5
- [Pipenv](https://github.com/kennethreitz/pipenv)
- [requests](http://docs.python-requests.org/en/latest/)

# License

[MIT](http://en.wikipedia.org/wiki/MIT_License)
