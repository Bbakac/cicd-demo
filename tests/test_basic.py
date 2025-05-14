import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import greet, add, multiply
import pytest

def test_greet():
    assert greet("Berkay") == "Hello, Berkay!"

def test_add():
    assert add(3, 5) == 8

def test_multiply():
    assert multiply(4, 6) == 24

# ❌ Edge Case
def test_greet_empty_string():
    assert greet("") == "Hello, !"

# 🧪 Hatalı input → TypeError bekleniyor
def test_greet_none_input():
    with pytest.raises(TypeError):
        greet(None)
