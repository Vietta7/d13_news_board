import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import SignUpForm, ConfirmationForm
from .models import Code


def signup(request):
    # First step of registration including secret code generation (generated_code) and
    # temporary user creation (usr with is_active=False flag). Sending mail to usr
    # with that code and redirecting to next page with comparison form. Filling context
    # with generated_code to bring it through to the next view function. Redirecting to
    # 'reset' page in a case of validation problem (repeating usr object in db) which deletes
    # all user objects with is_active=False flag.
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            usr = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                           password=request.POST['password1'], is_active=False)
            generated_code = Code.objects.create(name=User.objects.get(id=usr.id), code=random.randint(10000, 99999))
            print(generated_code.code)
            send_mail(subject='Подтверждение регистрации.',
                      message=f'Отправьте следующий код {generated_code.code} для подтверждения регистрации.',
                      from_email=None,
                      recipient_list=[request.POST['email']])
            context = {
                'generated_code': generated_code,
                'usr': usr
            }
            return render(request, 'registration/confirm.html', context)
        else:
            return render(request, 'registration/reset.html')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


def confirm(request, code_id):
    # Second step of registration including comparison of usr_code and generated code (confirmation.code).
    # If succeeded we get is_active=True flag for user object in db.
    if request.method == 'POST':
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            usr = request.POST['name']
            usr_code = request.POST['code']
            confirmation = Code.objects.get(id=code_id)
            if int(usr_code) == int(confirmation.code):
                usr_upd = User.objects.get(username=confirmation.name)
                usr_upd.is_active = True
                usr_upd.save()
                return render(request, 'templates/registration/successful.html', {'usr': usr})
            return render(request, 'templates/registration/unsuccessful.html')
        return render(request, 'templates/registration/unsuccessful.html')
    else:
        form = ConfirmationForm()
        return render(request, 'templates/registration/confirm.html', {'form': form})


def reset(request):
    obj = User.objects.filter(is_active=False)
    obj.delete()
    return redirect('desk:index')
