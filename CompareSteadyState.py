import InputData as D
import SurvivalModelClasses as Cls
import SupportSteadyState as Support

# create a cohort of patients for when the drug is not available
cohortNoDrug = Cls.Cohort(
    id=1,
    pop_size=D.SIM_POP_SIZE,
    mortality_prob=D.MORTALITY_PROB)
# simulate the cohort
cohortNoDrug.simulate(n_time_steps=D.TIME_STEPS)

# create a cohort of patients for when the drug is available
cohortWithDrug = Cls.Cohort(

)
# simulate the cohort
cohortWithDrug.simulate(n_time_steps=D.TIME_STEPS)

# print outcomes of each cohort
Support.print_outcomes(simulated_cohort=cohortNoDrug,
                       strategy_name='When drug is not available:')
Support.print_outcomes(simulated_cohort=cohortWithDrug,
                       strategy_name='When drug available:')

# draw survival curves and histograms
Support.draw_survival_curves_and_histograms(cohort_no_drug=cohortNoDrug,
                                            cohort_with_drug=cohortWithDrug)

# print comparative outcomes
Support.print_comparative_outcomes(cohort_no_drug=cohortNoDrug,
                                   cohort_with_drug=cohortWithDrug)
