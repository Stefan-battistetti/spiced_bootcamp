import pandas as pd
import numpy as np
import random

from faker import Faker
f = Faker()

import datetime
from datetime import timedelta, datetime

class Customer():
    """  Customer class from Damoon github - creates customer who makes decisions on where to go next 
    """
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __repr__(self):
        return f'Customer {self.name} in {self.state}'

    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        #self.state = random.choices(['checkout', 'dairy', 'drinks', 'fruit', 'spices'], weights= prob_df.loc[self.state])
        if self.is_active() == True:
            self.state = random.choices(population=ALL_STATES, weights=TRANSITION_MATRIX[self.state])[0]

    def is_active(self):
        if self.state == 'checkout':
            return False
        else:
            return True