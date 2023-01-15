import os
print("Welcome to the HW Planner!")
print("\n"+"There are two inputs the calendar.txt file and the hw.txt file")
print("\n"+"This is the format for importing to the calendar file: Date(dd/mm/yy), Start Time, End Time, Event Name(for this one no spaces between the event name, ex. hwplanner(correct), hw planner(incorrect))")
print("\n"+"For the hw file this is the format: Name(no spaces between the name, as said above), Subject, Duration(in mins), and the Due Date(dd/mm/yy)")
print("\n"+ "The calendar.txt is basically the events and the hw.txt is your todo list")
print("The output will be in the output.txt file.")

calend=[]
hw=[]
fn=open("calendar.txt","r")
fn2=open("hw.txt","r")
flp=open("output.txt","w+")
reader=fn.readlines()
reader = [read.strip() for read in reader]
for i in range(len(reader)):
    calend.append(reader[i].strip().split())
fn.close()
reader2=fn2.readlines()
reader2 = [read.strip() for read in reader2]
for i in range(len(reader2)):
    hw.append(reader2[i].strip().split())
#12/13/2023 --> 12, 13,2023 (down)
def sortc(calend):
    for i in range(len(calend)):

        date=""
        gotd=False
        month=""
        gotm=False
        year=""
        goty=False
        sl=""
        sc=False
        sr=""
        ec=False
        el=""
        er=""
        for j in range(len(calend[i][0])):
            if calend[i][0][j]=="/":
                if gotd==False:
                    gotd=True
                elif gotm==False:
                    gotm=True
                elif goty==False:
                    goty=True
                continue 
            if gotd==False:
                date+=calend[i][0][j]
            elif gotm==False:
                month+=calend[i][0][j]
            elif goty==False:
                year+=calend[i][0][j]
        for k in range(len(calend[i][1])):
            if calend[i][1][k]==":":
                sc=True
                continue
            if sc==False:
                sl+=calend[i][1][k]
            else:
                sr+=calend[i][1][k]
        for h in range(len(calend[i][2])):
            if calend[i][2][h]==":":
                ec=True
                continue
            if ec==False:
                el+=calend[i][2][h]
            else:
                er+=calend[i][2][h]
        calend[i].pop(1)
        calend[i].insert(1,int(sr))
        calend[i].insert(1,int(sl))
        calend[i].pop(3)
        calend[i].insert(3,int(er))
        calend[i].insert(3,int(el))
        calend[i].pop(0)
        calend[i].insert(0,int(year))
        calend[i].insert(0,int(month))
        calend[i].insert(0,int(date))
    # buggle sort
    for i in range(len(calend)):
        for j in range(len(calend)-1):
            if calend[j][2]> calend[j+1][2]:
                save=calend[j][2]
                calend[j]=calend[j+1]
                calend[j+1]=save  
            elif calend[j][2]== calend[j+1][2]:
                if calend[j][1]> calend[j+1][1]:
                    save=calend[j]
                    calend[j]=calend[j+1]
                    calend[j+1]=save  
                elif calend[j][1]==calend[j+1][1]:

                    if calend[j][0]> calend[j+1][0]:
                        save=calend[j]
                        calend[j]=calend[j+1]
                        calend[j+1]=save  
                    elif calend[j][0]==calend[j+1][0]:

                        if calend[j][3]>calend[j+1][3]:
                            save=calend[j]
                            calend[j]=calend[j+1]
                            calend[j+1]=save
    return calend
