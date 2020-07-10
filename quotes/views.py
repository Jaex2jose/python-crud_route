from django.shortcuts import render, HttpResponse, render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'id' not in request.session:
        return render(request, 'add_account.html')
    return render(request, 'success.html')

def dashboard(request):
        if 'id' not in request.session:
            return render(request, 'add_account.html')
        context = {
            'all_quotes' : Quote.objects.all()
            
        }
        return render(request, 'dashboard.html', context)

def quote_info(request, id):
    context = {
        'all_info' : User.objects.get(id=id)

    }
    print('info')
    return render(request, 'user_quotes.html', context)


def edit(request, quote_id):
    context = {
        'quote' : Quote.objects.get(id=quote_id)
    }
    return render(request,'edit.html', context)

def registration(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hash_pw = bcrypt.hashpw(request.POST['password_input'].encode(), bcrypt.gensalt()).decode()

    new_user=User.objects.create(first_name=request.POST['name_input'], email=request.POST['email_input'], password=hash_pw)

    request.session['name'] = new_user.first_name
    request.session['id'] = new_user.id 

    return redirect('/success')

def login(request):
    user = User.objects.filter(email=request.POST['email_input'])
    if user:
        user_logged = user[0]
        if bcrypt.checkpw(request.POST['password_input'].encode(), user_logged.password.encode()):
            request.session['name'] = user_logged.first_name
            request.session['id'] = user_logged.id 
            return redirect('/success')
    return redirect('/')

def quotes(request):
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quotes')

        quotes = Quote.objects.create(
        author=request.POST['quotedby_input'], 
        quote=request.POST['message_input'], 
        posted=User.objects.get(id=request.session['id'])
        )
        print(quotes)
        return redirect('/quotes')

def edit_quote(request, id):
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/edit/'+str(id))

        quotes = Quote.objects.get(id=id)
        quotes.author=request.POST['quotedby_input']
        quotes.quote=request.POST['message_input']
        quotes.save()
               
        return redirect('/edit/'+ str(id))


def delete(request, quote_id):
    one_quote = Quote.objects.get(id=quote_id)
    one_quote.delete()
    return redirect('/quotes')




def logout(request):
    request.session.clear()
    return redirect('/')

