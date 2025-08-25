How to Run
```bash
docker-compose up --build
```


Prometheus: http://localhost:9090

Grafana: http://localhost:3000
 (login: admin/admin)

Metrics endpoint (exposed by Python app): http://localhost:8000/metrics

📊 Grafana Setup

Log into Grafana → Add data source → Select Prometheus.

URL: http://prometheus:9090

Save & Test.

Create a Dashboard → Add Panel.

Query: example_requests_total{type="success"}

Query: example_requests_total{type="failure"}