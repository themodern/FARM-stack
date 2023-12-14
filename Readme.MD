## Setup MongoBD Altas via Django


### 1. Setup virtual environment

``` bash
python -m venv venv
```

### 2. Start virtual environment
``` bash
source venv/bin/activate
```

### 3. Install Django
``` bash
pip install django
```

### 4. Create the django project folder and app folder
``` bash
django-admin startproject MyFirstDjangoProj
cd MyFirstDjangoProj
python manage.py myfirstapp
```

### 5. Install PyMongo and dnspython
``` bash
pip install pymongo
pip install dnspython
```

### 6. Create a "utils.py" file in project folder root (same location as manage.py)
``` bash
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                        )
    db_handle = client['db_name']
    return db_handle, client
```

### 7. access the connection detail by importing it into "myfirstapp/view.py"
``` bash
from pymongo import MongoClient
client = pymongo.MongoClient('connection_string')
db = client['db_name']
```

