import asyncio

from ctc import evm
from ctc import rpc


def get_command_spec():
    return {
        'f': add_proxy_abi_comamand,
        'help': 'download proxy abi for contract',
        'args': [
            {
                'name': 'contract_address',
                'help': 'address that points toward implementation',
            },
            {
                'name': 'implementation_address',
                'help': 'address that implements functionality',
            },
        ],
    }


def add_proxy_abi_comamand(contract_address, implementation_address, **kwargs):
    print('saving proxy contract implementation...')
    print('     for contract:', contract_address)
    print('   implementation:', implementation_address)
    answer = input('continue? ')
    if answer not in ['y', 'yes']:
        print('aborting')
        return
    else:
        asyncio.run(run(contract_address, implementation_address))


async def run(contract_address, implementation_address):
    await evm.async_save_proxy_contract_abi_to_filesystem(
        contract_address=contract_address,
        proxy_implementation=implementation_address,
    )

    from ctc.rpc.rpc_backends import rpc_http_async

    provider = rpc.get_provider()
    await rpc_http_async.async_http_close_session(provider=provider)

