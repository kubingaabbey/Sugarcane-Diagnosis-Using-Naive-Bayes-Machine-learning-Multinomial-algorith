from urllib import response
from django.shortcuts import render
import numpy as np
from django.http import JsonResponse
import pandas as pd

# Create your views here.
from django.http import HttpResponse, JsonResponse
from datetime import date

from django.contrib import messages
from sklearn.metrics import accuracy_score
from .models import farmers
#from django.contrib.auth.models import User
#from chats.models import Chat,Feedback

def index(response):
    return render(response, "main/index.html")

def home(response):
    return render(response,"main/home.html")

def diagnosis(response):

  symptomslist=['Emergence of smut whips',
     'Erect spindle leaves',
     'Profuse tillering forming grass',
     'brown-orange_or_red_brown spots',
     'Brown foliage','Contrasting shades of green Leaves',
     'chlorotic areas on the leaf blade','Leaf necrosis'
    ,'plant necrosis especially on internodes',
     'Dry 3rd and 4th leaf','emits acidic_alcholic sour smell',
     'reddening of the internal tissues',
     'red tissue with white transverse patches',
     'Short_thin stalks','Up and down appearance of canopy',
     'Decline in cane thickness',
     'Poor vigour','Wrinkling of leaves',
     'Twisting of leaves',
     'Shortening of leaves',
     'narrow young leaves',
     'reduced tillering',
     'pineapple smell',
     'Orange-red vascular bundles',
     'Poor_patchy germination',
     'Burnt appearance_on leaf tips',
     'White stripes_patches on leaves',
     'leaf wilting','Cream-white leaf stripes',
     'Red leaf stripes',
     'Growing point_mycelium present',
     'Fungal growth','Yellowing of crowns',
     'Yellow midribs','Hollow stem','internode red streaks',
     'Bushy appearance_grasslike','small internodes',
     'premature tillering','pale yellow leaves']

  
  alphabaticsymptomslist = sorted(symptomslist)

  if response.method =='GET':
    return render(response, "main/diagnosis.html",{"list2":alphabaticsymptomslist})
  elif response.method =='POST':
    inputno = int(response.POST["noofsym"])
    print(inputno)
    if (inputno == 0):
      return JsonResponse({'predicteddisease': "none",'confidencescore': 0 })
    else :
#      NaiveBayes(symptomslist)
#      print(symptomslist)
      print(inputno)
      psymptoms = []
      psymptoms = response.POST.getlist("symptoms[]")
      print(psymptoms)
      NaiveBayes(psymptoms)

  return render(response, "main/diagnosis.html")



def NaiveBayes(psymptoms):
  from sklearn.naive_bayes import MultinomialNB
  gnb = MultinomialNB()
  from sklearn.metrics import accuracy_score

  symptomslist2=['Emergence of smut whips',
     'Erect spindle leaves',
     'Profuse tillering forming grass',
     'brown-orange_or_red_brown spots',
     'Brown foliage','Contrasting shades of green Leaves',
     'chlorotic areas on the leaf blade','Leaf necrosis'
    ,'plant necrosis especially on internodes',
     'Dry 3rd and 4th leaf','emits acidic_alcholic sour smell',
     'reddening of the internal tissues',
     'red tissue with white transverse patches',
     'Short_thin stalks','Up and down appearance of canopy',
     'Decline in cane thickness',
     'Poor vigour','Wrinkling of leaves',
     'Twisting of leaves',
     'Shortening of leaves',
     'narrow young leaves',
     'reduced tillering',
     'pineapple smell',
     'Orange-red vascular bundles',
     'Poor_patchy germination',
     'Burnt appearance_on leaf tips',
     'White stripes_patches on leaves',
     'leaf wilting','Cream-white leaf stripes',
     'Red leaf stripes',
     'Growing point_mycelium present',
     'Fungal growth','Yellowing of crowns',
     'Yellow midribs','Hollow stem','internode red streaks',
     'Bushy appearance_grasslike','small internodes',
     'premature tillering','pale yellow leaves']
  diseases=['Smut sugarcane','sugarcane rust','Sugarcane Mosaic',
          'Red rot','Ratoon Stunting','Pokkah Boeng',
          'pineapple disease','Leaf scald','Downy Mildew','wilt',
          'Grassy shoot']

