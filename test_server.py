from flask import Flask, request
app = Flask(__name__)

@app.route('/search')
def search():
    q = request.args.get('q', '')
    # intentionally vulnerable reflection
    return f"""<html>
    <head><title>Search</title></head>
    <body>
      <h1>Search results</h1>
      <p>You searched for: {q}</p>
    </body>
    </html>"""

if __name__ == '__main__':
    app.run(port=5000, debug=True)
