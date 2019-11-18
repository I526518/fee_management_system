from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404
from entry.models import Stud_PD,Stud_Admn,Fee_Record,Stud_Fees
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect

def stud_list(request):
    if request.method=='POST':
        text=request.POST['search']
        if text:
            match=Stud_PD.objects.filter(Q(Sname__icontains=text) |
                                         Q(USN__icontains=text)    
                                        ) 
            if match!=None:
                return render(request, 'details/stud_list.html',{'search':match,'text':text})
        else:
            return HttpResponseRedirect('/details/')
    else:
        stud_pds = Stud_PD.objects.all()   
        return render(request, 'details/stud_list.html', {'stud_pds':stud_pds})

def stud_details(request,usn):
    #return HttpResponse(usn)
    stud_pd = Stud_PD.objects.get(USN=usn)
    stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
    return render(request, 'details/stud_details.html', {'stud_pd':stud_pd, 'stud_ad':stud_ad})

def fee_record(request):   
    if request.method=='POST':
        text=request.POST['search']
        if text:
            search_fields = ['Date_Paid']
            match=Fee_Record.objects.filter(Q(Stud_Fee_ID__Adm_No_S__Adm_No__icontains=text) |
                                            Q(Added_by__username__icontains=text) |
                                            Q(Date_Paid__icontains=text)
                                            ) 
            if match!=None:
                return render(request, 'details/fee_record.html',{'search':match,'text':text})
        else:
            return HttpResponseRedirect('/details/fee-record/')
    else:
        fee_rcd=Fee_Record.objects.all()
        return render(request,'details/fee_record.html',{'fee_rcd':fee_rcd})