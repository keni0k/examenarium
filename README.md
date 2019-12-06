# Examenarium (python + django)

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). 
To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ heroku git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started

python3 -m venv getting-started
pip install -r requirements.txt

createdb python_getting_started

python manage.py migrate
python manage.py collectstatic

heroku local web -f Procfile.windows
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ git push heroku master

heroku run python manage.py migrate
heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
