#!/bin/bash

hypercorn dj.asgi:application --bind 0.0.0.0:8000