def sorthw(hwli):
    #12/13/2023 --> 12, 13,2023 (down)
    for i in range(len(hwli)):
        print(hwli[i])
        hwli[i][2]=int(hwli[i][2])
        date=""
        gotd=False
        month=""
        gotm=False
        year=""
        goty=False
        for j in range(len(hwli[i][3])):
            if hwli[i][3][j]=="/":
                if gotd==False:
                    gotd=True
                elif gotm==False:
                    gotm=True
                elif goty==False:
                    goty=True
                continue
            if gotd ==False:
                date+=hwli[i][3][j]
            elif gotm==False:
                month+=hwli[i][3][j]
            elif goty==False:
                year+=hwli[i][3][j]
        hwli[i].pop()
        hwli[i].append(int(date))
        hwli[i].append(int(month))
        hwli[i].append(int(year))
    

    #bubble sort
    for i in range(len(hwli)):
        for j in range(len(hwli)-1):
            if(hwli[j][5]>hwli[j+1][5]):
                save=hwli[j]
                hwli[j]=hwli[j+1]
                hwli[j+1]=save
            elif(hwli[j][5]==hwli[j+1][5]):

                if(hwli[j][4]>hwli[j+1][4]):
                    save=hwli[j]
                    hwli[j]=hwli[j+1]
                    hwli[j+1]=save
                elif hwli[j]==hwli[j][4]:

                    if(hwli[j][3]>hwli[j+1][3]):
                        save=hwli[j]
                        hwli[j]=hwli[j+1]
                        hwli[j+1]=save
                    elif hwli[j][3]==hwli[j+1][3]:
                        if(hwli[j][2]>hwli[j+1][2]):
                            save=hwli[j]
                            hwli[j]=hwli[j+1]
                            hwli[j+1]=save
    return hwli
def ot(hwli,calend):
    out=[]
    count=0
    for i in range(len(calend)):
        sh=calend[i][3]
        sm=calend[i][4]
        eh= calend[i][5]
        em= calend[i][6]
        if calend[i][7]=="HW":
            if calend[i][2]<hwli[i][5]:

                for j in range(count,len(hwli)):

                    durh=int(hwli[j][2]/60)
                    
                    durm=hwli[j][2]-int(durh*60)
                    
                    if sh+durh<eh:
                        
                        ap=str(sh)+":"+str(sm)+" to "+str(sh+durh)+":"+str(sm+durm)
                        out.append("You should finish "+hwli[j][0]+" for "+hwli[j][1]+" from "+ap+" on "+str(calend[i][0])+"/"+str(calend[i][1])+"/"+str(calend[i][2])+".")
                        count=j
                        sh+=durh
                        sm+=durm
            elif calend[i][2]==hwli[i][5]:
                if calend[i][1]<hwli[i][4]:
                    for j in range(count,len(hwli)):

                        durh=int(hwli[j][2]/60)
                        
                        durm=hwli[j][2]-int(durh*60)
                        
                        if sh+durh<eh:
                            
                            ap=str(sh)+":"+str(sm)+" to "+str(sh+durh)+":"+str(sm+durm)
                            out.append("You should finish "+hwli[j][0]+" for "+hwli[j][1]+" from "+ap+" on "+str(calend[i][0])+"/"+str(calend[i][1])+"/"+str(calend[i][2])+".")
                            count=j
                            sh+=durh
                            sm+=durm
                elif calend[i][1]== hwli[i][4]:
                    if calend[i][0]<hwli[i][3]:
                        for j in range(count,len(hwli)):

                            durh=int(hwli[j][2]/60)
                            
                            durm=hwli[j][2]-int(durh*60)
                            
                            if sh+durh<eh:
                                
                                ap=str(sh)+":"+str(sm)+" to "+str(sh+durh)+":"+str(sm+durm)
                                out.append("You should finish "+hwli[j][0]+" for "+hwli[j][1]+" from "+ap+" on "+str(calend[i][0])+"/"+str(calend[i][1])+"/"+str(calend[i][2])+".")
                                count=j
                                sh+=durh
                                sm+=durm
                    
                
    return out
mlp=ot(sorthw(hw),sortc(calend))

if(len(mlp)<len(hw)):
    flp.write("Sorry you don't have enough time to finish your work.")
else:
    for i in range(len(mlp)):
        flp.write(str(mlp[i])+"\n")
flp.close()
    




    

            


    




