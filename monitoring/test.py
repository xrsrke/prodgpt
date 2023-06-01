from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge('job_last_success_unixtime', 'finished', registry=registry)
g.set_to_current_time()
push_to_gateway('http://localhost:9091', job='batchA', registry=registry)
