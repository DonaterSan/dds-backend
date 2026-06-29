# ДДС — Веб-сервис управления движением денежных средств

Веб-приложение на Django для учёта, управления и анализа поступлений и списаний денежных средств.

## Возможности

- **CRUD записей ДДС** — создание, просмотр, редактирование, удаление
- **Фильтрация** — по дате (период), статусу, типу, категории, подкатегории
- **Управление справочниками** — статусы, типы, категории, подкатегории
- **Логические зависимости** — категории привязаны к типам, подкатегории к категориям
- **Валидация** — на клиенте и сервере
- **REST API** — полноценный API на Django REST Framework

## Стек

- Python 3.10+
- Django 6
- Django REST Framework
- django-filter
- SQLite
- Bootstrap 5 (CDN)

## Запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/DonaterSan/dds-backend.git
cd dds-backend
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 3. Применить миграции

```bash
python manage.py migrate
```

### 4. (Опционально) Загрузить тестовые данные

```bash
python manage.py seed
```

### 5. Запустить сервер

```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://127.0.0.1:8000/

## Структура страниц

| URL | Описание |
|-----|----------|
| `/` | Главная — таблица записей ДДС с фильтрами |
| `/references/` | Управление справочниками |
| `/api/` | REST API (browsable) |
| `/admin/` | Админ-панель Django |

## API эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET/POST | `/api/records/` | Список / создание записей |
| GET/PUT/DELETE | `/api/records/{id}/` | Просмотр / редактирование / удаление записи |
| GET/POST | `/api/statuses/` | Статусы |
| GET/POST | `/api/types/` | Типы |
| GET/POST | `/api/categories/` | Категории (фильтр: `?type=ID`) |
| GET/POST | `/api/subcategories/` | Подкатегории (фильтр: `?category=ID`) |

### Фильтрация записей

```
GET /api/records/?date_from=2025-01-01&date_to=2025-12-31&status=1&type=2&category=3
```
