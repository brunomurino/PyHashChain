class Transaction:

    def do_transaction(self, args):
        """Performs transaction
        
        """

        self.transaction = {}

        self.transaction['sender'] = input('\n\tSender: ')
        while self.transaction['sender'] == '':
            self.transaction['sender'] = input('\n\tSender: ')

        self.transaction['receiver'] = input('\n\tReceiver: ')
        while self.transaction['receiver'] == '':
            self.transaction['receiver'] = input('\n\tReceiver: ')

        while True:
            try:
                self.transaction['amount'] = float(input('\n\tAmount: '))
                break
            except ValueError:
                print(colored("\tNot a valid number.",'red'))

        print('')
             
