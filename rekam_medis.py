#import simple gui and pandas
import PySimpleGUI as sg
import pandas as pd


# add some color to the window
sg.theme('GreenTan')

#tambah excel file
EXCEL_FILE1 = 'RMoffline.xlsx'
df = pd.read_excel(EXCEL_FILE1)


#-----Menu Definition -----#
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Copy', 'Paste',['Special', 'Norrmal', ], 'Undo', 'Redo']],
            ['Help', 'About ....'], ]

#----Column Definition ----#
column1 = [[sg.Text('Dokter', size=(15,1)), sg.InputOptionMenu(default_value='Zico permadi,MD', values=('Zico permadi,MD', 'Tri Widyastuti'), key='Dokter Pemeriksa'),
            sg.Text('Keluhan Utama', size=(15,1)), sg.Multiline(default_text='', size=(35,3), key='Keluhan Utama')],]



column2 = [[sg.Text('Kesadaran', justification='center', size=(15,1)),
            sg.InputOptionMenu(default_value='Compos Mentis', values=('Compos Mentis', 'Somnolen', 'Sopor', 'Coma'), key='Kesadaran'),],
            [sg.Text('Sistole', justification='center', size=(15,1),), sg.Slider(range=(1,220), orientation='h', size=(14, 15), default_value=120, key='Sistole'), sg.Text('mm')],
            [sg.Text('Diastole', justification='center', size=(15,1),), sg.Slider(range=(1,140), orientation='h', size=(14, 15), default_value=80, key='Diastole'), sg.Text('Hg')],
            [sg.Text('Tinggi Badan', justification='center', size=(15,1)), sg.InputText('', size=(18,1), key=('Tinggi Badan')), sg.Text('Cm')],
            ]

column3 = [[sg.Text('Suhu', justification='center', size=(15,1)), sg.InputText('', size=(18,1), key=('Suhu')), sg.Text('°C')],
            [sg.Text('Berat Badan', justification='center', size=(15,1)), sg.InputText('', size=(18,1), key=('Berat Badan')),sg.Text('KG')],
            [sg.Text('Nadi', justification='center', size=(15,1)), sg.InputText('', size=(18,1), key=('Nadi')), sg.Text('x/menit')],
            [sg.Text('Nafas', justification='center', size=(15,1)), sg.InputText('', size=(18,1), key=('Nafas')), sg.Text('x/menit')],]

column4 = [[sg.Text('Diagnosa 1'), sg.InputText('', size=(20,1), key=('Diagnosa 1')),
            sg.Text('Diagnosa 2'), sg.InputText('', size=(20,1), key=('Diagnosa 2'))],] 

column5 = [[sg.Multiline('', size=(40,4), key='Resep')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Rekam Medis', size=(45,1), justification='center', font=("helvetica", 20), relief=sg.RELIEF_RAISED)],
    [sg.Frame('Anamnesa', [
        [sg.Column(column1,)]])],
    [sg.Frame('Pemeriksaan Fisik', [
        [sg.Column(column2,), sg.Column(column3)]], relief=sg.RELIEF_SUNKEN)],
    [sg.Frame( layout=[
    [sg.Checkbox('Tidak ada', size=(10,1), default=True, key=('Riwayat Penyakit')),  sg.Checkbox('Alergi Obat', key=('Alergi Obat'))]], title='Riwayat Penyakit', title_color='red', relief=sg.RELIEF_SUNKEN)],
    [sg.Frame('Diagnosa', [
        [sg.Column(column4)]])],
    [sg.Frame('Resep', [
        [sg.Column(column5)]],)],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Rekam Medis Offline dr. zico', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE1, index=False)
        sg.popup('Data SAVED!!!!')
        clear_input()
window.close()