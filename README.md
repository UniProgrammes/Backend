# How to run the server

## Step 1 - Env setup
Create a `.env` file inside api and fill it with the variables indicated in `.example.env`.

## Step 2 - Create virtualenv (recommended)
Create a virtual environment running the following steps in the console.

1. Create virtual environment
``` bash
  python3 -m venv venv
```
2. Activate env
``` bash
  source venv/bin/activate
```

## Step 3 - Install requirements
``` bash
pip install -r requirements.txt
```

## Step 4 - Run server
``` bash
python3 manage.py runserver
```


___


# Make and run migrations

## Step 1
Create or add modifications to the model in the folder `model` of the app.

## Step 2 - Create migrations
Run:
``` bash
python3 manage.py makemigrations
```
This sphould create a file in the folder `migrations` of your app.

## Step 3 - Run migrations
Run:
``` bash
python3 manage.py migrate
```
