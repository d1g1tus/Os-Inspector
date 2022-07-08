import os
import datetime
import easygui

from bin.variables import main_vars as mv
from bin.variables import gui as g


def create_folder(name):
    if not os.path.isdir(f"{mv.default_path}/{name}"):
        os.mkdir(f"{mv.default_path}/{name}")


def create_file(path, url):
    if not os.path.isfile(f"{mv.default_path}/{path}/{datetime.date.today()} - {path}.txt"):
        with open(f"{mv.default_path}/{path}/{datetime.date.today()} - {path}.txt", "w") as f:
            f.write(url)
            f.close()


def append_link(path, url):
    create_file(path, url)
    with open(f"{mv.default_path}/{path}/{datetime.date.today()} - {path}.txt", "a") as f:
        f.write(f"\n{url}")
        f.close()


def read_file(file):
    with open(file, "r") as f:
        txt = f.readlines()
        f.close()
    return txt


def sort_url(txt):
    txt_list = []

    for i in range(len(txt)):
        if txt[i] not in txt_list:
            txt_list.append(txt[i])

    return txt_list


def handle_file_to_open():
    path_file = easygui.fileopenbox(msg="Select file to sort URLs")
    txt = read_file(path_file)
    txt_sorted = sort_url(txt)
    return txt_sorted


def sort_commands(x):
    items_list = ['help', 'list']
    for i in range(len(x)):
        if str(str(x[i]).split())[4] != '_':
            if str(x[i][0]) not in mv.exceptions:
                items_list.append(x[i][0])

    for j in range(len(items_list)):
        print(g.commands_help[items_list[j]])


def handle_file_anonfiles(command, index):
    if command[2] == "select" and index == 1:
        command[2] = str(easygui.fileopenbox())
    elif command[3] == "select" and index == 1:
        command[3] = str(easygui.fileopenbox())
    if command[2] == "select" and index == 2:
        command[2] = str(easygui.diropenbox())
    return command

def check_path(path):
    if "\\" not in list(path):
        raise FileNotFoundError
