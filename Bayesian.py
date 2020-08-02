from Simulation import Simulation 

class Bayesian (Simulation):
    """
    Bayesian method class
    :param: user_{}
    :type: User class object
    :param: epsilon - when the expected loss for one of the variants falls below the threshold: epislon, we stop the experiment.
    :type: int between 0 and 1 
    :param: plotter - paramert needed to be able to plot
    :param: time_off - the number of first observations we ignore
    :type: int
    :type: equeal to Plotter class object. 
    :param: size_of_sample - size of sample for calculating the number integral and selecting better arm.
    :type: int
    """
    def __init__ (self, user_a, user_b, epsilon, plotter, time_off=25, size_of_sample = 5000):
        super().__init__(user_a, user_b, plotter, size_of_sample)
        self.epsilon = epsilon 
        self.time_off = time_off

    def index_of(self): 
        for a,b in zip(self.loss_a[self.time_off:], self.loss_b[self.time_off:]):
            if b < self.epsilon and a > self.epsilon: 
                index_of_b = self.loss_b.index(b)
                index_of_a = self.user_a.get_number_of_observations() 
                break 
            elif a < self.epsilon and b > self.epsilon: 
                index_of_a = self.loss_a.index(a) 
                index_of_b = self.user_b.get_number_of_observations()
                break
            else: 
                index_of_a = self.user_a.get_number_of_observations() 
                index_of_b = self.user_b.get_number_of_observations()
        
        return index_of_a, index_of_b

    def plot_loss(self): 
        index_of_winner = min(self.index_of())
        self.plotter.plot_loss(self.choose_a, self.choose_b, self.loss_a, self.loss_b, self.epsilon, index_of_winner)