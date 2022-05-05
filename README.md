# Тестовое задание - создать простой веб сервис
Сервис принимает POST запрос с параметром содержащим количество вопросов, обращается к публичному API с вопросами для викторин и сохраняет эти вопросы в базу данных. Если вопрос не уникальный, то делается дополнительный запрос к внешнему API для получения другого вопроса. Операция повторяется пока не будет получено необходимое количество уникальных вопросов для записи в базу данных. 
В ответ сервис возвращает последний вопрос для викторины из предыдущего запроса.

## Описание:
- Фреймворк Fastapi
- База данных PostgreSQL

Получить вопрос:
```
    POST /question
    
    Request Headers
    Content-Type  application/json
	
	Body
    {
      "amount": <amount>
    }
```

## Подготовка и запуск проекта
### Скопируйте проект:
```
git clone https://github.com/vkorey/test_api_questions.git
```
### Перейдите в папку с проектом и запустите:
```
cd test_api_questions
```
### Если необходимо отредактируйте файл .env с настройками базы данных:
```
DB_USER="root"
DB_PASS="root"
DB_HOST="db"
DB_PORT=5432
DB_NAME="questions"
```

#### Для тестирования API в проекте есть файл с коллекцией запросов Postman - test_api_questions.postman_collection.json
