from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # database object
        self.dbo = Database()
        self.apio = API()
        # Load Login GUI
        self.root = Tk()
        self.root.title("NLP Application")
        self.root.geometry('350x600')
        self.root.config(bg='#24495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root,text='NLP App',bg='#24495E',fg='white')
        heading.config(font=('verdana',24,'bold'))
        heading.pack(pady=(30,30))

        label1 = Label(self.root,text='Enter email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a Member?')
        label3.pack(pady=(20, 10))
        redirect_btn = Button(self.root, text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#24495E', fg='white')
        heading.config(font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 30))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?')
        label3.pack(pady=(20, 10))
        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration Successful. You can Login Now')
        else:
            messagebox.showerror('Error','Email Already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#24495E', fg='white')
        heading.config(font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 30))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))


        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#24495E', fg='white')
        heading.config(font=('verdana', 24, 'bold'))
        heading.pack(pady=(30, 30))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#24495E', fg='white')
        heading2.config(font=('verdana', 20))
        heading2.pack(pady=(10, 30))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=30)

        sentiment_btn = Button(self.root, text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#24495E',fg='white')
        self.sentiment_result.config(font=('verdana', 15))
        self.sentiment_result.pack(pady=(10, 10))


        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + (i + '->' + str(result['sentiment'][i]) + '\n')
        self.sentiment_result['text'] = txt

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#24495E', fg='white')
        heading.config(font=('verdana', 24, 'bold'))
        heading.pack(pady=(15, 15))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#24495E', fg='white')
        heading2.config(font=('verdana', 18))
        heading2.pack(pady=(10, 15))

        label1 = Label(self.root, text='Enter the Text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=30)

        ner_btn = Button(self.root, text='Extract',command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='',bg='#24495E',fg='white')
        self.ner_result.config(font=('verdana', 10))
        self.ner_result.pack(pady=(10, 10))


        goback_btn = Button(self.root, text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner(self):

        text = self.ner_input.get()
        result = self.apio.ner(text)

        print(result)

        txt = ''
        for entity in result['entities']:
            txt += "{}:{} \n".format(entity['category'].capitalize(),entity['name'])
        self.ner_result['text'] = txt

nlp = NLPApp()