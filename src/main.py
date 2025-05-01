import tkinter as tk
import tkinter.messagebox as messagebox
import datetime as dt

import data_management as dm
import widgets as ws


class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry('700x640')
        self.root.resizable(False, False)

        # FLAGS
        self.modify_mode = False

        self.students_database = dm.load_data("./database/students.csv")
        self.programs_database = dm.load_data("./database/programs.csv")
        self.colleges_database = dm.load_data("./database/colleges.csv")
        self.list_mode = 0
        self.current_year = dt.datetime.now().year

        self.programs_list = []
        self.colleges_list = []

        self.main_student = None
        self.main_program = None

        self.search_setting = 0
        self.themeColors = ["#454148", "#5c5960", "#757278", "#8f8d92"]
        self.root.configure(bg=self.themeColors[0])
        self.create_main_frames()



    def create_main_frames(self):
        self.updateProgramsList()
        self.updateCollegesList()

        self.frame1_obj = ws.Frame1(self)
        self.frame2_obj = ws.Frame2(self)
        self.frame3_obj = ws.Frame3(self)
        self.frame4_obj = ws.Frame4(self)
        self.frame5_obj = ws.Frame5(self)
        self.frame6_obj = ws.Frame6(self)
        self.frame7_obj = ws.Frame7(self)
        self.frame8_obj = ws.Frame8(self)
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
    def sort_programs(self, key_index=0, ascending=True):
        self.programs_database = sorted(self.programs_database, key=lambda program: program[key_index], reverse=not ascending)
    def sort_colleges(self, key_index=0, ascending=True):
        self.colleges_database = sorted(self.colleges_database, key=lambda college: college[key_index], reverse=not ascending)
    def delete_student(self, student_id, alert=True):
        confirm = messagebox.askyesno("Delete Student", "Are you sure you want to delete this student?")
        if confirm and alert:
            self.students_database = [student for student in self.students_database if student[3] != student_id]
            dm.write_data("./database/students.csv", self.students_database)

    def add_student(self, data):
        self.students_database.append(data)
        dm.write_data("./database/students.csv", self.students_database)

        self.updateProgramsList()
        self.updatePrograms_database()

    def replace_student(self, student_id, data):
        for i, student in enumerate(self.students_database):
            if student[3] == student_id:
                self.students_database[i] = data
                break
        dm.write_data("./database/students.csv", self.students_database)

        self.updateProgramsList()
        self.updatePrograms_database()

    def check_student(self, student_id):
        for student in self.students_database:
            if student[3] == student_id:
                return True
        return False

    def add_program(self, data):
        self.programs_database.append(data)
        dm.write_data("./database/programs.csv", self.programs_database, 1)

        self.updateProgramsList()
        self.updatePrograms_database()

    def delete_program(self, code, alert=True):
        confirm = messagebox.askyesno("Delete Program", "Are you sure you want to delete this program?")
        if confirm and alert:
            self.programs_database = [coll for coll in self.programs_database if coll[1] != code]
            dm.write_data("./database/programs.csv", self.programs_database, 1)

            self.updateProgramsList()
            self.updatePrograms_database()

            for i in self.students_database:
                if i[6] == code:
                    self.delete_student(i[3])
    
    def add_college(self, data):
        self.colleges_database.append(data)
        dm.write_data("./database/colleges.csv", self.colleges_database, 2)

        self.updateColleges_database()
        self.updateCollegesList()

    def delete_college(self, code):
        confirm = messagebox.askyesno("Delete College", "Are you sure you want to delete this college?")
        if confirm:
            self.colleges_database = [coll for coll in self.colleges_database if coll[1] != code]
            dm.write_data("./database/colleges.csv", self.colleges_database, 2)

            self.updateColleges_database()
            self.updateCollegesList()

            for i in self.programs_database:
                if i[0] == code:
                    self.delete_program(i[1], False)


    def updateProgramsList(self):
        for i in self.programs_database:
            if i[0] not in self.programs_list:
                self.programs_list.append(i[0])

    def updatePrograms_database(self):
        self.programs_database = dm.load_data("./database/programs.csv")

    def updateCollegesList(self):
        for i in self.colleges_database:
            if i[1] not in self.colleges_list:
                self.colleges_list.append(i[1])
    
    def updateColleges_database(self):
        self.colleges_database = dm.load_data("./database/colleges.csv")

    # Getter methods
    def getColor(self, index):
        return self.themeColors[index]

    def getRoot(self):
        return self.root

    
    def getStudentDb(self):
        return self.students_database
    
    def getProgramDb(self):
        return self.programs_database
    
    def getMainStud(self):
        return self.main_student
    
    def getMainColl(self):
        return self.main_program
    
    def getSearchSet(self):
        return self.search_setting
    
    def getProgramsList(self):
        return self.programs_list
    
    def setSearchSet(self, i):
        self.search_setting = i

    def getCurrYear(self):
        return self.current_year

    def setMainStud(self, student):
        self.main_student = student

    def setMainColl(self, program):
        self.main_program = program


        

def main():
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()