from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn import preprocessing
from ttkthemes import themed_tk as tk
from tkinter import filedialog
from PyInstaller.utils.hooks import collect_data_files
import os


### Backend ###
dataset = pd.DataFrame()
status = ''
dirName =''
cwd = os.getcwd()

def get_colnames():
    global colnames
    colnames = dataset.columns


def show_all_numeric_columns():
    listbox2.delete(0, END)
    colsToDelete = []
    global numericColumns
    numericColumns = dataset.select_dtypes(include=['float64', 'int64']).columns
    i = 0
    for col in numericColumns:
        if np.array_equal(np.unique(dataset[col]), [0, 1]) == False:
            listbox2.insert(i, col)
            i = i + 1
    numericColumns = listbox2.get(0, END)


def show_all_categorical_columns():
    listbox3.delete(0, END)
    global categoricalColumns
    categoricalColumns = dataset.select_dtypes(include=['object']).columns
    i = 0
    for column in categoricalColumns:
        listbox3.insert(i, column)
        i = i + 1

def export_dataset():
    if n.get() == "Standardize":
        standardize()
    val = entry2.get()
    dataset.to_csv(dirName+val, index=False)

def delete_columns():
    global dataset
    selectedItems = listbox.curselection()
    print(selectedItems)
    i = 0
    for columnNR in selectedItems:
        column = (dataset.columns[columnNR])
        dataset = dataset.drop([column], axis=1)
        show_all_columns()
        i = i + 1
    update_all()
    update_status(str(i) + " columns deleted")


def show_all_columns():
    global colnames
    global dataset
    listbox.delete(0, END)
    colnames = dataset.columns
    i = 0
    for column in colnames:
        listbox.insert(i, column)
        i = i + 1

def get_dataset():
    global dataset
    global status
    listbox.delete(0, END)
    val = entry.get()
    try:
        dataset = pd.read_csv(dirName + val)
        print('Dataset imported!')
        update_status("Dataset imported")
        get_colnames()
        update_all()
        print(dataset.dtypes)

    except:
        update_status("Dataset not found")

def update_status(newStatus):
    global label7
    label7.config(text=newStatus)

def print_dataset():
    print(dataset.dtypes)

def create_Dummies():
    global dataset
    selectedObjectItems = listbox3.curselection()
    for columnNR in selectedObjectItems:
        colname = categoricalColumns.values[columnNR]
        dummyvalues = pd.get_dummies(dataset[colname])
        print(dummyvalues)
        dataset.drop([colname], axis = 1, inplace = True)
        dataset = pd.concat([dummyvalues,dataset], axis = 1)
        print(dataset)
        show_all_numeric_columns()
        show_all_categorical_columns()
        show_created_dummy_columns()
        show_boolean_columns()
        print(dataset.dtypes)
    update_all()
    update_status("Dummies created")


def show_created_dummy_columns():
    global dummyColumns
    global dataset
    global allDummies
    allDummies =[]
    listbox4.delete(0, END)
    columnnames = dataset.columns
    i = 0
    for col in columnnames:
        if np.array_equal(np.unique(dataset[col]), [0, 1]) == True and dataset[col].dtype != bool:
            listbox4.insert(i, col)
            allDummies.append(col)
            i = i + 1

def show_boolean_columns():
    global dataset
    global allBools
    allBools = []
    listbox5.delete(0, END)
    columnnames = dataset.columns
    i = 0
    for col in columnnames:
        if dataset[col].dtype == bool:
            listbox5.insert(i, col)
            allBools.append(col)
            i = i + 1

def print_dummies():
    print(allDummies)

def create_bools():
    global dataset
    selectedDummyItems = listbox4.curselection()
    for columnNR in selectedDummyItems:
        colname = allDummies[columnNR]
        print(colname)
        dataset[colname] = dataset[colname].astype(bool)
    update_all()
    update_status("Booleans created")


def bool_to_dummy():
    global dataset
    selectedBoolItems = listbox5.curselection()
    for columnNR in selectedBoolItems:
        colname = allBools[columnNR]
        print(colname)
        dataset[colname] = dataset[colname].astype(int)
    update_all()

def numerical_to_categorical():
    global dataset
    global numericColumns
    selectedNumericItems = listbox2.curselection()
    print(selectedNumericItems)
    if selectedNumericItems != ():
        for col in selectedNumericItems:
            colname = numericColumns[col]
            print(colname)
            dataset[colname] = dataset[colname].astype('object', copy=False)
        update_all()
        update_status("Categorical variables created")
    else:
        update_status("Select a column!")


