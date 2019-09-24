# PyHashChain

## Goal
The goal of this project is to play around with objects and with the concept of having a transaction hash chain (very simple)

## Usage

To start the app, run 
```
$ docker-compose run pyhashchain
```

To initialize the block, i. e. create the genesis hash, run:
```
PyHashChain: create_genesis_hash
```
This will create a `block.txt` file with the number of the transaction, which is 0 for the genesis, and the hash for the transaction. The genesis transaction is an empty dictionary. To create a new transaction, run:
```
PyHashChain: transaction
```
and follow the prompts. Then, to check the transaction info, run:
```
PyHashChain: show
```
Then, to get the hash from the previous transaction saved and add the new transaction number and hash to `block.txt`, run:
```
PyHashChain: add_transaction
```

To quit the command line interpreter, run:
```
PyHashChain: quit
```
