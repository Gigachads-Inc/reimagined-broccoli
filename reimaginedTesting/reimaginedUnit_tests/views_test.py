from reimaginedTesting import client, app
import pytest

def test_request_example():
    response = client(app).get("/posts")
    assert b"<h2>Hello, World!</h2>" in response.data