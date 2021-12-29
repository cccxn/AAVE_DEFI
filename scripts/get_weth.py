from scripts.helpful_scripts import get_account
from brownie import interface, config, network, accounts
import sys


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.

    :return: None

    """
    account = get_account()
    # account = accounts[0]
    weth = interface.IWeth(config['networks'][network.show_active()]['weth-token'])
    txn = weth.deposit({'from': account, 'value': 0.1 * 10**18})
    txn.wait(1)
    print('Received 0.1 WETH')
    return txn
