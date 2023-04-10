from fastapi.testclient import TestClient

from house_price_api.app.main import app

client = TestClient(app)


def test_valuate_valid_input():
    response = client.post("/", json={
        "bed": 3,
        "bath": 2,
        "acre_lot": 1.5,
        "zip_code": 19720,
        "house_size": 2000,
    })

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_valuate_invalid_parameter():
    response = client.post("/", json={
        "bed": 3,
        "bath": 2,
        "acre_lot": 1.5,
        "zip_code": 19720,
        "house_size": 2000,
        "invalid_parameter": 1,
    })  # invalid_parameter is not a valid parameter

    assert response.status_code == 422


def test_missing_parameter():
    response = client.post("/", json={
        "bed": 3,
        "bath": 2,
        "acre_lot": 1.5,
        "zip_code": 19720,
    })  # house_size is missing

    assert response.status_code == 422
    assert "detail" in response.json()


def test_valuate_string_value():
    response = client.post("/", json={
        "bed": "three",  # Invalid string value
        "bath": 2,
        "acre_lot": 1.5,
        "zip_code": 19720,
        "house_size": 2000,
    })

    assert response.status_code == 422
    assert "detail" in response.json()


def test_valuate_large_input_values():
    response = client.post("/", json={
        "bed": 1000,
        "bath": 1000,
        "acre_lot": 100000,
        "zip_code": 19720,
        "house_size": 1000000,
    })

    assert response.status_code == 422
    assert "detail" in response.json()