# MC_IKIT

## 1. О проекте

**Название проекта:** Афиша молодежного центра ИКИТ СФУ.

**Назначение системы:** система предназначена для структурирования и учёта мероприятий молодежного центра, а также для анализа деятельности центра.

## 2. Команда проекта

| Участник | Роль |
|---|---|
| Ильина Ксения А. | Руководитель проекта, специалист по развертыванию |
| Илющенко Богдан | Разработчик, архитектор |
| Новикова Мария | Аналитик проекта |
| Михалко Арина | Тестировщик |

Подробнее о распределении обязанностей — в [docs/team_roles.md](docs/team_roles.md).

## 3. Технологический стек

- **Python** — язык программирования.
- **Django** — веб-фреймворк.
- **SQLite** — система управления базами данных.

## 4. Трекер задач

[Перейти к Issues проекта](https://github.com/Ksenon011999/MC_IKIT/issues/2).

## 5. Локальный запуск

Команды из корня репозитория (Python 3.11):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pre_commit install
$env:DJANGO_DEBUG = "1"
$env:DJANGO_DB_PATH = Join-Path $PWD "local.sqlite3"
cd MCIKIT
python manage.py migrate
python manage.py runserver
```

В Bash активируйте окружение командой `source .venv/bin/activate`, затем задайте
`export DJANGO_DEBUG=1 DJANGO_DB_PATH="$PWD/local.sqlite3"` перед переходом в `MCIKIT`.
Для ручной проверки откройте `http://127.0.0.1:8000/health`. Ожидается HTTP 200
с JSON `{"status":"ok"}`.

## 6. Проверки и тесты

Из корня репозитория:

```bash
python -m ruff format --check MCIKIT
python -m ruff check MCIKIT
python -m pre_commit run --all-files
```

Из каталога `MCIKIT`, с теми же переменными окружения:

```bash
python manage.py check
python -m coverage run --rcfile=../pyproject.toml manage.py test
python -m coverage report --rcfile=../pyproject.toml
python -m coverage html --rcfile=../pyproject.toml
```

HTML-отчёт появится в `MCIKIT/htmlcov/index.html`. CI прикладывает его к запуску
как артефакт `module4-coverage`.

- [Практическая работа №4](docs/module4/team_plan.md)
- [Настройка рабочего места](docs/module4/environment_setup.md)
- [Развертывание и переменные окружения](docs/module4/deployment.md)
- [Аутентификация и восстановление пароля](docs/module4/authentication.md)
