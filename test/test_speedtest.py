from src.service import SpeedtestService


def test_run_speedtest():
    service = SpeedtestService()
    result = service.run_speedtest()
    assert "download" in result
    assert "upload" in result
    assert "ping" in result
