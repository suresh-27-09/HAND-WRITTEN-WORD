from django.shortcuts import render,redirect
from .models import *
from PIL import Image
import pytesseract
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from django.http import HttpResponse
from openpyxl import Workbook




def index(request):
          if 'username' in request.session:
                    
                              
                    return render(request,"index.html",{'session':request.session['username']})
                    
          else:

                    return render(request,"index.html",{'session':None})
def process():
        img='paper.jpg' #-> start
        print(img)
        o=[]
        q=pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\tesseract.exe"
        # b=pytesseract.image_to_boxes(img)
        # print(b)
        y=pytesseract.image_to_string(Image.open(img))
      
        # y=str(y)
       
        s=y.split('\n')
        print(s)
        for i in s:
            j=i.replace(',','')
            K=j.replace('"','')
            m=K.replace(' ','')
            l=m.replace(')','')
            if ':' in i:
                l=i.split(':')
                o.append(l[1])
        print(o)           
        print(len(o))
        modified_list = [s.replace(')', '') for s in o]
        print(modified_list) #-> end
        obj=Mark()
        obj.s_name=o[0]
        obj.roll_no=(o[1])
        obj.mark=o[2]
        obj.save()
        path='mark.xlsx' #-> excel well start
        wb=load_workbook(path)
        s=wb.active
        data=modified_list
        s.append(data)
        wb.save(filename=path) #-> excel well end
        return redirect('/')             
def file(request):
          if request.method=="POST":
                    file=request.FILES['imgfile']
                    print("File :",file)
                    img=cv2.imdecode(np.frombuffer(file.read(),np.uint8),cv2.IMREAD_COLOR)
                    print("Image :",img)
                    cv2.imwrite('paper.jpg',img)
                   
                    # img=cv2.resize(img,(760,658))
                    # # cv2.imshow("image",img)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    
#_________________________Answer_Sheet_Format___________________________________
                    plt.rcParams["figure.figsize"] = (40,60)
                    # img = cv2.imread("image.png")
                    # plt.imshow(img)
                    d = pytesseract.image_to_data(img, output_type=Output.DICT)
                    print(d)    
                    print(d.keys())
                    print(d['text'])
                    for i in range(100, 105):
                        for i in range(30):
                                print(f"Left Distance:{d['left'][i]}",
                                f"Top Distance:{d['top'][i]}",
                                f"Width:{d['width'][i]}",
                                f"Height:{d['height'][i]}",
                                f"Text:{d['text'][i]}",
                                f"Conf:{d['conf'][i]}\n")


                    n_boxes = len(d['text'])
                    for i in range(n_boxes):
                        if int(d['conf'][i]) > 60:
                            (x, y, w, h) = d["left"][i], d["top"][i], d["width"][i], d["height"][i] 
                        
                            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) #Plotting bounding box
                            img = cv2.putText(img, d['text'][i], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, 1) #Plotting texts on top of box

                            
                            
                            
                    cv2.imshow('image',img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    for i in d['text']:
                        if d['text'].index(i) ==75 :
                            r=i
                        if d['text'].index(i) ==79 :
                            t=i
                        if d['text'].index(i) ==90 :
                            y=i
                            print("WELCOME")
                            print(r,t,y)
                            obj=Mark()
                            obj.s_name=r
                            obj.roll_no=t
                            obj.mark=y
                            obj.save()
                             
                    # process()
                    return redirect('/')     
#______________________________Answer_sheet_working_End________________________________
            
                    
          return redirect('index')                    
                              
                  
def register(request):
          if request.method=="POST":
                    name=request.POST.get("username")
                    roll=request.POST.get("roll")
                    dept=request.POST.get("dept")
                    password=request.POST.get("psw")
                    phone=request.POST.get("phone")
                    obj=Register()
                    obj.uname=name
                    obj.roll=roll
                    obj.dept=dept
                    obj.password=password
                    obj.phone=phone
                    obj.save()
                    return redirect('login')
          return render(request,"register.html")
def login(request):
          if request.method=="POST":
                    name=request.POST.get("username")
                    password=request.POST.get("psw")
                    print(name,password)
                    user =Register.objects.get(uname=name)
                    if user.password==password:
                              request.session['username']= name
                              return redirect("index")
          return render(request,"login.html")
