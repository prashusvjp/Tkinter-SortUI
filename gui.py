from tkinter import *
import datetime
import time
import algorithms as sort


results = []
outputCanvas=outputFrame=inputTextBox=sortSelection=orderSelection=background= None
outputVScrollBar = None
sortAlgorithms = ['Tim Sort(Python default)','Bubble Sort','Insertion Sort','Selection Sort','Merge Sort','Quick Sort']
sortOrder = ['Ascending','Descending']

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def reset():
    global sortSelection,inputTextBox,orderSelection 
    sortSelection.set(0)
    orderSelection.set(0)
    inputTextBox.delete(0,'end')
    clearOutput()

def clearOutput():
    global outputFrame
    global results
    try:
        results = []
        outputFrame.destroy()
    except BaseException:
        print('hello')

def onAboutClick():
    about = Tk()
    about.title('About')
    about.resizable(False,False)
    headingLabel = Label(about,fg='black',
    text='PES University\nDepartment of Computer Science\n',
    font=('Calibri bold',15))
    headingLabel.pack(fill=BOTH,side=TOP,padx=10,pady=10)
    label1=Label(about, text='\n3rd Semester, Python assignment:Sort Test\n\nDeveloped by:\nPavankumar Hegde (PES1UG20CS823)\nPrashanth S (PES1UG20CS824)',
    font=('Calibri bold',10),justify=LEFT)
    label1.pack(fill=BOTH,side=TOP,padx=10,pady=10,anchor='w')

def onHelpClick():
    helpScreen =Tk()
    helpScreen.title('Help')
    helpScreen.resizable(False,False)
    headingLabel = Label(helpScreen,fg='black',
    text='PES University\nDepartment of Computer Science\nSort test',
    font=('Calibri bold',15))
    headingLabel.pack(fill=BOTH,side=TOP,padx=10,pady=10,expand=1)
    label1=Label(helpScreen, text='\nThis application allows users to play around with many algorithms or techniques for sorting an array\n\n'+
    'The sorting algorithms available in this application are:\nBubble sort\nInsertion sort\nSelection sort'+
    '\nMerge sort\nQuick sort\nTimsort(Default sorting technique used in python)\n\nInstructions:\n'+
    "Please enter the values in the textbox seperated with a comma ','\nSelect the required order in which the values needs to be sorted\n"+
    "Select the sorting technique that you prefer, and press 'Sort' button.\n"+"The 'All' option is to choose all the algorithms at once\n"+
    "The result will be availbale in the output frame\n"+
    "The application is developed in a robust way, wherein if the values entered in the textbox are numbers,\n they are analyzed and converted to Integer or Float"+
    " instead of considering it as a string of values.\nTo consider a string of numbers to be a string and sort alphabettically, just add a ',' at the end of the input line\n"+
    "Time taken for a sorting technique to finish its task is also recorded."+
    " The time may not be required for small array lengths,\n however there will be difference in time depending upon the number of values entered.\n",
    font=('Calibri',10),justify=LEFT)
    label1.pack(fill=BOTH,side=TOP,padx=10,pady=10,anchor='w',expand=1)

def sortValues(array,algo=0,order=0):
    startTime=datetime.datetime.now()
    if algo==0:
        if order==0:
            array.sort()
            result = array
        else:
            array.sort(reverse=True)
            result = array
    if algo==1:
        if order==0:
            result = sort.bubbleSortAsc(array)
        else:
            result = sort.bubbleSortDsc(array)
    elif algo==2:
        if order==0:
            result = sort.insertionSortAsc(array)
        else:
            result = sort.insertionSortDsc(array)
    elif algo==3:
        if order==0:
            result = sort.selectionSotAsc(array)
        else:
            result = sort.selectionSortDsc(array)
    elif algo==4:
        if order==0:
            result = sort.mergeSortAsc(array)
        else:
            result = sort.mergeSortDsc(array)
    elif algo==5:
        if order==0:
            result = sort.quickSortAsc(array)
        else:
            result = sort.quickSortDsc(array)
    elif algo==6:
        for i in range(algo):
            sortValues(array,i,order)
        return

    endTime=datetime.datetime.now()
    timeTaken=int(endTime.strftime('%f')) - int(startTime.strftime('%f'))
    outMessage ='\n'+ sortAlgorithms[algo] +', Order: ' + sortOrder[order] + '\t\t\t\tTime: '+str(timeTaken)+'ms\nResult: ' + str(result) +'\n'
    results.append(outMessage)

    global outputFrame
    try:
        outputFrame.destroy()
    except BaseException:
        print("hello")

    outputFrame = Frame(primaryOutputFrame,background='white')
    outputFrame.pack(fill=BOTH,expand=1,side=LEFT)

    outputCanvas = Canvas(outputFrame)
    outputCanvas.pack(fill=BOTH,expand=1,side=LEFT)

    outputVScrollBar = Scrollbar(outputFrame,orient='vertical',command=outputCanvas.yview)
    outputVScrollBar.pack(side=RIGHT,fill=Y)
    outputCanvas.configure(yscrollcommand=outputVScrollBar.set)
    outputCanvas.bind('<Configure>',lambda e: outputCanvas.configure(scrollregion=outputCanvas.bbox('all')))

    secondaryFrame=Frame(outputCanvas)

    outputCanvas.create_window((0,0),window=secondaryFrame,anchor='nw')

    for i in results:
        outputText = Label(secondaryFrame,text=i,font=('Calibri',10),justify=LEFT)
        outputText.pack(fill=X,anchor='w',padx=5)
    



