import numpy as np
import scipy.stats as scs
import random 
from abc import ABC, abstractmethod


class Simulation(ABC):
    """
    Class that make single simulation
    """ 
    def __init__ (self, user_a, user_b, plotter, size_of_sample):
        self.user_a = user_a 
        self.user_b = user_b 
        self.size_of_sample = size_of_sample 
        self.plotter = plotter

        self.p_a = []
        self.p_b = []
        self.choose_a = []
        self.choose_b = [] 
        #multi:
        self.percent_of_choosen_a = [] 
        self.percent_of_choosen_b = [] 
        #bayesian: 
        self.loss_a = [] 
        self.loss_b = []

    def __get_p (self, alpha, beta): 
        return alpha/(alpha+beta)

    def __calculate_alpha_beta(self, alpha, beta, reward):
        alpha = alpha + reward
        beta = beta + (1-reward)
        return alpha,beta  

    def __choose_arm(self, alpha_a, beta_a, alpha_b, beta_b):
        a_sample = scs.beta.rvs(alpha_a, beta_a, size=self.size_of_sample ,random_state = 10)
        b_sample = scs.beta.rvs(alpha_b, beta_b, size=self.size_of_sample ,random_state = 10)
        max_a = max(a_sample)
        max_b = max(b_sample)
        return max_a, max_b  

    def __get_loss(self, alpha_a, beta_a, alpha_b, beta_b):
        a_sample = scs.beta.rvs(alpha_a, beta_a, size=self.size_of_sample ,random_state = 10)
        b_sample = scs.beta.rvs(alpha_b, beta_b, size=self.size_of_sample ,random_state = 10)
        loss_a_one = np.mean((a_sample < b_sample) * (b_sample - a_sample))
        loss_b_one = np.mean((a_sample > b_sample) * (a_sample - b_sample))
        return loss_a_one, loss_b_one
        
    def simulate(self, time_of_random_arm, alpha_a=1, beta_a=1, alpha_b=1, beta_b=1):
        """
        Method that make single simulation 
        :param: time_of_random_arm - percent of time when algoritm pick random arm. For bayesian symulation equal to 1 
        :type: int between 0 and 1 
        :param: alpha_{} and beta_{} - starts alpha and beta from bernulli distibution 
        :type: int
        """
        count_a = 0 
        count_b = 0 

        for a,b in zip(self.user_a.get_user_clicks(), self.user_b.get_user_clicks()): 
            if random.random() < time_of_random_arm:
                # choose random arm by epsilon time.
                if random.random() < 0.5:
                    #choose A: 
                    reward = a 
                    alpha_a, beta_a = self.__calculate_alpha_beta(alpha_a,beta_a,reward)
                    count_a +=1 
                else: 
                    #choose B: 
                    reward = b
                    alpha_b, beta_b = self.__calculate_alpha_beta(alpha_b,beta_b,reward)
                    count_b +=1
            else:
                #choose better arm: 
                max_a, max_b = self.__choose_arm (alpha_a,beta_a,alpha_b,beta_b)
                if max_a > max_b: 
                    #choose A: 
                    reward = a
                    alpha_a, beta_a = self.__calculate_alpha_beta(alpha_a, beta_a, reward)
                    count_a +=1 
                else: 
                    #choose B: 
                    reward = b
                    alpha_b, beta_b = self.__calculate_alpha_beta(alpha_b, beta_b, reward)
                    count_b +=1 

            self.p_a.append(self.__get_p(alpha_a, beta_a))
            self.p_b.append(self.__get_p(alpha_b, beta_b))      
    
            self.choose_a.append(count_a)
            self.choose_b.append(count_b)
    
            self.percent_of_choosen_a.append(count_a/(count_a+count_b))
            self.percent_of_choosen_b.append(count_b/(count_a+count_b))

            loss_a_one, loss_b_one = self.__get_loss(alpha_a, beta_a, alpha_b, beta_b)
            self.loss_a.append(loss_a_one)
            self.loss_b.append(loss_b_one)

    def get_loss_vector (self):
        return self.loss_a, self.loss_b 

    @abstractmethod
    def index_of(self):
        pass

    def get_winner_arm (self):
        index_a, index_b = self.index_of()
        if index_a < index_b: 
            return "a"
        if index_b < index_a: 
            return "b" 
        else: 
            return "we can't pick the winner"

    def observations_performed(self):
        index_a, index_b = self.index_of()
        if (index_a == self.user_a.get_number_of_observations() and index_b == self.user_b.get_number_of_observations()): 
            sum_of_observations = "we can't pick the winner"
        else: 
            min_of_index = min(self.index_of())
            sum_of_observations = self.choose_a[min_of_index] + self.choose_b[min_of_index]
        return sum_of_observations

    def plot_probabilities(self):
        self.plotter.plot_probabilities(self.choose_a, self.choose_b, self.user_a.get_p_known(), self.p_a, self.user_b.get_p_known(), self.p_b)
