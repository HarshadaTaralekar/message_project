from django.shortcuts import render, HttpResponse, redirect
from .models import Msg
# Create your views here.
def create(request):
    if request.method=='POST':
       # print("Request is:",request.method)
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
       
      # print(n)
     # print(mail)
       # print(mob)
        #print(msg)
        
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')
        #return HttpResponse("data fetched successfully")
    else:
         #print("request is:",request.method)
         return render(request,'create.html')
def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
   # return HttpResponse("Data fetched")
def delete(request,rid):
  m=Msg.objects.filter(id=rid)
  m.delete()
  return redirect('/dashboard')
  #return HttpResponse("id to be deleted:"+rid) 
def edit(request,rid):
  if request.method=='POST':
    #submit form with new  data
      n=request.POST['uname']
      mail=request.POST['uemail']
      mob=request.POST['mobile']
      msg=request.POST['msg']
      m=Msg.objects.filter(id=rid)
      m.update(name=n,email=mail,mobile=mob,msg=msg)
      return redirect('/dashboard')
       

  else:
    m=Msg.objects.get(id=rid)
    context={}
    context['data']=m
    return render(request,'edit.html',context)
 # return HttpResponse("id to be edited:"+rid) 