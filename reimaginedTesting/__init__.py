from reimaginedPackages.reimaginedServer.views import app as FlaskApp
import pytest

@pytest.fixture()
def app():
    app = FlaskApp
    app.config.update({"TESTING": True})
    yield app 

@pytest.fixture()
def client(app):
    return app.test_client()