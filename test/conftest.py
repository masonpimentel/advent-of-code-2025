import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runs",
        action="store",
        default=1,
        type=int,
        help="Number of times to run each solver for timing",
    )


@pytest.fixture
def runs(request):
    return request.config.getoption("--runs")
