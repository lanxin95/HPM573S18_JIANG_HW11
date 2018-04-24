POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52        # year (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03     # annual discount rate

# transition rate matrix
Rate_MATRIX = [
    [None, 0.0135,      0,  0.0015, 0.018],   # Well
    [0   ,   None,  52.14,       0,   0.0],   # Stroke
    [0   ,0.02984,   None, 0.00746, 0.018],   # Post-Stroke
    [0   ,      0,      0,    None,     0],   # Stroke Death
    [0   ,      0,      0,       0,  None]   # non-stroke Death
    ]

anticoag_Rate_MATRIX = [
    [None, 0.0135,      0,  0.0015, 0.018],   # Well
    [0   ,   None,  52.14,       0,   0.0],   # Stroke
    [0   ,0.02238,   None, 0.00746,0.0189],   # Post-Stroke
    [0   ,      0,      0,    None,     0],   # Stroke Death
    [0   ,      0,      0,       0,  None]   # non-stroke Death
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,       # Well
    0.2,  # Stroke
    0.9,    # Post-Stroke
    0,        #  Stroke Death
    0  # non-stroke Death
    ]

# annual cost of each health state
STATE_COST = [
    0,     # Well
    0,  # Stroke, one time
    200,   # Post-Stroke, annual
    0 ,     # Dead
    0  # Dead
    ]


# annual cost of each health state
anticoag_STATE_COST = [
    0,     # Well
    0,  # Stroke, one time
    750,   # Post-Stroke, annual, if anitcoag is used
    0  ,     # Dead
    0  # Dead
  ]

Stroke_cost=5000 # one time stroke cost
