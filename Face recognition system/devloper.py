from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_image\facialrecognition.png") # paste the path of image with .jpg format this image will be in back ground
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"collage_images\priyam.jpg")# paste path of your image with jpg format this image is of devlopers it may be in group
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer info
        dev_label = Label(main_frame, text="Hello my name , priyam", front=("times new roman", 20, "bold"),bg="white")# write the name of devlopers happy , shiva and priyam
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="we are the devloper team of this project", front=("times new roman", 20, "bold"),bg="white")
        dev_label.place(x=0, y=40)

        img2 = Image.open(r"college_image\facialrecognition.png")  # paste the path of image with .jpg format this image will be under the devloper name
        img2 = img2.resize((500,390), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=390)








if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()




# main module
#line 9
from developer import Developer

#line 174
 def developer_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Developer(self.new_window)


#in line 132 and 135 after hand2"",
command=self.developer_data

