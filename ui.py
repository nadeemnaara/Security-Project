import tkinter as tk
import tkinter.ttk as ttk
import core_funcntionality as cf
import tkinter.messagebox as tkm


class PopUpWindow:
    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        l1 = tk.Label(top, text='Enter HOST IP and PORT')
        l1.grid(row=0, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5, columnspan=2, rowspan=1)
        l2 = tk.Label(top, text='HOST IP').grid(row=1, column=0, sticky=tk.W)
        l3 = tk.Label(top, text='PORT').grid(row=2, column=0, sticky=tk.W)

        self.e1 = tk.Entry(top)
        self.e1.grid(row=1, column=1)

        self.e2 = tk.Entry(top)
        self.e2.grid(row=2, column=1)
        b = tk.Button(top, text='Ok', command=self.ok)
        b.grid(row=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5, columnspan=2, rowspan=1)
        self.host = ''
        self.port = ''
        top.resizable(False, False)
        top.lift()

    def ok(self):
        host = self.host = self.e1.get()
        port = self.port = self.e2.get()
        if host == '' or port == '':
            tkm.showerror('Error', 'invalid HOST or PORT!')
            self.top.focus_force()
        else:
            self.top.destroy()

class UI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # init the main window
        master.title('Client')
        # master.geometry('500x550')
        master.resizable(False, False)
        master.configure(background='#003c71')
        self.grid()

        while True:
            self.popup = PopUpWindow(master)
            master.wait_window(self.popup.top)
            if self.popup.host != '' and self.popup.port != '':
                break

        self.create_tabs(master)
        self.core = cf.CoreFunctionality(self.popup.host, self.popup.port)

    def create_tabs(self, master):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=1, fill='both')

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Register Employee')
        self.notebook.add(self.tab2, text='Request Allowance')
        self.notebook.add(self.tab3, text='Release Employee')

        tab1_f = ['First Name', 'Last Name', 'ID Number', 'Country', 'Email', 'Gender', 'Department', 'Job Title',
                  'Manager', 'Office Location', 'Start Date', 'Items Issued', 'Bank No.', 'Section',
                  'Bank Account No', 'Employee Signature']

        tab2_f = ['First Name', 'Last Name', 'Employee ID', 'Country', 'Department' 'Job Title', 'Submit Date',
                  'Due Date', 'Purpose', 'Money Amount' 'Bank No.', 'Section', 'Bank Account No',
                  'Employee Signature']

        tab3_f = ['First Name', 'Last Name', 'Employee ID', 'Country', 'Department', 'Job Title', 'Reason Of Leaving',
                  'Last Day At Work', 'Fiscal Department', 'HR Department']

        self.create_tab(self.tab1, tab1_f, 1)
        self.create_tab(self.tab2, tab2_f, 2)
        self.create_tab(self.tab3, tab3_f, 3)

    def create_tab(self, master, fields, tab_n):
        N = len(fields)

        tab_frame = tk.Frame(master)
        tab_frame.pack()
        entries_tab = [tk.Entry(tab_frame) for _ in range(N)]
        for i, e in enumerate(entries_tab):
            tk.Label(tab_frame, text=fields[i]).grid(row=i, column=0, sticky=tk.W)
            e.grid(row=i, column=1)

        button = tk.Button(tab_frame, text='Submit', width=15,
                           command=lambda x=entries_tab, op=tab_n: self.on_submit(x, op))
        button.grid(row=N, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5, columnspan=2, rowspan=1)

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