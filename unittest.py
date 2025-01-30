import pytest
from ip_tool import checking_duplicates, initialization

def test_checking_duplicates():
    ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "10.0.0.1"]
    assert checking_duplicates(ip_list) == {"192.168.1.1"}

def test_initialization(tmp_path):
    test_file = tmp_path / "test.csv"
    test_file.write_text("192.168.1.1\n192.168.1.2\n")
    
    assert initialization(str(test_file)) == ["192.168.1.1", "192.168.1.2"]
