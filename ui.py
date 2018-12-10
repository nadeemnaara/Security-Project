import tkinter as tk
import tkinter.ttk as ttk
import core_funcntionality as cf
import time


class UI(tk.Frame):
    core = cf.CoreFunctionality('', 0)
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # init the main window
        master.title('DEMO')
        master.geometry('440x510')
        master.resizable(False, False)
        master.configure(background='#003c71')
        self.grid()
        self.create_tabs(master)

    def create_tabs(self, master):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=1, fill='both')

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Register Employee')
        self.notebook.add(self.tab2, text='Request Allowance')
        self.notebook.add(self.tab3, text='Release Employee')

        self.create_widgets_tab1(self.tab1)
        self.create_widgets_tab2(self.tab2)
        self.create_widgets_tab3(self.tab3)

    def create_widgets_tab1(self, master):
        # first_name
        # last_name
        # id_number
        # country
        # email
        # gender
        # job_title
        # department
        # manager
        # office_location
        # start_date
        # items_issued
        # bank_no
        # section
        # bank_account_no
        # employee_signature
        fields_tab1 = ['First Name', 'Last Name', 'ID Number', 'Country', 'Email', 'Gender', 'Department', 'Job Title',
                       'Manager', 'Office Location', 'Start Date', 'Items Issued', 'Bank No.', 'Section',
                       'Bank Account No', 'Employee Signature']
        N = len(fields_tab1)

        fields_var_tab1  = [tk.StringVar(value='') for _ in range(N)]
        entries_tab1 = [tk.Entry(master, textvariable=fields_var_tab1[i]) for i in range(N)]
        for i, e in enumerate(entries_tab1):
            e.insert(0, fields_tab1[i])
            e.config(fg='grey', font=('Clear Sans Light', 11))
            string = fields_tab1[i]
            e.bind('<FocusIn>', lambda event, x=e: self.on_entry_click(string, x))
            e.bind('<FocusOut>', lambda event, y=e: self.on_focusout(string, y))
            e.pack()

        button = tk.Button(master, text='Submit', width=15, command=lambda x=entries_tab1, op=1: self.on_submit(x, op))
        button.pack()

    def create_widgets_tab2(self, master):
        # first_name
        # last_name
        # employee_id
        # country
        # department
        # job_title
        # submit_date
        # due_date
        # purpose
        # money_amount
        # bank_no
        # section
        # bank_account_no
        # employee_signature
        fields_tab2 = ['First Name', 'Last Name', 'Employee ID', 'Country', 'Department' 'Job Title', 'Submit Date',
                       'Due Date', 'Purpose', 'Money Amount' 'Bank No.', 'Section', 'Bank Account No',
                       'Employee Signature']
        N = len(fields_tab2)

        fields_var_tab2 = [tk.StringVar(value='') for _ in range(N)]
        entries_tab2 = [tk.Entry(master, textvariable=fields_var_tab2[i]) for i in range(N)]
        for i, e in enumerate(entries_tab2):
            e.insert(0, fields_tab2[i])
            e.config(fg='grey', font=('Clear Sans Light', 11))
            # e.bind('<FocusIn>', lambda event, x=e: self.on_entry_click(str(self.fields_text[i]), x))
            # e.bind('<FocusOut>', lambda event, y=e: self.on_focusout(str(self.fields_text[i]), y))
            e.pack()

        button = tk.Button(master, text='Submit', width=15, command=lambda x=entries_tab2, op=2: self.on_submit(x, op))
        button.pack()

    def create_widgets_tab3(self, master):
        # first_name
        # last_name
        # employee_id
        # country
        # department
        # job_title
        # reason of leaving
        # last day at work
        # fiscal department: approver name, approval date
        # HR department: approver name, approval date

        fields_tab3 = ['First Name', 'Last Name', 'Employee ID', 'Country', 'Department', 'Job Title',
                       'Reason Of Leaving', 'Last Day At Work', 'Fiscal Department', 'HR Department']
        N = len(fields_tab3)

        fields_var_tab3  = [tk.StringVar(value='') for _ in range(N)]
        entries_tab3 = [tk.Entry(master, textvariable=fields_var_tab3[i]) for i in range(N)]
        for i, e in enumerate(entries_tab3):
            e.insert(0, fields_tab3[i])
            e.config(fg='grey', font=('Clear Sans Light', 11))
            # e.bind('<FocusIn>', lambda event, x=e: self.on_entry_click(str(self.fields_tab3[i]), x))
            # e.bind('<FocusOut>', lambda event, y=e: self.on_focusout(str(self.fields_tab3[i]), y))
            e.pack()

        button = tk.Button(master, text='Submit', width=15, command=lambda x=entries_tab3, op=3: self.on_submit(x, op))
        button.pack()

    @staticmethod
    def on_entry_click(event, entry):
        if entry.get() == event:
            entry.delete(0, "end")  # delete all the text in the entry
            entry.insert(0, '')  # Insert blank for user input
            entry.config(fg='black')

    @staticmethod
    def on_focusout(event, entry):
        if entry.get() == '':
            entry.insert(0, event)
            entry.config(fg='grey')

    def on_submit(self, entries_list, op_code):
        str_list = [e.get() for e in entries_list]
        switcher = {
            1: self.core.register_employee,
            2: self.core.request_allowance,
            3: self.core.release_employee
        }

        switcher[op_code](str_list)


root = tk.Tk()
app = UI(root)
app.mainloop()