# !/bin/bash

# docker-compose up -d

# python3 -m venv ../venv-instagram-query

# source ../venv-instagram-query/bin/activate

# pip install fastapi "uvicorn[standard]" pydantic-settings redis bcrypt sqlalchemy psycopg2-binary

export PYTHONPATH=/Users/jeongjun-u/Documents/GitHub/instagram_query

uvicorn main:app --reload