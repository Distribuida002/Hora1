from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hora_actual():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h2>Hora actual del servidor:</h2><p>{ahora}</p>"

if __name__ == "__main__":
    app.run(debug=True)
