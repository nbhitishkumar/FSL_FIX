import Tkinter, tkFileDialog, Tkconstants ,os
import os.path
import sys
import re
from Tkinter import * 

#Creating Font Styles

font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
font11 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
font15 = "-family {Courier New} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 14 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 13 -weight bold -slant "  \
   "roman -underline 0 -overstrike 0"


# Defining Functions

def browsefunc():
    global folder_path
    filename = tkFileDialog.askdirectory(parent=root, initialdir='/home/mac/Desktop', title='Browse .feat folder directory')
    Entry2.config(text=filename)# take input in this function and return as strung.
    folder_path.set(filename)
    os.chdir(filename)
    cwd=os.getcwd()
    print("Getting .feat Directory ........\n")
    print("Feat Directory :- "+cwd +"\n")
    return filename   
    
# Defining Function for Running FIX

def fixfunc():
    global thres_val
    thres_val=Entry1.get()
    path=os.path.join('/usr/local/fix/fix'+" "+str(folder_path.get())+" " +'/usr/local/fix/training_files/Standard.RData'+" "+thres_val)
    print("Start Denoising on Feat Directory ........\n")
    os.system(path)
    denoisingfunc()   # Calls Denoised Function



def denoisingfunc():
    mylines = []                             
    with open ('.fix', 'rt') as myfile: 
         for myline in myfile:                
            mylines.append(myline.rstrip('\n'))          
    mynewlist=",".join(map(str,mylines))
    mylist=[str(mynewlist).replace(' ',',') for myline in mylines]
    lis=" ".join(mylist)
    denoised_dir_path=os.path.join('fsl_regfilt -i filtered_func_data -o denoised_data -d filtered_func_data.ica/melodic_mix -f'+ " "+"'"+lis+"'")
    print("Fix Completed  \n Now Denoising ")
    print(denoised_dir_path)
    os.system(denoised_dir_path)
    print("successfully")   # Denoising Completed


# Defining Function for Running Melodic 

def melodic_denoisingfunc():
    global thres_val
    thres_val=Entry1.get()
    mel_path=str(folder_path.get())+"/denoised_data.ica"
    os.chdir(mel_path)
    print(os.getcwd()+"\n")
    mylines =[]                             
    with open ('.fix', 'rt') as myfile: 
         for myline in myfile:                
            mylines.append(myline.rstrip('\n'))          
    mynewlist=",".join(map(str,mylines))
    mylist=[str(mynewlist).replace(' ',',') for myline in mylines]
    lis=" ".join(mylist)
    mel_denoised_dir_path=os.path.join('fsl_regfilt -i filtered_func_data -o denoised_data -d filtered_func_data.ica/melodic_mix -f'+ " "+"'"+lis+"'")
    print("Fix Completed  \n Now Denoising ")
    print(mel_denoised_dir_path+"\n")
    os.system(mel_denoised_dir_path)
    print("successfully")


def melodifunc():
    global thres_val
    thres_val=Entry1.get()
    melo_path=os.path.join('/usr/local/fix/fix'+" "+str(folder_path.get())+"/denoised_data.ica"+" " +'/usr/local/fix/training_files/Standard.RData '+str(thres_val))
    print("Start Denoising on melodic Directory ........\n")
    copy_dir_path=os.path.join('cp -avr'+" "+str(folder_path.get())+"/mc"+" "+str(folder_path.get())+"/denoised_data.ica")
    os.system(copy_dir_path)
    print(melo_path+"\n")
    os.system(melo_path)
    melodic_denoisingfunc()

# Exit Button

def exit():
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

# Creating Frame Window

root=Tk()
root.title("FIX_GUI")
thres_val=int()
folder_path=StringVar()
root.geometry("595x250+205+101")
root.configure(background="#EEE8AA")


Labelframe1 = LabelFrame(root)
Labelframe1.place(relx=0.06, rely=0.040, relheight=0.803
                , relwidth=0.908)
Labelframe1.configure(relief='groove')
Labelframe1.configure(borderwidth="4")
Labelframe1.configure(font=font9)
Labelframe1.configure(foreground="black")
Labelframe1.configure(background="#F5F5DC")
Labelframe1.configure(width=600)

browsebutton = Button(root,command=browsefunc)
browsebutton.place(relx=0.807, rely=0.076, height=44, width=87)
browsebutton.configure(activebackground="#ececec",activeforeground="#000000",background="#FF6347")
browsebutton.configure(borderwidth="0",disabledforeground="#a3a3a3",font=font12,foreground="#000000")
browsebutton.configure(highlightbackground="#d9d9d9",highlightcolor="black",text="Browse")

Entry2 = Label(root)
Entry2.place(relx=0.073, rely=0.076,height=40, relwidth=0.723)
Entry2.configure(background="white")
Entry2.configure(disabledforeground="#a3a3a3")
Entry2.configure(font=font11)
Entry2.configure(foreground="#000000")
Entry2.configure(width=394)

# Threshold label

Label2 = Label(Labelframe1)
Label2.place(relx=0.233, rely=0.300, height=41, width=160
                , bordermode='ignore')
Label2.configure(background="#F5F5DC")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font=font13)
Label2.configure(foreground="#000000")
Label2.configure(text='''Threshold Value''')
Label2.configure(width=160)

# Take Threshold value by user

Entry1 = Entry(Labelframe1)
Entry1.place(relx=0.550, rely=0.300, height=42, relwidth=0.090
                , bordermode='ignore')
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font=font13)
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")
Entry1.configure(width=44)
Entry1.insert(0, 20)


# Creating Feat Button to run FIX

Button2 = Button(Labelframe1,command=fixfunc)
Button2.place(relx=0.084, rely=0.703, height=44, width=157)
Button2.configure(activebackground="#ececec")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font=font11)
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Run FIX on Feat''')
Button2.configure(width=157)

# Creating Melodic Button to run FIX

Button3 = Button(Labelframe1,command=melodifunc)
Button3.place(relx=0.387, rely=0.703, height=44, width=187)
Button3.configure(activebackground="#ececec")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#d9d9d9")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font=font11)
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''Run FIX on Melodic''')
Button3.configure(width=187)

# Creating Exit Button 

Button4 = Button(Labelframe1,command=exit)
Button4.place(relx=0.756, rely=0.703, height=44, width=67)
Button4.configure(activebackground="#ececec")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#d9d9d9")
Button4.configure(disabledforeground="#a3a3a3")
Button4.configure(font=font11)
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(text='''Exit''')
Button4.configure(width=67)

root.mainloop()
