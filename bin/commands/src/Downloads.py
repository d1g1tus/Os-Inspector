import requests
import os
import urllib
import shutil
import ssl

from anonfile import AnonFile
from bin.variables import main_vars as mv
from bin.variables import gui as g
from bin.commands import main_functions as mf
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context

class AnonFiles:

    anon = AnonFile()
    api = str("undefined")
    output = "a.txt"

    def __init__(self, command, index):
        try:
            if index == 1:
                self.handle_upload(command)
            elif index == 2:
                self.handle_download(command)

        except FileNotFoundError:
            if command[1] == "up":
                print(g.file_not_exist)
            elif command[1] == "down":
                print(g.folder_not_exist(command))
        except TypeError:
            print(g.url_bad)
        except requests.exceptions.HTTPError:
            print(g.url_bad)
        except requests.exceptions.MissingSchema:
            print(g.url_bad)

    def handle_download(self, command):
        command = mf.handle_file_anonfiles(command, 2)
        self.download(str(command[3]), str(command[2]))

    def handle_upload(self, command):
        if len(command) == 3:
            command = mf.handle_file_anonfiles(command, 1)
            self.upload(command[2], self.api)
        else:
            if command[2] in mv.api_anonfiles:
                api = mv.api_anonfiles[command[2]]
                command = mf.handle_file_anonfiles(command, 1)
                self.upload(command[3], api)
            else:
                print(f"{mv.lgreen}/////{mv.lred} ERROR {mv.lblue} -> {mv.white} Api not found.")

    def upload(self, file, api):
        AnonFile.token = str(api)
        upload = self.anon.upload(file, progressbar=True)
        up = str(upload.url.geturl())
        print(f"\n{mv.lgreen}/////{mv.lred} FINISHED{mv.lblue} -> {mv.white} File successfully uploaded to -> {up}\n")

    def download(self, url, path):
        self.anon.download(url, path, progressbar=True)
        print(f"\n{mv.lgreen}/////{mv.lred} FINISHED{mv.lblue} -> {mv.white} File successfully downloaded in {path}\n")


class Download:

    def __init__(self, urls, path, filename, discord):
        try:
            print(f'''{mv.lgreen}/////{mv.download_start}
{mv.lgreen}/////''')
            path = self.make_dir(path, filename)
            for i in range(len(urls)):
                ext = self.check_discord(discord, urls, i)
                self.download(path, filename, ext, urls[i], i, len(urls), discord)
            print(f'''{mv.lgreen}/////{mv.download_finish}
{mv.lgreen}/////''')
        except ValueError:
            print(g.txt_url_bad)
        except TypeError:
            print(g.txt_url_bad)

    def check_discord(self, discord, urls, i):
        if discord:
            ext = self.clean_discord_url(urls)
            kol = self.read_parse_links(ext, i)
        else:
            kol = self.read_parse_links(urls, i)

        return kol

    @staticmethod
    def clean_discord_url(urls):
        urls_clean = []
        for i in range(len(urls)):
            url = list(str(urls[i]).strip())
            url_clean = []
            for j in range(len(url)):
                if url[j] != "?":
                    url_clean.append(url[j])
                elif url[j] == "?" and url[j + 1] == "w" and url[j + 2] == "i":
                    break
                else:
                    url_clean.append(url[j])
            urls_clean.append(str("".join(url_clean) + "\n"))
        return urls_clean

    @staticmethod
    def make_dir(path, filename):
        i = 1
        final_path = f"{path}/{filename}_Pictures_{i}"
        while True:
            try:
                if os.path.isdir(final_path):
                    final_path = f"{path}/{filename}_Pictures_{i + 1}"

                os.mkdir(final_path)
                return final_path

            except FileExistsError:
                i += 1

    @staticmethod
    def read_parse_links(urls, i):
        url = list(str(urls[i]).strip())
        frmat = ("".join(url[len(url) - 4:]))
        for j in range(len(mv.long_format_list)):
            if str(urls[i].strip()).endswith(mv.long_format_list[j]):
                frmat = str(mv.long_format_list[j])
        return frmat

    @staticmethod
    def download(path, filename, frmat, url, i, leng, discord):
        full_path = str(f"{path}/{filename}_{i}{frmat}")
        if discord:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)

        try:
            urllib.request.urlretrieve(url, full_path)
        except:
            r = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                with open(full_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

        result = f"{mv.lgreen}///// {mv.white}[+] {mv.yellow}" + full_path + f"{mv.lmagenta} ///// {mv.blue}-> {mv.lgreen}[" + str(
            i + 1) + " / " + str(leng) + f"{mv.lgreen}] -{mv.lcyan} Downloaded"
        print(result)
