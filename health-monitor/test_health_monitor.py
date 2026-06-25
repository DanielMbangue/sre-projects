from health_monitor import get_threshold_warnings, log_warning
import os


def test_all_healthy_no_warnings():
    # everything under threshold -> empty list
    warnings = get_threshold_warnings(cpu_percent=10, virtual_memory=20, disk_usage=30)
    assert warnings == []


def test_high_cpu_warns():
    # cpu over 80 -> one warning about CPU
    warnings = get_threshold_warnings(cpu_percent=95, virtual_memory=20, disk_usage=30)
    assert len(warnings) == 1
    assert "CPU" in warnings[0]


def test_multiple_warnings():
    # cpu and memory both over -> two warnings
    warnings = get_threshold_warnings(cpu_percent=95, virtual_memory=85, disk_usage=30)
    assert len(warnings) == 2


def test_boundary_exactly_at_threshold():
    # exactly 80 should NOT warn (the check is > 80, not >= 80)
    warnings = get_threshold_warnings(cpu_percent=80, virtual_memory=80, disk_usage=90)
    assert warnings == []


def test_disk_uses_90_threshold():
    # disk warns at >90, not >80 -- 85 disk should be fine
    warnings = get_threshold_warnings(cpu_percent=10, virtual_memory=10, disk_usage=85)
    assert warnings == []
    # but 95 disk should warn
    warnings = get_threshold_warnings(cpu_percent=10, virtual_memory=10, disk_usage=95)
    assert len(warnings) == 1
    assert "Disk" in warnings[0]


def test_log_warning_writes_to_file(tmp_path):
    # tmp_path is a pytest-provided temporary directory, cleaned up automatically
    log_file = tmp_path / "test_log.txt"
    log_warning("CPU percentage: 95%", filename=str(log_file))
    contents = log_file.read_text()
    assert "WARNING" in contents
    assert "CPU percentage: 95%" in contents
