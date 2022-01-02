# Migrate the default models first:
- `python manage.py migrate`
# Migrate our app models created:
- `python manage.py makemigrations todos`
# SQL
- `python manage.py sqlmigrate todos 0001`
- `python manage.py migrate`
