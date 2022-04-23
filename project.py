#FrontEnd

from doctest import master
from tkinter import *
import tkinter.messagebox
import projectbackend
import sqlite3
import datetime

 
class login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login in to GEMS Dubai International")
        self.root.config(bg="snow3")
        self.root.geometry("1350x720+0+0")

        Username = StringVar()
        Password = StringVar()
        def verify():
            if Username.get() == "User" and Password.get() == "root123":
                newMainFrame.destroy()
                StdID = StringVar()
                Firstname = StringVar()
                Lastname = StringVar()
                Dob = IntVar()
                Owncar = StringVar()
                # =============================================================Functions===============================================================
                def iExit():
                    iExit = tkinter.messagebox.askyesno("GEMS Dubai International School","Do you want to Exit the program?")
                    if iExit>0:
                        root.destroy()
                        return


                def Stdrec(event):
                    global sd
                    searchstd = studentlist.curselection()[0]
                    sd = studentlist.get(searchstd)


                def cleardata():
                    self.txtDob.delete(0, END)

                def addData():
                    if(len(StdID.get())!=0):
                        projectbackend.addStdRec(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() , Owncar.get() )
                        studentlist.delete(0,END)
                        studentlist.insert(END,(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() , Owncar.get()))

                def DisplayData():
                    studentlist.delete(0, END)
                    for row in projectbackend.Viewdata():
                        studentlist.insert(END,row,str(""))

                def deleteData():
                    # if(len(StdID.get())!=0):
                        projectbackend.deletRec(sd[0])
                        cleardata()
                        DisplayData()

                def Searchdatabase():
                    studentlist.delete(0,END)
                    for row in projectbackend.searchdata(StdID.get(), Firstname.get() , Lastname.get() , Dob.get(), Owncar.get()):
                        studentlist.insert(END, row, str(""))
                def UpdateDatabase():
                    if(len(StdID.get())!=0):
                        projectbackend.deletRec(sd[0])

                    if (len(StdID.get()) != 0):
                        projectbackend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Owncar.get())
                        studentlist.delete(0, END)
                        studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Owncar.get()))

                def FlowRate():
                    Wt=Dob.get()
                    con = sqlite3.connect("MYnewDatabase.db")
                    cur = con.cursor()
                    currentDateTime = datetime.datetime.now()
                    print(currentDateTime.date())
                    length=cur.execute("SELECT COUNT(ALL) from student WHERE Date = ?",(currentDateTime.date(),))
                    leng = cur.fetchone()
                    print(leng[0])
                    con.close()
                    FR = leng[0]/(Wt/60)
                    self.lblFna = Label(DataFrameBOTTOM, font=('arial', 20, 'bold'), text=FR, padx=2, pady=2, bg="aquamarine")
                    self.lblFna.grid(row=1, column=0, sticky=W)



                #=============================================================FRAMES===================================================================

                MainFrame = Frame(self.root, bg="snow3")
                MainFrame.grid()

                TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
                TitFrame.pack(side=TOP, padx=30, pady=30)


                self.lblTit = Label(TitFrame,font= ('arial',25,'bold'),text="GEMS Dubai International School", bg="snow")
                self.lblTit.grid()

                ButtonFrame = Frame(MainFrame, width=1200, height=90, padx=1, pady=1, bg="snow3" ,relief=RIDGE)
                ButtonFrame.pack(side=BOTTOM)

                DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=18, bg="snow3", relief=RIDGE)
                DataFrame.pack(side=BOTTOM)

                DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=500, padx=20, bg="aquamarine", relief=RIDGE,
                                           font=('arial',20,'bold'),text="Info\n")
                DataFrameLEFT.pack(side=LEFT)

                DataFrameRIGHTMAIN = Frame(DataFrame, bd=1, width=500, height=500, padx=20,bg="wheat", relief=RIDGE,)
                DataFrameRIGHTMAIN.pack(side=RIGHT)

                DataFrameRIGHT = LabelFrame(DataFrameRIGHTMAIN, bd=1, width=500, height=150, padx=2, bg="lightgoldenrod1", relief=RIDGE,
                                           font=('arial', 20, 'bold'), text="Details\n")
                DataFrameRIGHT.pack(side=TOP)

                DataFrameBOTTOM = LabelFrame(DataFrameRIGHTMAIN, bd=1, width=500, height=150, padx=2, bg="lightgreen", relief=RIDGE,
                                           font=('arial', 20, 'bold'), text="Flow Rate\n")
                DataFrameBOTTOM.pack(side=BOTTOM)

                # ========================================================Labels and Entry Widget===================================================================
                options = [
                "Front Gate",
                "Back Gate",
                ]
                options2 = [
                "6:40 - 7:00",
                "7:00 - 7:20",
                "7:20 - 7:40",
                "Past 7:40"
                ]
                options3 = [
                "yes",
                "no"
                ]
                Firstname.set("Select")
                Lastname.set("Select")
                Owncar.set("Select")


                self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Entry Gate: ", padx=2, pady=2, bg="aquamarine")
                self.lblFna.grid(row=1, column=0, sticky=W)
                self.txtFna = OptionMenu( DataFrameLEFT, Firstname, *options )
                self.txtFna.grid(row=1, column=1, padx=0, pady=30)
                # Radiobutton(DataFrameLEFT, text = "Front Gate", variable = Firstname,value = "Front Gate", indicator = 0, background = "light blue").grid(row=1, column=1, padx=0, pady=30)
                # Radiobutton(DataFrameLEFT, text = "Back Gate", variable = Firstname,value = "Back Gate", indicator = 0, background = "light blue").grid(row=2, column=1, padx=0, pady=30)


                self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Arrival Time at Entry Gate: ", padx=2, pady=2,
                                    bg="aquamarine")
                self.lblLna.grid(row=3, column=0, sticky=W)
                self.txtLna = OptionMenu( DataFrameLEFT, Lastname, *options2 )
                self.txtLna.grid(row=3, column=1, padx=80, pady=30)
                # self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=19)
                # self.txtLna.grid(row=3, column=1, padx=80, pady=30)

                self.lbloc = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Do you drive your own car?  ", padx=2, pady=2,
                                    bg="aquamarine")
                self.lbloc.grid(row=4, column=0, sticky=W)
                self.txtoc = OptionMenu( DataFrameLEFT, Owncar, *options3 )
                self.txtoc.grid(row=4, column=1, padx=80, pady=30)


                self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Waiting Time: ", padx=2, pady=2,
                                    bg="aquamarine")
                self.lblDob.grid(row=5, column=0, sticky=W)
                self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Dob, width=19)
                self.txtDob.grid(row=5, column=1, padx=80, pady=30)


                # self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mode Of Transport:", padx=1, pady=1, bg="aquamarine")
                # self.lblStdID.grid( row = 6, column = 0, sticky = W)
                Radiobutton(DataFrameLEFT, text = "Rental Vehicle", variable = StdID,value = "Rental Vehicle", indicator = 0,background = "white").grid(row=6, column=0, padx=0, pady=30)
                Radiobutton(DataFrameLEFT, text = "Personal Vehicle", variable = StdID,value = "Personal Vehicle", indicator = 0,background = "white").grid(row=6, column=1, padx=0, pady=30)
                # self.txtStdID = OptionMenu( DataFrameLEFT, StdID, *options )
                # # self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
                # self.txtStdID.grid(row=0, column=1, padx=0, pady=30)



                # ========================================================ScrollBar and ListBox===================================================================
                scrollbar = Scrollbar(DataFrameRIGHT)
                scrollbar.grid(row=0, column=1, sticky='ns')

                studentlist = Listbox(DataFrameRIGHT, width = 51 ,height = 15 , font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
                studentlist.bind('<<ListboxSelect>>',Stdrec)
                studentlist.grid(row=0, column=0, padx=8)
                scrollbar.config( command = studentlist.yview)

                # ========================================================Button Widget===================================================================
                self.btnAddData = Button(ButtonFrame, text="Add new", font= ('arial',12,'bold') , fg="white", bg="grey", width = 10 ,height = 1, bd=4, command = addData)
                self.btnAddData.grid(row=0, column=0, padx=10, pady=10)

                self.btnDispay = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command = DisplayData)
                self.btnDispay.grid(row=0, column=1, padx=10, pady=10)

                self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command=cleardata)
                self.btnClear.grid(row=0, column=2, padx=10, pady=10)

                self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command =deleteData)
                self.btnDelete.grid(row=0, column=3, padx=10, pady=10)

                self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), fg="white", bg="grey", width=10, height=1, bd=4 , command=iExit)
                self.btnExit.grid(row=0, column=6, padx=10, pady=10)

                self.btnExit = Button(ButtonFrame, text="Flow Rate", font=('arial', 12, 'bold'), fg="white", bg="grey", width=10, height=1, bd=4 , command=FlowRate)
                self.btnExit.grid(row=0, column=7, padx=10, pady=10)



        newMainFrame = Frame(self.root, bg="snow3")
        newMainFrame.grid()

        TitFrame = Frame(newMainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP, padx=30, pady=30)


        self.lblTit = Label(TitFrame,font= ('arial',25,'bold'),text="GEMS Dubai International School", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(newMainFrame, width=1200, height=90, padx=1, pady=1, bg="snow3" ,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(newMainFrame, bd=1, width=1300, height=400, padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=900, height=900, padx=350,pady=120,bg="aquamarine", relief=RIDGE,
                                           font=('arial',20,'bold'),text="Info\n")
        DataFrameLEFT.pack(side=TOP)


        self.lblUsr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Username: ", padx=2, pady=2,
                            bg="aquamarine")
        self.lblUsr.grid(row=1, column=0, sticky=W)
        self.txtusr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Username, width=19)
        self.txtusr.grid(row=1, column=1, padx=80, pady=30)


        self.lblPass = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Password: ", padx=2, pady=2,
                            bg="aquamarine")
        self.lblPass.grid(row=2, column=0, sticky=W)
        self.txtPass = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Password, width=19)
        self.txtPass.grid(row=2, column=1, padx=80, pady=30)

        self.btnLogin = Button(ButtonFrame, text="Login", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command =verify)
        self.btnLogin.grid(row=3, column=2, padx=10, pady=10)





