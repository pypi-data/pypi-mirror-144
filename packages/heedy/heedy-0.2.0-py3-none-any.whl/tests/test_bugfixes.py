import pytest
from heedy import App

# These tests are of bugfixes to heedy, making sure that things are working


def test_appscope():
    # Makes sure that removing owner's access doesn't affect the App's access
    a = App("testkey")
    o = a.objects.create("myobj")
    assert o.access == "*"
    o.key = "lol"
    o.owner_scopes = "read"
    assert o.read()["key"] == "lol"
    o.key = "hiya"
    assert o.read()["key"] == "hiya"


def test_indexerror():
    a = App("testkey")
    ts = a.objects.create("myobj")
    ts.insert("hi!")
    assert len(ts(i1=-1, i2=0)) == 0
