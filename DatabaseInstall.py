'''
code to create this database from our lesson 5/6

Student(ExamNo,Firstname, Surname, DOB, Address)
StudentQualification(ID, ExamNo, QualCode,QualGrade)
Qualification(QualCode, QualName)
'''

import sqlite3 #library for databases in python

def createDatabase():
  with sqlite3.connect("Exams.db")as db:
      cursor = db.cursor()
      #You can write your SQL on 1 line with normal brackets but use triple for formatting
      sql  = """CREATE Table Student(
                ExamNo integer PRIMARY KEY,
                Firstname text,
                Surname text,
                DOB text,
                Address text);"""
      cursor.execute(sql)

      sql  = """CREATE Table Qualification(
                QualCode text PRIMARY KEY,
                QualName text);"""
      cursor.execute(sql)

      sql  = """CREATE Table StudentQualification(
                ID integer PRIMARY KEY AUTOINCREMENT,
                ExamNo integer,
                QualCode text,
                QualGrade text,
                FOREIGN KEY (ExamNo) REFERENCES Student(ExamNo),
                FOREIGN KEY (QualCode) REFERENCES Qualification(QualCode));"""
      cursor.execute(sql)

def writeSQL():
     with sqlite3.connect("Exams.db") as db:
        cursor = db.cursor()
        sql  = input()
        cursor.execute(sql)
        result = cursor.fetchall()
        for each in result:
            print(each)

    
    
