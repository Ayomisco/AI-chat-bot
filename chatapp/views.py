from django.shortcuts import render, redirect
from chatapp.models import *
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm 
from django.contrib.auth.decorators import login_required
import openai
from django.contrib.auth.models import User


# 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
openai.api_key = "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"



@login_required(redirect_field_name='signin')
def AiChat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        ai_response = generate_response(user_input)
        Chat.objects.create(user=request.user, user_input=user_input, ai_response=ai_response)
        # return redirect('chat')
    else:
        user_input = ''
        ai_response = ''

    chat_history = Chat.objects.filter(user=request.user)

   
    context = {
        'user_input': user_input,
        'chatbot_response': ai_response,
        'chat_history': chat_history,
        
    }
    return render(request, 'index.html', context)



def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'signin.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def clear_chat(request):
    # clear the 'name' field for all records in the 'MyModel' model
    Chat.objects.all().delete()
    return redirect('index')