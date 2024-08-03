from flask import Flask
from main import main

app = Flask(__name__)


@app.route('/cats')
def fetch_cats():
    count, duration = main()
    return f"Completed: Downloaded {count} cats in {duration:.2f} seconds"


if __name__ == '__main__':
    app.run(debug=True)
