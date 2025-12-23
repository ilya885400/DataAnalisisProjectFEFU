# Weather Monitoring System

Система генерирует синтетические данные о погоде и визуализирует их.

## Запуск
1. Соберите и запустите контейнеры:
   ```bash
   docker compose up -d
   ```
2. Инициализируйте базу данных Redash (только при первом запуске):
   ```bash
   docker compose run --rm redash-server create_db
   ```

## Доступ к сервисам
- **Redash**: [http://localhost:5000](http://localhost:5000) (нужно создать админа при первом входе)
- **Jupyter**: [http://localhost:8888](http://localhost:8888) (пароль/токен: `docker`)
- **Postgres**: localhost:5432 (user: `user`, pass: `pass`, db: `weather_db`)

## Настройка Redash
1. Зайдите в Settings -> Data Sources.
2. Добавьте **PostgreSQL**.
3. Host: `db`, Database: `weather_db`, User: `user`, Password: `pass`.
4. Создайте Query: `SELECT * FROM weather_metrics ORDER BY timestamp DESC LIMIT 100;`
