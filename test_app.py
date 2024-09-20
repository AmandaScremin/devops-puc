
import pytest
from app import app

def test_root():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, Docker!'

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 3 * 4 == 12

def test_division():
    assert 10 / 2 == 5