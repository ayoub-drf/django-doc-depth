#!/bin/bash


gunicorn --reload  --access-logfile access.log dj.wsgi:application