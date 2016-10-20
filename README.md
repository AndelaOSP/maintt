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

- [Django RESTFramework (DRF)]()
- [Django]
- [python-dotenv](https://github.com/theskumar/python-dotenv) - loading configuration files the [12Factor]() way.
- [mysqlclient]()

## Development Setup
>_Beginners Edition_

- Fork and Clone the Repo

- Create a VirtualEnv for the project, see instructions here.

- `cd` into the `/maintt` package and run:
```
pip install -r requirements.txt
```

- Run migrations
**Optional:** You will need to create migrations for the `api` application in case they are not there.

```
python manage.py makemigrations api
```

```
python manage.py migrate
```

- Create a `superuser` for the purpose of testing
```
python manage.py createsuperuser
```
>_**TIP:** use admin / admin for simplicity._

- Run the server:
```
python manage.py runserver [port-number]
```

- Access DRF's _Browsable API_ at:
```
http://localhost:port/api/
```
Login with the _superuser_ created in the previous step above.


