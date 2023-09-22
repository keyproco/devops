from flask import Flask, render_template, request
import os
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
metrics =PrometheusMetrics(app)

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)

@app.route('/')
@by_path_counter
def home():
    return "Hello from Flask"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)