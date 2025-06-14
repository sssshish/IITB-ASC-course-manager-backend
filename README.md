# IIT ASC Course Manager (Backend)

This is the Django REST backend for managing courses and course instances.

### 📚 Features
- Django REST Framework API
- Supports CRUD for:
  - Courses
  - Course Instances (by year and semester)

### 📦 Setup
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py migrate
python manage.py runserver
