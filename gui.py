from tkinter import TRUE
import PySimpleGUI as sg
from os import path
import download_svg
import pull_svg

PATH = "C:\Program Files (x86)\chromedriver.exe"

file_list_column = [
    [
        sg.Text("Musescore URL", size=(15,1)),
        sg.In(size=(25, 1), enable_events=True, key="-URL-"),
        sg.Button("Clear", size=(5,1), button_color=('white', ''), enable_events=TRUE, key='-CLEAR-'),
    ],
    [
        sg.Text("Download Path", size=(15,1)),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Download PDF", size=(50,1), button_color=('white', ''), enable_events=TRUE, key='-DOWNLOAD-'),

    ],
]

window = sg.Window("Musescore Extractor", file_list_column)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-DOWNLOAD-":
        if values["-URL-"] == '':
            sg.Popup('No URL is selected') 
        elif values["-URL-"].find('https://musescore') == -1:
            sg.Popup('Invalid musescore link') 
        elif path.isdir(values["-FOLDER-"]) == False:
            sg.Popup('The download path is not valid')
        else:
            download_svg.download_musescore_svg(values["-URL-"], values["-FOLDER-"], PATH)
            pull_svg.svgs_to_pdf(values["-FOLDER-"])
            sg.Popup('Score downloaded!')
    if event == "-CLEAR-":
        window.find_element("-URL-").Update('')

window.close()