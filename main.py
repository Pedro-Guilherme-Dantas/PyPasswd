import PySimpleGUI as sg
import back
from tkinter import messagebox
sg.theme('dark grey 9')

def frontLogin():
    
    layout1 = [
        [sg.Text('LOGIN')],
        [sg.Text('User:', size=(7,1)),sg.InputText('', key='-NAME-')],
        [sg.Text('Senha:', size=(7,1)),sg.InputText('', key='-SENHA-', password_char='*')],
        [sg.Button('Entrar')]
        

    ]
    
    windowLogin = sg.Window('Login', layout1, size=(600,250), element_justification='center')

    while True:
        
        event, values = windowLogin.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break     

        if event == 'Entrar':
            
            if back.enter(values['-NAME-'], values['-SENHA-']) == None:

                windowLogin.close()
                messagebox.showinfo('ERRO', \
                'Credenciais incorretos')
                frontLogin()
        
            else:
                windowLogin.close()
                frontMain(back.enter(values['-NAME-'], values['-SENHA-']))

def frontMain(con):

    layout2 = [
        [sg.Text('Logins Registrados:')],
        [sg.Text('')],
        [sg.Text('Serviço', size=(15,1)), sg.Text('User/Email', size=(30,1))]
        
    ]

    listLogins = back.selectData(con)
    
    for row in listLogins:
        layout2.append([

                sg.Text(row[1], size=(15,1)), sg.Text(row[2], size=(30,1)), 
                sg.Button('Visualizar senha', size=(15,1), key=row[3]),
                sg.Button('Excluir', size=(15,1), key='del__'+str(row[0]), button_color=('white', '#B22222'))
                
                ])
        
        
    layout2.append( [sg.Button('Criar novo')] )

    window = sg.Window('Dados',layout2,size=(600,300))

    while True:
        
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Criar novo':
            window.close()
            newLogin(con)

        else:
            parting = event.split('__')
            if len(parting) > 1:              
                back.delete(con, parting[1])
                window.close()
                frontMain(con)
            else:
                messagebox.showinfo('Senha', \
            event)


def newLogin (con):

    layoutNewLogin = [
        [sg.Text('Plataforma:', size=(13,1)), sg.InputText('', key='-plataforma-')],
        [sg.Text('Email/username:', size=(13,1)), sg.InputText('', key='-email-')],
        [sg.Text('Senha:', size=(13,1)), sg.InputText('', key='-passwd-')],
        [sg.Button('Inserir')]
    ]
    
    windowNewLogin = sg.Window('Add', layoutNewLogin, size=(600,250))

    while True:

        event, values = windowNewLogin.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Inserir':
            if values['-plataforma-'] != "" and values['-email-'] != "" and values['-passwd-'] != "":
                back.insertLogin(con, values['-plataforma-'], values['-email-'], values['-passwd-'])
                windowNewLogin.close()
                frontMain(con)
            else:
                messagebox.showinfo('Senha', \
                'Preencha todos os campos!!')

frontLogin()
