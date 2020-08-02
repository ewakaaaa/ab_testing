from Simulation import Simulation 

class MultiArmBandit(Simulation): 
    """
    Multi arm bandit method class
    :param: user_{}
    :type: User class object
    :param: epsilon - the percentage of time that the winning variant is displayed. Once this threshold is reached, the experiment ends.
    :type: int between 0 and 1 
    :param: plotter - paramert needed to be able to plot
    :type: equeal to Plotter class object. 
    :param: size_of_sample - size of sample for calculating the number integral and selecting better arm.
    :type: int
    """

    def __init__ (self, user_a, user_b, epsilon, plotter, size_of_sample = 5000):
        super().__init__(user_a, user_b, plotter, size_of_sample)
        self.epsilon = epsilon 
        
    def __index_of(self, vector, number_of_observations, espilon):
        for i in vector[10:]:
            if i>espilon: 
                index_of = vector.index(i)
                break
            else: 
                index_of = number_of_observations
        return index_of 
    
    def index_of(self): 
        index_of_a = self.__index_of(self.percent_of_choosen_a, self.user_a.get_number_of_observations(), self.epsilon) 
        index_of_b = self.__index_of(self.percent_of_choosen_b, self.user_b.get_number_of_observations(), self.epsilon)
        return index_of_a, index_of_b 

    def plot_winning_arm(self):
        winner = self.get_winner_arm()
        index_of_winner = min(self.index_of())
        if winner == 'a': 
            percent_of_choosen_arm = self.percent_of_choosen_a
        elif winner == 'b': 
            percent_of_choosen_arm = self.percent_of_choosen_b
        else : 
            print(winner) 
            return

        self.plotter.plot_winning_arm(self.choose_a, self.choose_b, percent_of_choosen_arm, index_of_winner, winner)

