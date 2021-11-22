from brownie import accounts, config
# import os #not needed when using config


def deploy_simple_storage():
    # below different variants how to manage keys:
    # account = accounts[0]  # from local ganache
    # account = accounts.load("rinkebytest") #from brownie account manager
    # from environment variable (needs brownie-config.yaml)
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    account = accounts.add(config['wallets']['from_key'])
    print(account)


def main():
    deploy_simple_storage()
