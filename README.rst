AAVE
----
- touch README.rst ;
- brownie init ;

Path
====
#. Swap our ETH for WETH
#. Deposit some ETH into Aave
#. Borrow some asset with the ETH collateral
    #. Sell that borrowed asset. (Short selling)
#. Repay everything back

Testing
=======
- Integration test: Kovan
- Unit tests: Mainnet-forks

Mainnet-Fork
============
- brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://infura.io/v3/$WEB3_INFURA_PROJECT_ID' accounts=10 mnemonic=brownie port=8545
- brownie test --network mainnet-fork
