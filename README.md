
## Env запушен для удобства тестирования
## Структура репозитория
1. `tests` = 'source/patients/tests' , 'source/accounts/tests'
2. `code` = 'source'
3. `docker` = `docker-compose.yml`
4. `migrations` = 'source/accounts/migrations' , 'source/patients/migrations'

## Инструкции по локальному запуску
git clone git@github.com:Arthur138/patients.git

cd patients

docker compose up --build

Во время запуска в базу накатываются фикстуры.

## Логин

http://127.0.0.1:8001/login/

- Пользователь с правами доктора

{

    "username":"doctor",
    "password":"password123"

}

- Пользователь без прав доктора

{

    "username":"nondoctor",
    "password":"password123"

}



## Список пациентов

http://127.0.0.1:8001/patients/

Headers:
    
    Authorization: Bearer <token>

