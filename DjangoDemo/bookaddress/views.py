from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from bookaddress.forms import LoginForm, ContactModelForm
from bookaddress.models import Contact
from django.contrib.auth.decorators import login_required


# https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated
def index(request):
    if request.user.is_authenticated:
        return my_data(request)

    else:
        return login_view(request)


# https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-in
# https://docs.djangoproject.com/en/1.11/topics/http/shortcuts/#render
def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                url = reverse('my_data')
                return HttpResponseRedirect(url)

        form = LoginForm(initial={'user': request.POST['user']})
        return render(request, 'bookaddress/index.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'bookaddress/index.html', {'form': form})


# https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-out
def logout_view(request):
    logout(request)
    url = reverse('login')
    return HttpResponseRedirect(url)


# https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-login-required-decorator
# https://docs.djangoproject.com/en/1.11/topics/http/shortcuts/#get-object-or-404
@login_required()
def my_data(request):
    my_contact = get_object_or_404(Contact, user=request.user)
    if request.POST:
        form = ContactModelForm(request.POST, instance=my_contact)
        if form.is_valid():
            form.save()

    form = ContactModelForm(instance=my_contact)
    data = {'my_contact': my_contact,
            'form': form
            }
    return render(request, 'bookaddress/my_data.html', data)
