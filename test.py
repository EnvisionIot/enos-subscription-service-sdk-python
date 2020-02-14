import time

import websocket

try:
    import thread
except ImportError:
    import _thread as thread

from proto import sub_pb2
from proto import common_pb2

import hashlib


def sign(access_key=None, sub_id=None, secret=None):
    m = hashlib.sha256()
    m.update(b'access_key')
    m.update(access_key.encode('utf8'))
    m.update(b'access_secret')
    m.update(secret.encode('utf8'))
    m.update(b'sub_id')
    m.update(sub_id.encode('utf8'))
    return m.hexdigest()


def on_message(ws, message):
    print('receive')
    print(message)
    print(type(message))

    pkg = message[2:]
    resp = common_pb2.TransferPkg().FromString(bytearray(pkg))
    # print(resp)

    auth_rsp = resp.data
    auth = sub_pb2.AuthRsp().FromString(auth_rsp)
    print(auth)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_pong(ws, message):
    print('pong')
    print(message)


def on_open(ws):
    auth_req = sub_pb2.AuthReq()
    auth_req.accessKey = 'ea199c3e-f272-4e3d-96af-c59a707322cc'
    auth_req.subId = 'sub-1573716301144'
    auth_req.sign = sign('ea199c3e-f272-4e3d-96af-c59a707322cc', 'sub-1573716301144',
                         '9f545c81-9839-4907-999e-307724b401831')
    auth_req.subType = 0

    transfer_pkg = common_pb2.TransferPkg()
    transfer_pkg.seqId = 0
    transfer_pkg.cmdId = 2
    transfer_pkg.data = auth_req.SerializeToString()
    transfer_pkg.zip = False
    transfer_pkg.ver = 0

    outBytes = transfer_pkg.SerializeToString()

    ws.send(outBytes, websocket.ABNF.OPCODE_BINARY)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:9001",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_pong=on_pong)
    ws.on_open = on_open
    ws.run_forever(ping_interval=2)
