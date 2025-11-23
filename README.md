**🛡️ XSS Scanner – Lightweight Cross-Site Scripting Detection Tool**

A simple and efficient XSS (Cross-Site Scripting) vulnerability scanner built in Python.
This tool helps developers test web applications by injecting common XSS payloads into parameters and generating a clean HTML report of findings.

**🚀 Features**

✔️ Scan any GET/POST endpoint for potential XSS vulnerabilities
✔️ Test single or multiple parameters
✔️ Uses multiple pre-built XSS payloads
✔️ Generates a clean and readable HTML report
✔️ Easy to run & beginner friendly
✔️ Includes a local test application (test_server.py) to simulate a vulnerable endpoint

**📂 Project Structure**

```python
**xss-scanner/
│
├── scanner/
│   ├── cli.py         # Main CLI entry for the scanner
│   ├── core.py        # Payload injection and detection logic
│   ├── payloads.txt   # XSS payload list
│
├── test_server.py     # Sample Flask server with a vulnerable input
├── requirements.txt   # Dependencies
└── README.md          # Documentation**
```

**`🧰 Requirements`**

Make sure you have:

Python 3.8+

pip

(Optional) virtualenv

**Install dependencies:**

````pip install -r requirements.txt```


### If installing inside a virtual environment:

python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

**🧪 Running the Test Server (Optional)**

This project includes a small Flask application to test the scanner locally.

Start it using:

`python test_server.py`


The server runs at:

[http://127.0.0.1:5000/search?q=test](https://)


You can stop it anytime using CTRL + C, and re-run it whenever needed.

**🔍 Running the XSS Scanner**

Basic usage:

[python -m scanner.cli --url "http://127.0.0.1:5000/search" --params "q" --method GET --out report.html](https://)

**CLI Arguments**

| Flag       | Description          | Example                          |
| ---------- | -------------------- | -------------------------------- |
| `--url`    | Target endpoint URL  | `"http://127.0.0.1:5000/search"` |
| `--params` | Parameter(s) to test | `"q"` or `"q,id,name"`           |
| `--method` | HTTP method          | `GET` or `POST`                  |
| `--out`    | Output report file   | `report.html`                    |


**Example POST request:**

[`python -m scanner.cli --url "https://example.com/login" --params "username,password" --method POST --out login_report.html`](https://)

**📊 Report Output**

After scanning, the tool generates a report.html file that contains:

Tested URL
Parameters scanned
Payloads injected
Whether any reflected payload was detected
Highlighted vulnerabilities

[Open it in your browser:](https://)

[report.html](https://)

**📝** **Notes**

The test server is only for practicing — real applications may require authentication or headers.
This scanner checks for reflected XSS, not stored or DOM-based attacks.
Use responsibly — only scan applications that you have permission to test.

