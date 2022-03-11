from urllib import request
from django.shortcuts import render
import numpy as np
import joblib as jb

def home(request):
    return render(request,'index.html')

def predict(request):
    if request.method=='POST':
        TSH =(request.GET['TSH'])
        FTI =(request.GET['FTI'])
        TT4 =(request.GET['TT4'])
        T3 =(request.GET['T3'])
        query_hypothyroid =(request.GET['query_hypothyroid'])
        on_thyroxine =(request.GET["on_thyroxine"])
        sex =(request.GET['sex'])
        pregnant =(request.GET['pregnant'])
        psych =(request.GET['psych'])
        arr=np.array([[TSH, FTI ,TT4, T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])
        model=jb.load('test_app\model.pkl')

        result = model.predict(arr)

        if result ==1 :
            return render(request,'after.html',{'data': 'Your values are abnormal and positive for thyroid disorder'})
        else:
            return render(request,'after.html',{'data':'Your values are normal'})