from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from useradm.forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.conf import settings


def send_email(form):
    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    htmly = get_template('user/Email.html')
    d = { 'username': username }
    subject, from_email, to = 'welcome', 'your_email@gmail.com', email
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # send_email(form) - TODO
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'useradm/signup.html', {'form': form, 'title':'reqister here'})


class CustomLoginView(LoginView):
    template_name = 'useradm/login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse(settings.LOGIN_REDIRECT_URL)

