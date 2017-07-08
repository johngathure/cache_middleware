# Cache Middleware for Django

Automatically caches endpoints defined in the settings file(CACHE_URLS setting).
Expects a two tuple actual endpont and the number of seconds the page should be cached for.
```python
CACHE_URLS = [
    ('/todos/view_todos/', 60),
    ('/todos/get_todo/8521cccb-f683-4824-98f2-fa46c67526f1/', 60)
```

### Installation

```
mkdir venv
virtualenv -p /usr/bin/python2.7 .
git clone https://github.com/johngathure/cache_middleware.git
cd cache_middleware
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata todos.json
./manage.py runserver
```
