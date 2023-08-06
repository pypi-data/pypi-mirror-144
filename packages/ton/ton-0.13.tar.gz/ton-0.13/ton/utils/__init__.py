# -*- coding: utf-8 -*-
from .address import *
import codecs
import base64
import asyncio
import struct

import crc16


class TonLibWrongResult(Exception):
    pass


def pubkey_b64_to_hex(b64_key):
    bin_key = base64.b64decode(b64_key)
    words = 18
    ints_key = struct.unpack(f'{"H"*words}', bin_key)
    key = [x.to_bytes(2, byteorder='little') for x in ints_key]
    key = b''.join(key)
    key = [((x & 0x0F) << 4 | (x & 0xF0) >> 4).to_bytes(1, byteorder='little') for x in key]
    name = b''.join(key)
    return name.hex().upper()


def hex_to_b64str(x):
    return codecs.encode(codecs.decode(x, 'hex'), 'base64').decode().replace("\n", "")


def from_nano(value):
    return round(value / 10 ** 9, 9)

def to_nano(value):
    return int(value * (10 ** 9))

def coro_result(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def raw_to_userfriendly(address, tag=0x11):
    workchain_id, key = address.split(':')
    workchain_id = int(workchain_id)
    key = bytearray.fromhex(key)

    short_ints = [j * 256 + i for i, j in zip(*[iter(key)] * 2)]
    payload = struct.pack(f'Bb{"H"*16}', tag, workchain_id, *short_ints)
    crc = crc16.crc16xmodem(payload)

    e_key = payload + struct.pack('>H', crc)
    return base64.urlsafe_b64encode(e_key).decode("utf-8")


def userfriendly_to_raw(address):
    k = base64.urlsafe_b64decode(address)[1:34]
    workchain_id = struct.unpack('b', k[:1])[0]
    key = k[1:].hex().upper()
    return f'{workchain_id}:{key}'


def str_b64encode(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8') if s and isinstance(s, str) else None