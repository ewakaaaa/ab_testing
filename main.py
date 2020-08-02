#%%
from User import User 
from Plotter import Plotter
from Simulation import Simulation
from Bayesian import Bayesian
from MultiArmBandit import MultiArmBandit

if __name__ == "__main__": 

    user_a = User(0.1,1000)
    user_b = User(0.5,1000)

    user_a.generate_user_clicks()
    user_b.generate_user_clicks()

    plotter = Plotter()

    bayesian = Bayesian(user_a, user_b, 0.1, plotter)
    bayesian.simulate(1) 

    #multiarmbandit = MultiArmBandit(user_a, user_b, 0.8, plotter) 
    #multiarmbandit.simulate(0.1) 

    print(bayesian.get_winner_arm())
    print(bayesian.observations_performed())

    # print(multiarmbandit.get_winner_arm())
    # print(multiarmbandit.observations_performed())
