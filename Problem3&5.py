import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

#Problem 3: Simulation (Weight 4): Use Monte Carlo to simulate patients for 15 years (from age 65 to 80).
# To evaluate these continuous-time Markov models, we need to convert them to discrete-time Markov models.
# Find an appropriate cycle length to simulate these discrete-time Markov models.

# simulating no therapy
# create a cohort
cohort_no = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_no = cohort_no.simulate()

# simulating anticoagulation therapy
# create a cohort
cohort_ANTICOAG = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_ANTICOAG = cohort_ANTICOAG.simulate()

SupportMarkov.print_outcomes(simOutputs_no, "No Drug:")
SupportMarkov.print_outcomes(simOutputs_ANTICOAG, "Anticoagulation:")

# print comparative outcomes
print("Problem 2")
SupportMarkov.print_comparative_outcomes(simOutputs_no, simOutputs_ANTICOAG)

#Problem 5: Economic Evaluation (Weight 2): Perform economic evaluation using cost-utility analysis
# with discount rate 3%.
# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_no, simOutputs_ANTICOAG)