#testing data here
  tr=pd.read_csv('C:/django/mysite/main/templates/main/Book2.csv')
  tr.replace({'prognosis':{'Smut sugarcane':0,'sugarcane rust':1,'Sugarcane Mosaic':2,
          'Red rot':4,'Ratoon Stunting':5,'Pokkah Boeng':6,
          'pineapple disease':7,'Leaf scald':8,'Downy Mildew':9,'wilt':10,
          'Grassy shoot':11}},inplace=True)
  X_test=tr[symptomslist2]
  y_test =tr[["prognosis"]]
  np.ravel(y_test)



#training data
  df=pd.read_csv("C:/django/mysite/main/templates/main/Book256.csv")
  df.replace({'prognosis':{'Smut sugarcane':0,'sugarcane rust':1,'Sugarcane Mosaic':2,
          'Red rot':4,'Ratoon Stunting':5,'Pokkah Boeng':6,
          'pineapple disease':7,'Leaf scald':8,'Downy Mildew':9,'wilt':10,
          'Grassy shoot':11}},inplace=True)

  X=df[symptomslist2]
  y=df[["prognosis"]]
  np.ravel(y)
  gnb=gnb.fit(X,np.ravel(y))
  y_pred =gnb.predict(X_test)
  print(accuracy_score(y_test,y_pred))
  print(accuracy_score(y_test,y_pred, normalize=False))

  testingsymptoms = []
  for x in range(0, len(symptomslist2)):
          testingsymptoms.append(0)

  for k in range(0,len(symptomslist2)):
    for z in psymptoms:
      if(z==symptomslist2[k]):
        testingsymptoms[k]=1

  inputtest = [testingsymptoms]
  predict = gnb.predict(inputtest)
  print("The predicted disease is: ")
#  print(predict)
  confidencescore=y_pred.max() * 100
  con=confidencescore
  print(" confidence score of : = {0} ".format(confidencescore))
#  print(confidencescore)
  predicted_disease = predict[0]
 # print(predicted_disease)
  print(diseases[predicted_disease])
  ab=diseases[predicted_disease]
  consultdoctor = "Abbey"
  return JsonResponse({'predicteddisease':str(predicted_disease) ,'confidencescore':int(confidencescore),"consultdoctor": str(consultdoctor)})



def about(response):
  return render(response,"main/about.html")

def explore(response):
  return render(response,"main/explore.html")

def signup(response):
  if response.method =='POST':
          #saving to database.....................
    username = response.POST.get('username')
    email = response.POST.get('email')
    gender = response.POST.get('gender')
    address = response.POST.get('address')
    mobile = response.POST.get('mobile')
    password = response.POST.get('password')
    name = response.POST.get('name')

    new_user = farmers(username=username,name=name,email=email,gender=gender,address=address,mobile=mobile,password=password)
    new_user.save()

    print("disease record saved sucessfully.............................")
  return render (response,"signup.html")

def pineapple(response):
  return render(response,"main/pineapple.html")

def smut(response):
  return render(response,"main/smut.html")

def rust(response):
  return render (response,"main/rust.html")

def redrot(response):
  return render(response,"main/redrot.html")
def wilt(response):
  return render(response,"main/wilt.html")
def pokkah(response):
  return render(response, "main/pokkah.html")
def ratoon(response):
  return render(response,"main/ratoon.html")
def scald(response):
  return render(response,"main/scald.html")
def signin(response):
  return render(response,"main/signin.html")
def sign_in_admin(response):
  return render(response,"main/sign_in_admin.html")
