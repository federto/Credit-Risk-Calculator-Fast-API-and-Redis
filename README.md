# Fast Api ML API credit risk assignment


Below is the full project structure:

```
├── api
│   ├
│   ├── controller
│   ├── feedback
│   ├── lib
│   ├── model_database
│   ├── templates
│   │── Dockerfile
├   ├── main.py
├   ├── middleware.py
├   ├── requirements.txt
├   ├── schemas.py
├   ├── settings.py
├
├── model
├   ├── data
├   ├── model_notebooks
├   ├── Dockerfile
├   ├── ml_service.py
├   ├── model_lightgbm.pkl
├   ├── preeprocessing_pipeline.pkl
├   ├── requirements.txt
├   └── settings.py
├
├── users.db
```

Let's take a quick overview on each module:

- api: It has all the needed code to implement the communication interface between the users and our service. It uses FastAPI and Redis to queue tasks to be processed by our machine learning model.
    - `api/main.py`: Setup and launch our Fast api.
    - `api/settings.py`: It has all the API settings.
    - `api/templates`: Here we put the .html files used in the frontend.
    - `api/controller`: Generate Users.
    - `api/lib`: Check pass.
    - `api/model_database`: database users.
    - `api/feedback` : feedback csv

- model: Implements the logic to get jobs from Redis and process them with our Machine Learning model. When we get the predicted value from our model, we must encole it on Redis again so it can be delivered to the user.
    - `model/data`: the data used
    - `model/model_notebooks`: all the experiments notebooks
    - `model/ml_service.py`: Runs a thread in which it get jobs from Redis, process them with the model and returns the answers.
    - `model/settings.py`: Settings for our ML model.
    - `api/settings.py`: It has all the model settings.


- user.db : the user database with sqlalchemy


## Install and run

To run the services using compose:

```bash
$ docker-compose up --build -d
```

To stop the services:

```bash
$ docker-compose down
```

## Create a user and impute personal info

you need to create a user or sign in if you have one and ask for a loan with your personal info. if the model dont approve the loan you can send your personal info as feedback

scores + 500 rejectec
scores - 500 approve