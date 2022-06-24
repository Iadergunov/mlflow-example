## Пример MLflow project

Пример для запуска MLflow project в docker-е, на базе iris датасета из библиотеки scikit-learn.

### Запуск проекта

Изначально необходимо установить [MLflow](https://www.mlflow.org/) (pip install mlflow), а также установить 
[Docker](https://docs.docker.com/get-docker/).

Затем необходимо собрать docker образ, в котором будет запускаться проект. 
Используйте то же имя образа, которое указано в поле docker_env.image в файле MLproject. 
В этом примере использовано имя образа — iris_project. 

Команда для сборки образа с этим именем:

```
docker build -f .dockerfile -t iris_project .
```
Также необходимо указать путь до mlflow сервера, задав переменную окружения MLFLOW_TRACKING_URI. 
Наконец, чтобы запустить данный проект, воспользуйтесь командами:

#### Для локального репозитория

```
mlflow run MLproject --experiment-name=iris
```
#### Git вариант
```
mlflow run git@github.com:iadergunov/mlflow-example.git#MLProject --experiment-name=iris
```
### Запуск Mlflow server

Для сохранения результатов запуска проекта необходим запущенный mlflow server. 
Вы можете поднять его локально в docker-е. Изначально потребуется собрать docker образ:

```
docker build -f mlflow.dockerfile -t mlflow .
```

И воспользоваться файлом docker-compose.yml

В определении переменных окружения PUBLICHOST и в ARTIFACT_ROOT присутствует IP адрес HOST_IP - это должен быть IP 
адрес вашей машины. Его можно задать через переменную окружения или задать в файле docker-compose вручную.
Также вам потребуется обновить секцию volumes, указав валидные пути для сохранения данных на вашей машине.

Команда для запуска mlflow:
```
docker-compose up -d
```

В результате мы можем посмотреть UI mlflow по адресу: http://{HOST_IP}:5000