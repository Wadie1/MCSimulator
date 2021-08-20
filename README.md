# MCSimulator
A Simulator model to assist in quantifying risk in Cybersecurity Risk-management.
## How to use it
The interface gives the user two possible ways of entering data. The first one is to enter it manually, and the other way is by importing a .csv file  (that can be exported from Excel or any other tool the user prefer).

- Manual method:
The user enters manually and one by one the events, by entering in each field the requested data of the event. The control effectiveness and the costs of control fields are optional, meaning the user can leave them empty if he/she doesn’t want to make an analysis on mitigation.
 - Enter its Likelihood:  it's the estimatinon of the probability of the event occurring in a year (it has to be beteween 0 and 1).
  - Estimating a 90% confidence interval for a monetized loss, i.e. we are 90% confident that the loss would fall in that range. Example: “If event X occurs, there is a 90% chance the loss will be between $1 million and $8 million.” For that :
    - Enter its Lower Bound.
    - Then its Upper Bound.
  - *(Optional)* Estimating the mitigation control effectiveness. For that :
    - Enter the effectiveness of the control (it has to be beteween 0 and 1)
    - Enter the total cost of control for this event.
- Repeat as many times as the number of risks you want to simulate.

He clicks then on ‘Add Risk’ button and repeats the process for every events he wishes to enter. 
When all events are entered, he/she only have to click on ‘Submit’.

- Importing a csv file:
This methods is the simplest, as the user only have to click on ‘Browse’ button and selects the .csv file containing the data, then to click on ‘Submit’.

And that's it, you will then get some relevent data, plus a graph will pop up showing two loss exceedance curves; one of the inherent loss and the other of the residual risk.
