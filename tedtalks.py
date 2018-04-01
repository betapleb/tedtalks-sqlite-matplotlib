#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:08:25 2018

@author: jenniferquach
"""

#energy use per capita of India, Nepal, Pakistan from google public data


import sqlite3
import csv
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')   #style matplotlib graphs


#define connection and cursor.
conn = sqlite3.connect('tedTalks.db')    #creates if doesn't exist.
c = conn.cursor()   #cursor does stuff.



#create database
def create_table():
    #create col its datatype. REAL datatype is a python float
    #convention: all sql commands are ALL CAPS
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(comments REAL, event TEXT, languages INT, title TEXT, views REAL)')
    
    
#inserts data into table
def data_entry():
    #insert stuff into database in order of create_table 
    c.execute("INSERT INTO stuffToPlot VALUES(145, '2016-01-01', 'Python', 5)")
    #conn.commit() anytime you modify anything in database.
    conn.commit()
    #stop connection, stop memory from being used. 
    c.close()
    conn.close()


#nsert dynamically into a database's table, using variables.
def dynamic_data_entry():
    
    with open('ted_main.csv', 'rt') as fin:      #rt readtext
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)        # comma is default delimiter
        to_db = [(i['comments'], i['event'], i['languages'], i['title'], i['views']) for i in dr]
    c.executemany("INSERT INTO stuffToPlot (comments, event, languages, title, views) VALUES (?, ?, ?, ?, ?) ", to_db)
    conn.commit()
    
#    
#    unix = time.time()
#    #convert unix stamp to datestamp
#    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: 5M: %S'))
#    keyword = 'Python'
#    value = random.randrange(0,10)
#    #sqlite uses ? whereas mysql uses %s
#    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?) ",
#              (unix, date, keyword, value))
#    conn.commit()
#    #no closing bc we are inserting 10 datapoints.
#    #dont want to open and close connection for every insertion.


#pull certain rows or columns from database
def read_from_db():
    #cursor selects from table things you specify using 'WHERE'
    #c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python' ")
    c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix > 145")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
        #print(row[0]) to reference unix stamp, it's indexed so unix is 0


#graph value for every type in db. 
#interate thru the return to populate dates and values lists. 
#then use matplotlib to plot data 
def graph_data():
    c.execute('SELECT comments, views FROM stuffToPlot')
    views = []
    comments = []
    data = c.fetchall()
    for row in data:
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        #dates.append(parser.parse(row[0]))
        views.append((row[-1]))
        comments.append(row[0])
        #event.append(row[2])
        #title.append(row[5])
        
    
    plt.plot(comments, views, 'o')  #'-' draws a line through the points
    plt.show()


#select and del or update data permanently
def del_and_update():
    #c.execute('SELECT * FROM stuffToPlot')
    #one line for loop 
    #[print(row) for row in c.fetchall()]     #select and prints every row for every row in c.fetchall()
    
#   #CHANGE DATA PERMANENTLY
#   c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 8 ')    #open file, change values of 8 to 99.
#   conn.commit()    #save changes
#    
#   c.execute('SELECT * FROM stuffToPlot')
#   [print(row) for row in c.fetchall()]
    
    
    #PERMANENTLY DEL DATA  WITH VALUE 99
    c.execute("DELETE FROM stuffToPlot WHERE title = 'What’s wrong with your pa$$w0rd?'")   
    conn.commit()
#   print(50 * '#')
#    c.execute('SELECT * FROM stuffToPlot WHERE value = 2')
#    [print(row) for row in c.fetchall()]     #select and prints every row for every row in c.fetchall()
#    
#    c.execute('SELECT * FROM stuffToPlot WHERE value = 2')
#    print(len(c.fetchall()))




#create_table()
#dynamic_data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    #sleep for 1 sec so timestamp goes up 1 sec.
#    time.sleep(1)  

graph_data()
#del_and_update()

c.close()
conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    