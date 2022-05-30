#import simple gui and pandas
import PySimpleGUI as sg
import pandas as pd


# add some color to the window
sg.theme('GreenTan')


#-----Menu Definition -----#
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Copy', 'Paste',['Special', 'Norrmal', ], 'Undo', 'Redo']],
            ['Help', 'About ....'], ]

#----Column Definition ----#
column1 = [[sg.Text('Dokter', size=(15,1)), sg.InputOptionMenu(default_value='Zico permadi,MD', values=('Zico permadi,MD', 'Tri Widyastuti'), key='Dokter Pemeriksa'),
            sg.Text('Keluhan Utama', size=(15,1)), sg.Multiline(default_text='', size=(35,3), key='Keluhan Utama')],]



column2 = [[sg.Text('Kesadaran', justification='center', size=(10,1)),
            sg.InputOptionMenu(default_value='Compos Mentis', values=('Compos Mentis', 'Somnolen', 'Sopor', 'Coma'), key='Kesadaran'),],
            [sg.Text('Sistole', justification='center', size=(10,1),), sg.Slider(range=(1,220), orientation='h', size=(10, 20), default_value=120, key='Sistole')],
            [sg.Text('Diastole', justification='center', size=(10,1),), sg.Slider(range=(1,140), orientation='h', size=(10, 20), default_value=80, key='Diastole')],]


layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Rekam Medis', size=(35,1), justification='center', font=("helvetica", 20), relief=sg.RELIEF_RIDGE)],
    [sg.Frame('Anamnesa', [
        [sg.Column(column1,)]])],
    [sg.Frame('Pemeriksaan Fisik', [
        [sg.Column(column2, background_color='#ffffff')]])],
    
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Rekam Medis Offline dr. zico', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        clear_input()
window.close()