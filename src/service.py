from nameko.rpc import rpc
import speedtest
from loguru import logger


logger.add("speedtest.log")


class RPCSpeedTest:
    name = "speedtest"

    @rpc
    def run_speedtest(self):
        logger.info("Starting speedtest")
        result = self.speedtest()
        download, upload, ping = result["download"], result["upload"], result["ping"]
        logger.info(
            f"Speedtest completed: Download={download} Mbps, Upload={upload} Mbps, Ping={ping} ms"
        )
        return {"download": download, "upload": upload, "ping": ping}

    def speedtest(self):
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000
        ping = st.results.ping
        return {"download": download, "upload": upload, "ping": ping}