def onSortClick(values,algo=0,order=0):

    areFloat=areInt = False
    array = []
    values= values.strip()
    values = values.split(',')

    for i in values:
        if i.isdigit():
            areInt = True
        elif isFloat(i):
            areFloat = True
        else :
            areFloat=areInt= False 
            break
    
    if areFloat:
        for i in values:
           array.append(float(i))  
    elif areInt:
        for i in values:
           array.append(int(i))  
    else:
        array = values

    sortValues(array,algo,order)


home = Tk()
home.title('Sort Test')

#Menu Bar
menuBar = Menu(home)
optionsMenu = Menu(menuBar,tearoff=0)
optionsMenu.add_command(label='Clear Output',command=clearOutput)
optionsMenu.add_command(label='Reset',command=reset)
optionsMenu.add_separator()
optionsMenu.add_command(label='Exit',command=quit)
menuBar.add_cascade(label='Options',menu=optionsMenu)
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label='Help',command=onHelpClick)
helpMenu.add_command(label='About',command=onAboutClick)
menuBar.add_cascade(label='Help',menu=helpMenu)
home.config(menu=menuBar)

#Background Image
img = PhotoImage(file='F:/Workspace/Project 2021/Python/Sort Test/background.png')
background = Label(home,image=img)
background.pack()




#frame for input
inputFrame = LabelFrame(background,background='white',padx=20,pady=20)
inputFrame.place(relwidth=0.8,relheight=0.6,relx=0.1,rely=0.02)

#Labels
label1 = Label(inputFrame,text="Sort Test",background='white',font=('Calibri bold',17),justify=LEFT)
label1.pack(side=TOP,anchor='w')

label2 = Label(inputFrame,text="Instructions:"
,background='white',font=('Calibri bold',12),justify=LEFT)
label2.pack(side=TOP,anchor='w',pady=10)

label3 = Label(inputFrame,text="1)Enter values seperated by a comma ','"+
"\n2)Select the order of sorting\n3)Select any of the sorting algorithm\n\nEnter the values:"
,background='white',font=('Calibri',10),justify=LEFT)
label3.pack(side=TOP,anchor='w',)

#TextBox
inputTextBox = Entry(inputFrame,width=100,font=('Calibri',10))
inputTextBox.pack(anchor='w')

#Order seletion
orderSelection=IntVar()
orderSelection.set(0)
Radiobutton(inputFrame,value=0,text='Ascending',
variable=orderSelection,background='white',font=('Calibri',10)).pack(anchor='w')
Radiobutton(inputFrame,value=1,
text='Descending',variable=orderSelection,background='white',font=('Calibri',10)).pack(anchor='w')

label4 = Label(inputFrame,text="\nSelect a sorting algorithm:"
,background='white',font=('Calibri',10),justify=LEFT)
label4.pack(side=TOP,anchor='w',)

sortSelectionFrame = Frame(inputFrame,background='white',)
sortSelectionFrame.pack(anchor='w')

#Sort Selection
sortSelection = IntVar()
sortSelection.set(0)
Radiobutton(sortSelectionFrame,value=0,
text='Tim Sort(Python default)',variable=sortSelection,background='white',font=('Calibri',10),padx=5).grid(row=0,column=0)
Radiobutton(sortSelectionFrame,value=1,
text='Bubble Sort',variable=sortSelection,background='white',font=('Calibri',10),padx=5).grid(row=0,column=1)
Radiobutton(sortSelectionFrame,value=2,
text='Insertion Sort',variable=sortSelection,background='white',font=('Calibri',10)).grid(row=0,column=2)
Radiobutton(sortSelectionFrame,value=3,
text='Selection Sort',variable=sortSelection,background='white',font=('Calibri',10)).grid(row=0,column=3)
Radiobutton(sortSelectionFrame,value=4,
text='Merge Sort',variable=sortSelection,background='white',font=('Calibri',10)).grid(row=0,column=4)
Radiobutton(sortSelectionFrame,value=5,
text='Quick sort',variable=sortSelection,background='white',font=('Calibri',10)).grid(row=0,column=5)
Radiobutton(sortSelectionFrame,value=6,
text='All',variable=sortSelection,background='white',font=('Calibri',10)).grid(row=0,column=6)


#Output Frame
primaryOutputFrame = LabelFrame(background,text='Output',background='white')
primaryOutputFrame.place(relwidth=0.8,relheight=0.3,relx=0.1,rely=0.65)

sortButton = Button(inputFrame,background='black',fg='white',text='Sort',padx=40,
command=lambda : onSortClick(inputTextBox.get(),sortSelection.get(),orderSelection.get()))
sortButton.pack(anchor='w',pady=10)

home.mainloop()