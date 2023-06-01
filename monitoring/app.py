from fastapi import FastAPI
from prometheus_client import CollectorRegistry, Gauge
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    value: float


# Create a Gauge metric
g = Gauge('my_metric', 'Description of my metric', ['name'])
registry = CollectorRegistry()


@app.post("/monitoring")
def update_metrics():
    # Update the Gauge with the value from the POST request
    # g.labels(name=item.name).set(item.value)
    # g.labels(name="hello").set("42")

    # # Push the metrics to the pushgateway
    # push_to_gateway('localhost:9091', job='my_job', registry=registry)

    from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

    registry = CollectorRegistry()
    g = Gauge('job_last_success_unixtime', 'finished', registry=registry)
    g.set_to_current_time()
    push_to_gateway('localhost:9091', job='batchA', registry=registry)

    return {"message": "Metrics updated successfully"}
