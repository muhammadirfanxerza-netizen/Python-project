folder = "C:/Users/muham/Desktop/CSV files project/"
filenames=["Grades CA 1.csv","Grades CA 2.csv","Grades Final Exam.csv","Grades Groups.csv","Groups.csv","Grades Exercises.csv"]

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
   
        first_name.append(col[1])
        last_name.append(col[0])
        student_id.append(col[2])
    return first_name,last_name,student_id

def calculate_total_mark(col,start,end):
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
        total_mark_100=round(total_mark/21*100,2)
        ca1_result_100.append(total_mark_100)
        total_mark=round(total_mark/21*15,2)     
        ca1_result_15.append(total_mark)
    return ca1_total,ca1_result_15,ca1_result_100

def ca2_calculation(ca2_rows): #function to calculate the ca2 result and change to %15
    ca2_result_100=[]
    ca2_result_15=[]
    ca2_total=[]  
    for row in ca2_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,8)
        ca2_total.append(total_mark)
        total_mark_100=round(total_mark/16*100,2)
        ca2_result_100.append(total_mark_100)
        total_mark=round(total_mark/16 *15,2)
        ca2_result_15.append(total_mark)
    return ca2_total,ca2_result_15,ca2_result_100

def final_calculation(final_rows): #function to calculate the final result and change to %40
    final_result_100=[]
    final_result_40=[]
    final_total=[]
    for row in final_rows[1:]:
        col=row.split(";")
        total_mark=calculate_total_mark(col,3,16)
        final_total.append(total_mark)
        total_mark_100=round(total_mark/50*100,2)
        final_result_100.append(total_mark_100)
        total_mark_40=round(total_mark/50 *40,2)
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

def find_group_grade(group, group_grade_rows):
    for row in group_grade_rows[1:]:
        col=row.split(";")
        if col[0]==group:
            return float(col[1])

def overall_calculation(ca1_15,ca2_15,exercise_15,project_15,final_40):
    overall_result=[]
    for i in range(len(ca1_15)):
        total=(ca1_15[i]+ca2_15[i]+exercise_15[i]+project_15[i]+final_40[i])
        overall_result.append(round(total,2))
    return overall_result


        
#to call the function in the main
def main():
    project_results = []
    group_list = []

    ca1_file = read_file(folder + filenames[0])
    ca2_file = read_file(folder + filenames[1])
    final_file = read_file(folder + filenames[2])
    group_grade_file=read_file(folder + filenames[3])
    group_file=read_file(folder + filenames[4])
    exercise_file = read_file(folder + filenames[5])

    ca1_rows=split_rows(ca1_file)
    ca2_rows=split_rows(ca2_file)
    final_rows=split_rows(final_file)
    group_grade_rows=split_rows(group_grade_file)
    group_rows=split_rows(group_file)
    exercise_rows = split_rows(exercise_file)


    first_name_list,last_name_list,id_list=student_info(ca1_rows)
    for student_id in id_list:
        group = find_group(student_id, group_rows)
        group_list.append(group)
        project_grade = find_group_grade(group, group_grade_rows)
        project_grade = round(project_grade / 10 * 15, 2)
        project_results.append(project_grade)

    ca1_total,ca1_result_15,ca1_result_100=ca1_calculation(ca1_rows)    #to call ca1 calc function
    ca2_total,ca2_result_15,ca2_result_100=ca2_calculation(ca2_rows)    #to call ca2 calc function
    final_total,final_result_40,final_result_100=final_calculation(final_rows)     #to call final calc function
    exercise_total,exercise_result_15,exercise_result_100=exercise_calculation(exercise_rows)
    overall_result=overall_calculation(ca1_result_15,ca2_result_15,exercise_result_15,project_results,final_result_40)


if __name__=="__main__":
    main()
