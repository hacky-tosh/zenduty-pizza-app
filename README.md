# zenduty-pizza-app

<br />Installation
<br />1. Clone the repository:

```bash
   https://github.com/hacky-tosh/zenduty-pizza-app.git
```
2. Install the required dependencies:
<br />
    ```bash
    cd QuizApp
    pip install -r requirements.txt
   ```
<br />3. Apply the database migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate

<br />4. Run the development server:
```bash
   python manage.py runserver
```
In another terminal
```bash
   python -m celery -A pizzeria worker
```

<br />The application will be accessible at http://localhost:8000/.
