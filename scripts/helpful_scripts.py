from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    'developement',
    'ganache',
    'hardhat',
    'local-ganache',
    'mainnet-fork'
]


def get_account(index = None, id = None):
    if index is not None:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id is not None:
        return accounts.load(id)
    if network.show_active() in config['networks']:
        return accounts.add(config['wallets']['from_key'])
    return None
