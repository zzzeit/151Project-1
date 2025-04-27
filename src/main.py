import tkinter as tk
import datetime as dt

import data_management as dm
import widgets as ws


class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('700x640')
        self.root.resizable(False, False)


        self.students_database = dm.load_data("./database/students.csv")
        self.collegeData = dm.load_data("./database/colleges.csv")
        self.list_mode = 0
        self.current_year = dt.datetime.now().year

        self.colleges_list = []

        self.main_student = None
        self.main_college = None

        self.search_setting = 0
        self.themeColors = ["#454148", "#5c5960", "#757278", "#8f8d92"]
        self.root.configure(bg=self.themeColors[0])
        self.create_main_frames()



    def create_main_frames(self):
        self.updateCollegesList()

        self.frame1_obj = ws.Frame1(self)
        self.frame2_obj = ws.Frame2(self)
        self.frame3_obj = ws.Frame3(self)
        self.frame4_obj = ws.Frame4(self)
        self.frame5_obj = ws.Frame5(self)
        self.frame6_obj = ws.Frame6(self)
        self.transition_frames(self.frame1_obj)



    def transition_frames(self, mainFrame):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        mainFrame.transition()

    def get_student(self, id):
        for student in self.students_database:
            if id == student[3]:
                return student
        return None

    def sort_students(self, key_index=0, ascending=True):
        self.students_database = sorted(self.students_database, key=lambda student: student[key_index], reverse=not ascending)

    def delete_student(self, student_id):
        self.students_database = [student for student in self.students_database if student[3] != student_id]
        dm.write_data("./database/students.csv", self.students_database)

    def add_college(self, data):
        self.collegeData.append(data)
        dm.write_data("./database/colleges.csv", self.collegeData, 1)

    def delete_college(self, code):
        print(code)
        self.collegeData = [coll for coll in self.collegeData if coll[1] != code]
        dm.write_data("./database/colleges.csv", self.collegeData, 1)
    

    # Getter methods
    def getColor(self, index):
        return self.themeColors[index]

    def getRoot(self):
        return self.root

    
    def getStudentDb(self):
        return self.students_database
    
    def getCollegeDb(self):
        return self.collegeData
    
    def getMainStud(self):
        return self.main_student
    
    def getMainColl(self):
        return self.main_college
    
    def getSearchSet(self):
        return self.search_setting
    
    def getCollegesList(self):
        return self.colleges_list
    
    def setSearchSet(self, i):
        self.search_setting = i

    def getCurrYear(self):
        return self.current_year

    def setMainStud(self, student):
        self.main_student = student

    def setMainColl(self, college):
        self.main_college = college

    def updateCollegesList(self):
        for i in self.collegeData:
            if i[0] not in self.colleges_list:
                self.colleges_list.append(i[0])


        

def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()