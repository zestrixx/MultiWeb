import datetime
import random
import string

import pywhatkit as kit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import shorturl, Issues


# Create your views here.


@login_required(login_url='/login/')
def dashboard(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


@login_required(login_url='/login/')
def generate(request):
    if request.method == "POST":
        # generate
        pass
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_query=short)
            if not check:
                newurl = shorturl(
                    user=usr,
                    original_url=original,
                    short_query=short,
                )
                newurl.save()
                messages.success(request, "Successfully shorted!")
                return redirect("/#urlshortener")
            else:
                messages.error(request, "Already Exists")
                return redirect("/#urlshortener")
        elif request.POST['original']:
            # generate randomly
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = shorturl.objects.filter(short_query=short)
                if not check:
                    newurl = shorturl(
                        user=usr,
                        original_url=original,
                        short_query=short,
                    )
                    newurl.save()
                    messages.success(request, "Successfully shorted!")
                    return redirect("/#urlshortener")
                else:
                    continue
        else:
            messages.error(request, "Empty Fields")
            return redirect("/#urlshortener")
    else:
        return redirect('/')


def home(request, query=None):
    if not query or query is None:
        return render(request, 'index.html')
    else:
        try:
            check = shorturl.objects.get(short_query=query)
            check.visits = check.visits + 1
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'index.html', {'error': "error"})


# added delete URl

@login_required(login_url='/login/')
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = shorturl.objects.filter(short_query=short)
            check.delete()
            return redirect(dashboard)
        except shorturl.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)


@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        query = request.POST['query']
        msg = Issues(name=name, email=email, subject=subject, query=query)
        msg.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('/#contact')
    else:
        return redirect(home)


def message(request):
    user = request.user
    phone = request.POST.get('number')
    message = request.POST.get('msg')
    hour = int(datetime.datetime.now().strftime("%H"))
    min = int(datetime.datetime.now().strftime("%M"))
    try:
        kit.sendwhatmsg("+91" + phone, message, 23, 34)
        messages.success(request, 'Message sent Successfully!')
        return redirect('/#messages')
    except:
        messages.error(request, 'Message sent Error')
        return redirect('/#messages')