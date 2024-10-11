marks1 = int(input("Enter marks: "))
marks2 = int(input("Enter marks: "))
marks3 = int(input("Enter marks: "))
if ((marks1+marks2+marks3)<0.40*300):
    print("Grade: F")
else:
    if (marks1>=0.33*100):
        if (marks2>=0.33*100):
            if (marks3>=0.33*100):
                print("Grade: P")
            else:
                print("Grade: F")
        else:
            print("Grade: F")
    else:
        print("Grade: F")