import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

class Plotter: 
    """
    Class that can plot
    """
    def plot_probabilities(self, choose_a, choose_b , p_a_known, p_a, p_b_known, p_b):
        #fig, ax = plt.subplots(figsize=(12, 6))
        number_of_iteration = max(choose_a) + max(choose_b)
        x = np.arange(number_of_iteration)
        plt.plot(x,p_a, label = "p_a") 
        plt.plot(x,p_b, label = "p_b") 
        plt.axhline(y=p_a_known, color='r', linestyle='dashed')
        plt.axhline(y=p_b_known, color='b', linestyle='dashed')
        plt.xlabel('the number of iterations of the algorithm')
        plt.ylabel('value of probability')
        plt.legend()
        plt.show()

    def plot_loss(self, choose_a, choose_b, loss_a, loss_b, epsilon, index_of_winner): 
        #fig, ax = plt.subplots(figsize=(12, 6))
        number_of_iteration = max(choose_a) + max(choose_b)
        x = np.arange(number_of_iteration)
        plt.plot(x,loss_a, label = "loss_a") 
        plt.plot(x,loss_b, label = "loss_b") 
        plt.axhline(y=epsilon, color='b', linestyle='dashed')
        plt.axvline(x=index_of_winner,color='b', linestyle='dashed')
        plt.xlabel('the number of iterations of the algorithm')
        plt.ylabel('value of probability')
        plt.legend()
        plt.show()

    def plot_winning_arm(self, choose_a, choose_b, percent_of_choosen_arm, index_of_winner, winner):
        #fig, ax = plt.subplots(figsize=(12, 6))
        number_of_iteration = max(choose_a) + max(choose_b)
        x = np.arange(number_of_iteration)
        plt.plot(x, percent_of_choosen_arm, label = "p_{}".format(winner), color ='tab:blue') 
        plt.xlabel('the number of iterations of the algorithm')
        plt.ylabel('arm eligibility percentage')
        plt.axvline(index_of_winner,color='b', linestyle='dashed')
        plt.legend()
        plt.show()