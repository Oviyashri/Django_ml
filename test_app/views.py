from urllib import request
from django.shortcuts import render
import numpy as np
import joblib as jb

def home(request):
    if request.method=='GET':
        return render(request,'index.html')

def predict(request):
    if request.method=='POST':
        TSH=(request.POST['TSH'])
        FTI=(request.POST['FTI'])
        TT4=(request.POST['TT4'])
        T3=(request.POST['T3'])
        query_hypothyroid=(request.POST['query_hypothyroid'])
        on_thyroxine=(request.POST["on_thyroxine"])
        sex=(request.POST['sex'])
        pregnant=(request.POST['pregnant'])
        psych=(request.POST['psych'])
        arr=np.array([[TSH, FTI ,TT4, T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])
        model=jb.load(open("test_app/model.pkl", 'rb'))

        result = model.predict(arr)

        if result ==1 :
            return render(request,'after.html',{'data': 'Your values are abnormal and positive for thyroid disorder'})
        else:
            return render(request,'after.html',{'data':'Your values are normal'})