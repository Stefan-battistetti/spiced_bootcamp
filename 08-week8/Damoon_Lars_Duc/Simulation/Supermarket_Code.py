import pandas as pd
import numpy as np
import random
from faker import Faker
f = Faker()
from datetime import timedelta, datetime


class Supermarket:
    """
    an MCMC simulation that takes customers from Customer class and moves them throughout store during opening times
    """
    def __init__(self, market_name, opening,  closing):
        self.market_name = market_name
        self.opening = datetime.strptime(opening, '%H:%M')
        self.closing = datetime.strptime(closing, '%H:%M')
        self.active_customers = []
        self.customer_id = 0
        self.current_time = self.opening
        self.customer_list = []
        self.customer_df = pd.DataFrame()
        
    def open_store(self):
        """ 
        initialises the store to start counter and begin accepting customers  
        """
        self.open_for_business()
        self.timer()
        self.get_customers()

    def open_for_business(self) -> bool:
        """
        limiting setting to stop new customers entering store too late
        """
        while self.current_time <= self.closing - timedelta(minutes=3):
            return True
            
    def timer(self):
        """ 
        counter to run customer activity for each minute of opening time 
        """
        while self.current_time != self.closing: 
            self.current_time += timedelta(minutes=1)
            self.get_customers()
            self.move_customers()
            self.remove_customers()
            self.add_to_df()
        
    def get_customers(self):
        """ 
        allows random number of ne wcustomers to enter the store
        """
        if self.open_for_business() == True:
            n = np.random.poisson(5)
            for i in range(n):
                self.customer_id += 1
                self.customer_name = f.name()
                new_customer = Customer(self.customer_name, "entrance")
                self.customer_list.append(new_customer)
                self.active_customers.append(new_customer)

    def move_customers(self):
        """ 
        moves all customers active in the store to their next state
        """
        for customer in self.active_customers:
            customer.next_state()

    def remove_customers(self):
        """ 
        removes all inactive customers from the active list
        """
        for customer in self.active_customers:
            if customer.is_active == False:
                self.active_customers.remove(customer)
                
    def get_time(self):
        return datetime.strftime(self.current_time, '%H:%M')

    def add_to_df(self):
        """ 
        creates dataframe with time/customer/location for each minute 'freezeframe' for active customers
        """
        for customer in self.active_customers:
                self.customer_df = self.customer_df.append({'timestamp': self.get_time(),
                                                        'customer_name': str(customer.name),
                                                        'location': customer.state
                                                        }, ignore_index=True)