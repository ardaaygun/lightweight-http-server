#  Lightweight HTTP Server & Dynamic Markdown Parser

A custom, dependency-free web server built entirely from scratch using Python's fundamental `socket` programming. This project was developed as part of the **CMPE 322 - Computer Networks** course to deconstruct the "black box" of modern web frameworks and understand the lowest levels of the OSI model.

## -> Key Features
* **Zero Dependencies:** Built without any high-level web frameworks (like Flask, Django).
* **Manual HTTP Parsing:** Intercepts and processes raw 1024-byte HTTP GET payloads.
* **Dynamic Markdown Engine:** Intercepts `.md` file requests and compiles plain text into styled HTML pages on-the-fly.

##  -> How to Run
1. Run the server: `python server.py`
2. Open your browser: `http://localhost:8080`

