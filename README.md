# How to run the server

## Step 1 - Docker
You need to have docker installed in your PC.

## Step 2 - Build
Run in the terminal:
``` bash
  make build
```


## Step 3 - Makemigrations and run them
1. Create migrations
``` bash
  make makemigrations
```

2. Run migrations
``` bash
  make migrate
```

## Step 4 - Run server
``` bash
make runserver
```

___


# Make and run migrations

## Step 1
Create or add modifications to the model in the folder `model` of the app.

## Step 2 - Create migrations
Run in the terminal:
``` bash
make makemigrations
```
This should create a file in the folder `migrations` of your app.

## Step 3 - Run migrations
Run:
``` bash
make migrate
```
