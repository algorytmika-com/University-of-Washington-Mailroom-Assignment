import pytest
from src.assignment05.utils import validations as v

def test_is_full_name_pass():
    assert v.is_full_name('Bill Gates')
    assert v.is_full_name('Mr. Gates')
    assert v.is_full_name('Gates')
    assert v.is_full_name('  Bill Gates   ')

def test_is_full_name_fail():
    assert not v.is_full_name('Bill Gates1')
    assert not v.is_full_name('Mr, Gates')
    assert not v.is_full_name('Gates %')

def test_is_money_pass():
    assert v.is_money(1)
    assert v.is_money(1.12)
    assert v.is_money(1.3)
    assert v.is_money(0.01)

def test_is_money_fail():
    assert not v.is_money("1")
    assert not v.is_money(0)
    assert not v.is_money(-1)
    assert not v.is_money(1.3456315)    
    
