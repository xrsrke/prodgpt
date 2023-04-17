from prodgpt.disllation.flow import DistillationFlow


def test_distillation(model):
    flow = DistillationFlow()
    flow.run(model=model)
