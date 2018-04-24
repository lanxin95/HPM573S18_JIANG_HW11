from enum import Enum
import InputData as Data
import scr.MarkovClasses as MarkovCls

class HealthStats(Enum):
    """ health states of patients with stroke """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    Stroke_DEATH = 3
    BACKGROUND_DEATH = 4


class Therapies(Enum):
    """ none vs. anticoagulation """
    NONE = 0
    ANTICOAG = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # calculate the adjusted discount rate
        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T
        #one time stroke cost
        self._onetime_Stroke_cost=Data.Stroke_cost
        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk

        # calculate transition probabilities and treatment cost depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix =calculate_prob_matrix()
            self._annualStateCosts = Data.STATE_COST
        else:
            self._prob_matrix = calculate_prob_matrix_anticoag()
            self._annualStateCosts = Data.anticoag_STATE_COST

        # annual state costs and utilities
        self._annualStateUtilities = Data.ANNUAL_STATE_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state == HealthStats.Stroke_DEATH or state==HealthStats.BACKGROUND_DEATH:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state == HealthStats.Stroke_DEATH or state==HealthStats.BACKGROUND_DEATH:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_onetime_Stroke_cost(self):
        return self._onetime_Stroke_cost



def calculate_prob_matrix():
    """ :returns convert continuous-time Markov matrix to discrete time matrix"""
    prob_matrix=[]
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(Data.Rate_MATRIX, Data.DELTA_T)
    return prob_matrix

def calculate_prob_matrix_anticoag():
    """ :returns transition probability matrix under anticoagulation use convert continuous-time Markov matrix to discrete time matrix"""

    # create an empty matrix populated with zeroes
    prob_matrix = []
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(Data.anticoag_Rate_MATRIX, Data.DELTA_T)
    return prob_matrix
