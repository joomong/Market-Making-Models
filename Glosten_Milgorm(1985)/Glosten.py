""" 
Glosten Milgorm 1985 
"""

class GlostenMilgrom():
    """
    phi : probability of informed trader
    mu : price 
    theta : probability of high value 
    beta_buy : probability of buy who is noise trader  
    """

    theta = None
    phi = None
    beta_buy = None
        
    def __init__(self,theta,phi,beta_buy):
        self.theta = theta
        self.phi = phi
        self.beta_buy = beta_buy

    def cal_ask_price(self,mu,high_value,low_value):
        ask = mu + ((self.theta*(1-self.theta)*self.phi)/((1-self.phi)*self.beta_buy + self.phi*self.theta))*(high_value-low_value)
        return ask

    def cal_bid_price(self,mu,high_value,low_value):
        bid = mu - (((self.theta*(1-self.theta))*self.phi)/((1-self.phi)*(1-self.beta_buy) + self.phi*(1-self.theta)))*(high_value - low_value)
        return bid

    def spread(self,mu,high_value,low_value):
        spread = self.cal_ask_price(mu,high_value,low_value) - self.cal_bid_price(mu,high_value,low_value) 
        return spread
    