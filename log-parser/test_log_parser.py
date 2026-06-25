from log_parser import count_error_types, read_log_file
import pytest


def test_counts_single_level():
    # one ERROR line should produce a count of 1 for ERROR
    lines = ["ERROR something broke\n"]
    counts, unique = count_error_types(lines)
    assert counts["ERROR"] == 1


def test_counts_multiple_levels():
    # mix of levels should each be counted correctly
    lines = [
        "ERROR disk full\n",
        "INFO started up\n",
        "ERROR timeout\n",
        "WARNING low memory\n",
    ]
    counts, unique = count_error_types(lines)
    assert counts["ERROR"] == 2
    assert counts["INFO"] == 1
    assert counts["WARNING"] == 1


def test_unique_errors_deduplicates():
    # the same line twice should count as 2 ERRORs but only 1 unique message
    lines = [
        "ERROR same message\n",
        "ERROR same message\n",
    ]
    counts, unique = count_error_types(lines)
    assert counts["ERROR"] == 2
    assert len(unique) == 1


def test_empty_input():
    # no lines should produce empty results, not a crash
    counts, unique = count_error_types([])
    assert counts == {}
    assert len(unique) == 0


def test_read_missing_file_raises():
    # reading a file that doesn't exist should raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_log_file("this_file_does_not_exist.log")
        
def test_blank_line_does_not_crash():
    # a blank line in the middle should be skipped, not crash
    lines = ["ERROR disk full\n", "\n", "INFO recovered\n"]
    counts, unique = count_error_types(lines)
    assert counts == {"ERROR": 1, "INFO": 1}

def test_whitespace_only_line():
    # a line of just spaces should also be skipped
    lines = ["   \n", "WARNING low disk\n"]
    counts, unique = count_error_types(lines)
    assert counts == {"WARNING": 1}

def test_single_line():
    # boundary: exactly one line
    counts, unique = count_error_types(["INFO ok\n"])
    assert counts == {"INFO": 1}
    assert len(unique) == 1