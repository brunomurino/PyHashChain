import os
import json
import cmd
import pprint
from pprint import pprint

import hashlib
from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
init()

import transaction
from transaction import Transaction

assert hasattr(Transaction, 'do_transaction'),\
     "Transaction class doesn't have 'do_transaction' method."

class PyHashChain(cmd.Cmd, Transaction):

    def do_quit(self, args):
        """Quits the program."""

        print("Quitting.")
        raise SystemExit
        
    def do_show(self, args):
        """Prints the current transaction."""
        try:
            print(self.transaction)
        except AttributeError:
            print('No transaction yet.')

    def hash_transaction(self, transaction):
        y = json.dumps(transaction, sort_keys=True)
        return hashlib.sha256(y.encode()).hexdigest()
        
    def do_create_genesis_hash(self, args):
        """Initializes block with empty transaction hash."""
        
        self.genesis_hash = self.hash_transaction({})
        with open('block.txt', 'w+') as block:
            block.write("0 {}".format(self.genesis_hash))

    def get_prev_hash(self):
        """Reads latest block and gives the previous hash."""

        with open("block.txt", 'r') as block_file:
            content = block_file.readlines()
            last_line = content[-1].split(' ')
            self.transaction['prev_num'] = int(last_line[0])
            self.transaction['prev_hash'] = last_line[1]

    def do_add_transaction(self, args):
        """Get latest block and add transaction to it."""

        if not hasattr(self, 'transaction'):
            print("\n\tNo transaction defined yet.\n")
        else:
            self.get_prev_hash()
            new_hash = self.hash_transaction(self.transaction)
            new_num = self.transaction['prev_num'] + 1
            print(new_hash)
            with open("block.txt",'a')\
                as current_block:
                current_block.write("\n{} {}".format(new_num, new_hash))
            delattr(self, "transaction")


if __name__ == '__main__':
    os.system('clear')
    prompt = PyHashChain()
    prompt.prompt = 'PyHashChain: '
    prompt.cmdloop(figlet_format('PyHashChain'))
