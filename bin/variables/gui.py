import platform

from bin.variables import main_vars as mv


welcome = f'''
{mv.lcyan}////////////////////////////////////////////////////////////////////////////////
{mv.lcyan}/////////////////////////////// {mv.lgreen} UTILITIES{mv.lcyan} /////////////////////////////////////
{mv.lcyan}////////////////////////////////////////////////////////////////////////////////
{mv.lcyan}/////                                                                      /////
///// {mv.lmagenta}Current OS: {mv.yellow}{platform.system()}{mv.lcyan}                                                  /////
/////                                                                      /////
///// {mv.lmagenta}Coded by: {mv.lred}d1g1tus{mv.lcyan}                                                    /////
/////                                                                      /////
///// {mv.lmagenta}Github: {mv.lgreen}https://www.github.com/d1g1tus{mv.lcyan}                               /////
/////                                                                      /////
/////      {mv.yellow}               Write list for command list {mv.lcyan}                     /////
/////      {mv.yellow}         Write elist for extended command list {mv.lcyan}                 /////
/////                                                                      /////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////'''

# COMMAND LIST GUI

command_list = f'''{mv.lcyan}///// 
{mv.lcyan}/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////// COMMAND LIST ////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- GENERAL COMMANDS
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· clear -> {mv.white}Clears output screen
{mv.lgreen}/////     {mv.yellow}· exit -> {mv.white}Stops Script  
{mv.lgreen}/////     {mv.yellow}· list -> {mv.white}Displays a simpler command list
{mv.lgreen}/////     {mv.yellow}· elist -> {mv.white}Displays this command list
{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- SPECIFIC COMMANDS - {mv.lblue}[* -> Only for Windows OS]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· anonfiles -> {mv.white}It uploads and downloads files from anonfiles. Includes APIKEY functions.
{mv.lgreen}/////     {mv.yellow}· download -> {mv.white}Downloads given urls from a txt. It can also download links from Discord
{mv.lgreen}/////     {mv.yellow}· help -> {mv.white}Returns more specific information about a command and its syntax.
{mv.lgreen}/////     {mv.yellow}· temp -> {mv.white}Clears all basic temp files in system. {mv.lblue}*
{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- SPECIFIC COMMANDS - {mv.lmagenta}INFO GATHERERS {mv.lblue}[* -> Only for Windows OS]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· ipinfo -> {mv.white}Returns Local and Public IP with some useful information. It also return information about a given Public Ip 
{mv.lgreen}/////     {mv.yellow}· ports -> {mv.white}Returns which ports are currently open in localhost.
{mv.lgreen}/////     {mv.yellow}· wlan -> {mv.white}Returns all SSID profiles stored in device, with passwords and interface info {mv.lblue}* [PENDING]
{mv.lgreen}///// '''

# SHORT COMMAND HELPS

clear_help = f'''{mv.lgreen}/////
{mv.lgreen}///// {mv.lred}- clear [SYNTAX] {mv.yellow}== {mv.lblue}clear 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan} Clears all current data on the screen
{mv.lgreen}///// '''

elist_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- elist [SYNTAX] {mv.yellow}== {mv.lblue}elist 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan} Gives an extended version of list commands
{mv.lgreen}///// '''

list_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- list [SYNTAX] {mv.yellow}== {mv.lblue}list 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan} Gives a short version of list commands
{mv.lgreen}///// '''

temp_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- temp [SYNTAX] {mv.yellow}== {mv.lblue}temp 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan} Deletes temporal files from the system. Currently only works in Windows OS
{mv.lgreen}///// '''

exit_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- exit [SYNTAX] {mv.yellow}== {mv.lblue}exit 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan} Closes this script
{mv.lgreen}///// '''

# SPECIFIC COMMANDS HELP

anonfiles_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- anonfiles [SYNTAX] {mv.yellow}== {mv.lblue}anonfiles {mv.lgreen}[arg] [arg]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan}Uploads or downloads a given file/url to an specific folder. It also takes personal anonfile API keys.
{mv.lgreen}/////     To add as many APIs as you want, edit {mv.lgreen}main_vars.py -> api_anonfiles, {mv.lcyan} and add as many entries as you want. 
{mv.lgreen}/////     
{mv.lgreen}/////     {mv.yellow}· select = {mv.white}Write select instead of PATH to choose a path with a GUI.
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lmagenta} EXAMPLE OF USE
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· anonfiles {mv.lred}up {mv.lgreen}[API_KEY] {mv.lblue}[FILE_PATH / select]{mv.yellow} -> {mv.white}Uploads FILE and returns its URL
{mv.lgreen}/////     {mv.yellow}· anonfiles {mv.lred}down {mv.lgreen}[FOLDER_PATH / select] {mv.lblue}[URL]{mv.yellow} -> {mv.white}Downloads file to specific folder. 
{mv.lgreen}///// '''

