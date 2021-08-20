import PySimpleGUI as sg
import numpy
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from event import *
from montecarlo_simulation import *
from lec import plot_graph

sg.change_look_and_feel('DarkTanBlue')

data_list_column = [
    #[sg.Text('Enter the number of risks you want to enter:'), sg.InputText(size=(25, 1), enable_events=True, key="-MANUAL-", text_color='grey')],
    [sg.Text('Please enter the data of your event')],
    [sg.Text('Enter its Name : '), sg.InputText(size=(25, 1), enable_events=True, key="-name-" , text_color='grey')],
    [sg.Text('enter its likelihood : '), sg.InputText(size=(25, 1), enable_events=True, key="-likelihood-" , text_color='grey')],
    [sg.Text('enter its lower bound : '), sg.InputText(size=(25, 1), enable_events=True, key="-lb-" , text_color='grey')],
    [sg.Text('enter its upper bound : '), sg.InputText(size=(25, 1), enable_events=True, key="-ub-" , text_color='grey')],
    [sg.Text('enter its control effectiveness (Optional) : '), sg.InputText(size=(25, 1), enable_events=True, key="-ctrleff-" , text_color='grey')],
    [sg.Text('enter the cost of control lower bound (Optional) : '), sg.InputText(size=(25, 1), enable_events=True, key="-costctrl_lb-" , text_color='grey')],
    [sg.Text('enter the cost of control upper bound (Optional) : '), sg.InputText(size=(25, 1), enable_events=True, key="-costctrl_ub-" , text_color='grey')],
    [sg.Button("Add Risk")],
    [sg.Text()],
    [sg.Text('Or choose your csv file:'), sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"), sg.FileBrowse()],
    [sg.Button("Submit")],
    ]

graph_viewer_column = [
    [sg.Text("The graphs :")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Text('Relevant computed data :')],
    [sg.Text('Mean : '), sg.Text(size=(25,1), key='-mean-')],
    [sg.Text('Median : '), sg.Text(size=(25,1), key='-median-')],
    [sg.Text('Standard deviation : '), sg.Text(size=(25,1), key='-std-')],
    ]

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


layout = [
    [
        sg.Column(data_list_column),
        sg.VSeperator(),
        sg.Column(graph_viewer_column),
    ]
]

window = sg.Window("Simulation Window", layout)
risk_list = []
eff_true = False

def interface():
    global eff_true
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            file = values["-FOLDER-"]
            risk_list_csv = pd.read_csv(file, sep=";").head()
            for _, risk in risk_list_csv.iterrows():
                eff_true = risk["control_eff"]
                risk = Event(risk["likelihood"], risk["lb"], risk["ub"], risk["control_eff"],
                             risk["cost_of_control_lb"], risk["cost_of_control_ub"], risk['Name'])
                risk_list.append(risk)
        if event == "Add Risk":
            if values["-ctrleff-"]:
                eff_true = True
                risk = Event(float(values["-likelihood-"]), int(values["-lb-"]), int(values["-ub-"]), float(values["-ctrleff-"]), int(values["-costctrl_lb-"]), int(values["-costctrl_ub-"]), values["-name-"])
            else:
                risk = Event(float(values["-likelihood-"]), int(values["-lb-"]), int(values["-ub-"]), None, None, None, values["-name-"])
            risk_list.append(risk)
        if event == "Submit":
            if eff_true:
                table_list = []
                for event in risk_list:
                    table_list.append([event.name, event.expected_residual_loss(), event.roc()])
                layout2 = [
                    [sg.Text('The return on control')],
                    [sg.Table(values=table_list, headings=['Name', 'Expected Residual Loss', 'Return on Control'],
                              max_col_width=25, background_color='black',
                              auto_size_columns=True,
                              display_row_numbers=True,
                              justification='right',
                              num_rows=10,
                              alternating_row_color='darkblue',
                              key='-TABLE-',
                              tooltip='This is a table')],
                    [sg.Button('Exit')]
                ]
                window2 = sg.Window('Window 2', layout2, grab_anywhere=True)
                event, values = window2.read(timeout=100)
                if event != sg.TIMEOUT_KEY:
                    print("win2 ", event)
                if event == 'Exit':
                    window2.close()

            """Monte Carlo simulation"""
            result_losses_list = mc_simulation(risk_list, True)
            if eff_true:
                result_residual_list = mc_simulation(risk_list, False)

            """Important computed data"""
            window['-mean-'].update(numpy.mean(result_losses_list))
            window['-median-'].update(numpy.median(result_losses_list))
            window['-std-'].update(numpy.std(result_losses_list))

            """Plotting the lec graph"""
            fig = plot_graph(result_losses_list, not eff_true)
            """Plotting Residual risk plot"""
            if eff_true:
                fig = plot_graph(result_residual_list)
            draw_figure(window['-CANVAS-'].TKCanvas, fig)



    window.close()