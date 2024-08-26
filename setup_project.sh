#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found! Creating one now..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Navigate to the Django project directory (relative path)
cd "$(dirname "$0")"

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Set up the DJANGO_SETTINGS_MODULE environment variable
export DJANGO_SETTINGS_MODULE=UANews.settings

# Delete any existing superuser 'admin' and create a new one
echo "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UANews.settings')
import django
django.setup()
from django.contrib.auth.models import User

# Delete existing 'admin' user if it exists
User.objects.filter(username='admin').delete()

# Create new superuser 'admin' with password 'test'
User.objects.create_superuser('admin', 'admin@example.com', 'test')
" | python manage.py shell

echo ""
echo "Superuser 'admin' with password 'test' has been created."
echo "Warning: Using default credentials is unsafe for production. Please change the username and password in a real environment!"
# Provide additional instructions for manually creating or resetting a superuser
echo "To manually create a new safe superuser and reset a default one using the Django shell, follow these steps:"
echo "1. Run: python manage.py shell"
echo "2. Then input the following script into the console:"
echo ""
echo "   import os"
echo "   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UANews.settings')"
echo "   import django"
echo "   django.setup()"
echo "   from django.contrib.auth.models import User"
echo ""
echo "   # Delete existing default superuser 'admin':"
echo "   User.objects.filter(username='admin').delete()"
echo ""
echo "   # Create a new superuser:"
echo "   User.objects.create_superuser('your-name-here', 'your-email-here', 'your-password-here')"
echo ""
echo "Make sure to replace 'your-name-here', 'your-email-here', and 'your-password-here' with the desired superuser credentials."
echo ""

# Check the SECRET_KEY in settings.py
SECRET_KEY=$(python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UANews.settings')
from django.conf import settings
print(settings.SECRET_KEY)
")

DEFAULT_SECRET_KEY='django-insecure-a+nc&45)0l9q%f)hz%@05nlr+psmrx@91lb&ijm*9a70nv^c%6'

if [ "$SECRET_KEY" = "$DEFAULT_SECRET_KEY" ]; then

    echo "Warning: Using default secret key! Do not use this key in production."
    echo "To change the SECRET_KEY:"
    echo "1. Open UANews/settings.py."
    echo "2. Replace the default SECRET_KEY with a new one."
    echo ""
fi

# Deactivate virtual environment
deactivate

echo "Project setup completed. You can now run the project with run_project.sh."