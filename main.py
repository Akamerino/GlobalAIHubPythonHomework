class Student:

    def __init__(self, temp):
        self.name = temp
        self.lessons = list()
        self.exams = list()
        self.active = True

    def getName(self):
        return self.name

    def getLessons(self):
        return self.lessons

    def addLesson(self,lesson):
        self.lessons.append(lesson)

    def lessonMenu(self):

        while True:

            print("-----Grading System-----\n")
            temp = int(input("\n1-) Select lesson!\n2-)Exit\n"))

            if temp == 1:

                print(self.lessons)

                temp1 = input("Select one of the lessons!\n")

                if temp1 in self.lessons:

                    index = self.lessons.index(temp1)

                    print(self.lessons[index])
                    choice = int(input("1-)Take Exam\n2-)See your score\n"))

                    if choice == 1:
                        self.takeExam(index)
                    elif choice == 2:
                        self.score(index)
                else:
                    print("Wrong lesson name!\n")

            elif temp == 2:
                break
            else:
                print("Wrong choice!\n")

    def takeExam(self,index):

        midterm = int(input("Enter your midterm grade!\n"))
        final = int(input("Enter your final grade!\n"))
        project = int(input("Enter your project grade!\n"))

        dic1 = {"midterm": midterm, "final" : final, "project" : project}

        self.exams.insert(index, dic1)
        print(self.exams)

    def score(self, index):

        midterm = self.exams[index]["midterm"]
        final = self.exams[index]["final"]
        project = self.exams[index]["project"]

        score = midterm * 0.3 + final * 0.5 + project * 0.2

        print("Your score is\n")

        if score > 90:
            print("AA")
        elif 70 < score < 90:
            print("BB")
        elif 50 < score < 70:
            print("CC")
        elif 30 < score < 50:
            print("DD")
        elif score < 30:
            print("FF")
            print("You are failed!\n")

class StudentManagementSys:

    def __init__(self):
        self.studentList = list()
        self.lessonList = ["CSE231", "CSE241", "ENG151", "CSE233", "CSE211"]

    def menu(self):
        while True:
            print("Welcome student management system\n1-)Login\n2-)Sign up\n3-)Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if self.login():
                    break
            elif choice == 2:
                self.signup()
            elif choice == 3:
                print("Exiting from the system!\n")
                break
            else:
                print("Wrong choice!\n")

    def signup(self):

        control = True
        name1 = str(input("Please enter your name!\n"))

        for i in range(0, len(self.studentList)):
            if name1.upper() == self.studentList[i].getName():
                print("There is already a student named -{}-".format(name1))
                control = False

        if control:
            student1 = Student(name1.upper())           # Büyük küçük kontrolü için
            self.studentList.append(student1)
            print("You are signed up!\n")

    def login(self):

        name = str(input("Please enter your name!\n"))
        counter = 1

        while counter < 3:

            control = False

            for i in range(0, len(self.studentList)):
                if name.upper() == self.studentList[i].getName():
                    control = True
                    print("You are in the system.\n")
                    studentNo = i

            if control:
                break
            else:
                print("You are not in the system!\n")
                name = str(input("Please enter your name!\n"))
                counter += 1

        if counter == 3:
            print("Please try again later!\n")
            return True
        else:
            print(self.selectLesson(studentNo))
            return False

    def selectLesson(self, studentNo):

        print(self.lessonList)
        print("select lesson codes from list  (min:3 , max:5)\n")

        lessonCount = 0
        i = 1
        tempList = self.studentList[studentNo].getLessons()

        while i == 1:

            if lessonCount == 5:
                break

            i = int(input("Do you want to select lessons!\n1-)Yes\n2-)No\n"))

            if i == 1:
                temp = str(input("Select one of the lessons\n"))

                if temp in self.lessonList:
                    if temp in tempList:
                        print("This lesson is already selected!\n")
                    else:
                        tempList.append(temp)
                        lessonCount += 1
                else:
                    print("Wrong lesson name!\n")

            elif i == 2:
                break
            else:
                print("Wrong choice!")

        if lessonCount < 3:
            return "You have failed!"
        else:
            self.studentList[studentNo].lessonMenu()
            return "Succesful logout!"


system = StudentManagementSys()
system.menu()
