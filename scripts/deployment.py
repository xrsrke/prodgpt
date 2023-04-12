from datetime import timedelta

from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule

from training import train

deployment_dev = Deployment.build_from_flow(
    flow=train,
    name="model_training-dev",
    schedule=IntervalSchedule(interval=timedelta(minutes=1))
)

deployment_dev.apply()

deployment_prod = Deployment.build_from_flow(
    flow=train,
    name="model_training-prod",
    schedule=IntervalSchedule(interval=timedelta(minutes=1))
)

deployment_prod.apply()
