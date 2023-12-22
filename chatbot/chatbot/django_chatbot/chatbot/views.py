import os
import sys

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User

# from .models import Member
from .models import Chat
from .models import Poll
from .forms import CreatePollForm 

from django.utils import timezone

from django.http import HttpResponse
from django.template import loader

# this library is for conversion of speech to text
import speech_recognition as sr

# openai_api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key_path = 'api_key_file.txt'

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    # print(response)

    # Extract the text from the API response and remove leading/trailing whitespace
    answer = response.choices[0].message['content'].strip()
    return answer

# def index(request):
#     return render(request, 'index.html')

# this convert speech to text
def speech(request):
     return redirect(request, '')


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
    

def main(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    else:
        return render(request, 'main.html', {'chats': chats})  
    
def chatbot(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    else:
        return render(request, 'chatbot.html', {'chats': chats})    

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('main')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'login.html', {'error_message': error_message})
        else:    
            return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('login')
                # return redirect('main')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def landing_page(request):
     return redirect(request, 'index')


# =================
# COURSES
# =================

# def excel(request):
#   template = loader.get_template('excel.html')
#   return HttpResponse(template.render())

def excel(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    else:
        return render(request, 'excel.html', {'chats': chats})  


def hr(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    else:
        return render(request, 'hr.html', {'chats': chats})  
    

def infotech(request):
   chats = Chat.objects.filter(user = request.user)
   if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
   else:
        return render(request, 'infotech.html', {'chats': chats})


def video(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    else:
        return render(request, 'video.html', {'chats': chats})

# ========================================================

# Example 2:
def speechtext(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audio')  # Access the recorded audio data
        # Process the audio data as needed
        # Implement your chatbot logic here
        response_data = {'response': 'Processed audio successfully'}  # Replace with the actual response
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request method'})



  

# =============QUESTIONAIRE OR POLL ============

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('pollhome')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'create.html', context)


# def home(request):
#     polls = Poll.objects.all()

#     context = {
#         'polls' : polls
#     }
#     return render(request, 'poll/home.html', context)


# def pollhome2(request):
#     polls = Poll.objects.all()

#     context = {
#         'polls' : polls
#     }

#     chats = Chat.objects.filter(user = request.user)
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = ask_openai(message)

#         chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
#         chat.save()

#         return JsonResponse({'message': message, 'response': response})
#     else:
#         return render(request, 'pollhome.html', {'chats': chats})    


def pollhome(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls
    }
    return render(request, 'pollhome.html', context)


def pollvote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    # poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        elif selected_option == 'option5':
            poll.option_five_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')
    
        poll.save()

        return redirect('pollresult', poll.id)
        # return redirect('pollresult', poll.id)

    context = {                                                        
        'poll' : poll
    }
    return render(request, 'pollvote.html', context)


def pollresult(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    # poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
    return render(request, 'pollresult.html', context)

#=============================================
# POLL
#=============================================

# def home(request):
#     polls = Poll.objects.all()

#     context = {
#         'polls' : polls
#     }
#     return render(request, 'poll/home.html', context)

# def create(request):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('home')
#     else:
#         form = CreatePollForm()

#     context = {'form' : form}
#     return render(request, 'poll/create.html', context)

# def results(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)

#     context = {
#         'poll' : poll
#     }
#     return render(request, 'poll/results.html', context)

# def vote(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)

#     if request.method == 'POST':

#         selected_option = request.POST['poll']
#         if selected_option == 'option1':
#             poll.option_one_count += 1
#         elif selected_option == 'option2':
#             poll.option_two_count += 1
#         elif selected_option == 'option3':
#             poll.option_three_count += 1
#         elif selected_option == 'option4':
#             poll.option_four_count += 1
#         elif selected_option == 'option5':
#             poll.option_five_count += 1
#         else:
#             return HttpResponse(400, 'Invalid form option')
    
#         poll.save()

#         return redirect('results', poll.id)

#     context = {
#         'poll' : poll
#     }
#     return render(request, 'poll/vote.html', context)