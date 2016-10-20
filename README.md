# maintt
[![Code Climate](https://codeclimate.com/github/open-andela/maintt/badges/gpa.svg)](https://codeclimate.com/github/open-andela/maintt) [![Test Coverage](https://codeclimate.com/github/open-andela/maintt/badges/coverage.svg)](https://codeclimate.com/github/open-andela/maintt/coverage)

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

1. Fork and Clone the Repo

2. Create a VirtualEnv for the project, see instructions here.

3. `cd` into the `/maintt` package and run:
```
pip install -r requirements.txt
```
4. Run migrations
**Optional:** You will need to create migrations for the `api` application in case they are not there.

```
python manage.py makemigrations api
```

```
python manage.py migrate
```

5. Create a `superuser` for the purpose of testing
```
python manage.py createsuperuser
```
>_**TIP:** use admin / admin for simplicity._

6. Run the server:
```
python manage.py runserver [port-number]
```

7. Access DRF's _Browsable API_ at:
```
http://localhost:port/api/
```
Login with the _superuser_ created in step 5 above.


