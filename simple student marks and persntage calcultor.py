try :
    while True:


        name = input ("enter the student name :").upper()

        marks=500


        sub1=int(input ("enter the subject - 1 marks:"))
        sub2=int(input ("enter the subject - 2 marks:"))
        sub3=int(input ("enter the subject - 3 marks:"))
        sub4=int(input ("enter the subject - 4 marks:"))
        sub5=int(input ("enter the subject - 5 marks:"))

        print(f"📋 Report Card for 🧑‍🎓 Student:-->{name}")
        print(f"Total Marks:{(sub1) + (sub2)+ (sub3) + (sub4) + (sub5)}/{marks}")
        total=(sub1+sub2+sub3+sub4+sub5)/marks*100
        print(f"Percentage:{total}")

        if total==100:
            print("VARY GOOD 👌 ")
            print(f"Grade A+")
        elif 90<total<100:
            print("GOOD")
            print(f"Grade A")
        elif 75<total <90:
            print("AVERAGE 😐")
            print(f"Grade B")
        elif 50<total<70:
            print("pass")
            print(f"Grade C")
        elif 25<total<50:
            print(f"pass -c grade ")
        elif 0<total<25:
            print(f"FAIL")
        elif total==0:
            print("you failed all the subjects")
            print("Bro dont thik of your grade")
        r=input("enter the choice (yes/no):)")
        if r == "yes":
            print("")
            continue
        else:
            print("thanku for using msrks to Percentage calculator")
            break




except ZeroDivisionError:
    print("something went wrong")
except KeyboardInterrupt:
    print("some thing went wrong")
except ValueError:
    print("something went wrong")

except Exception as e:
    print(e)
    print("some thing went wrong")
