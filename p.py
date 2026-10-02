folder = "C:/Users/muham/Desktop/CSV files project/"
filenames=[
    "Grades CA 1.csv",
    "Grades CA 2.csv",
    "Grades Final Exam.csv",
    "Grades Groups.csv",
    "Groups.csv",
    "Grades Exercises.csv"]

def read_file(path):                #function to read file
    with open(path,encoding="utf-8") as f:
        file_string=f.read()
    return file_string

def split_rows(file_string):    #function to split ";" to get the rows
    rows=file_string.split("\n")
    return rows

def student_info(ca1_rows):    
    first_name=[]
    last_name=[]
    student_id=[]
    for row in ca1_rows[1:]:
        col=row.split(";")
   
        first_name.append(col[0])
        last_name.append(col[1])
        student_id.append(col[2])
    return first_name,last_name,student_id

def calculate_total_mark(col,start,end):
    total_mark=0
    for i in range(start,end):
        total_mark+=float(col[i])
    return total_mark

def ca1_calculation(ca1_rows): #function to calculate the ca1 result and change to %
    ca1_result=[]
    for row in ca1_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,10) #to get total marks
        total_mark=round(total_mark/21*15,2)     
        ca1_result.append(total_mark)
    return ca1_result

def ca2_calculation(ca2_rows): #function to calculate the ca2 result and change to %15
    ca2_result=[]
    for row in ca2_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,8)
        total_mark=round(total_mark/16 *15,2)
        ca2_result.append(total_mark)
    return ca2_result

def final_calculation(final_rows): #function to calculate the final result and change to %40
    final_result=[]
    for row in final_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,16)
        total_mark=round(total_mark/50 *40,2)
        final_result.append(total_mark)
    return final_result

def find_group(student_id, groups_rows):    #to match the group number to the student id
    for row in groups_rows[1:]:
        col = row.split(";")
        if col[0]==student_id:
            return col[1]

def find_group_grade(group, group_grade_rows):
    for row in group_grade_rows[1:]:
        col=row.split(";")
        if col[0]==group:
            return float(col[1])

def main():
    first_name_list=[]
    last_name_list=[]
    id_list=[]
    ca1_total=[]
    ca1_results=[]
    ca2_total=[]
    ca2_results=[]
    final_total=[]
    final_results=[]


    ca1_file = read_file(folder + filenames[0])
    ca2_file = read_file(folder + filenames[1])
    final_file = read_file(folder + filenames[2])
    group_grade_file=read_file(folder + filenames[3])
    group_file=read_file(folder + filenames[4])

    ca1_rows=split_rows(ca1_file)
    ca2_rows=split_rows(ca2_file)
    final_rows=split_rows(final_file)
    group_grade_rows=split_rows(group_grade_file)
    group_rows=split_rows(group_file)


    first_name_list,last_name_list,id_list=student_info(ca1_rows)

    group=find_group(id_list,group_rows)
    print(group)

    ca1_results=ca1_calculation(ca1_rows)    #to call ca1 calc function
    ca2_results=ca2_calculation(ca2_rows)    #to call ca2 calc function
    final_results=final_calculation(final_rows)     #to call final calc function





if __name__=="__main__":
    main()