# Doing imports
import PySimpleGUI as sg

# Creating a function inicial 
def criar_janela_inicial():
    
    # Defining the window's theme
    sg.theme('DarkAmber')
    
    # Creating objects to add in layout 
    line = [
        [sg.Text('Objetivo:', size=(15,0)), sg.InputText(key='objectives', size=(45,0))],
        [sg.Text('ERP:', size=(15,0)), sg.InputText(key='erp', size=(45,0))],
        [sg.Text('Método:', size=(15,0)), sg.InputText(key='method', size=(45,0))],
        [sg.Text('Validação:', size=(15,0)), sg.InputText(key='validation', size=(45,0))],
        [sg.Text('Tarefa:', size=(15,0)), sg.Combo(['Resolvida', 'Deletada', 'Aguardando'], enable_events=True, key='toDo', size=(43,0))],
        [sg.Text('Considerações:', size=(15,0)), sg.InputText(key='considerations', size=(45,0))],
        [sg.Text('Necessário:', size=(15,0)), sg.Multiline(key='needs', size=(43,5))],
        [sg.Text('Responsável:', size=(15,0)), sg.InputText(key='responsable', size=(45,0))],
        [sg.Button('Formatar'), sg.Button('Resetar')],
        [sg.Multiline(size=(60, 15), key='textbox')]
    ]

    # Create layout of window
    layout = [
        [sg.Frame('BOLETIM ETL', layout=line, key='container')],  
    ]
    
    # Return complete layout
    return sg.Window('Boletim ETL', layout=layout, finalize=True)

# Create window
janela = criar_janela_inicial() 

# Creating rules for window
while True:
    
    # Reading events and values of window 
    event, values = janela.read()
    
    # Creating conditional for in case you close the window
    if event == sg.WIN_CLOSED:
        break  
    
    # Creating conditional for in case you click in button 'Formatar'
    elif event == 'Formatar':
        # Taking InputText values
        objectives = values['objectives']
        erp = values['erp']
        method = values['method']
        validation = values['validation']
        toDo = values['toDo']
        considerations = values['considerations']
        needs = values['needs']
        responsable = values['responsable']
        
        # Cleaning and formating object Multiline
        text = janela['textbox']
        janela.find_element('textbox').Update('')
        text.update(text.get()+
f"""**BOLETIM ETL**\n
**Objetivo:** {objectives}
**ERP:** {erp}
**Método:** ETL / {method}
**Validação:** {validation}
**Tarefa:** {toDo}
**Considerações:** {considerations}\n
**Necessário:** {needs}
**Responsável:** {responsable}
""")
    
    # Creating conditional for in case you click in button 'Resetar'
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()