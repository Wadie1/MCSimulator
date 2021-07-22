# MCSimulator
A Simulator model to assist in quantifying risk in Cybersecurity Risk-management.
## How to use it
This version of the model is still pretty basic as the interface is still not done. Thus, everything works with your terminal.
After you have set the terminal in the right path of your device, execute the file `main.py` and then follow these steps :
- First, enter the number of risks/events you want to the model to simulate.
- Then, for each event:
  - Enter its Likelihood:  it's the estimatinon of the probability of the event occurring in a year (it has to be beteween 0 and 1).
  - Estimating a 90% confidence interval for a monetized loss, i.e. we are 90% confident that the loss would fall in that range. Example: “If event X occurs, there is a 90% chance the loss will be between $1 million and $8 million.” For that :
    - Enter its Lower Bound.
    - Then its Upper Bound.
  - *(Optional)* Estimating the mitigation control effectiveness. For that :
    - Enter the effectiveness of the control (it has to be beteween 0 and 1)
    - Enter the total cost of control for this event.
- Repeat as many times as the number of risks you want to simulate.

And that's it, you will then get some relevent data in the terminal plus a graph will pop up showing two loss exceedance curves; one of the inherent loss and the other of the residual risk.
