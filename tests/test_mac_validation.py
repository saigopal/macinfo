# Test with mac address format
from libs import common

def test_mac_with_colon():
    assert common.is_valid_mac('ff:ff:ff:ff:ff:ff') == True

def test_mac_with_colon_caps():
    assert common.is_valid_mac('FF:FF:FF:FF:FF:FF') == True

def test_mac_with_no_separator():
    assert common.is_valid_mac('FFFFFFFFFFFF') == True

def test_mac_with_dash():
    assert common.is_valid_mac('FF-FF-FF-FF-FF-FF') == True

def test_mac_with_extra_colon():
    assert common.is_valid_mac('ff::ffff::ff::ffff') == False
