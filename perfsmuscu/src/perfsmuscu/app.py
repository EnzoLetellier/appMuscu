"""
Application to track your progress during your fitness journey
"""

# coding: utf-8

import sys

sys.path.insert(1, 'C:\\Users\\enzol\\appMuscu\\perfsmuscu\\src\\perfsmuscu\\packages')

import psycopg2

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import add_session
import history

class Perfsmuscu(toga.App):

    

    def dbConnect(self, dbHost, dbname, usr,pwd, port):
        conn = psycopg2.connect(
            host = dbHost,
            database = dbname,
            user = usr,
            password = pwd,
            port = port
        )
        cur = conn.cursor()
        return cur

    def startup(self):
        dbHost = '127.0.0.1'
        dbname = 'muscu'
        usr = 'postgres'
        pwd = 'enzo'
        port = '5432'
        cursor = self.dbConnect(dbHost,dbname,usr,pwd,port)

        self.history_box = history.history(self.add_session_press, cursor)
        self.add_session_box = add_session.addSession(self.history_press, cursor)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.history_box
        self.main_window.show()

    def history_press(self,widget):
        self.main_window.content = self.history_box

    def add_session_press(self,widget):
        self.main_window.content = self.add_session_box

def main():
    return Perfsmuscu()
