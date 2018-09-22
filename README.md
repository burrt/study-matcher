# Study Matcher

Tinder equivalent for finding study buddies

## Prerequisites

* SQLite3 with tools
* Virtualenv - optional but highly recommended

## Running

### Linux

```
# activate your virtualenv
./venv/bin/activate

FLASK_APP=study-matcher.py

# install pip package dependencies 
pip install -r requirements.txt
```

### Windows

```
# activate your virtualenv
\venv\Scripts\activate

set FLASK_APP=study-matcher.py

# install pip package dependencies 
pip install -r requirements.txt
```

### Database migrations

Make sure to upgrade databases - there is a way to do this automatically...

```
flask db upgrade
```
