# REPLIQ Test

### Create Virtual Environment and install packages
```
    python -m venv .repliq_env
    source .repliq_env/biv/active
    pip install -r requirements.txt
```
### Run the Project 
```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
```

### API Gateway - Swagger
```
    http://127.0.0.1:8000/swagger/
```
### API Documentation - Redoc
```
    http://127.0.0.1:8000/redoc/
```

## Testing - PyTest
```
    pytest -v
```


## [Optional Section]
### Containerizing the project - Docker
 - Build the project with docker-compose
    ``` 
        # if building for the first time
        docker-compose up --build
   
        # if wishing to run the pre-built containers
        docker-compose up -d
    ```
 - Swagger and redoc
   ``` 
   http://127.0.0.1:8001/swagger/
   http://127.0.0.1:8001/redoc/
   # admin panel
   http://127.0.0.1:8001/admin/ 
   # username & pass: repliq
   ```
     