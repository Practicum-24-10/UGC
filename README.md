# Сервис UGC

### Запуск приложения
- Создать файл .env в директории ugc_service/ по примеру ugc_service/.env.example и из корня проекта выполнить команду:
```
docker compose -f ugc_service/docker-compose.yml up
```

### Запуск приложения для разработки (с проброской портов и монтированием директории приложения)
- Создать файл .env в директории ugc_service/ по примеру ugc_service/.env.example и из корня проекта выполнить команду:
```
docker compose -f ugc_service/docker-compose.yml -f ugc_service/docker-compose.override.yml up
```
### Запуск тестов FastApi
- Создать файл .env в директории ugc_service/tests/functional/ по примеру ugc_service/tests/functional/.env.example и из корня проекта выполнить команду:
```
docker compose -f ugc_service/tests/functional/docker-compose.yml up
```
- Для запуска локальных тестов необходимо создать файл .env в директории ugc_service/tests/functional/ по примеру ugc_service/tests/functional/.env.dev.example и запустить приложение в Docker