import smtplib
import os
#Function to: start server, login/send the mail, and close the server
#sn:sender_address/sp:sender_password/r:receiver_address/m:msg
def createServer(sn,sp,r,m):
    smtplibObj = smtplib.SMTP("smtp.gmail.com",587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login(sn,sp)
    smtplibObj.sendmail(sn,r,m)
    smtplibObj.quit()

def readTxt(filename):
    filename += '.txt'
    #List to hold information
    info = []
    #Read the information
    with open(filename, 'r') as fileobj:
        for line in fileobj:
            info.append(line.rstrip('\n'))
    #Assign the information
    global sender_address,sender_password,receiver_address,name,prof_name,course,email_sub,email_msg
    sender_address = info[0]
    sender_password = info[1]
    receiver_address = info[2]
    name = info[3]
    prof_name = info[4]
    course = info[5]
    email_sub = info[6]
    email_msg = info[7]

def readTxt_generic(filename):
    filename += '.txt'
    #List to hold information
    info = []
    #Read the information
    with open(filename, 'r') as fileobj:
        for line in fileobj:
            info.append(line.rstrip('\n'))
    #Assign the information
    global sender_address,sender_password,receiver_address,name
    sender_address = info[0]
    sender_password = info[1]
    receiver_address = info[2]
    name = info[3]

def takeInput():
    global sender_address,sender_password,receiver_address,name,prof_name,course,email_sub,email_msg,msg
    #Take sender's info
    sender_address = input('Please enter your Email: ')
    os.system("cls")
    sender_password = input('Please enter your password: ')
    os.system("cls")
    #Take receiver's info
    receiver_address = input('Please enter the receiver\'s Email: ')
    os.system("cls")
    #Take info to construct mail
    name = input('Please enter the your full name: ')
    os.system("cls")
    prof_name = input('Please enter the professor\'s last name: ')
    os.system("cls")
    course = input('Please enter the course name: ')
    os.system("cls")
    email_sub = input('Please enter the email\'s subject: ')
    os.system("cls")
    email_msg = input('Please enter your message: ')
    os.system("cls")

def customEmail():          
    button_2 = int(input('1.Read txt file\n2.Enter information manually\n'))
    os.system("cls")
    if button_2 == 1:
        check = False
        while check == False:
            filename = input('Please enter the file name(that contains your credentials): ')
            os.system("cls")
            readTxt(filename)
            #Construct the email
            txt = "Dear Professor " + prof_name + ",\n\n\n" + email_msg
            msg = 'Subject: {}\n\n{}\n\n{}'.format(email_sub + ": " + course, txt,"Thank You.\n\nSincerely,\n" + name)
            #Information Validation
            print('Your Email: ' + sender_address)
            print('Your Password: ' + sender_password)
            print('Receiver\'s Email: ' + receiver_address)
            print("\n" + msg + "\n")
            tmp = input('This is the information you entered.\nDo you wish to continue?(Y/N): ')
            os.system("cls")
            if tmp == 'Y':
                check = True
    elif button_2 == 2:
        check = False
        while check == False:
            takeInput()
            #Construct the email
            txt = "Dear Professor " + prof_name + ",\n\n\n" + email_msg
            msg = 'Subject: {}\n\n{}\n\n{}'.format(email_sub + ": " + course, txt,"Thank You.\n\nSincerely,\n" + name)
            #Information Validation
            print('Your Email: ' + sender_address)
            print('Your Password: ' + sender_password)
            print('Receiver\'s Email: ' + receiver_address)
            print("\n" + msg + "\n")
            tmp = input('This is the information you entered.\nDo you wish to continue?(Y/N): ')
            os.system("cls")
            if tmp == 'Y':
                check = True     
    else:
        print('Incorrect Input')
        return
    createServer(sender_address,sender_password,receiver_address,msg)
    print("Message sent successfully")
    x = input('Press any key to continue...')
    os.system("cls")

def genericEmail():
    button_3 = int(input('1.Attendance\n2.Rescheduling\n'))
    os.system("cls")
    if button_3 == 1:
        check = False
        while check == False:
            os.system("cls")
            filename = input('Please enter the file name(that contains your credentials): ')
            os.system("cls")
            readTxt_generic(filename)
            prof_name = input('Please enter the professor\'s last name: ')
            os.system("cls")
            course = input('Please enter the course name: ')
            os.system("cls")
            weekNo = input('Please enter the week number: ')
            os.system("cls")
            email_msg = 'I attended week no.' + weekNo + ' but I can see on the website that I was written as absent, can we fix this problem?'
            email_sub = 'Attendance'
            #Construct the email
            txt = "Dear Professor " + prof_name + ",\n\n\n" + email_msg
            msg = 'Subject: {}\n\n{}\n\n{}'.format(email_sub + ": " + course, txt,"Thank You.\n\nSincerely,\n" + name)
            #Information Validation
            print('Your Email: ' + sender_address)
            print('Your Password: ' + sender_password)
            print('Receiver\'s Email: ' + receiver_address)
            print("\n" + msg + "\n\n")
            tmp = input('This is the information you entered.\nDo you wish to continue?(Y/N): ')
            os.system("cls")
            if tmp == 'Y':
                check = True
    elif button_3 == 2:
        choice = int(input('1.Assignment\n2.Project\n3.Exam\n'))
        os.system("cls")
        date1 = input('Please enter the submission date(old): ')
        os.system("cls")
        date2 = input('Please enter the submission date(new): ')
        os.system("cls")
        if choice == 1:
            assignmentNo = input('Assignment(no.):')
            os.system("cls")
            email_sub = 'Rescheduling Assignment'
            email_msg = 'Is it possible to reschedule Assignment(' + assignmentNo + ') from ' + date1 + ' to ' + date2 + '?'
        elif choice == 2:
            projectNo = input('Project(no.):')
            os.system("cls")
            email_sub = 'Rescheduling Project'
            email_msg = 'Is it possible to reschedule Project(' + projectNo + ') from ' + date1 + ' to ' + date2 + '?'
        elif choice == 3:
            exam = input('Quiz(no.), Midterm, Final:')
            os.system("cls")
            email_sub = 'Rescheduling Exam'
            email_msg = 'Is it possible to reschedule the ' + exam + ' from ' + date1 + ' to ' + date2 + '?'
        else:
            print('Incorrect Input')
            x = input('Press any key to continue...')
            os.system("cls")
            return
        check = False
        while check == False:
            os.system("cls")
            filename = input('Please enter the file name(that contains your credentials): ')
            os.system("cls")
            readTxt_generic(filename)
            prof_name = input('Please enter the professor\'s last name: ')
            os.system("cls")
            course = input('Please enter the course name: ')
            os.system("cls")
            #Construct the email
            txt = "Dear Professor " + prof_name + ",\n\n\n" + email_msg
            msg = 'Subject: {}\n\n{}\n\n{}'.format(email_sub + ": " + course, txt,"Thank You.\n\nSincerely,\n" + name)
            #Information Validation
            print('Your Email: ' + sender_address)
            print('Your Password: ' + sender_password)
            print('Receiver\'s Email: ' + receiver_address)
            print("\n" + msg + "\n\n")
            tmp = input('This is the information you entered.\nDo you wish to continue?(Y/N): ')
            os.system("cls")
            if tmp == 'Y':
                check = True
    else:
        print('Incorrect Input')
        x = input('Press any key to continue...')
        os.system("cls")
        return
    createServer(sender_address,sender_password,receiver_address,msg)
    print("Message sent successfully")
    x = input('Press any key to continue...')
    os.system("cls")

def mainMenu():
    os.system("cls")
    button = 0
    while button != 3:
        button = int(input('-----Main menu-----\n1.Custom Email.\n2.Generic Email\n3.End Program.\n'))
        os.system("cls")
        if button == 1:
            customEmail()
        elif button == 2:
            genericEmail()
        elif button == 3:
            print('Thank you for using this program.\n')
            x = input('')
        else:
            print("Incorrect Input")
            x = input('Press any key to continue...')
            os.system("cls")

mainMenu()