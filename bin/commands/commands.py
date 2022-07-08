import os
import random
import sys
import urllib
import socket
import threading
import concurrent.futures
import platform
import time
import shutil
import easygui

from urllib import request
from bin.variables import main_vars as mv
from bin.variables import gui as g
from bin.commands import main_functions as mf
from bin.commands.src import Downloads as dw


def anonfiles(command):
    if len(command) == 1:
        print(g.anonfiles_help)
    if command[1] == "up":
        while True:
            if len(command) < 4:
                if len(command) == 3 and command[2] != "select" or len(command) == 2:
                    print(f"\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}File does not exist...\n")
            dw.AnonFiles(command, 1)
            break
    elif command[1] == "down":
        while True:
            if len(command) < 4:
                print(f"\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}Folder does not exist...")
                print(f"{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}URL does not exist...\n")
            elif len(command) == 4 and str(command[3]).startswith("http") is False:
                print(f"\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}URL does not exist...\n")
                break
            dw.AnonFiles(command, 2)
            break


def clear(opt):
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Linux":
        os.system("clear")
    print(g.welcome)


class ports:

    prin_lock = threading.Lock()
    target = socket.gethostbyname(socket.gethostname())

    def __init__(self, args):
        print(f'''{mv.lgreen}/////
///// {mv.lcyan} CHECKING OPEN PORTS IN SYSTEM
{mv.lgreen}/////''')

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1000):
                executor.submit(self.scan, self.target, port + 1, args)

        print(f"{mv.lgreen}/////")

    def scan(self, ip, port, args):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            scanner.close()
            with self.prin_lock:
                print(f"{mv.lgreen}/////{mv.lmagenta} IP: {mv.lred}{ip}{mv.lgreen} [{port}]{mv.blue} Opened")

        except IndexError:
            if args[1] == "-v":
                print(mv.white + f"[{port}]" + mv.lred + " Closed\n")


def ipinfo(ip):
    while True:
        if len(ip) == 1:
            print(g.commands_help["ipinfo"])
            break
        elif ip[1] == "host":
            mv.public_ip = urllib.request.urlopen('http://api.ipify.org').read().decode('utf8')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            mv.local_ip = s.getsockname()[0]
            s.close()

        else:
            mv.public_ip = ip[1]
            mv.local_ip = "None"

        mv.country = urllib.request.urlopen(f'https://ipapi.co/{mv.public_ip}/country/').read().decode('utf8')
        mv.city = urllib.request.urlopen(f'https://ipapi.co/{mv.public_ip}/city/').read().decode('utf8')
        mv.latlong = urllib.request.urlopen(f'https://ipapi.co/{mv.public_ip}/latlong/').read().decode('utf8')
        mv.org = urllib.request.urlopen(f'https://ipapi.co/{mv.public_ip}/org/').read().decode('utf8')
        mv.postal = urllib.request.urlopen(f'https://ipapi.co/{mv.public_ip}/postal/').read().decode('utf8')

        print(f'''{mv.lcyan}/////
{mv.lgreen}/////
{mv.lgreen}/////    +----------------------------------------+---------------------------------------+
{mv.lgreen}/////    |{mv.lblue}           LOCATION INFO{mv.lgreen}                |{mv.lblue}                  IP {mv.lgreen}                  |
{mv.lgreen}/////    +----------------------------------------+---------------------------------------+
{mv.lgreen}/////    | {mv.lcyan}Country ->{mv.lgreen} {mv.country}                          | {mv.yellow}Local IP ->{mv.lred} {mv.local_ip}{mv.lgreen}             
{mv.lgreen}/////    | {mv.lcyan}City -> {mv.lgreen}{mv.city}                       | {mv.yellow}Public IP -> {mv.lred}{mv.public_ip}{mv.lgreen}           
{mv.lgreen}/////    | {mv.lcyan}Latitude -> {mv.lgreen}{mv.latlong[0]}                          +---------------------------------------+
{mv.lgreen}/////    | {mv.lcyan}Longitude -> {mv.lgreen}{mv.latlong[1]}                         |
{mv.lgreen}/////    | {mv.lcyan}Organization -> {mv.lgreen}{mv.org}      |
{mv.lgreen}/////    | {mv.lcyan}Postal -> {mv.lgreen}{mv.postal}                        |
{mv.lgreen}/////    +----------------------------------------+
{mv.lgreen}/////    ''')
        break


def download(command):
    discord = bool(True)
    default = bool(True)
    path_bool = bool(True)
    name = bool(True)
    path = mv.default_path
    file_name = "File"

    if "discord" not in command:
        discord = bool(False)
    if "def" in command:
        default = bool(False)
    while True:
        try:
            if "-p" in command and "-n" in command:
                default = bool(False)
                path = command[command.index("-p")+1]
                file_name = command[command.index("-n")+1]
                mf.check_path(path)
            elif "-p" in command and "-n" not in command:
                path_bool = bool(False)
                path = command[command.index("-p") + 1]
                mf.check_path(path)
            elif "-n" in command and "-p" not in command:
                name = bool(False)
                file_name = command[command.index("-n") + 1]
        except FileNotFoundError:
            print(g.folder_not_exist(["", "", path]))
            break

        try:
            pass
            txt_sorted = mf.handle_file_to_open()
        except TypeError:
            print(g.file_not_exist)
            break
        try:
            if default:
                if path_bool:
                    path = input(f"{mv.lgreen}/////\n{mv.lgreen}///// {mv.lred}Choose Folder {mv.lblue} [Write select for GUI]] ->{mv.yellow} ")
                    if path == 'select':
                        path = easygui.diropenbox(msg="Choose download path")
                    mf.check_path(path)
                if name:
                    file_name = input(f"{mv.lgreen}/////\n{mv.lgreen}/////{mv.lred} Write file name ->{mv.yellow} ")

            dw.Download(txt_sorted, path, file_name, discord)
            break
        except FileNotFoundError:
            print(g.folder_not_exist(["", "", path]))
            break
        except TypeError:
            print(g.txt_url_bad)
            break


class temp:

    userprofile = os.environ.get("USERPROFILE")
    appdata_temp = f"{userprofile}\\Appdata\\Local\\Temp"
    windows_temp = "C:\\Windows\\Temp"

    def __init__(self, opt):

        print(f"{mv.lgreen}///// \n{mv.lgreen}///// -> {mv.lblue}STARTING WINDOWS CLEANER")
        print(f"{mv.lgreen}///// \n{mv.lgreen}///// -> {mv.lblue}CLEANING APPDATA TEMP\n{mv.lgreen}///// ")
        self.cleaner(self.appdata_temp)
        print(f"{mv.lgreen}/////\n{mv.lgreen}///// -> {mv.lblue}CLEANING WINDOWS TEMP\n{mv.lgreen}/////")
        self.cleaner(self.windows_temp)
        print(f"{mv.lgreen}/////\n{mv.lgreen}///// -> {mv.lblue}PROCESS COMPLETED \n{mv.lgreen}/////")


    @staticmethod
    def cleaner(path):
        list_dir = os.listdir(path)
        for filename in list_dir:
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    print(f"{mv.lgreen}///// {mv.lcyan}[+] - {mv.lred}Deleting file{mv.yellow}   ///// {mv.lmagenta}->{mv.white} ", file_path)
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    print(f"{mv.lgreen}///// {mv.lcyan}[+] - {mv.lred}Deleting folder{mv.yellow} ///// {mv.lmagenta}->{mv.white} ", file_path)
                    shutil.rmtree(file_path)
            except PermissionError:
                pass

def escrig(command):

    print(random.choice(mv.frases))

def exit(opt):
    sys.exit()
