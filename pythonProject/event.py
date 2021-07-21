import numpy as np
from scipy.stats import lognorm


class Event:
    CONTROL = False

    def __init__(self, likelihood, lb, ub, control_eff=0, cost_of_control=0, name=None):
        self.name = name
        self.likelihood = likelihood
        self.lb = lb
        self.ub = ub
        self.control_eff = control_eff
        self.cost_of_control = cost_of_control
        if self.control_eff:
            self.CONTROL = True

    def expected_inherent_loss(self):
        return np.exp((np.log(self.ub) + np.log(self.lb)) / 2 + (
                np.square((np.log(self.ub) - np.log(self.lb)) / 3.28971) * 0.5)) * self.likelihood

    def simulated_inherent_loss(self):
        # Compute the simulated inherent loss of event using the lognormal distribution
        pb = np.random.rand()
        if pb >= self.likelihood:
            sil = 0
        else:
            sil = lognorm.ppf(pb, (np.log(self.ub) - np.log(self.lb)) / 3.29, loc=0,
                              scale=np.exp((np.log(self.ub) + np.log(self.lb)) / 2))
        return sil

    def expected_residual_loss(self):
        if self.control_eff:
            return (1 - self.control_eff) * self.expected_inherent_loss()
        return self.expected_inherent_loss()

    def roc(self):
        if self.control_eff:
            return ((self.expected_inherent_loss() - self.expected_residual_loss()) / self.cost_of_control) - 1
        return 0

    def simulated_residual_loss(self):
        pb = np.random.rand()
        if pb >= self.likelihood:
            sil = 0
        else:
            sil = lognorm.ppf(pb, 0.02896965951, loc=0, scale=self.cost_of_control)
        return sil
