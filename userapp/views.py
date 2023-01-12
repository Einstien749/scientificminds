from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate

from .forms import CustomUserCreationForm

from django.contrib import messages

from django.views.generic.edit import CreateView

from django.contrib.auth import get_user_model

from .models import *

from .tokens import *

from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site


from django.core.mail import send_mail
# Create your views here.

def Login_View(request):
    pre_path = request.COOKIES.get("lastpat")

    print(pre_path)

    pre_lit = ''

    if pre_path is not None:
        
        pre_lit = pre_path.split('/')

    pre_pet = ''

    if 'post' in pre_lit:

        pre_pet = pre_lit[int(pre_lit.index('post')) + 1]

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        print(pre_pet)
        if user is not None:

            print(user.is_active)
            
            if user.is_active:
                
                login(request, user)

                if pre_pet != '':
                    return redirect("post",pre_pet)
                
                return  redirect("home")
            else:
                messag = messages.error(request, "Please Confirm your email before you can proceed")
                return render(request, "login.html")
        else:
            messag = messages.error(request, "Please Provide the correct details")
            return render(request, "login.html")

    else:
        response = render(request, "login.html")
        response.set_cookie("lastpat", request.META.get("HTTP_REFERER"))
        return response

class SignUpView(CreateView):
    form_class = CustomUserCreationForm

    template_name = "signup.html"

    #success_url = redirect("login")
    def get(self, request):

        return render(request, self.template_name, {'form': self.form_class})
        

    def post(self, request):
        
        username = request.POST["username"]

        #print(request.POST["picture"])

        email = request.POST["email"]

        password1 = request.POST["password1"]

        password2 = request.POST["password2"]

        if username == "" or email == "" or password1 =="" or password2 == "":

            messag = messages.error(request, "Please Fill Out All Necessary Fields")

            return render(request, "signup.html", {'form': self.form_class})
        else:
            
            userexist = get_user_model().objects.filter(username = username)
            
            emailexist = get_user_model().objects.filter(email = email)

            
            if (len(userexist) != 0) or (len(emailexist) != 0):

                messag = messages.error(request, "Username and Email Must Be Unique")

                return render(request, "signup.html", {'form': self.form_class})
            
            elif password1 != password2:

                messag = messages.error(request, "Password Did Not Match ")

                return render(request, "signup.html", {'form': self.form_class})
            else:
                

                user = CustomUserCreationForm(request.POST, request.FILES)

                if user.is_valid():
                    
                    user = user.save()

                    user.is_active = False
                    
                    token = token_generator.make_token(user)

                    current_site = get_current_site(request).domain

                    subject = "Welcome To My Blog"

                    message = render_to_string(
                            "activate.html",
                            {
                                "domain": current_site,
                                "uid": user.pk,
                                "token": token,
                                "username": user.username.capitalize(),
                            }
                        )

                    user.email_user(subject, message, html_message = message, fail_silently=False)
                    print(user.is_active, token)
                    
                    return redirect("success") 

        return render(request, "signup.html")
        

def SuccessReg(request):

    if request.META.get('HTTP_REFERER') is not None:

        pre_paths = request.META.get('HTTP_REFERER').split('/')

        pre_path = pre_paths[len(pre_paths) - 1]

        if pre_path == 'signup':
        
            return render(request, "success.html")
        else:

            return redirect('logins')
    else:

        return redirect('home')

def ActivateView(request, uid, token):
    print(uid, token)

    try:
        user = CustomUser.objects.get(pk=uid)

    except:

        user = None

    if user is not None and token_generator.check_token(user, token):

        print(user.is_active)

        user.is_active = True

        user.save()

        login(request, user)

        return redirect("logins")

    else:
        print("home")
        return redirect("home")

