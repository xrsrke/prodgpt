from prefect import flow, task

@task
def start_x():
    print("starting x...")

@task
def stop_x():
    print("stopping x...")

@flow(name="training") # ignore the name
def train():
    start_x()
    stop_x()