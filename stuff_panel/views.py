from django.shortcuts import render,HttpResponseRedirect
from stuff_panel.forms import Massage, notificationform,pointaddform
from stuff_panel.models import OfferTable,Notification,Pointaddmodel
from user.models import User
from user.forms import RegistrationForm

# Create your views here.

# add item and show all items
def add_show(request):
    if request.method == 'POST':
        fm= Massage(request.POST)
        offer_name = request.POST['offer_name']
        print(offer_name)
        duration_date = request.POST['duration_date']
        reg=OfferTable(offer_name=offer_name, duration_date=duration_date)
        reg.save()
        fm= Massage()
        
    else:
        fm= Massage()
    alldata=OfferTable.objects.all()
    return render(request, 'stuff_panel/addandshow.html',{'form' : fm,'alldata':alldata})


# this function will delete data
def delete_data(request,id):
    if request.method == 'POST':
        pi=OfferTable.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/stuff_panel/')
    
    
# this Function will update/Edit
def update_data(request,id):
    if request.method == 'POST':
        pi=OfferTable.objects.get(pk=id)
        fm =Massage(request.POST, instance=pi)
        fm.save()
    else:
        pi=OfferTable.objects.get(pk=id)
        fm =Massage(instance=pi)
    return render(request,'stuff_panel/update.html', {'form':fm})
    
    



def shownotificationform(request):
    if request.method == 'POST':
        fm= notificationform(request.POST)
        givenotification = request.POST['givenotification']
        reg=Notification(givenotification=givenotification)
        reg.save()
        fm= notificationform()
        
    else:
        fm= notificationform()
    #alldata=Notification.objects.all()
    return render(request, 'stuff_panel/notification.html',{'form' : fm})


def givenotification(request,id):
    user = User.objects.filter(user_id=id).first()
    getnotification=Notification.objects.all()
    return render(request, 'stuff_panel/shownotification.html',{'user':user,'getnotification':getnotification})








def pointadding(request):
    user = User.objects.filter(user_id=id).first()
    fetchdata=User.objects.all()
    #print(fetchdata)
    
    if request.method == 'POST':
        fm= pointaddform(request.POST)
        email = request.POST['email']
        pointno=request.POST['pointno']
        print(pointno)
        
        user = User.objects.filter(email=email).first()
        
        reg=Pointaddmodel(email=email,pointno=pointno)
        reg.save()
        newp=user.point + int(pointno)
        user.point=newp
        user.save()
        fm= pointaddform()
        
    else:
        fm= pointaddform()
    alldata=Pointaddmodel.objects.all()  
    #x=User.objects.get(email=email)   
    #x=User.objects.filter(email=email).update(point=pointno)
    
    return render(request, 'stuff_panel/stuffaddpoint.html',{'form' : fm,'alldata':alldata , 'fetchdata':fetchdata })




        
