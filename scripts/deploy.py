from brownie import accounts, config, SimpleStorage
# import os #not needed when using config


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve() # since its a "view" function, doesnt need "from"
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account}) #since its transaction, need from
    transaction.wait(1) # how many blocks to wait, for transaction to finish
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)

def main():
    deploy_simple_storage()
