from monitoring.log import DistributionDrift, send_inference_log_to_mongo


def test_send_inference_log_to_mongo():
    log = {
        "model_id": "123",
        "user_id": "456",
        "input": "hello",
        "output": "world"
    }

    send_inference_log_to_mongo(log)


def test_distribution_drift():
    drift = DistributionDrift(window_length=100)

    output = drift.compute()

    assert isinstance(output, dict)
