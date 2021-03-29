import pytest


def pytest_addoption(parser):
    parser.addoption("--game_type",
                     action="store",
                     default="simple",
                     help="Set game type, default is simple")


@pytest.fixture
def game_type(request):
    return request.config.getoption("--game_type")