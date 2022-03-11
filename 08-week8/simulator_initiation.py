import pandas as pd

#restrict user input type and return suggestions on error


class Simulation():
    """ 
    class to take user input for store data and initiate the simulation
    """
    #def __init__(self) -> None:

    def input(self):
        """ 
        method to ask user for store data
        """
        store = input(f'What is the name of your store?')
        open = input(f'What time does your store open?')
        close = input(f'What time does your store close?')
        confirmation = input('Thank you. The simulation will run and output saved as CSV file. Do you wish to proceed [Y/N]?')

        if confirmation == 'Y':
            my_store = Supermarket(store, open, close)

            my_store.open_store()

            my_store.customer_df.set_index('timestamp', inplace=True)
            my_store.customer_df.to_csv(simulated_market_output.csv')

        else:
            print('Goodbye')