def dummy_to_categorical():
    global dataset
    global status
    global label7
    selectedDummyItems = listbox4.curselection()
    selectedDummies = []

    for columnNR in selectedDummyItems:
        colname = allDummies[columnNR]
        selectedDummies.append(colname)
    newColumn = []

    for index, row in dataset[selectedDummies].iterrows():
        if row.nunique() == 1:
            newColumn.append("Other")
        else:
            newColumn.append(row.idxmax(axis=1))

    val = entry3.get()
    if val!= '':
        print(val)
        dataset[val] = newColumn
        dataset[val] = dataset[val].astype('object', copy=False)
        #Delete old columns
        for column in selectedDummies:
            dataset = dataset.drop([column], axis=1)
        update_all()
        entry3.config(text='')
        update_status("Categorical var. created")

    else:
        update_status("Type in name for variable")

def categorical_to_numerical():
    global dataset
    le = preprocessing.LabelEncoder()
    selectedCategoricalItems = listbox3.curselection()
    if selectedCategoricalItems!=():
        for columnNR in selectedCategoricalItems:
            colname = categoricalColumns[columnNR]
            le.fit(dataset[colname])
            dataset[colname] = le.transform(dataset[colname])
            dataset[colname] = dataset[colname].astype('int64', copy=False)
            print(dataset[colname])
            update_all()
            update_status("Numerical var. created")
    else:
        update_status("Select a column!")


def update_all():
    show_boolean_columns()
    show_created_dummy_columns()
    show_all_columns()
    show_all_numeric_columns()
    show_all_categorical_columns()


def getRbValue():
    print(n.get())


def standardize():
    global dataset
    selectedNumericItems = listbox2.curselection()
    for columnNR in selectedNumericItems:
        colname = numericColumns[columnNR]
        dataset[colname] = preprocessing.scale(dataset[colname])

def removeNAs():
    global dataset
    dataset = dataset.dropna()
    update_all()


def changeDir():
    global dirName
    dirName = filedialog.askdirectory(initialdir=cwd) + "/"
    print(dirName)

def showTypes():
    global dataset
    print(listbox2.get(0, END))

def renameColumn():
    global dataset
    colnr = listbox.curselection()[0]
    print(colnr)
    allcolumns = listbox.get(0,END)
    print(allcolumns)
    colname = allcolumns[colnr]
    print(colname)
    newName = entry5.get()
    dataset.rename(columns={colname: newName}, inplace=True)
    update_all()
    update_status("Column renamed")


def binning():
    global dataset
    columnnr = listbox2.curselection()
    if listbox2.curselection()== ():
        update_status("Select a column!")
    elif entry4.get() == '' :
        update_status("Forgot nr. of. bins!")
    else:
        for nr in columnnr:
            print(nr)
            columnname = listbox2.get(0,END)[nr]
            print(columnname)
            binNr = int(entry4.get())
            dataset[columnname] = pd.qcut(dataset[columnname], binNr, labels=range(1, 1+binNr), duplicates ="drop" )
            print(dataset[columnname])
            update_status("Created " + str(binNr) + " bins")



##### Frontend #####

window = tk.ThemedTk()
window.get_themes()
window.configure(background='#414141')
window.set_theme("equilux")

window.grid_rowconfigure(12, minsize=40)
window.grid_rowconfigure(1, minsize=40)
window.grid_rowconfigure(3, minsize=40)
window.grid_rowconfigure(5, minsize=40)
window.grid_columnconfigure(0, minsize=40)
window.grid_columnconfigure(3, minsize=160)
window.grid_columnconfigure(4, minsize=160)
window.grid_columnconfigure(5, minsize=160)
window.grid_columnconfigure(6, minsize=160)


window.grid_rowconfigure(0, minsize=40)

window.iconbitmap('SUPERINTELLIGENCE.ico')
window.title("PrePro-Helper")
window.geometry("1000x700")
window.resizable(0, 0)

img = PhotoImage(file="robo.png")
logo = Label(window, image= img)

font='Helvetica 8 bold'

