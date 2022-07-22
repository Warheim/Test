import requests
import configparser
import os


class Yandex:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.token = config["Yandex"]["token"]
        self.host = config["Yandex"]["host"]
        self.path = "Test"
        self.headers = None
        self.folder_link = None
        self.folder_params = None

    def get_headers(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_folder_params(self):
        self.folder_params = {
            "overwrite": True,
            "path": "Test"
        }

    def ya_folder(self):
        url = self.host
        search = requests.get(url, headers=self.headers, params=self.folder_params)
        if search.status_code == 404:
            return requests.put(url, headers=self.headers, params=self.folder_params).status_code

    def search_folder(self):
        url = self.host
        return requests.get(url, headers=self.headers, params=self.folder_params).status_code