# class Student:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("GEMS Dubai International School")
#         self.root.config(bg="snow3")
#         self.root.geometry("1350x720+0+0")

        # StdID = StringVar()
        # Firstname = StringVar()
        # Lastname = StringVar()
        # Dob = IntVar()
        # # =============================================================Functions===============================================================
        # def iExit():
        #     iExit = tkinter.messagebox.askyesno("GEMS Dubai International School","Do you want to Exit the program?")
        #     if iExit>0:
        #         root.destroy()
        #         return


        # def Stdrec(event):
        #     global sd
        #     searchstd = studentlist.curselection()[0]
        #     sd = studentlist.get(searchstd)


        # def cleardata():
        #     self.txtDob.delete(0, END)

        # def addData():
        #     if(len(StdID.get())!=0):
        #         projectbackend.addStdRec(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() )
        #         studentlist.delete(0,END)
        #         studentlist.insert(END,(StdID.get(), Firstname.get() , Lastname.get() , Dob.get()))

        # def DisplayData():
        #     studentlist.delete(0, END)
        #     for row in projectbackend.Viewdata():
        #         studentlist.insert(END,row,str(""))

        # def deleteData():
        #     if(len(StdID.get())!=0):
        #         projectbackend.deletRec(sd[0])
        #         cleardata()
        #         DisplayData()

        # def Searchdatabase():
        #     studentlist.delete(0,END)
        #     for row in projectbackend.searchdata(StdID.get(), Firstname.get() , Lastname.get() , Dob.get()):
        #         studentlist.insert(END, row, str(""))
        # def UpdateDatabase():
        #     if(len(StdID.get())!=0):
        #         projectbackend.deletRec(sd[0])

        #     if (len(StdID.get()) != 0):
        #         projectbackend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get())
        #         studentlist.delete(0, END)
        #         studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dob.get()))


        # #=============================================================FRAMES===================================================================

        # MainFrame = Frame(self.root, bg="snow3")
        # MainFrame.grid()

        # TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        # TitFrame.pack(side=TOP, padx=30, pady=30)


        # self.lblTit = Label(TitFrame,font= ('arial',25,'bold'),text="GEMS Dubai International School", bg="snow")
        # self.lblTit.grid()

        # ButtonFrame = Frame(MainFrame, width=1200, height=90, padx=1, pady=1, bg="snow3" ,relief=RIDGE)
        # ButtonFrame.pack(side=BOTTOM)

        # DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=18, bg="snow3", relief=RIDGE)
        # DataFrame.pack(side=BOTTOM)

        # DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=500, padx=20, bg="aquamarine", relief=RIDGE,
        #                            font=('arial',20,'bold'),text="Info\n")
        # DataFrameLEFT.pack(side=LEFT)

        # DataFrameRIGHTMAIN = Frame(DataFrame, bd=1, width=500, height=500, padx=20,bg="wheat", relief=RIDGE,)
        # DataFrameRIGHTMAIN.pack(side=RIGHT)

        # DataFrameRIGHT = LabelFrame(DataFrameRIGHTMAIN, bd=1, width=500, height=150, padx=2, bg="lightgoldenrod1", relief=RIDGE,
        #                            font=('arial', 20, 'bold'), text="Details\n")
        # DataFrameRIGHT.pack(side=TOP)

        # DataFrameBOTTOM = LabelFrame(DataFrameRIGHTMAIN, bd=1, width=500, height=150, padx=2, bg="lightgreen", relief=RIDGE,
        #                            font=('arial', 20, 'bold'), text="Flow Rate\n")
        # DataFrameBOTTOM.pack(side=BOTTOM)

        # # ========================================================Labels and Entry Widget===================================================================
        # options = [
        # "Front Gate",
        # "Back Gate",
        # ]
        # options2 = [
        # "6:40 - 7:00",
        # "7:00 - 7:20",
        # "7:20 - 7:40",
        # "Past 7:40"
        # ]
        # Firstname.set("Select")
        # Lastname.set("Select")
        

        # self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Entry Gate: ", padx=2, pady=2, bg="aquamarine")
        # self.lblFna.grid(row=1, column=0, sticky=W)
        # self.txtFna = OptionMenu( DataFrameLEFT, Firstname, *options )
        # self.txtFna.grid(row=1, column=1, padx=0, pady=30)
        # # Radiobutton(DataFrameLEFT, text = "Front Gate", variable = Firstname,value = "Front Gate", indicator = 0, background = "light blue").grid(row=1, column=1, padx=0, pady=30)
        # # Radiobutton(DataFrameLEFT, text = "Back Gate", variable = Firstname,value = "Back Gate", indicator = 0, background = "light blue").grid(row=2, column=1, padx=0, pady=30)


        # self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Arrival Time at Entry Gate: ", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblLna.grid(row=3, column=0, sticky=W)
        # self.txtLna = OptionMenu( DataFrameLEFT, Lastname, *options2 )
        # self.txtLna.grid(row=3, column=1, padx=80, pady=30)
        # # self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=19)
        # # self.txtLna.grid(row=3, column=1, padx=80, pady=30)


        # self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Waiting Time: ", padx=2, pady=2,
        #                     bg="aquamarine")
        # self.lblDob.grid(row=5, column=0, sticky=W)
        # self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Dob, width=19)
        # self.txtDob.grid(row=5, column=1, padx=80, pady=30)


        # # self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mode Of Transport:", padx=1, pady=1, bg="aquamarine")
        # # self.lblStdID.grid( row = 6, column = 0, sticky = W)
        # Radiobutton(DataFrameLEFT, text = "Rental Vehicle", variable = StdID,value = "Rental Vehicle", indicator = 0,background = "white").grid(row=6, column=0, padx=0, pady=30)
        # Radiobutton(DataFrameLEFT, text = "Personal Vehicle", variable = StdID,value = "Personal Vehicle", indicator = 0,background = "white").grid(row=6, column=1, padx=0, pady=30)
        # # self.txtStdID = OptionMenu( DataFrameLEFT, StdID, *options )
        # # # self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        # # self.txtStdID.grid(row=0, column=1, padx=0, pady=30)


        
        # # ========================================================ScrollBar and ListBox===================================================================
        # scrollbar = Scrollbar(DataFrameRIGHT)
        # scrollbar.grid(row=0, column=1, sticky='ns')

        # studentlist = Listbox(DataFrameRIGHT, width = 51 ,height = 15 , font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        # studentlist.bind('<<ListboxSelect>>',Stdrec)
        # studentlist.grid(row=0, column=0, padx=8)
        # scrollbar.config( command = studentlist.yview)

        # # ========================================================Button Widget===================================================================
        # self.btnAddData = Button(ButtonFrame, text="Add new", font= ('arial',12,'bold') , fg="white", bg="grey", width = 10 ,height = 1, bd=4, command = addData)
        # self.btnAddData.grid(row=0, column=0, padx=10, pady=10)

        # self.btnDispay = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command = DisplayData)
        # self.btnDispay.grid(row=0, column=1, padx=10, pady=10)

        # self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command=cleardata)
        # self.btnClear.grid(row=0, column=2, padx=10, pady=10)

        # self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command =deleteData)
        # self.btnDelete.grid(row=0, column=3, padx=10, pady=10)

        # self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), fg="white", bg="grey", width=10, height=1, bd=4 , command=iExit)
        # self.btnExit.grid(row=0, column=6, padx=10, pady=10)


if __name__ =='__main__':
    root = Tk()

    application = login(root)
    root.mainloop()







