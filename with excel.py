import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

folder = os.path.dirname(os.path.abspath(__file__)) + os.sep
filenames=["Grades CA 1.csv","Grades CA 2.csv","Grades Final Exam.csv","Grades Groups.csv","Groups.csv","Grades Exercises.csv"]

class Student:      #class 
    def __init__(self,first_name,last_name,student_id,ca1_total,ca1_100,ca1_15,ca2_total,ca2_100,ca2_15,exercise_total,exercise_100,exercise_15,project_group,project_total,project_15,final_total,final_100,final_40,overall,grade):            #constructor
       self.first_name=first_name
       self.last_name=last_name
       self.student_id=student_id
       self.ca1_total=ca1_total
       self.ca1_100=ca1_100
       self.ca1_15=ca1_15
       self.ca2_total=ca2_total
       self.ca2_100=ca2_100
       self.ca2_15=ca2_15
       self.exercise_total=exercise_total
       self.exercise_100=exercise_100
       self.exercise_15=exercise_15
       self.project_group=project_group
       self.project_total=project_total
       self.project_15=project_15
       self.final_total=final_total
       self.final_100=final_100
       self.final_40=final_40
       self.overall=overall
       self.grade=grade

def read_file(path):                #function to read file
    with open(path,encoding="utf-8") as f:
        file_string=f.read()
    return file_string

def split_rows(file_string):    #function to split ";" to get the rows
    rows=file_string.split("\n")
    return rows

def student_info(ca1_rows):    #function to get first,last and student id
    first_name=[]
    last_name=[]
    student_id=[]
    for row in ca1_rows[1:]:
        col=row.split(";")
        first_name.append(col[1])
        last_name.append(col[0])
        student_id.append(col[2])
    return first_name,last_name,student_id

def calculate_total_mark(col,start,end):  #total mark calculation function
    total_mark=0
    for i in range(start,end):
        total_mark+=float(col[i])
    return total_mark

def ca1_calculation(ca1_rows): #function to calculate the ca1 result and change to %
    ca1_result_100=[]
    ca1_result_15=[]
    ca1_total=[]     
    for row in ca1_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,10) #to get total marks
        ca1_total.append(total_mark)
        total_mark_100=round(total_mark/21*100,2)   #to get 100%
        ca1_result_100.append(total_mark_100) 
        total_mark=round(total_mark/21*15,2)    #to get 15% 
        ca1_result_15.append(total_mark)
    return ca1_total,ca1_result_15,ca1_result_100

def ca2_calculation(ca2_rows): #function to calculate the ca2 result and change to %15
    ca2_result_100=[]
    ca2_result_15=[]
    ca2_total=[]  
    for row in ca2_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,8)    #to get total
        ca2_total.append(total_mark)
        total_mark_100=round(total_mark/16*100,2)   #to get 100%
        ca2_result_100.append(total_mark_100)
        total_mark=round(total_mark/16 *15,2)   #to get 15%
        ca2_result_15.append(total_mark)
    return ca2_total,ca2_result_15,ca2_result_100

def final_calculation(final_rows): #function to calculate the final result and change to %40
    final_result_100=[]
    final_result_40=[]
    final_total=[]
    for row in final_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,16)   #to get total
        final_total.append(total_mark)
        total_mark_100=round(total_mark/50*100,2)   #to get 100
        final_result_100.append(total_mark_100) 
        total_mark_40=round(total_mark/50 *40,2)    #to get 40
        final_result_40.append(total_mark_40)  
    return final_total,final_result_40,final_result_100

def exercise_calculation(exercise_rows):
    exercise_result_100=[]
    exercise_result_15=[]
    exercise_total=[] 
    for row in exercise_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,13) #to get total marks
        exercise_total.append(total_mark)
        total_mark_100=round(total_mark/10*100,2)   #to get the 100%
        exercise_result_100.append(total_mark_100)
        total_mark_15=round(total_mark/10*15,2)     #to get 15%
        exercise_result_15.append(total_mark_15)
    return exercise_total,exercise_result_15,exercise_result_100

def find_group(student_id, groups_rows):    #to match the group number to the student id
    for row in groups_rows[1:]:
        col = row.split(";")
        if col[0]==student_id:
            return col[1]

def find_group_grade(group, group_grade_rows):  #to get the respect grade to the respect group mate
    for row in group_grade_rows[1:]:
        col=row.split(";")
        if col[0]==group:
            return float(col[1])

def overall_calculation(ca1_15,ca2_15,exercise_15,project_15,final_40): #Total grade
    overall_result=[]
    for i in range(len(ca1_15)):
        total=(ca1_15[i]+ca2_15[i]+exercise_15[i]+project_15[i]+final_40[i])
        overall_result.append(round(total,2))
    return overall_result

def grade_check(overall):   #to check overall grade
    if overall>=85 and overall<=100:
        return "A+"
    elif overall>=80 and overall<85:
        return "A"
    elif overall>=75 and overall<80:
        return "A-"
    elif overall>=70 and overall<75:
        return "B+"
    elif overall>=65 and overall<70:
        return "B"
    elif overall>=60 and overall<65:
        return "B-"
    elif overall>=55 and overall<60:
        return "C+"
    elif overall>=50 and overall<55:
        return "C"
    elif overall>=45 and overall<50:
        return "D+"
    elif overall>=40 and overall<45:
        return "D"
    else:
        return "F"

