# About
Ця программа може знаходити відровіді до тестів [naurok](https://naurok.com.ua).
Ми маємо свій cli інструмент та вебсайт.

Наш веб сайт: <https://naurok-test.tk>.

# Як запустити cli
```
git clone https://github.com/FtcSerhiy/naurok-backend.git
cd naurok-backend
poetry install
poetry run cli
```

Для запуску вам потрібен менедер пакетів пайтон [poetry](https://python-poetry.org).

# Встановлення poetry
```
pip3 install poetry --upgrade pip
```

# Параметри cli
poetry run cli `назва тесту` `предмет(обов'язково в англомовному форматі)` `клас(тільки число)` `кількість запитань(тільки число)`

# Як розгорнути в себе на сервері
```
echo PASSWORD | docker login ghcr.io -u username --password-stdin
docker pull ghcr.io/ftcserhiy/naurok-backend
docker run -d -p 8000:8000 ghcr.io/ftcserhiy/naurok-backend
```

# Технології які використовувалися в проєкті:
- Веб фреймворк [Flask (та його шаблонізатор)](https://flask.palletsprojects.com/en/2.2.x/)
- Бібліотека для парсингу [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- Біблітока для cli [rich](https://pypi.org/project/rich/)
- [Docker](https://www.docker.com/)
- [github actions](https://github.com/features/actions)
- [github container registry](https://docs.github.com/ru/enterprise-server@3.6/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- Менеджер пакетів [poetry](https://python-poetry.org)
- Лінтер [autopep8](https://pypi.org/project/autopep8/)
- Біблітоека для тестування [pytest](https://pytest.org)
- Веб сервер [gunicorn](https://gunicorn.org)
- Віддалена ide для розробки [gitpod](https://www.gitpod.io)

# Зв'язатися зі мною
- Telegram [ftc](https://t.me/ftcserhiy)
- email: <serhiyftc@tuta.io>

