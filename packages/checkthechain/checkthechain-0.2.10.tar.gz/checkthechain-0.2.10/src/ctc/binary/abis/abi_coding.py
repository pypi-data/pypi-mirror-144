# replace eth_abi with eth_abi_lite

import typing

from ctc import spec


def abi_decode(data: bytes, types: spec.ABIDatatypeStr) -> typing.Any:
    # TODO: allow for any input format, allow specifying any output format
    import eth_abi

    return eth_abi.decode_single(types, data)


def abi_encode(data: typing.Any, types: spec.ABIDatatypeStr) -> bytes:
    # TODO: allow for any input format, allow specifying any output format
    import eth_abi

    return eth_abi.encode_single(types, data)