def save_results(students, filename):

    # Tell Excel that ; is the separator

    # Header
    s + "Last name;First name;ID;"
    s += "Total marks CA 1;Percentage achieved CA 1;Percentage CA 1 normalized to 15%;"
    s += "Total marks CA 2;Percentage achieved CA 2;Percentage CA 2 normalized to 15%;"
    s += "Total marks Exercises;Percentage achieved Exercises;Percentage Exercises normalized to 15%;"
    s += "Project Group;Total marks Project;Percentage achieved Project;Percentage Project normalized to 15%;"
    s += "Total marks Final Exam;Percentage achieved Final Exam;Percentage Final Exam normalized to 40%;"
    s += "Total percentage;Overall grade\n"

    for student in students:

        project_100 = round(student.project_total / 10 * 100, 2)

        s += f"{student.last_name};"
        s += f"{student.first_name};"
        s += f"{student.student_id};"

        s += f"{student.ca1_total:.2f};"
        s += f"{student.ca1_100:.2f};"
        s += f"{student.ca1_15:.2f};"

        s += f"{student.ca2_total:.2f};"
        s += f"{student.ca2_100:.2f};"
        s += f"{student.ca2_15:.2f};"

        s += f"{student.exercise_total:.2f};"
        s += f"{student.exercise_100:.2f};"
        s += f"{student.exercise_15:.2f};"

        s += f"{student.project_group};"
        s += f"{student.project_total:.2f};"
        s += f"{project_100:.2f};"
        s += f"{student.project_15:.2f};"

        s += f"{student.final_total:.2f};"
        s += f"{student.final_100:.2f};"
        s += f"{student.final_40:.2f};"

        s += f"{student.overall:.2f};"
        s += f"{student.grade}\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)

def create_pdf(students, filename): #to create pdf

    pdf = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4)
    )

    data = [
        ["Last name", "First name", "ID",
         "CA1 15%", "CA2 15%", "Exercise 15%",
         "Project 15%", "Final 40%",
         "Overall", "Grade"]
    ]

    for student in students:
        data.append([
            student.last_name,
            student.first_name,
            student.student_id,
            f"{student.ca1_15:.2f}",
            f"{student.ca2_15:.2f}",
            f"{student.exercise_15:.2f}",
            f"{student.project_15:.2f}",
            f"{student.final_40:.2f}",
            f"{student.overall:.2f}",
            student.grade
        ])

    table = Table(data, repeatRows=1)

    style = TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTSIZE", (0, 0), (-1, -1), 8)
    ])

    # make failed students red
    for i, student in enumerate(students, start=1):
        if student.grade == "F":
            style.add(
                "TEXTCOLOR",
                (0, i),
                (-1, i),
                colors.red
            )

    table.setStyle(style)

    pdf.build([table])
        
#to call the function in the main
def main():
    project_total= []
    project_15 = []
    group_list = []

    #read all the csv files
    ca1_file = read_file(folder+filenames[0])
    ca2_file = read_file(folder+filenames[1])
    final_file = read_file(folder+filenames[2])
    group_grade_file=read_file(folder+filenames[3])
    group_file=read_file(folder+filenames[4])
    exercise_file = read_file(folder+filenames[5])

    #split into rows
    ca1_rows=split_rows(ca1_file)
    ca2_rows=split_rows(ca2_file)
    final_rows=split_rows(final_file)
    group_grade_rows=split_rows(group_grade_file)
    group_rows=split_rows(group_file)
    exercise_rows = split_rows(exercise_file)

    #to call student_info function to make list for first,last and id
    first_name_list,last_name_list,id_list=student_info(ca1_rows)

    #to get the group id,total group mark and 15
    for student_id in id_list:
        group = find_group(student_id, group_rows)
        group_list.append(group)
        project_grade = find_group_grade(group, group_grade_rows)
        project_total.append(project_grade)
        project_grade_15 = round(project_grade / 10 * 15, 2)
        project_15.append(project_grade_15)

    ca1_total,ca1_result_15,ca1_result_100=ca1_calculation(ca1_rows)    #to call ca1 calc function
    ca2_total,ca2_result_15,ca2_result_100=ca2_calculation(ca2_rows)    #to call ca2 calc function
    final_total,final_result_40,final_result_100=final_calculation(final_rows)     #to call final calc function
    exercise_total,exercise_result_15,exercise_result_100=exercise_calculation(exercise_rows)   #to call exercise function
    overall_result=overall_calculation(ca1_result_15,ca2_result_15,exercise_result_15,project_15,final_result_40)

    students = []
    #to put all the information for each student
    for i in range(len(id_list)):
        grade=grade_check(overall_result[i])
        student = Student(
            first_name_list[i],
            last_name_list[i],
            id_list[i],
            ca1_total[i],
            ca1_result_100[i],
            ca1_result_15[i],
            ca2_total[i],
            ca2_result_100[i],
            ca2_result_15[i],
            exercise_total[i],
            exercise_result_100[i],
            exercise_result_15[i],
            group_list[i],
            project_total[i],
            project_15[i],
            final_total[i],
            final_result_100[i],
            final_result_40[i],
            overall_result[i],
            grade
        )

        students.append(student)
    #save as csv
    save_results(students,folder+"results.csv")  
    create_pdf(students, folder + "results.pdf")
if __name__=="__main__":
    main()
