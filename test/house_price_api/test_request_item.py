import pytest
from house_price_api.request_item import RequestItem


def test_request_item_valid():
    item = RequestItem(bed=3, bath=2.5, acre_lot=1.5, zip_code=19720, house_size=2000)
    assert item.bed == 3
    assert item.bath == 2.5
    assert item.acre_lot == 1.5
    assert item.zip_code == 19720
    assert item.house_size == 2000


def test_request_item_invalid_bed():
    with pytest.raises(ValueError):
        item = RequestItem(bed=0, bath=2.5, acre_lot=1.5, zip_code=19720, house_size=2000)


def test_request_item_invalid_bath():
    with pytest.raises(ValueError):
        item = RequestItem(bed=3, bath=0, acre_lot=1.5, zip_code=19720, house_size=2000)


def test_request_item_invalid_acre_lot():
    with pytest.raises(ValueError):
        item = RequestItem(bed=3, bath=2.5, acre_lot=-1, zip_code=19720, house_size=2000)


def test_request_item_invalid_zip_code():
    with pytest.raises(ValueError):
        item = RequestItem(bed=3, bath=2.5, acre_lot=1.5, zip_code=-1, house_size=2000)


def test_request_item_invalid_house_size():
    with pytest.raises(ValueError):
        item = RequestItem(bed=3, bath=2.5, acre_lot=1.5, zip_code=19720, house_size=0)

