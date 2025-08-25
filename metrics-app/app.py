from prometheus_client import start_http_server, Counter
import random
import time

# Define a metric
requests_total = Counter("example_requests_total", "Total example requests", ["type"])

def generate_metrics():
    while True:
        # Simulate increments
        requests_total.labels(type="success").inc(random.randint(1, 5))
        requests_total.labels(type="failure").inc(random.randint(0, 2))
        time.sleep(2)

if __name__ == "__main__":
    start_http_server(8000)  # Prometheus scrapes here
    generate_metrics()
