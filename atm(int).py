from tkinter import *  # type: ignore
from tkinter import messagebox
import random
from PIL import ImageTk, Image


credentials = {
    "Jay":"1224",
    "Garri":"1345",
    "Thanos":"1234",
    "Unnamed":"2245",
    "Santa":"2345",
    "z":"z"
}

accounts = {
    "Jay":"0000001",
    "Garri":"0000002",
    "Thanos":"0000003",
    "Unnamed":"0000004",
    "Santa":"0000005",
    "z":"0000006"
}

amounts = {
    "Jay":"5450000",
    "Garri":"2342000",
    "Thanos":"345500",
    "Unnamed":"430000",
    "Santa":"995000",
    "z":"925000"
}

icol = {
    "Jay":"5450000",
    "Garri":"2342000",
    "Thanos":"345500",
    "Unnamed":"430000",
    "Santa":"995000",
    "z":"925000"
}

emails = {
    "Jay":"jaymono@gmail.com",
    "Garri":"hardgarri@eba.com",
    "Thanos":"Buchukwu@hypa.com",
    "Unnamed":"baijo@slimfit.com",
    "Santa":"hayo@hfactor.com",
    "z":"z@z.com"
}


Allowed = "1234567890"


def logpage():
    new = Tk()
    root.destroy()

    new.geometry("1000x680")
    new.title(f"Welcome, {name.get()}")
    new.resizable(False,False)
    new.config(bg="black")

    labels = Label(new, text=f"Welcome {name.get()}", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
    labels.pack()

    labels = Label(new, text=f"{accounts[name.get()]}", width=15, font=("arial", 20, "bold"),  bg="black", fg="red")
    labels.place(x=350, y=100)

    labels = Label(new, text="Choose an action", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
    labels.place(x=300, y=150) 


    def check():
        order = name.get()
        box = Tk()
        box.overrideredirect()
        box.withdraw()
        messagebox.showinfo("Balance", f"Account Balance: ${amounts.get(order)}")
        box.destroy()

        
    def loan():

        user = name.get()
        amt = int(amounts[user])
        allowed = amt * 0.1

        l = Tk()

        l.geometry("1000x500")
        l.title(f"Take a loan")
        l.resizable(False,False)
        l.config(bg="black")

        labels = Label(l, text="Input amount", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
        labels.place(x=300, y=150) 

        labels = Label(l, text=f"MAX: ${allowed}", width=15, font=("arial", 15, "bold"),  bg="black", fg="red")
        labels.place(x=400, y=200)

        labels = Label(l, text="Take a Loan", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
        labels.pack()

        num=IntVar()
        Entry(width=15, font=("arial", 28), textvariable=num, bd=0, border=2).place(x=320, y=230)
        
        labels = Label(l, text="Enter Passkey", width=15, font=("arial", 30, "bold"),  bg="black", fg="red").place(x=320, y=300)

        nums=StringVar()
        Entry(width=15, font=("arial", 28), textvariable=nums, bd=0, border=2, show="*").place(x=320, y=350)

        def doit():
            ask = num.get()
            pin = (nums.get())
            user = name.get()
            otherd = int(icol[user]) * 1.15
            amt = int(amounts[user])
            allowed = amt * 0.1
            maxes = amt + ask

            if pin == credentials[user]:
                if maxes < (otherd):
                    if ask <= allowed:
                        amt += ask
                        amounts[user] = str(amt)

                        box = Tk()
                        box.overrideredirect()
                        box.withdraw()
                        messagebox.showinfo("Take a Loan", f"Loan Successful")
                        box.destroy()    

                        l.destroy()

                    else:
                        box = Tk()
                        box.overrideredirect()
                        box.withdraw()
                        messagebox.showinfo("Loan Error", f"amount exceeds allowable loan")
                        box.destroy() 

                        l.destroy()
                
                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Loan Error", f"Repay some of the debt you owe")
                    box.destroy() 

                    l.destroy()
            
            else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Error", f"Wrong Passkey")
                    box.destroy() 

                    l.destroy()          

        
        Button(l, width=20, text="Take Loan", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=doit).place(x=280 ,y=420)


    def withdraw():
        
        a = Tk()

        a.geometry("1000x600")
        a.title(f"Welcome, {name.get()}")
        a.resizable(False,False)
        a.config(bg="black")

        labels = Label(a, text="WITHDRAWAL", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
        labels.pack()

        labels = Label(a, text="Choose an amount", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
        labels.place(x=300, y=150) 

        def five_h():
            order = name.get()
            if int(amounts[order]) >= 500:
                amt = int(amounts.get(order)) # type: ignore
                new_amt = amt - 500
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()
            
            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()


        def one_k():
            order = name.get()
            if int(amounts[order]) >= 1000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 1000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()

            
            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()

        def two_k():
            order = name.get()
            if int(amounts[order]) >= 2000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 2000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()
            
            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()

        def five_k():
            order = name.get()
            if int(amounts[order]) >= 5000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 5000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()
            
            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()
                
                a.destroy()

        def ten_k():
            order = name.get()
            if int(amounts[order]) >= 10000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 10000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()

            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()

        def fifteen_k():
            order = name.get()
            if int(amounts[order]) >= 15000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 15000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()

            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()

        def twenty_k():
            order = name.get()
            if int(amounts[order]) >= 20000:
                amt = int(amounts.get(order))  # type: ignore
                new_amt = amt - 20000
                amounts[order] = str(new_amt)

                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Successful","Withdrawal Complete")
                box.destroy() 

                a.destroy()
            
            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo(f"Error","Insufficient Funds!!!")
                box.destroy()

                a.destroy()

        def other():
            a.destroy()
            other = Tk()
            other.geometry("1000x400")
            other.title(f"Welcome, {name.get()}")
            other.resizable(False,False)
            other.config(bg="black")

            labels = Label(other, text="WITHDRAWAL", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(other, text="Input amount", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100) 

            num=IntVar()
            Entry(other, width=15, font=("arial", 28), textvariable=num, bd=0, border=2).place(x=320, y=230)

            def others():
                a = num.get()
                order = name.get()
                if a <= int(amounts[order]):
                    amt = amounts.get(order)
                    new_amt = int(amt) - a  # type: ignore
                    amounts[order] = str(new_amt)

                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo(f"Successful","Withdrawal Complete")
                    box.destroy() 

                    other.destroy()

                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                    box.destroy()

                    other.destroy()
            
            
            Button(other, width=20, text="Withdraw", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=others).place(x=280 ,y=300)


        Button(a, width=20, text="500", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=five_h).place(x=20 ,y=230)
        Button(a, width=20, text="1000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=one_k).place(x=20 ,y=320)
        Button(a, width=20, text="2000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=two_k).place(x=20 ,y=410)
        Button(a, width=20, text="10000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=ten_k).place(x=550 ,y=230)
        Button(a, width=20, text="15000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=fifteen_k).place(x=550 ,y=320)
        Button(a, width=20, text="20000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=twenty_k).place(x=550 ,y=410)
        Button(a, width=20, text="5000", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=five_k).place(x=20 ,y=500)
        Button(a, width=20, text="Other Amount", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=other).place(x=550 ,y=500)


    def change():
            users = name.get()
            change = Tk()
            change.geometry("1000x500")
            change.title(f"Welcome, {name.get()}")
            change.resizable(False,False)
            change.config(bg="black")

            labels = Label(change, text="Change Pin", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(change, text="Input old pin", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100)

            nums=StringVar()
            Entry(width=15, font=("arial", 28), textvariable=nums, bd=0, border=2, show="*").place(x=320, y=180)

            labels = Label(change, text="Input new pin", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=260)

            num=StringVar()
            Entry(width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=340)       
            

            def do():
                olds = nums.get()

                if olds == credentials[users]:
                    pins = num.get()
                    credentials[users] = str(pins)

                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Change Pin", f"Pin Changed Successfully")
                    box.destroy()

                    change.destroy()
                
                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Change Pin Error", f"Please input the correct old pin")
                    box.destroy()     


                    change.destroy()         
            

            Button(change, width=20, text="Change Pin", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=do).place(x=280 ,y=420)
   

    def transfer():
            users = name.get()
            tran = Tk()
            tran.geometry("1000x500")
            tran.title(f"Welcome, {name.get()}")
            tran.resizable(False,False)
            tran.config(bg="black")

            labels = Label(tran, text="transfer", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(tran, text="Destination Account", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100)

            nums=StringVar()
            Entry(width=15, font=("arial", 28), textvariable=nums, bd=0, border=2).place(x=320, y=180)

            labels = Label(tran, text="Input Amount", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=260)

            num=IntVar()
            Entry(width=15, font=("arial", 28), textvariable=num, bd=0, border=2).place(x=320, y=340)       
            
            def proceed():
                userb=nums.get()
                for i in accounts:
                    if accounts[i] == userb:
                        userb_name = i
                        break
                    else:
                        userb_name = userb

                if userb_name in credentials:     # type: ignore
                    if userb_name != users:     # type: ignore
                        tran.destroy()
                        tr= Tk()
                        tr.geometry("1000x360")
                        tr.title(f" ")
                        tr.resizable(False,False)
                        tr.config(bg="black")  

                        labels = Label(tr, text=f"reciever: {userb_name}", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")   # type: ignore
                        labels.pack()

                        labels = Label(tr, text="Enter Passkey", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        numu=StringVar()
                        Entry(tr, width=15, font=("arial", 28), textvariable=numu, bd=0, border=2, show="*").place(x=320, y=200)

                        def conf():
                            trial=numu.get()
                            req=num.get()

                            if req <= int(amounts[users]):
                                if trial == credentials[users]:
                                    amta = int(amounts[users])
                                    amtb = int(amounts[userb_name])    # type: ignore
                                    amta -= req
                                    amtb += req

                                    amounts[users] = str(amta)
                                    amounts[userb_name] = str(amtb)    # type: ignore

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Transfer Complete")
                                    box.destroy() 

                                    tr.destroy()  

                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Wrong passkey")
                                    box.destroy() 

                                    tr.destroy()
                            
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","You don't have enough money")
                                box.destroy() 

                                tr.destroy()                               


                        Button(tr, width=20, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=conf).place(x=280 ,y=280)

                    else: 
                        box = Tk()
                        box.overrideredirect()
                        box.withdraw()
                        messagebox.showinfo("Error", f"Did you just try to transfer money to yourself?\nBloddy Idiot")
                        box.destroy()                           


                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Error", f"Account number inaccurate\nNo warning next time... Your Money will just vanish\n\n\nJust know that there is no bank branch to run to")
                    box.destroy()                       


            Button(tran, width=20, text="Proceed", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=proceed).place(x=280 ,y=420)
 

    def logout():
        new.destroy()
    

    def terminate():
        state = Tk()
        state.geometry("600x280")
        state.title(f"Account Termination")
        state.resizable(False,False)
        state.config(bg="black")

        labels = Label(state, text="Terminate Account", width=15, font=("arial", 35, "bold"),  bg="black", fg="red")
        labels.pack()

        labels = Label(state, text="Input Passkey", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
        labels.place(x=140, y=80)

        num=StringVar()
        Entry(width=15, font=("arial", 28), textvariable=num, bd=0, border=2,show="*").place(x=150, y=150) 

        def term():
            user = name.get()
            fine=num.get()
            if fine == credentials[user]:
                last = Tk()
                
                last.geometry("500x280")
                last.title(f"Account Statement")
                last.resizable(False,False)
                last.config(bg="black")

                labels = Label(last, text="Are You Sure", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                labels.pack()

                def yes():
                    credentials.pop(user)
                    amounts.pop(user)
                    accounts.pop(user)
                    icol.pop(user)
                    emails.pop(user)

                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Termination Notice", "Your Account has been Terminated\n Thank you for Banking with us")
                    box.destroy()
                    
                    last.destroy()
                    new.destroy()
                    state.destroy()
                    

                def no():
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Termination cancelled", "You came so far\nOnly to turn tail like the Bitch you are\nGood to know we own you")
                    box.destroy()
                    last.destroy()   

                Button(last, width=9, text="YES", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=yes).place(x=20 ,y=160)
                Button(last, width=9, text="NO", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=no).place(x=270 ,y=160)


            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo("Termination Error", "Wrong passkey\nImagine failing suicide")
                box.destroy()
                state.destroy()
                

        Button(state, width=12, text="Terminate", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=term).place(x=185 ,y=210)


    def statement():
        state = Tk()
        state.geometry("1000x400")
        state.title(f"Account Statement")
        state.resizable(False,False)
        state.config(bg="black")

        labels = Label(state, text="Account Statement", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
        labels.pack()

        labels = Label(state, text="Input Email", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
        labels.place(x=300, y=100)

        num=StringVar()
        Entry(width=15, font=("arial", 28), textvariable=num, bd=0, border=2).place(x=320, y=230) 

        def does():
            users = name.get()
            email = emails[users]    
            mail = num.get()
            number = accounts[users]

            if email == mail:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo("Account Statement", f"Statement for account: {number} Will Be Sent To {mail} shortly")
                box.destroy() 

                state.destroy()

            else:
                box = Tk()
                box.overrideredirect()
                box.withdraw()
                messagebox.showinfo("Account Statement", f"Wrong Email Address Provided")
                box.destroy()         

                state.destroy()       

        Button(state, width=20, text="Send Statement", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=does).place(x=280 ,y=300)

    def quickteller():
        qt = Tk()

        qt.geometry("1000x360")
        qt.title(f"Quick Teller")
        qt.resizable(False,False)
        qt.config(bg="black")

        labels = Label(qt, text=f"Quick Teller", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
        labels.pack()

        labels = Label(qt, text="Choose an action", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
        labels.place(x=300, y=100) 

        def safe():
            qt.destroy()
            safe = Tk()
        
            safe.geometry("1000x360")
            safe.title(f"Quick Teller")
            safe.resizable(False,False)
            safe.config(bg="black")   

            labels = Label(safe, text=f"Generate OTP", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(safe, text="Enter Passkey", width=15, font=("arial", 30, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100) 

            num=StringVar()
            Entry(safe, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=200) 

            def safer():
                gim = num.get()
                user = name.get()

                if gim == credentials[user]:
                    import random  #important                           #not that difficult though
                    length = 4
                    Pass = "".join(random.sample(Allowed,length))

                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Generate OTP", f"Your OTP is {Pass}\nDo Not Share This OTP with anyone")
                    box.destroy()    

                    safe.destroy()

                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Passkey Error", f"Password provided is wrong")
                    box.destroy()    

                    safe.destroy() 

            Button(safe, width=20, text="Generate", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=safer).place(x=280 ,y=280)


        def airtime():
            qt.destroy()
            safe = Tk()
        
            safe.geometry("1000x430")
            safe.title(f"Quick Teller")
            safe.resizable(False,False)
            safe.config(bg="black")   

            labels = Label(safe, text=f"Buy Airtime", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(safe, text="Phone Number", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100) 

            phone=StringVar()
            Entry(safe, width=15, font=("arial", 28), textvariable=phone, bd=0, border=2).place(x=320, y=150) 

            labels = Label(safe, text="Enter Amount", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=220) 

            amount=StringVar()
            Entry(safe, width=15, font=("arial", 28), textvariable=amount, bd=0, border=2).place(x=320, y=270) 


            def buyit():
                ph = (phone.get())

                if len(ph) == 11:
                    safe.destroy()
                    safer = Tk()
            
                    safer.geometry("1000x360")
                    safer.title(f"Quick Teller")
                    safer.resizable(False,False)
                    safer.config(bg="black")   

                    labels = Label(safer, text=f"Buy Airtime", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                    labels.pack()

                    labels = Label(safer, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                    labels.place(x=300, y=100) 

                    num=StringVar()
                    Entry(safer, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Error", f"You have Entered a wrong phone number")
                    box.destroy() 


                def right():
                    ph = int(phone.get())
                    want = int(amount.get())
                    order = name.get()
                    pin = num.get()

                    if pin == (credentials[order]):
                        if want <= int(amounts[order]):
                            amt = amounts.get(order)
                            new_amt = int(amt) - want  # type: ignore
                            amounts[order] = str(new_amt)

                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Purchase Successful", f"Purchase Successful ")
                            box.destroy() 

                        else:
                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Purchase Unsuccessful", f"INSUFFICIENT FUNDS")
                            box.destroy()

                    else:
                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Error", f"You have entered the wrong passkey")
                            box.destroy()

                    safer.destroy()

                Button(safer, width=20, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=right).place(x=280 ,y=280)


            Button(safe, width=20, text="Proceed", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=buyit).place(x=280 ,y=350)


        def dstv():
            qt.destroy()
            safe = Tk()
        
            safe.geometry("1000x300")
            safe.title(f"Quick Teller")
            safe.resizable(False,False)
            safe.config(bg="black")   

            labels = Label(safe, text=f"Subscribe to DSTV", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(safe, text="Smartcard Number", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100) 

            phone=StringVar()
            Entry(safe, width=18, font=("arial", 28), textvariable=phone, bd=0, border=2).place(x=300, y=150) 

            def buyit():
                ph = (phone.get())

                if len(ph) == 16:
                    safe.destroy()
                    safer = Tk()
            
                    safer.geometry("1000x550")
                    safer.title(f"Quick Teller")
                    safer.resizable(False,False)
                    safer.config(bg="black")   

                    labels = Label(safer, text=f"Subscribe to Dstv", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                    labels.pack()

                    labels = Label(safer, text="Choose Plan", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                    labels.place(x=300, y=100) 
                    

                    def padi():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Padi", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 2500:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 2500
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                                    
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()

                                
                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)

                    def yanga():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Yanga", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 3500:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 3500
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                                 
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()

                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)                    

                    def confam():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Confam", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 6200:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 6200
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                              
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()


                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)

                    def comp():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Compact", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 10500:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 10500
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                                   
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()


                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)

                    def compP():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Compact Plus", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 


                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 16600:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 16600
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                                   
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()


                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)

                    def prem():
                        safer.destroy()
                        safes = Tk()
                
                        safes.geometry("1000x360")
                        safes.title(f"Quick Teller")
                        safes.resizable(False,False)
                        safes.config(bg="black")   

                        labels = Label(safes, text=f"Dstv Premium", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                        labels.pack()

                        labels = Label(safes, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                        labels.place(x=300, y=100) 

                        num=StringVar()
                        Entry(safes, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                        def final():
                            order = name.get()
                            pin = num.get()

                            if pin == credentials[order]:
                                if int(amounts[order]) >= 24500:
                                    amt = int(amounts.get(order))  # type: ignore
                                    new_amt = amt - 24500
                                    amounts[order] = str(new_amt)

                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Successful","Subscription Successful")
                                    box.destroy() 

                                                                   
                                else:
                                    box = Tk()
                                    box.overrideredirect()
                                    box.withdraw()
                                    messagebox.showinfo(f"Error","Insufficient Funds!!!")
                                    box.destroy()
                                
                            else:
                                box = Tk()
                                box.overrideredirect()
                                box.withdraw()
                                messagebox.showinfo(f"Error","Wrong Passkey")
                                box.destroy()

                            safes.destroy()


                        Button(safes, width=17, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=final).place(x=320 ,y=230)

                    Button(safer, width=17, text="Dstv Padi \n $2500", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=padi).place(x=80 ,y=160)
                    Button(safer, width=17, text="Dstv Yanga \n $3500", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=yanga).place(x=80 ,y=280)
                    Button(safer, width=17, text="Dstv Confam \n $6200", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=confam).place(x=80 ,y=400)
                    Button(safer, width=17, text="Dstv Compact \n $10500", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=comp).place(x=550 ,y=160)
                    Button(safer, width=17, text="Dstv Compact Plus \n $16600", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=compP).place(x=550 ,y=280)
                    Button(safer, width=17, text="Dstv Premium \n $24500", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=prem).place(x=550 ,y=400)


                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Error", f"You have Entered a DSTV Smartcard Number")
                    box.destroy() 


            Button(safe, width=20, text="Proceed", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=buyit).place(x=280 ,y=220)


        def bet():
            qt.destroy()
            safe = Tk()
        
            safe.geometry("1000x430")
            safe.title(f"Quick Teller")
            safe.resizable(False,False)
            safe.config(bg="black")   

            labels = Label(safe, text=f"Transfer to your bet9ja account", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
            labels.pack()

            labels = Label(safe, text="Account Number", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=100) 

            phone=StringVar()
            Entry(safe, width=15, font=("arial", 28), textvariable=phone, bd=0, border=2).place(x=320, y=150) 

            labels = Label(safe, text="Enter Amount", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
            labels.place(x=300, y=220) 

            amount=StringVar()
            Entry(safe, width=15, font=("arial", 28), textvariable=amount, bd=0, border=2).place(x=320, y=270) 


            def buyit():
                ph = (phone.get())

                if len(ph) == 10:
                    safe.destroy()
                    safer = Tk()
            
                    safer.geometry("1000x360")
                    safer.title(f"Quick Teller")
                    safer.resizable(False,False)
                    safer.config(bg="black")   

                    labels = Label(safer, text=f"Transfer", width=15, font=("arial", 50, "bold"),  bg="black", fg="red")
                    labels.pack()

                    labels = Label(safer, text="Enter Passkey", width=15, font=("arial", 28, "bold"),  bg="black", fg="red")
                    labels.place(x=300, y=100) 

                    num=StringVar()
                    Entry(safer, width=15, font=("arial", 28), textvariable=num, bd=0, border=2, show="*").place(x=320, y=150) 

                else:
                    box = Tk()
                    box.overrideredirect()
                    box.withdraw()
                    messagebox.showinfo("Error", f"You have Entered a wrong account number")
                    box.destroy() 


                def right():
                    ph = int(phone.get())
                    want = int(amount.get())
                    order = name.get()
                    pin = num.get()

                    if pin == (credentials[order]):
                        if want <= int(amounts[order]):
                            amt = amounts.get(order)
                            new_amt = int(amt) - want  # type: ignore
                            amounts[order] = str(new_amt)

                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Transfer Successful", f"Transfer Successful ")
                            box.destroy() 

                        else:
                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Purchase Unsuccessful", f"INSUFFICIENT FUNDS")
                            box.destroy()

                    else:
                            box = Tk()
                            box.overrideredirect()
                            box.withdraw()
                            messagebox.showinfo("Error", f"You have entered the wrong passkey")
                            box.destroy()

                    safer.destroy()

                Button(safer, width=20, text="Confirm", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=right).place(x=280 ,y=280)


            Button(safe, width=20, text="Proceed", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=buyit).place(x=280 ,y=350)


        Button(qt, width=20, text="Airtime", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=airtime).place(x=20 ,y=180)
        Button(qt, width=20, text="Dstv", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=dstv).place(x=20 ,y=280)
        Button(qt, width=20, text="Safe Tokens", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=safe).place(x=550 ,y=180)
        Button(qt, width=20, text="Bet9ja", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=bet).place(x=550 ,y=280)
        

    Button(new, width=20, text="Check Balance", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=check).place(x=20 ,y=230)
    Button(new, width=20, text="Withdrawal", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=withdraw).place(x=20 ,y=320)
    Button(new, width=20, text="Transfer", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=transfer).place(x=20 ,y=410)
    Button(new, width=20, text="Change Pin", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=change).place(x=550 ,y=230)
    Button(new, width=20, text="Quickteller", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=quickteller).place(x=550 ,y=320)
    Button(new, width=20, text="Account Statement", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=statement).place(x=550 ,y=410)
    Button(new, width=20, text="Take Loan", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=loan).place(x=20 ,y=500)
    Button(new, width=20, text="Terminate Account", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=terminate).place(x=550 ,y=500)
    Button(new, width=18, text="Logout", font=("arial", 25, "bold"),bg="#3697f5", bd=1, border=2, command=logout).place(x=320 ,y=590)


statements = {
    "atmospheric pressure":"1",
    "Bank Of Fuckery":"2",
    "This is a completely random message":"3",
    "Nameless Bank":"4",
    "I AM HIM":"5",
    "Your account is quite literally RED":"6"
}

choices = random.randint(1,6)
choice = str(choices)

for i in statements:
    if statements[i] == choice:
        dec=i
        break


root=Tk()
root.geometry("600x600")
root.title("ATM Machine")
root.resizable(False,False)
root.config(bg="black")


image_icon=PhotoImage(file="Py_Project Directory\Tesla.png")   # type: ignore
root.iconphoto(False, image_icon)


imag=ImageTk.PhotoImage(Image.open("Py_Project Directory\\Untitled59.jpg"))   # type: ignore
photo=Label(image=imag, bg="black")
photo.pack()


labels = Label(root, text=f"{dec}", width=50, font=("arial", 20, "bold"),bg="black", fg="red")     # type: ignore
labels.place(x=-120, y=10)

label = Label(root ,text="Enter Username", width=15, font=("arial", 23),  bg="black", fg="red")
label.place(x=10, y=350)  

name=StringVar()
Entry(width=12, font=("arial", 28), textvariable=name, bd=0, border=2).place(x=20, y=410)

label = Label(root ,text="Enter Passcode", width=15, font=("arial", 23), bg="black", fg="red")
label.place(x=310, y=350) 

code=StringVar()
Entry(width=12, font=("arial", 28), textvariable=code, bd=0, show="*", border=2).place(x=320, y=410)

def author():
    users = name.get()     
    codes = code.get()

    if users in credentials:
        new = credentials.get(users)
    else:
        messagebox.showinfo("ERROR", "Username not Found")

    if new == codes:  # type: ignore
        logpage()
    else:
        messagebox.showinfo("INFO", "Wrong Passkey")

Button(root, width=10, text="Login", font=("arial", 20, "bold"),bg="#3697f5", bd=1, border=2, command=author).place(x=200 ,y=500)


root.mainloop()