import pytest
from xprodgpt.evaluation.model import ModelPerformance


@pytest.mark.skip(reason="Not implemented")
def test_evaluate_model_performance():
    model = None

    evaluator = ModelPerformance()
    output = evaluator.evaluate(model)

    assert ["accuracy", "memory", "speed"] == list(output.keys())
    assert 0 <= output["accuracy"] <= 1
    assert output["memory"] > 0
    assert output["speed"] > 0
