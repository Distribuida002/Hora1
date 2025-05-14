from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def hora_actual():
    zona_ecuador = pytz.timezone("America/Guayaquil")
    ahora = datetime.now(zona_ecuador).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h2>Hora actual en Ecuador:</h2><p>{ahora}</p>"

if __name__ == "__main__":
    app.run(debug=True)
