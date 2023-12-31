"""=======================================================================
 * API Class 
 * Objective: Calculate the gain for the Lump Sum model
========================================================================"""
from API import API

class LumpSum:
    def __init__(self, amount: float, tkr: str, intvl: str, prd: str):

        #ASSUME we are investing for 10 years 
        #MUST CHANGE
        self.amount=amount*10*11.8
        self.tkr=tkr
        self.intvl = intvl
        self.prd=prd

    #return the profit and annual growth rate of the investment as a list
    def outcome(self):
        """
        return the profit and annual growth rate of the investment as a list

        returns: list with float type values
        """

        price_list=API(self.tkr, self.intvl, self.prd).closing_price()
        
        buying_price=price_list[0]
        selling_price=price_list[len(price_list)-1]
        
        shares=self.amount/buying_price
        profit=(selling_price-buying_price)*shares

        growth_rate= ((selling_price)/buying_price)**(12/len(price_list))-1
        
        return [profit, growth_rate]

