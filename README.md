### 1. Prerequisites

- python3
- django

### 2. Start Project

1. Install all dependicies

   ```bash
   pip install -r requirements.txt
   ```

2. In the bottom of settings.py, add api key of sendgrid

   ```python
   SENDGRID_API_KEY='YOUR API KEY'
   ```

3. Start django project

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```