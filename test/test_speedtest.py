from src.service import RPCSpeedTest


def test_run_speedtest():
    service = RPCSpeedTest()
    result = service.run_speedtest()
    assert "download" in result
    assert "upload" in result
    assert "ping" in result
