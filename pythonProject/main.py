# Model 1.1
# Can evaluate n events and optionally their residual risk
# Events are supposed independent in this model


from event import *
from montecarlo_simulation import *
from lec import plot_graph

import numpy
import pandas as pd


def main():
    global control_eff, result_residual_list
    risk_list = []
    csv = input('Do you want to enter data manually ? y/n ')
    if csv == 'y':
        n_risks = int(input('enter the number of risks you want to enter: '))
        while n_risks:
            print('enter the data of your risk')
            likelihood = float(input('enter its likelihood : '))
            lb = int(input('enter its lower bound : '))
            ub = int(input('enter its upper bound : '))
            control_eff = input('enter control effectiveness (Optional): ')
            if control_eff:
                control_eff = float(control_eff)
                cost_of_control = int(input('enter total cost of control (Optional): '))
                risk = Event(likelihood, lb, ub, control_eff, cost_of_control)
            else:
                control_eff = False
                risk = Event(likelihood, lb, ub)
            risk_list.append(risk)
            n_risks -= 1

    else:
        risk_list_csv = pd.read_csv('test.csv', sep=";").head()
        for _, risk in risk_list_csv.iterrows():
            control_eff = risk["control_eff"]
            risk = Event(risk["likelihood"], risk["lb"], risk["ub"], risk["control_eff"],
                         risk["cost_of_control"], risk['Name'])
            risk_list.append(risk)

    for event in risk_list:
        print(event.name, '-> expected residual loss : ', event.expected_residual_loss(), 'Return on Control : ', event.roc())

    """Monte Carlo simulation"""
    result_losses_list = mc_simulation(risk_list, True)
    if control_eff:
        result_residual_list = mc_simulation(risk_list, False)

    """Important computed data"""
    print('Relevant computed data')
    print('Mean : ', numpy.mean(result_losses_list))
    print('Median : ', numpy.median(result_losses_list))
    print('Standard deviation : ', numpy.std(result_losses_list))

    """Plotting the lec graph"""
    plot_graph(result_losses_list, not control_eff)

    """Plotting Residual risk plot"""
    if control_eff:
        plot_graph(result_residual_list)


if __name__ == "__main__":
    main()
