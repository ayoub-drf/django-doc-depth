#!/bin/bash

git add .
echo "Enter the new app name"
read app
python manage.py startapp $app
echo "from django.urls import path" > $app/urls.py
