Быстрый запуск

```bash
cp .env.example .env
# заполняете OPENAI_API_KEY и TELEGRAM_TOKEN
docker-compose up --build
```

Откроется:
- Frontend: http://localhost:5173
- API: http://localhost:8000

Админ:
```
login: admin
password: admin
```

---

Архитектура

- **backend** — FastAPI + SQLAlchemy + Alembic + Scraper worker  
- **frontend** — React (Vite) SPA  
- **bot** — Telegram (aiogram) + OpenAI Function Calling  
- **db** — PostgreSQL  

Сервисы запускаются через docker‑compose.

---

API

### POST /api/login
Авторизация.

```
POST /api/login
{
  "username": "admin",
  "password": "admin"
}
```

Ответ:
```
{ "access_token": "JWT" }
```

GET /api/cars
Список автомобилей (JWT).

---

Telegram‑бот

Пример запросов:
- Найди красную BMW до 2 млн
- Toyota 2018
- черный Mercedes

LLM извлекает фильтры → бот делает запрос к API → возвращает список.

---

Scraper

Воркер периодически обращается к:
```
https://carsensor.net/api/search
```

Поля:
- brand
- model
- year
- price
- color
- url

Логика:
- upsert по url
- обновление изменений
- добавление новых

Интервал: `SCRAPER_INTERVAL` (env)

---

Миграции

Alembic выполняется автоматически при старте backend:

```
alembic upgrade head
```

---

Переменные окружения

См. `.env.example`

Обязательные:
- DATABASE_URL
- JWT_SECRET
- OPENAI_API_KEY
- TELEGRAM_TOKEN

---

Структура

```
backend/
frontend/
bot/
docker-compose.yml
.env.example
```
