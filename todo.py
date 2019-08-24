import PySimpleGUI as s
import file

lst=[]
lst=file.fileread()
layout=[
    [s.Text("Enter New Task to be added"),s.InputText("",key='data'),s.Button("ADD")],
    [s.Slider(orientation='horizontal',key='priority')],
    [s.Text("TO-DO List")],
    [s.Listbox(lst,size=(50,10),key='box')],
    [s.Button("CLEAR"),s.Button("CLEAR LIST"),s.Button("EXIT")]
]

w=s.Window("My",layout)


while True:
    button,values=w.Read()
    w.FindElement('box').Update(lst)
    if button=="ADD":
        lst.sort()
        l=values['data']+" | Priority:"+str(int(values['priority']))
        lst.append(l)
        w.FindElement('data').Update("")
        w.FindElement('box').Update(lst)
        file.filewrite(lst)

    elif button=="CLEAR":
        lst.remove(values['box'][0])
        file.filedelete(lst,values['box'][0])
        w.FindElement('box').Update(lst)


    elif button=="EXIT":
        break

    elif button=="CLEAR LIST":
        w.FindElement('box').Update("")
        lst.clear()
        print(lst)
        file.fileclear()
