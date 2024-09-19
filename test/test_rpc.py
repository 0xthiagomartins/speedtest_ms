from nameko.extensions import ClusterRpcProxy


def test_rpc_speedtest(rabbitmq_config):
    with ClusterRpcProxy(rabbitmq_config) as rpc:
        result = rpc.speedtest.run_speedtest()
    assert result["download"] > 0
    assert result["upload"] > 0
    assert result["ping"] > 0
