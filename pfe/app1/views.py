from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import JsonResponse

import json
import requests
# import urllib3

# Create your views here.
URL
USERNAME
PASSWORD
#                                    callqueues
# -----------------------------------------------------------------------------------
@login_required()
def afficher_callqueues(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
 
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/QueueList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/QueueList')
    data=json.loads(data.text)
    return render(request, 'queue.html',{"data":data})


#                                    crap
# -----------------------------------------------------------------------------------
@login_required()
def afficher_extensions(request):
    return render(request, 'Extensions.html')

#                                    get_dashboard
# -----------------------------------------------------------------------------------
@login_required()
def get_dashboard(request):
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD

    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)

    data=session.get(URL+'api/SystemStatus')
    data=json.loads(data.text)
    data1=session.get(URL+'api/CurrentUser')
    data1=json.loads(data1.text)
    data2=session.get(URL+'api/SystemStatus/GetSingleStatus')
    data2=json.loads(data2.text)

    return render(request, 'child.html',{"data":data,"data1":data1,"data2":data2})

#                                    RingGroups
# -----------------------------------------------------------------------------------
@login_required()
def afficher_RingGroups(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/RingGroupList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/RingGroupList')
    data=json.loads(data.text)
    return render(request, 'RingGroups.html',{"data":data})

#                                    SIPTrunks
# -----------------------------------------------------------------------------------
@login_required()
def afficher_SIPTrunks(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/TrunkList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/TrunkList')
    data=json.loads(data.text)
    return render(request, 'SIPTrunks.html',{"data":data})
#                                    afficher_InboundRules
# -----------------------------------------------------------------------------------
@login_required()
def afficher_InboundRules(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/InboundRulesList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/InboundRulesList')
    data=json.loads(data.text)
    return render(request, 'InboundRules.html',{"data":data})
#                                    afficher_OutboundRules
# -----------------------------------------------------------------------------------
@login_required()
def afficher_OutboundRules(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/OutboundRuleList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/OutboundRuleList')
    data=json.loads(data.text)
    return render(request, 'OutboundRules.html',{"data":data})
#                                    afficher_DigitalReceptionists
# -----------------------------------------------------------------------------------
@login_required()
def afficher_DigitalReceptionists(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(request.GET.get('delete')):
        ID=int(request.GET.get('id'))
        Param={"Ids":[ID]}
        print(Param)
        d=session.post(URL+'api/IVRList/delete',json=Param)
        print(d)
    data=session.get(URL+'api/IVRList')
    data=json.loads(data.text)
    return render(request, 'DigitalReceptionists.html',{"data":data})

#                                    update_session_data
# -----------------------------------------------------------------------------------
@login_required()
def update_session_data(request):

    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()
    # session.verify=False
    global URL,USERNAME,PASSWORD
    ids={'Username': str(USERNAME),'Password': str(PASSWORD)}
    r=session.post(URL+'api/login',json=ids)
    if(not r) :
        print("hi")
    data=session.get(URL+'api/SystemStatus')
    session_data = data.json()

    
    return JsonResponse({'session_data': session_data})

#                                    register
# -----------------------------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request, f'Please correct the error below.')
            return render(request, 'register.html', {'form': form})    
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

