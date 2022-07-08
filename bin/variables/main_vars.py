import os

from colorama import Fore


# GUI

lcyan = Fore.LIGHTCYAN_EX
yellow = Fore.YELLOW
lmagenta = Fore.LIGHTMAGENTA_EX
lgreen = Fore.LIGHTGREEN_EX
green = Fore.GREEN
lred = Fore.LIGHTRED_EX
white = Fore.WHITE
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX

# GUI DOWNLOAD

download_start = (f'''
{lgreen}/////{lmagenta} +-----------------------------------------------------+
{lgreen}///// {lmagenta}|             {lgreen}DOWNLOAD {lred}STARTED {lblue}PROPERLY{lmagenta}               |
{lgreen}///// {lmagenta}+-----------------------------------------------------+''')

download_finish = (f'''
{lgreen}/////{lmagenta} +-----------------------------------------------------+
{lgreen}///// {lmagenta}|             {lgreen}DOWNLOAD {lred}FINISHED {lblue}PROPERLY{lmagenta}              |
{lgreen}///// {lmagenta}+-----------------------------------------------------+''')


# NETWORK INFORMATION

local_ip = ""
public_ip = ""
country = ""
city = ""
latlong = ""
org = ""
postal = ""

# FOLDERS / DIRECTORIES

default_path = f"C:{os.environ['HOMEPATH']}/Downloads"

# COMMANDS HELP
command_list = f'''{lgreen}///// 
{lgreen}///// ·{yellow} anonfiles {lgreen}-> {white}Upload/Download files with Anonfiles. API friendly
{lgreen}///// ·{yellow} clear {lgreen}-> {white} Clears all data in console
{lgreen}///// ·{yellow} download {lgreen}-> {white}A download manager that read URLs on a file and retrieves them
{lgreen}///// ·{yellow} elist {lgreen}-> {white}A more extended version of this command list
{lgreen}///// ·{yellow} exit {lgreen}-> {white}Closes this script
{lgreen}///// ·{yellow} help {lgreen}-> {white}Gives specific help for any command
{lgreen}///// ·{yellow} ipinfo {lgreen}-> {white}Displays some sensitive info about a given ip 
{lgreen}///// ·{yellow} list {lgreen}-> {white}Displays this command list
{lgreen}///// ·{yellow} ports {lgreen}-> {white}Displays which ports are open in local system
{lgreen}///// ·{yellow} temp {lgreen}-> {white}Deletes temporal files from the system
{lgreen}///// '''

# ANONFILES API DICTS

api_anonfiles = {
    "d1g1tus": "None"
}
# DOWNLOADS VARIABLES

long_format_list = [".jpeg", ".mpeg"]
