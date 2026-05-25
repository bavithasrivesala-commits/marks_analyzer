import csv
import os
class Marks:
    def __init__(self,name,marks1,marks2):
        self.name=name
        self.mid1_marks=marks1
        self.mid2_marks=marks2
    def store_in_csv(self):
        self.name=input('Enter name of student:')
        self.mid1_marks=int(input('Enter mid 1 marks:'))
        self.mid2_marks=int(input('Enter mid 2 marks:'))
        a=(self.mid1_marks//3)+(self.mid2_marks//3)
        self.lab_marks=int(input('Enter your lab marks:'))
        m1=a+self.lab_marks
        if m1>=56:
             msg='you need to get 85 or above marks in sem to get grade A'
        elif 50<=m1<=55:
            msg='you need to get 100 out of 100 in sem to get grade A but if you can score atleast 63 marks you can get grade B'
        elif 30<=m1<=49:
            msg='you need to get atleast 20 marks so that you can get grade C'
        else:
            msg='your internal marks are below 30 you are not eligible to write semester exams'
        file_exists=os.path.exists('marks.csv')
        with open('marks.csv',mode='a',newline='') as f:
            w=csv.writer(f)
            if not file_exists:
                 w.writerow(['Name','Mid1 marks','Mid2 marks','Lab marks','Message'])
            w.writerow([self.name,self.mid1_marks,self.mid2_marks,self.lab_marks,msg])
ob=Marks('',0,0)
ob.store_in_csv()