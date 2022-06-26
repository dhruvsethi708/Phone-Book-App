from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'Contact/home.html')


def addcontact(request):
    fm = UserForm()

    if request.method == 'POST':
        pass

    else:
        fm = UserForm()

    return render(request, 'Contact/form.html', {'form': fm})


def getAllContacts(request):
    if request.method == "POST":
        nm = request.POST['name']
        pm = request.POST['phoneno']
        adddet = Contact(name=nm, phoneno=pm)
        adddet.save()
    con = Contact.objects.all()
    return render(request, 'Contact/allcontacts.html', {'contact': con})



# This function will delete
def delete_data(request, id):
    if request.method == "POST":
        pi = Contact.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/allcontacts')



# This function will update/edit
def update_data(request, id):
    print(request.method)

    if request.method == 'POST':
        pi = Contact.objects.get(pk=id)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()


    else:
        pi = Contact.objects.get(pk=id)
        print(pi)
        fm = UserForm(instance=pi) 
    
    return render(request, 'Contact/updatecontact.html', {'form':fm})




def searchContact(request):
    pass