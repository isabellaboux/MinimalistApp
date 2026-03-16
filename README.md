# Streamlit Docker App

A minimal web application built with **Python** and **Streamlit**, containerized with **Docker**, and deployed online via **Render & GitHub**.

**Live demo:**  
https://minimalistapp.onrender.com/

## Overview

This project demonstrates a simple workflow for building and deploying a Python web app:

1. Develop a Streamlit app locally
2. Manage dependencies using `uv`
3. Package the application in a Docker container
4. Deploy the container automatically using Render

The app provides a small interactive Streamlit interface accessible through a web browser.


## Running Locally

Install dependencies and start the app:

```bash
pip install uv
uv sync
uv run streamlit run app.py
```

## Running on Docker locally

```bash
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```