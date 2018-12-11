import tkinter as tk
import tkinter.ttk as ttk
import core_funcntionality as cf
import copy


class UI(tk.Frame):
    core = cf.CoreFunctionality('', 0)
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # init the main window
        master.title('Client')
        master.geometry('500x550')
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
            e.config(fg='grey', font=('Clear Sans Light', 12))
            e.pack()

        entries_tab1[0].bind('<FocusIn>', lambda event, x=entries_tab1[0]: self.on_entry_click(fields_tab1[0], x))
        entries_tab1[0].bind('<FocusOut>', lambda event, y=entries_tab1[0]: self.on_focusout(fields_tab1[0], y))

        entries_tab1[1].bind('<FocusIn>', lambda event, x=entries_tab1[1]: self.on_entry_click(fields_tab1[1], x))
        entries_tab1[1].bind('<FocusOut>', lambda event, y=entries_tab1[1]: self.on_focusout(fields_tab1[1], y))

        entries_tab1[2].bind('<FocusIn>', lambda event, x=entries_tab1[2]: self.on_entry_click(fields_tab1[2], x))
        entries_tab1[2].bind('<FocusOut>', lambda event, y=entries_tab1[2]: self.on_focusout(fields_tab1[2], y))

        entries_tab1[3].bind('<FocusIn>', lambda event, x=entries_tab1[3]: self.on_entry_click(fields_tab1[3], x))
        entries_tab1[3].bind('<FocusOut>', lambda event, y=entries_tab1[3]: self.on_focusout(fields_tab1[3], y))

        entries_tab1[4].bind('<FocusIn>', lambda event, x=entries_tab1[4]: self.on_entry_click(fields_tab1[4], x))
        entries_tab1[4].bind('<FocusOut>', lambda event, y=entries_tab1[4]: self.on_focusout(fields_tab1[4], y))

        entries_tab1[5].bind('<FocusIn>', lambda event, x=entries_tab1[5]: self.on_entry_click(fields_tab1[5], x))
        entries_tab1[5].bind('<FocusOut>', lambda event, y=entries_tab1[5]: self.on_focusout(fields_tab1[5], y))

        entries_tab1[6].bind('<FocusIn>', lambda event, x=entries_tab1[6]: self.on_entry_click(fields_tab1[6], x))
        entries_tab1[6].bind('<FocusOut>', lambda event, y=entries_tab1[6]: self.on_focusout(fields_tab1[6], y))

        entries_tab1[7].bind('<FocusIn>', lambda event, x=entries_tab1[7]: self.on_entry_click(fields_tab1[7], x))
        entries_tab1[7].bind('<FocusOut>', lambda event, y=entries_tab1[7]: self.on_focusout(fields_tab1[7], y))

        entries_tab1[8].bind('<FocusIn>', lambda event, x=entries_tab1[8]: self.on_entry_click(fields_tab1[8], x))
        entries_tab1[8].bind('<FocusOut>', lambda event, y=entries_tab1[8]: self.on_focusout(fields_tab1[8], y))

        entries_tab1[9].bind('<FocusIn>', lambda event, x=entries_tab1[9]: self.on_entry_click(fields_tab1[9], x))
        entries_tab1[9].bind('<FocusOut>', lambda event, y=entries_tab1[9]: self.on_focusout(fields_tab1[9], y))

        entries_tab1[10].bind('<FocusIn>', lambda event, x=entries_tab1[10]: self.on_entry_click(fields_tab1[10], x))
        entries_tab1[10].bind('<FocusOut>', lambda event, y=entries_tab1[10]: self.on_focusout(fields_tab1[10], y))

        entries_tab1[11].bind('<FocusIn>', lambda event, x=entries_tab1[11]: self.on_entry_click(fields_tab1[11], x))
        entries_tab1[11].bind('<FocusOut>', lambda event, y=entries_tab1[11]: self.on_focusout(fields_tab1[11], y))

        entries_tab1[12].bind('<FocusIn>', lambda event, x=entries_tab1[12]: self.on_entry_click(fields_tab1[12], x))
        entries_tab1[12].bind('<FocusOut>', lambda event, y=entries_tab1[12]: self.on_focusout(fields_tab1[12], y))

        entries_tab1[13].bind('<FocusIn>', lambda event, x=entries_tab1[13]: self.on_entry_click(fields_tab1[13], x))
        entries_tab1[13].bind('<FocusOut>', lambda event, y=entries_tab1[13]: self.on_focusout(fields_tab1[13], y))

        entries_tab1[14].bind('<FocusIn>', lambda event, x=entries_tab1[14]: self.on_entry_click(fields_tab1[14], x))
        entries_tab1[14].bind('<FocusOut>', lambda event, y=entries_tab1[14]: self.on_focusout(fields_tab1[14], y))

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
            e.config(fg='grey', font=('Clear Sans Light', 12))
            e.pack()

        entries_tab2[0].bind('<FocusIn>', lambda event, x=entries_tab2[0]: self.on_entry_click(fields_tab2[0], x))
        entries_tab2[0].bind('<FocusOut>', lambda event, y=entries_tab2[0]: self.on_focusout(fields_tab2[0], y))

        entries_tab2[1].bind('<FocusIn>', lambda event, x=entries_tab2[1]: self.on_entry_click(fields_tab2[1], x))
        entries_tab2[1].bind('<FocusOut>', lambda event, y=entries_tab2[1]: self.on_focusout(fields_tab2[1], y))

        entries_tab2[2].bind('<FocusIn>', lambda event, x=entries_tab2[2]: self.on_entry_click(fields_tab2[2], x))
        entries_tab2[2].bind('<FocusOut>', lambda event, y=entries_tab2[2]: self.on_focusout(fields_tab2[2], y))

        entries_tab2[3].bind('<FocusIn>', lambda event, x=entries_tab2[3]: self.on_entry_click(fields_tab2[3], x))
        entries_tab2[3].bind('<FocusOut>', lambda event, y=entries_tab2[3]: self.on_focusout(fields_tab2[3], y))

        entries_tab2[4].bind('<FocusIn>', lambda event, x=entries_tab2[4]: self.on_entry_click(fields_tab2[4], x))
        entries_tab2[4].bind('<FocusOut>', lambda event, y=entries_tab2[4]: self.on_focusout(fields_tab2[4], y))

        entries_tab2[5].bind('<FocusIn>', lambda event, x=entries_tab2[5]: self.on_entry_click(fields_tab2[5], x))
        entries_tab2[5].bind('<FocusOut>', lambda event, y=entries_tab2[5]: self.on_focusout(fields_tab2[5], y))

        entries_tab2[6].bind('<FocusIn>', lambda event, x=entries_tab2[6]: self.on_entry_click(fields_tab2[6], x))
        entries_tab2[6].bind('<FocusOut>', lambda event, y=entries_tab2[6]: self.on_focusout(fields_tab2[6], y))

        entries_tab2[7].bind('<FocusIn>', lambda event, x=entries_tab2[7]: self.on_entry_click(fields_tab2[7], x))
        entries_tab2[7].bind('<FocusOut>', lambda event, y=entries_tab2[7]: self.on_focusout(fields_tab2[7], y))

        entries_tab2[8].bind('<FocusIn>', lambda event, x=entries_tab2[8]: self.on_entry_click(fields_tab2[8], x))
        entries_tab2[8].bind('<FocusOut>', lambda event, y=entries_tab2[8]: self.on_focusout(fields_tab2[8], y))

        entries_tab2[9].bind('<FocusIn>', lambda event, x=entries_tab2[9]: self.on_entry_click(fields_tab2[9], x))
        entries_tab2[9].bind('<FocusOut>', lambda event, y=entries_tab2[9]: self.on_focusout(fields_tab2[9], y))

        entries_tab2[10].bind('<FocusIn>', lambda event, x=entries_tab2[10]: self.on_entry_click(fields_tab2[10], x))
        entries_tab2[10].bind('<FocusOut>', lambda event, y=entries_tab2[10]: self.on_focusout(fields_tab2[10], y))

        entries_tab2[11].bind('<FocusIn>', lambda event, x=entries_tab2[11]: self.on_entry_click(fields_tab2[11], x))
        entries_tab2[11].bind('<FocusOut>', lambda event, y=entries_tab2[11]: self.on_focusout(fields_tab2[11], y))

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
            e.config(fg='grey', font=('Clear Sans Light', 12))
            e.pack()

        entries_tab3[0].bind('<FocusIn>', lambda event, x=entries_tab3[0]: self.on_entry_click(fields_tab3[0], x))
        entries_tab3[0].bind('<FocusOut>', lambda event, y=entries_tab3[0]: self.on_focusout(fields_tab3[0], y))

        entries_tab3[1].bind('<FocusIn>', lambda event, x=entries_tab3[1]: self.on_entry_click(fields_tab3[1], x))
        entries_tab3[1].bind('<FocusOut>', lambda event, y=entries_tab3[1]: self.on_focusout(fields_tab3[1], y))

        entries_tab3[2].bind('<FocusIn>', lambda event, x=entries_tab3[2]: self.on_entry_click(fields_tab3[2], x))
        entries_tab3[2].bind('<FocusOut>', lambda event, y=entries_tab3[2]: self.on_focusout(fields_tab3[2], y))

        entries_tab3[3].bind('<FocusIn>', lambda event, x=entries_tab3[3]: self.on_entry_click(fields_tab3[3], x))
        entries_tab3[3].bind('<FocusOut>', lambda event, y=entries_tab3[3]: self.on_focusout(fields_tab3[3], y))

        entries_tab3[4].bind('<FocusIn>', lambda event, x=entries_tab3[4]: self.on_entry_click(fields_tab3[4], x))
        entries_tab3[4].bind('<FocusOut>', lambda event, y=entries_tab3[4]: self.on_focusout(fields_tab3[4], y))

        entries_tab3[5].bind('<FocusIn>', lambda event, x=entries_tab3[5]: self.on_entry_click(fields_tab3[5], x))
        entries_tab3[5].bind('<FocusOut>', lambda event, y=entries_tab3[5]: self.on_focusout(fields_tab3[5], y))

        entries_tab3[6].bind('<FocusIn>', lambda event, x=entries_tab3[6]: self.on_entry_click(fields_tab3[6], x))
        entries_tab3[6].bind('<FocusOut>', lambda event, y=entries_tab3[6]: self.on_focusout(fields_tab3[6], y))

        entries_tab3[7].bind('<FocusIn>', lambda event, x=entries_tab3[7]: self.on_entry_click(fields_tab3[7], x))
        entries_tab3[7].bind('<FocusOut>', lambda event, y=entries_tab3[7]: self.on_focusout(fields_tab3[7], y))

        entries_tab3[8].bind('<FocusIn>', lambda event, x=entries_tab3[8]: self.on_entry_click(fields_tab3[8], x))
        entries_tab3[8].bind('<FocusOut>', lambda event, y=entries_tab3[8]: self.on_focusout(fields_tab3[8], y))

        entries_tab3[9].bind('<FocusIn>', lambda event, x=entries_tab3[9]: self.on_entry_click(fields_tab3[9], x))
        entries_tab3[9].bind('<FocusOut>', lambda event, y=entries_tab3[9]: self.on_focusout(fields_tab3[9], y))

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