import PySimpleGUI as sg
import pandas as pd

def file_chooser_popup():
    layout = [
        [sg.Text('Select an input file:')],
        [sg.FileBrowse(file_types=(('CSV Files', '*.csv'), ('ODF Files', '*.ods'), ('Excel Files', '*.xlsx')))],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('File Chooser', layout)
    event, values = window.read()
    window.close()
    if event == 'Submit':
        filename = values['Browse']
        return filename
    else:
        return None

def data_selection_popup(df):
    layout = [
        [sg.Text('Select the column that contains the act name:'), sg.Combo(df.columns)],
        [sg.Text('Select the column that contains the primary contact name:'), sg.Combo(df.columns)],
        [sg.Text('Select the column that contains the number of people in the act:'), sg.Combo(df.columns)],
        [sg.Text('Select the column that contains the time the act takes the stage:'), sg.Combo(df.columns)],
        [sg.Text('Select the column that contains the time the performance begins:'), sg.Combo(df.columns)],
        [sg.Text('Select the column that contains the time the act must vacate the stage:'), sg.Combo(df.columns)],
        [sg.Submit()]
    ]
    window = sg.Window('Data Selection', layout)
    event, values = window.read()
    window.close()
    return values


def main():
    # Display the file chooser popup
    filename = file_chooser_popup()
    if filename is None:
        return
    file_extension = filename.split('.')[-1].lower()

    if file_extension == 'xlsx':
        # Read data from Excel file
        df = pd.read_excel(filename)
    elif file_extension == 'csv':
        # Read data from CSV file
        df = pd.read_csv(filename)
    elif file_extension == 'ods':
        # Read data from ODS file
        df = pd.read_excel(filename, engine='odf')
    else:
        return # Invalid file type
    selections = data_selection_popup(df)

    # Extract the selected columns from the DataFrame
    act_col = df[selections[0]]
    contact_col = df[selections[1]]
    num_people_col = df[selections[2]]
    stage_time_col = df[selections[3]]
    begin_time_col = df[selections[4]]
    vacate_time_col = df[selections[5]]

    # Process the data as needed
    # ...

main()