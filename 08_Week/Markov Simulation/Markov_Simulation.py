import random 
import pandas as pd
import numpy as np
from faker import Faker

transition_matrix=pd.read_csv('transition_matrix.csv')
transition_matrix=transition_matrix.set_index('before')

class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation.
    new line
    """
    
    def __init__(self, id, name):
        self.id=id
        self.name = name
        self.location='drinks'
        self.transition_probs=transition_matrix
        
    def __repr__(self):
        return f"{self.name}, customer {self.id}, is in {self.location}"
    
    def next_state(self):
        ''' Propagates the customer to the next state. Returns nothing.   '''
        self.location = np.random.choice(self.transition_probs.columns.values, p=self.transition_probs.loc[self.location])
    
    def is_active(self):
        """ Returns True if the customer has not reached the checkout yet. """
        if self.location=='checkout':
            return False
        else:
            return True

class Supermarket:
    """manages multiple Customer instances that are currently in the market.    
    new comments"""
    
    def __init__(self):
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.opening_hour = 7
        self.df = pd.DataFrame()

    def get_time(self):
        hour = self.opening_hour + self.minutes // 60
        min = self.minutes % 60
        self.timestamp = pd.Timestamp(year=2022, month=2, day=1, hour= hour, minute = min)
        return None
    
    def add_new_customers(self):
        """randomly creates new customers."""
        f = Faker()
        name = f.name()
        id = self.last_id
        self.customers.append(Customer(id, name))
        self.last_id += 1
        
    def next_minute(self):
        """propagates all customers to the next state."""
        self.minutes += 1
        for each in self.customers:
            each.next_state()
    
    def remove_exited_customers(self):
        """removes every customer that is not active any more.
        """
        self.customers = [i for i in self.customers if i.is_active()]
    
    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            self.get_time()
            timestamp = self.timestamp
            customer_id = customer.id
            location = customer.location
            self.df = self.df.append({'timestamp' : timestamp, 'id' : customer_id, 'location' : location}, ignore_index = True)

if __name__ == "__main__":
    Minutes_to_simulate = 100
    simulated_customer_behavior = Supermarket()
    for i in range(Minutes_to_simulate):
        simulated_customer_behavior.next_minute()
        simulated_customer_behavior.add_new_customers()
        simulated_customer_behavior.remove_exited_customers()
        simulated_customer_behavior.print_customers()
    simulated_customer_behavior.df.to_csv('simulated_customer_behavior.csv')
