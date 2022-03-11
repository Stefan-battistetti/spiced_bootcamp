class Simulation():
    """ 
    class to take user input for store data and initiate the simulation
    """
    def __init__(self) -> None:
        self.confirmation()
        print('is this done?')

    def confirmation(self):    
        return input('Thank you. The simulation will run and output saved as CSV file. Do you wish to proceed [Y/N]?')