download_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- download [SYNTAX] {mv.yellow}== {mv.lblue}download {mv.lgreen}[args] 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan}Download all URLs from a given txt file. This file simply has to contain all links, 1 link per line.
{mv.lgreen}/////     You can also simply write {mv.lgreen} download {mv.lcyan} to run this script, but it also takes some arguments.
{mv.lgreen}/////     By default this script will make you choose a {mv.lred} download path, file name {mv.lcyan}and {mv.lred} txt file.
{mv.lgreen}/////     {mv.lcyan}You can use some args to avoid these steps. 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· def = {mv.lred}File name {mv.white}and {mv.lred}Download Path {mv.white}take default values.
{mv.lgreen}/////     {mv.yellow}· -p {mv.lgreen}[DOWNLOAD_PATH] = {mv.white}Declare {mv.lred}Download Path {mv.white}manually.
{mv.lgreen}/////     {mv.yellow}· -n {mv.lgreen}[FILE_NAME] = {mv.white}Declare {mv.lred}File Name {mv.white}manually.
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lmagenta} EXAMPLE OF USE
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· download
{mv.lgreen}/////     {mv.yellow}· download {mv.lred}def {mv.yellow}  
{mv.lgreen}/////     {mv.yellow}· download {mv.lred}-p {mv.lgreen}[DOWNLOAD_PATH]
{mv.lgreen}/////     {mv.yellow}· download {mv.lred}-n {mv.lgreen}[FILE_NAME]
{mv.lgreen}/////     {mv.yellow}· download {mv.lred}-p {mv.lgreen}[DOWNLOAD_PATH] {mv.lred}-n {mv.lblue}[FILE_NAME]{mv.yellow}  
{mv.lgreen}///// '''

ports_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- ports [SYNTAX] {mv.yellow}== {mv.lblue}ports {mv.lgreen}[args]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan}Scans all ports and returns data.
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· -v = {mv.white}Returns all port scan results. It might be glitchy when printing closed ports. 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lmagenta} EXAMPLE OF USE
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· ports {mv.lred}-o {mv.yellow}-> {mv.white}Appends ip output to output.txt
{mv.lgreen}/////     {mv.yellow}· ports {mv.lred}-v {mv.yellow} -> {mv.white}Returns all port scan results
{mv.lgreen}///// '''

help_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- help [SYNTAX] {mv.yellow}== {mv.lblue}help {mv.lgreen}[COMMAND]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan}Just a little help for commands in specific 
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lmagenta} EXAMPLE OF USE
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.yellow}· help {mv.lred} * {mv.yellow} -> {mv.white}Prints all command use instructions
{mv.lgreen}/////     {mv.yellow}· help {mv.lred} ipinfo {mv.yellow} -> {mv.white}Prints specific command use instructions
{mv.lgreen}///// '''

ip_help = f'''{mv.lgreen}///// 
{mv.lgreen}///// {mv.lred}- ipinfo [SYNTAX] {mv.yellow}== {mv.lblue}ip {mv.lgreen}[-o]
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lcyan}Shows sensitive info related to local and public IP of the victim.
{mv.lgreen}///// 
{mv.lgreen}/////     {mv.lmagenta} EXAMPLE OF USE
{mv.lgreen}///// 
{mv.lgreen}/////      {mv.yellow}· ipinfo {mv.lred}ip {mv.yellow}-> {mv.white}Searches info about given public Ip
{mv.lgreen}/////      {mv.yellow}· ipinfo {mv.lred}host {mv.yellow}-> {mv.white}Searches info about host public and local Ip
{mv.lgreen}/////      {mv.yellow}· ipinfo {mv.lred}-o {mv.yellow}-> {mv.white}Appends local public ip output to output.txt
{mv.lgreen}///// '''


def print_all():
    opt_list = [anonfiles_help, clear_help, download_help, elist_help, exit_help, help_help, ip_help, list_help,
                ports_help, temp_help]
    for i in range(len(opt_list)):
        print(opt_list[i])


commands_help = {
    "*": print_all,
    "anonfiles": anonfiles_help,
    "clear": clear_help,
    "download": download_help,
    "elist": elist_help,
    "exit": exit_help,
    "help": help_help,
    "ipinfo": ip_help,
    "list": list_help,
    "ports": ports_help,
    "temp": temp_help
}

###### ERROR MESSAGES

file_not_exist = f"{mv.lgreen}/////\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}File does not exist...\n{mv.lgreen}/////"
url_bad = f"{mv.lgreen}/////\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}URL provided is not accepted or is not an URL\n{mv.lgreen}/////"
txt_url_bad = f"{mv.lgreen}/////\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}File provided does not contain valid URLs\n{mv.lgreen}/////"

def folder_not_exist(command):
    return str(f"{mv.lgreen}/////\n{mv.lgreen}/////{mv.lred} ERROR{mv.lblue} -> {mv.white}Folder '{command[2]}' does not exist...\n{mv.lgreen}/////")


####### MESSAGES

tem_fin = f"{mv.lgreen}/////\n{mv.lcyan}///// -> {mv.lblue}PROCESS COMPLETED {mv.lgreen} Process will continue in {mv.lred}10 Seconds\n"
