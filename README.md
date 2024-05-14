# Aiohttp Hash Task

## Запуск

Для того чтобы запустить приложение понадобится:

- Docker >= 1.12
- Python >= 3.12
- Клонировать данный проект локально

### Для запуска приложения в Docker:

1. **Создать образ:**
    
    ```sh
   docker build . -t aiohttp-app:latest
   ```

2. **Запустить контейнер:**

    ```sh
   docker run -p 8080:8080 aiohttp-app
   ```

### Для запуска приложение используя Python:

1. **Активировать виртуальное пространство:**

    ```sh
   source /path/to/venv/activate.sh
   ```
2. **Запустить приложение:**

    ```sh
   python main.py --host 127.0.0.1 --port 8080
   ```
   или если вы находитесь в главной директории
   
   ```sh
   python src/main.py --host 127.0.0.1 --port 8080
   ```

## Тестирование

### Pytest

   ```sh
   pytest
   ```