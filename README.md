# About
Ця программа може знаходити відровіді до тестів naurok.
Ми маємо свій cli інструмент та вебсайт.

Наш веб сайт. [site](https://naurok-test.tk)

# Як запустити cli
```
git clone https://github.com/FtcSerhiy/naurok-backend.git
cd naurok-backend
poetry install
poetry run cli
```
Для запуску вам потрібен менедер пакетів пайтон poetry.

# Встановлення poetry
```
pip3 install poetry --upgrade pip
```

# Параметри cli
poetry run cli 'назва тесту' предмет(обов'язково в ангомовному форматі) клас(тільки число) кількість запитань(тільки число)

# Як розгорнути в себе на сервері
```
echo PASSWORD | docker login ghcr.io -u username --password-stdin
docker pull ghcr.io/ftcserhiy/naurok-backend
docker run -d -p 8000:8000 ghcr.io/ftcserhiy/naurok-backend
```

# Технології які використовувалися в проєкті
Веб фреймворк [bold black]Flask (та його шаблонізатор)
Бібліотека для парсингу [bold black]BeautifulSoup[bold black]
Біблітока для cli [bold black]rich[bold black]
[bold black]Docker[bold black]
github [bold black]actions[bold black]
[bold black]github container registry[bold black]
Менеджер пакетів poetry
Лінтер autopep8
Біблітоека для тестування pytest
Веб сервер gunicorn
Віддалена ide для розробки gitpod

