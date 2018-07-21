""" Developed by Asim Roy
Python Batch 3 2018
Date: 16.07.18 """

from tkinter import *
import mysql.connector

class Login:
    def __init__(self):

        self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='tinder3')
        self.mycursor=self.conn.cursor()

        self.root=Tk()

        self.root.title("Gareeb Tinder")

        self.root.minsize(250,350)
        self.root.maxsize(250,350)

        self.email_lable=Label(self.root, text="Enter Email")
        self.email_lable.pack()

        self.email_input=Entry(self.root)
        self.email_input.pack()

        self.password_lable=Label(self.root, text="Enter Password")
        self.password_lable.pack()

        self.password_input=Entry(self.root)
        self.password_input.pack()

        self.button=Button(self.root, text="Login", command=lambda :self.login())
        self.button.pack()

        self.result=Label(self.root, text="", fg="red")
        self.result.pack()

        self.regbutton=Button(self.root, text="Register", command=lambda :self.regwindow())
        self.regbutton.pack()

        self.current_user_id=0

        self.root.mainloop()

    def login(self):

        email=self.email_input.get()
        password=self.password_input.get()

        self.mycursor.execute("SELECT * FROM users WHERE `email` LIKE '{}' AND `password` LIKE '{}'".format(email,password))

        user_list=self.mycursor.fetchall()

        counter = 0
        current_user = 0
        for i in user_list:
            counter = counter + 1
            current_user = i

        if counter > 0:
            self.result.configure(text="Welcome")
            self.current_user_id = current_user[0]
            self.user_window()
        else:
            self.result.configure(text="Incorrect Credentials...Register...")

    #Functionalities of the buttons and function calls...
    def view_command(self):

        self.list1.delete(0,END)
        self.view_users()
        print(len(self.all_users_list))

        for i in self.all_users_list:
            self.list1.insert(END, i)

    def view_proposal_command(self):
        self.list1.delete(0, END)
        self.view_proposal()

        for i in self.proposed_user_list:
            self.list1.insert(END, i)

    def view_requests_command(self):

        self.list1.delete(0, END)

        self.view_requests()

        for i in self.request_user_list:
            self.list1.insert(END, i)

    def view_matches_command(self):

        self.list1.delete(0, END)

        self.view_matches()

        for i in self.matched_user:
            self.list1.insert(END, i)

    # functionalities of the buttons end here.....

    #2nd menu tinder main menu
    def user_window(self):

        self.root3 = Tk()

        self.root3.title("Tinder Menu")

        self.root3.minsize(350, 150)
        self.root3.maxsize(350, 150)

        self.b1=Button(self.root3, text="View Users", command=self.view_command)
        self.b1.grid(row=0, column=0)

        self.b2 = Button(self.root3, text=" Proposed ", command=self.view_proposal_command)
        self.b2.grid(row=1, column=0)

        self.b3 = Button(self.root3, text=" Requests  ", command=self.view_requests_command)
        self.b3.grid(row=2, column=0)

        self.b4 = Button(self.root3, text="  Matches  ", command=self.view_matches_command)
        self.b4.grid(row=3, column=0)

        self.b5 = Button(self.root3, text="  Propose  ", command=self.propose_window)
        self.b5.grid(row=4,column=0)

        self.sb1=Scrollbar(self.root3)
        self.sb1.grid(row=0, column=1, rowspan=5)

        self.list1=Listbox(self.root3, height=7, width=40)
        self.list1.grid(row=0, column=2, rowspan=6, columnspan=4)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.entry_value= StringVar()





    #registration window
    def regwindow(self):

        self.root1=Tk()

        self.root1.title("Register")

        self.root1.minsize(250, 350)
        self.root1.maxsize(250, 350)

        self.name_lable = Label(self.root1, text="Enter Name")
        self.name_lable.pack()

        self.name_input = Entry(self.root1)
        self.name_input.pack()

        self.email_lable = Label(self.root1, text="Enter Email")
        self.email_lable.pack()

        self.email_input = Entry(self.root1)
        self.email_input.pack()

        self.password_lable = Label(self.root1, text="Enter Password")
        self.password_lable.pack()

        self.password_input = Entry(self.root1)
        self.password_input.pack()

        self.gender_lable = Label(self.root1, text="Enter Gender")
        self.gender_lable.pack()

        self.gender_input = Entry(self.root1)
        self.gender_input.pack()

        self.age_lable = Label(self.root1, text="Enter Age")
        self.age_lable.pack()

        self.age_input = Entry(self.root1)
        self.age_input.pack()

        self.city_lable = Label(self.root1, text="Enter City")
        self.city_lable.pack()

        self.city_input = Entry(self.root1)
        self.city_input.pack()

        self.regcomplete=Button(self.root1, text="Register", fg="pink", bg="black", command=lambda :self.registerkarlo())
        self.regcomplete.pack()

        self.result1 = Label(self.root1, text="", fg="red")
        self.result1.pack()

    #propose window after clicking propose button
    def propose_window(self):

        self.root4 = Tk()

        self.root4.title("Insert Id")

        self.e1_value = StringVar()
        self.e1_pid = Entry(self.root4, textvariable=self.e1_value)
        self.e1_pid.grid(row=0, column=0)

        self.b1_propose = Button(self.root4, text="propose", command=lambda: self.proposing())
        self.b1_propose.grid(row=0, column=1)

        self.status = Label(self.root4, text="", fg="red")
        self.status.grid(row=1, column=0, columnspan=1)


    #This is where all the database functions are!!!

    def proposing(self):
        print(self.e1_pid.get())
        print(self.current_user_id)
        self.propose(self.current_user_id, self.e1_pid.get())
        self.status.configure(text="Proposed")

    def view_users(self):
        self.mycursor.execute(
            """SELECT `user_id`,`name`,`gender`,`age`,`city` FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(
                self.current_user_id))
        self.all_users_list = self.mycursor.fetchall()

    def propose(self, romeo_id, juliet_id):
        self.mycursor.execute(
            """INSERT INTO `proposals` SET `romeo_id`='{}',`juliet_id`='{}'""".format(romeo_id, juliet_id))
        self.conn.commit()

    def view_proposal(self):
        self.mycursor.execute(
            """SELECT u.`name`,u.`gender`,u.`city`,u.`age` FROM `proposals` p JOIN `users` u ON p.`juliet_id` = u.`user_id` 
            WHERE p.`romeo_id` LIKE '{}'""".format(self.current_user_id))
        self.proposed_user_list = self.mycursor.fetchall()

    def view_requests(self):
        self.mycursor.execute(
            """SELECT u.`name`,u.`gender`,u.`city`,u.`age` FROM `proposals` p JOIN `users` u ON p.`romeo_id` = u.`user_id` 
            WHERE p.`juliet_id` LIKE '{}'""".format(self.current_user_id))
        self.request_user_list = self.mycursor.fetchall()

    def view_matches(self):
        # tripple subquery
        self.mycursor.execute(
            """SELECT `name`,`gender`,`age`,`city` FROM `users` WHERE `user_id` IN 
            (SELECT `juliet_id` FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `juliet_id` IN (SELECT `romeo_id` FROM `proposals` 
            WHERE `juliet_id` LIKE '{}'))""".format(self.current_user_id, self.current_user_id))
        self.matched_user = self.mycursor.fetchall()

    #This is where they end!!!

    #registration function
    def registerkarlo(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        gender = self.gender_input.get()
        age = self.age_input.get()
        city = self.city_input.get()

        self.mycursor.execute("""INSERT INTO `users` 
                    (`user_id`,`name`, `email`, `password`, `gender`, `age`, `city`) VALUES
                    (NULL, '{}', '{}', '{}', '{}', '{}', '{}')""".format(name, email, password, gender, age, city))

        self.conn.commit()

        self.result1.configure(text="Registration Complete")


        self.root1.mainloop()

login=Login()