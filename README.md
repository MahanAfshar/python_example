# OpenLibrary Books Fetcher

A simple Python script that fetches 50 books from the Open Library API, filters books published after 2000, and saves the results to a CSV file.

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The filtered books will be saved to:

```text
books.csv
```

## Requirements

* Python 3.9+
* requests
* Internet connection
