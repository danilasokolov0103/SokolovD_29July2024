
### Как запустить тесты?


1.Создать виртуальное окружение
```
python3 -m virtualenv venv
```

2.Запустить виртуальное окружение
```
source venv/bin/activate
```

3.Установить poetry
```
pip3 install poetry==1.1.13  
```

4.Установить зависимости
```
python3 -m poetry install
```

5.Запустить тесты
```
python3 -m poetry run pytest
```