label1 = ttk.Label(window, text = "Enter the name of the dataset")
placeholder = Label(window, text = "")
label2 = ttk.Label(window, text = "Select numeric columns which you want to change")
label3 = ttk.Label(window, text = "Select categorical columns which you want to change")
label4 = ttk.Label(window, text = "Select the label")
label5 = ttk.Label(window, text = "All Columns of the dataset", font=font)
label6 = ttk.Label(window, text = "Status:",font='Helvetica 12 bold')
label7 = ttk.Label(window, text = '',font='Helvetica 12 bold')
label8 = ttk.Label(window, text = "Numerical Columns", font=font)
label9 = ttk.Label(window, text = "Categorical Columns", font=font)
label10 = ttk.Label(window, text = "Dummy Columns", font=font)
label11 = ttk.Label(window, text = "")
label12 = ttk.Label(window, text = "Enter name for new dataset")
label13 = ttk.Label(window, text = "Boolean Columns", font=font)

entry = ttk.Entry(window, width=20)
entry2 = ttk.Entry(window, width=20)
entry3 = ttk.Entry(window, width=10)
entry4 = ttk.Entry(window,width=10)
entry5 = ttk.Entry(window,width=10)



button = ttk.Button(window, text="Import Dataset", command = get_dataset)
button4 = ttk.Button(window, text="Delete Column", command = delete_columns)
button5 = ttk.Button(window, text="----->", command = create_Dummies)
button6 = ttk.Button(window, text="Print dataset", command = print_dummies)
button7 = ttk.Button(window, text="Export dataset", command = export_dataset)
button8 = ttk.Button(window, text="----->", command = create_bools)
button9 = ttk.Button(window, text="<-----", command = bool_to_dummy)
button10 = ttk.Button(window, text="----->", command = numerical_to_categorical)
button11 = ttk.Button(window, text="<-----", command = dummy_to_categorical)
button12 = ttk.Button(window, text="<-----", command = categorical_to_numerical)
button13 = ttk.Button(window, text="Rename", command = renameColumn
                    )
button14 = ttk.Button(window, text="Remove NAs", command = removeNAs)
button15 = ttk.Button(window, text="Change Dir.", command = changeDir)
button16 = ttk.Button(window, text="Binning", command = binning)



listbox = Listbox(window, width = 20, height = 15,  selectmode = SINGLE,fg='#414141')
listbox2 = Listbox(window, width = 20, height = 15, selectmode =  EXTENDED,fg='#414141')
listbox3 = Listbox(window, width = 20, height = 15, selectmode =  SINGLE,fg='#414141')
listbox4 = Listbox(window, width = 20, height = 15, selectmode =  SINGLE,fg='#414141')
listbox5 = Listbox(window, width = 20, height = 15, selectmode =  SINGLE,fg='#414141')




n = StringVar()
n.set("None")
rb = ttk.Radiobutton(window, text= "Standardize", value = "Standardize", variable = n)
#rb2 = ttk.Radiobutton(window, text= "Normalize", value = "Normalize", variable = n)
rb3 = ttk.Radiobutton(window, text= "None", value = "None", variable = n)

#### Grid ####

label1.grid(row = 1, column = 1)
entry.grid(row=2, column=1)
entry2.grid(row=15, column = 1)
entry3.grid(row=14, column = 5)
entry4.grid(row=14, column = 3)
entry5.grid(row=8, column = 2)


button.grid(row = 2, column = 2)
button4.grid(row = 6, column = 2)
button5.grid(row= 12, column= 4)
button7.grid(row=15, column=2)
button8.grid(row=12, column=5)
button9.grid(row=12, column=6)
button10.grid(row=12, column=3)
button11.grid(row=13, column=5)
button12.grid(row=13, column=4)
button13.grid(row=7, column=2)
button14.grid(row=9, column=2)
button15.grid(row=2, column=3)
button16.grid(row=13, column=3)


label6.grid(row = 2, column = 4)
label7.grid(row = 2,column = 5)
label11.grid(row = 2,column = 5, columnspan = 4)
label12.grid(row=14, column = 1)
#logo.grid(row =0, column = 4)

label5.grid(row=5, column = 1)

label8.grid(row=5, column = 3)
label9.grid(row=5, column =4)
label10.grid(row=5, column =5)
label13.grid(row=5, column = 6)

listbox.grid(row = 6, column = 1, rowspan = 6)
listbox2.grid(row = 6, column = 3, rowspan = 6)
listbox3.grid(row = 6, column = 4, rowspan = 6)
listbox4.grid(row = 6, column = 5, rowspan = 6)
listbox5.grid(row = 6, column = 6, rowspan = 6)

rb.grid(row =16, column=1)
#rb2.grid(row =15, column=0)
rb3.grid(row =18, column=1)


window.mainloop()