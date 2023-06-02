from monitoring.log import DistributionDrift


def test_distribution_drift():
    drift = DistributionDrift(window_length=100)

    output = drift.compute()

    assert isinstance(output, dict)
