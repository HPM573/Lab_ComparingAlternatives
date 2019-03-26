import InputData as D
import MultiSurvivalModelClasses as Cls
import SupportTransientState as Support

# create multiple cohorts for when the drug is not available
multiCohortNoDrug = Cls.MultiCohort(
    ids=range(D.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[D.REAL_POP_SIZE] * D.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[D.MORTALITY_PROB] * D.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortNoDrug.simulate(n_time_steps=D.TIME_STEPS)

# create multiple cohorts for when the drug is available
multiCohortWithDrug = Cls.MultiCohort(

)

# simulate all cohorts
multiCohortWithDrug.simulate(n_time_steps=D.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(multi_cohort=multiCohortNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(multi_cohort=multiCohortWithDrug,
                       strategy_name='When drug is available:')

# draw histograms of average survival time
Support.draw_histograms(multi_cohort_no_drug=multiCohortNoDrug,
                        multi_cohort_with_drug=multiCohortWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(multi_cohort_no_drug=multiCohortNoDrug,
                                   multi_cohort_with_drug=multiCohortWithDrug)
