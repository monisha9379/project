import csv

def write_into_csv(info_list):
    with open("student_info.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["name","age","contact no", "email ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    
    student = 1

    
    while(True):
        student_info = input("enter student #{} information in the following format(name age contact no email ID): ".format(student))
        student_info_list = student_info.split(' ')
        
        print("the entered info is: \n Name: {}\nAge: {}\nCONTACT NO: {}\nE-MAIL ID: {}" .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        ch = input("is the entered info correct enter yes/no: ")
        
        if ch == "yes":
            write_into_csv(student_info_list)
            check = input("enter yes/no if u want to enter information for another student: ")
            if check == "yes" or check == "y":
                student = student + 1
                continue
            else:
                print("thank you")
                break
            
        elif ch == "no":
            print("\nplease re enter ")
            

