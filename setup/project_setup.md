
# Basic Installation & setup


```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev nginx
```


# Create a virtual environment

```
virtualenv -p python3 venv
```


# Install packages

```
pip install -r requirements.txt
```


# Run Migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Run Tests

```
python3 manage.py tests app.club.tests

```

# Run server & use api

```
python3 manage.py runserver
```

## API Information can be found here: 

```
https://docs.google.com/document/d/1kiEG6h5VAC6P9xYmF3BM0gsQ1ZcKMT1-brtkMAlZgrU/edit#
```