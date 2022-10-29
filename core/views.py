from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import words, contact_message
from django.db.models import Q
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        if request.POST['username'] != '' and request.POST['password'] != '':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                # login success
                request.session['user_login'] = {
                    'logged_in' : True,
                    'username' : username
                }
                login(request, user)
                return redirect('/?login=True')
            return redirect(f"/login?login=False&msg=Invalid%Credentials")   
        return redirect(f"/login?login=Error")     
    return render(request, 'login.html')


@login_required(login_url='/login')
def add(request):
    if request.method == 'POST':
        if request.POST['word'] != '' and request.POST['meaning'] != '':
            word = request.POST['word']
            meaning = request.POST['meaning']
            pronunciation = ''
            desc = ''
            if request.POST['pronunciation'] != '':
                pronunciation = request.POST['pronunciation']
            if request.POST['desc'] != '':
                desc = request.POST['desc']

            new_word = words.objects.create(
                word = word,
                pronunciation = pronunciation,
                meaning = meaning,
                desc = desc,
                added_by = request.user
            )   
            return redirect(f'/add?added=True&word={word}')     
        return redirect(f"/edit?added=False&msg=Add%Failed")     
    return render(request, 'add.html')


@login_required(login_url='/login')
def edit(request):
    if 'word_no' in request.GET and request.GET['word_no'] != '' and words.objects.filter(id=int(request.GET['word_no'])).exists():

        edit_word =  words.objects.get(id=int(request.GET['word_no']))

        if request.method == 'POST':
            if request.POST['word'] != '' and request.POST['meaning'] != '':
                word = request.POST['word']
                meaning = request.POST['meaning']
                pronunciation = ''
                desc = ''
                if request.POST['pronunciation'] != '':
                    pronunciation = request.POST['pronunciation']
                if request.POST['desc'] != '':
                    desc = request.POST['desc']

                edit_word.word = word
                edit_word.pronunciation = pronunciation
                edit_word.meaning = meaning
                edit_word.desc = desc
                edit_word.save()  

                return redirect(f"/edit?word_no={edit_word.id}&edited=True&word={word}")
            return redirect(f"/edit?word_no={edit_word.id}&edited=False&msg=Edit%Failed")    
        return render(request, 'edit.html', {'edit_word' : edit_word})
    return redirect('/')


def logout_user(request):
    try :
        del request.session['user_login']
    except:
        pass
    logout(request)
    return redirect('/')



def word(request):
    if 'word_no' in request.GET and request.GET['word_no'] != '' and words.objects.filter(id=int(request.GET['word_no'])).exists():
        selected_word =  words.objects.get(id=int(request.GET['word_no']))
        return render(request, 'word.html', {'word' : selected_word})
    return redirect('/')


def index(request):
    list_words = words.objects.all()
    if 'q' in request.GET and request.GET['q'] != '':
        query = request.GET['q'] 
        list_words = list_words.filter(
            Q(word__icontains=query) | 
            Q(pronunciation__icontains=query) |  
            Q(meaning__icontains=query) | 
            Q(desc__icontains=query)
        )
    return render(request, 'index.html', {'words' : list_words})

def contact(request):
    if request.method == 'POST':
        if request.POST['name'] != '' and request.POST['subject'] != '' and request.POST['contact'] != '' and request.POST['msg'] != '':
            name = request.POST['name']
            subject = request.POST['subject']
            contact = request.POST['contact']
            msg = request.POST['msg']

            new_msg = contact_message.objects.create(
                name = name,
                subject = subject,
                contact = contact,
                msg = msg,
            )   
            return redirect(f'/contact?sent=True')     
        return redirect(f"/contact?sent=False&msg=Message%Failed")     
    return render(request, 'contact.html')

