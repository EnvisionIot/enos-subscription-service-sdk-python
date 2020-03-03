=======================
enos-subscribe-python
=======================

enos-subscribe 订阅客户端python版本

使用该客户端可以订阅Enos平台的实时、告警和离线数据

License
=======

 - BSD

安装
============

本模块支持Python 2.7 和 Python 3.4及以上版本

使用 "python setup.py install" 或者 "pip install enos-subscribe" 进行安装.

本项目依赖如下模块

 - six
 - google.protobuf
 - websocket_client


Examples
========

实时数据订阅
---------------------

.. code:: python
    from enos_subscribe import DataClient

    if __name__ == '__main__':
        client = DataClient(host='sub-host', port='sub-port',
                            access_key='Your Access Key of this subscription',
                            access_secret='Your Access Secret of this subscription')

        client.subscribe(sub_id='Your subscription Id')

        for message in client:
            print(message)



告警数据订阅
---------------------

.. code:: python
    from enos_subscribe import AlertClient

    if __name__ == '__main__':
        client = AlertClient(host='sub-host', port='sub-port',
                            access_key='Your Access Key of this subscription',
                            access_secret='Your Access Secret of this subscription')

        client.subscribe(sub_id='Your subscription Id')

        for message in client:
            print(message)


离线数据订阅
---------------------

.. code:: python
    from enos_subscribe import OfflineDataClient

    if __name__ == '__main__':
        client = OfflineDataClient(host='sub-host', port='sub-port',
                            access_key='Your Access Key of this subscription',
                            access_secret='Your Access Secret of this subscription')

        client.subscribe(sub_id='Your subscription Id')

        for message in client:
            print(message)