import tkinter as tk
import datetime as dt

import data_management as dm
import widgets as ws


class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('400x600')
        self.root.resizable(False, False)

        self.bg_color = "white"
        self.students_database = dm.load_data("./database/students.csv")
        self.current_year = dt.datetime.now().year

        self.search_setting = 0

        self.create_main_frames()

    def create_main_frames(self):
        self.frame1_obj = ws.Frame1(self)
        self.frame2_obj = ws.Frame2(self)
        self.frame3_obj = ws.Frame3(self)
        self.frame4_obj = ws.Frame4(self)
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
        if key_index == 3:
            key_index = 1
        self.students_database = sorted(self.students_database, key=lambda student: student[key_index], reverse=not ascending)



    # Getter methods
    def getRoot(self):
        return self.root
    
    def getBg(self):
        return self.bg_color
    
    def getStudentDb(self):
        return self.students_database
    
    def getMainStud(self):
        return self.main_student
    
    def getSearchSet(self):
        return self.search_setting
    
    def setSearchSet(self, i):
        self.search_setting = i

    def getCurrYear(self):
        return self.current_year

    def setMainStud(self, student):
        self.main_student = student


        

def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()