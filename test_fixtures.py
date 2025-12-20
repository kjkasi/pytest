# test_fixtures.py

import pytest


@pytest.fixture
def sample_list():
    """Возвращает список из трёх целых чисел."""
    return [1, 2, 3]


@pytest.fixture
def sample_dict():
    """Возвращает словарь с двумя парами ключ-значение."""
    return {"a": 10, "b": 20}


@pytest.fixture
def sample_tuple():
    """Возвращает кортеж из двух строк."""
    return ("hello", "world")


@pytest.fixture(scope="module")
def shared_resource():
    """Фикстура с scope='module', используемая в нескольких тестах."""
    print("\n[SETUP] Setting up shared_resource")
    data = {"counter": 0}
    yield data
    print("\n[TEARDOWN] Tearing down shared_resource")


def test_use_sample_list(sample_list):
    assert len(sample_list) == 3
    assert sample_list == [1, 2, 3]


def test_use_sample_dict(sample_dict):
    assert sample_dict["a"] == 10
    assert "b" in sample_dict


def test_use_sample_tuple(sample_tuple):
    assert sample_tuple[0] == "hello"
    assert len(sample_tuple) == 2


def test_first_using_shared_resource(shared_resource):
    shared_resource["counter"] += 1
    assert shared_resource["counter"] == 1


def test_second_using_shared_resource(shared_resource):
    shared_resource["counter"] += 1
    assert shared_resource["counter"] == 2