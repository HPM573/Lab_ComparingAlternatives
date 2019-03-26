import SimPy.SamplePathClasses as PathCls
import SimPy.FigureSupport as Figs
import SimPy.StatisticalClasses as Stat
import InputData as D


def print_outcomes(simulated_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param simulated_cohort: a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # create a summary statistics
    survival_time_stat = Stat.SummaryStat(name='Survival time statistics',
                                          data=simulated_cohort.cohortOutcomes.survivalTimes)

    # get mean and confidence confidence interval
    mean = survival_time_stat.get_mean()
    conf_int = survival_time_stat.get_t_CI(alpha=D.ALPHA)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)


def draw_survival_curves_and_histograms(cohort_no_drug, cohort_with_drug):
    """ draws the survival curves and the histograms of survival time
    :param cohort_no_drug: a cohort simulated when drug is not available
    :param cohort_with_drug: a cohort simulated when drug is available
    """

    # get survival curves of both treatments
    survival_curves = [
        cohort_no_drug.cohortOutcomes.nLivingPatients,
        cohort_with_drug.cohortOutcomes.nLivingPatients
    ]

    # graph survival curve
    PathCls.graph_sample_paths(
        sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step',
        y_label='Number of alive patients',
        legends=['No Drug', 'With Drug']
    )

    # histograms of survival times
    set_of_survival_times = [
        cohort_no_drug.cohortOutcomes.survivalTimes,
        cohort_with_drug.cohortOutcomes.survivalTimes
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of patient survival time',
        x_label='Survival time',
        y_label='Counts',
        bin_width=1,
        legend=['No Drug', 'With Drug'],
        transparency=0.6
    )


def print_comparative_outcomes(cohort_no_drug, cohort_with_drug):
    """ prints expected and percentage increase in survival time when drug is available
    :param cohort_no_drug: a cohort simulated when drug is not available
    :param cohort_with_drug: a cohort simulated when drug is available
    """

    # create a difference statistics for the increase in survival time
    increase_stat =

    # get mean and t-based confidence interval for the increase in survival time
    mean = increase_stat.get_mean()
    conf_int = increase_stat.get_t_CI(alpha=D.ALPHA)

    print("Average increase in survival time (years) and {:.{prec}%} confidence interval:"
          .format(1 - D.ALPHA, prec=0), mean, conf_int)
