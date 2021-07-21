class MonteCarlo_simulation:
    MC_COUNTER = 10000

    @property
    def mc_counter(self):
        return self.MC_COUNTER


# events is a list of objects of type Event
def simulate_inherent_risk_portfolio(events):
    total_loss_amount = 0
    for event in events:
        total_loss_amount += event.simulated_inherent_loss()
    return total_loss_amount

def simulate_residual_risk_portfolio(events):
    total_loss_amount = 0
    for event in events:
        total_loss_amount += event.simulated_residual_loss()
    return total_loss_amount

def mc_simulation(events, inherent):
    mc = MonteCarlo_simulation()
    result_losses_list = []
    if inherent:
        for _ in range(mc.MC_COUNTER):
            result_losses_list.append(simulate_inherent_risk_portfolio(events))
    else:
        for _ in range(mc.MC_COUNTER):
            result_losses_list.append(simulate_residual_risk_portfolio(events))
    return result_losses_list


