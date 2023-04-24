## About
The purpose of the application is to build an internal service for its 'employees which helps them to make a decision at the lunch place.

## Technical Requirements
- Use PEP8 for your Python code
- Python 3
- Django
- DRF
- JWT-Auth
- Docker (docker-compose)
- PostgreSQL

## First:
```shell
git clone https://github.com/Fhockk/restaurant_app.git
```

## How to run this project?
- Make sure you have docker installed
- Open the terminal and hit the following command:

Change the directory:
```shell
cd restaurant_app/
```
Build and Run
```shell
docker-compose up --build
```

## Endpoints:
| Endpoint                | CRUD Method | Result                                                                        |
|-------------------------|-------------|-------------------------------------------------------------------------------|
| `api/v1/employees/`     | POST        | Creates employee account. Allow Any.                                          |
| `api/v1/token/`         | POST        | Allows to obtain JWT token                                                    |
| `api/v1/token/refresh/` | POST        | Allows to refresh JWT token                                                   |
| `api/v1/token/verify/`  | POST        | Allows to verify JWT token                                                    |
| `api/v1/menu/`          | POST        | Allows to create menu. Authenticated allow only.                              |
| `api/v1/menu/today`     | GET         | Allows to get today's menus. Authenticated allow only.                        |
| `api/v1/restaurant/`    | POST        | Allows to create a restaurant with a specific name. Authenticated allow only. |
| `api/v1/vote/`          | POST        | Allows to vote for a specific menu. Authenticated allow only.                 |
| `api/v1/vote/today/`    | POST        | Allows to get results of today's votes. Authenticated allow only.             |

## Tests:
```shell
docker exec backend-web-1 python manage.py test
```
