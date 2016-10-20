# maintt
[![Build Status](https://travis-ci.org/AndelaOSP/maintt.svg?branch=develop)](https://travis-ci.org/AndelaOSP/maintt) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/22b9d145fdba4af7a23ce2c4dac8e232)](https://www.codacy.com/app/AndelaOSP/maintt?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andelaosp/maintt&amp;utm_campaign=Badge_Grade)

A maintenance tracker system

- See [the project proposal here](https://github.com/open-andela/project-proposals/issues/2)
- Preliminary guidlines on how to get started with the project are [here in the wiki](https://github.com/open-andela/maintt/wiki)


## Dependencies

They are all listed in `maintt/requirements.txt`. Install them via:
```
pip install -r <file-name>
```
**Main:**
- [Django RESTFramework (DRF)](http://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [python-dotenv](https://github.com/theskumar/python-dotenv) - loading configuration files the [12Factor](https://12factor.net/config) way.
- [mysqlclient](https://pypi.python.org/pypi/mysqlclient)

**Dev Dependencies:**
- [fake-factory](https://pypi.python.org/pypi/fake-factory) - for faking fixtures for tests.

## Development Setup
- See the [wiki entry here](https://github.com/AndelaOSP/maintt/wiki/Dev-Setup) for details.
