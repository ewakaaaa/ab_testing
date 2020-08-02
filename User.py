import scipy.stats as scs

class User: 
    """
    Class that generates user behavior, according to the Bernulli distribution with a given probability p_known
    :param p_known: 
    :type: int between 0 and 1 
    :param number_of_obsevations: the number of iterations of the algorithm we want 
    :type: int
    """ 
    def __init__(self, p_known, number_of_observations):
        self.p_known = p_known 
        self.number_of_observations = number_of_observations
        self.user_clicks =[]

    def generate_user_clicks(self):
        for i in range(self.number_of_observations): 
            self.user_clicks.append(scs.bernoulli(self.p_known).rvs())

    def get_user_clicks(self):
        return self.user_clicks

    def get_number_of_observations(self): 
        return self.number_of_observations
    
    def get_p_known(self): 
        return self.p_known
