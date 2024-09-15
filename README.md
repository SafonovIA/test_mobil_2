# Test Github api

### Установите зависимости.
```sh
pip install -r requirements.txt
```

### Создайте Токен.
- Перейдите на [GitHub Settings](https://github.com/settings/tokens).
- Нажмите "Generate new token(classic)".
- Выберите необходимые разрешения (поставте галочку напротив "repo" и "delete_repo").
- Нажмите "Generate token" и скопируйте сгенерированный токен.

### Добавьте переменные в .env
- GITHUB_USERNAME - Ваш username из github
- GITHUB_TOKEN - Токен который вы скопировали
- REPO_NAME - Название нового репозитория

Запустите тест
```sh
pytest
```

