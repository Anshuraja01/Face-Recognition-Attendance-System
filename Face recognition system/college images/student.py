from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
     def __init__(self,root):
          self.root=root
          self.root.geometry("800x600")
          self.root.title("Face Recognition System")


           # first image 
          img=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/1526369384php2Zz81q.png")
          img=img.resize((500,150),Image.BILINEAR)
          self.photoimg=ImageTk.PhotoImage(img)

          f_lbl=Label(self.root,image=self.photoimg)
          f_lbl.place(x=0,y=0,width=500,height=150)

         # second image  
          img1=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/facialrecognition.png")
          img1=img1.resize((500,150),Image.BILINEAR)
          self.photoimg1=ImageTk.PhotoImage(img1)

          f_lbl=Label(self.root,image=self.photoimg1)
          f_lbl.place(x=500,y=0,width=500,height=150)
        
         # third image 
          img2=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/har.jpg")
          self.photoimg2=ImageTk.PhotoImage(img2)

          f_lbl=Label(self.root,image=self.photoimg2)
          f_lbl.place(x=1000,y=0,width=500,height=150)

          #bg image
          img3=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/bg1.jpg")
          img3=img3.resize((1530,710),Image.BILINEAR)
          self.photoimg3=ImageTk.PhotoImage(img3)

          bg_img=Label(self.root,image=self.photoimg3)
          bg_img.place(x=0,y=130,width=1530,height=710)

          title_lbl=Label(bg_img,text="STUDENT MANEGMENT SYSTEM",font =("heinrich",35,"italic"),bg="black",fg="red")
          title_lbl.place(x=0,y=0,width=1530,height=45)

          main_frame=Frame(bg_img,bd=2,bg="white")
          main_frame.place(x=10,y=55,width=1500,height=630)

          #left lable frame

          Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
          Left_frame.place(x=10,y=10,width=730,height=580)

          img_left=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/stu.jpeg")
          img_left=img_left.resize((750,150),Image.BILINEAR)
          self.photoimg_left=ImageTk.PhotoImage(img_left)

          f_lbl=Label(Left_frame,image=self.photoimg_left)
          f_lbl.place(x=5,y=0,width=720,height=130)

          #current course

          current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
          current_course_frame.place(x=5,y=135,width=720,height=150)

          dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
          dep_label.grid(row=0,column=0)

          dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17)
          dep_combo.grid(row=0,column=1)




          #right lable frame

          Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
          Right_frame.place(x=750,y=10,width=730,height=580)






if __name__ == "__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()

