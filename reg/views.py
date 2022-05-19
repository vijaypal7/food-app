from django.shortcuts import render,redirect
from reg.forms import UserRegisterForm,organisationForm,addressForm
from reg.models import Post
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from reg.forms import PostForm
from django.core.mail import send_mail
from actions.models import Action
from actions.utils import create_action
# Create your views here.

def register(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = addressForm(request.POST)
        form3 = organisationForm(request.POST)
        if form1.is_valid() and form3.is_valid() and form2.is_valid():
            form1.save()
            cmd = form2.save(commit=False)
            cmd1 = form3.save(commit = False)
            username = form1.cleaned_data.get('username')
            user_id = User.objects.get(username = username).id
            print(user_id)
            cmd.user_id = user_id
            cmd1.user_id = user_id
            cmd.save()
            cmd1.save()
            return redirect('login')
    else:
        form1 = UserRegisterForm()
        form2 = addressForm()
        form3 = organisationForm()
    return render(request, 'index.html',{'form1':form1,'form2':form2,'form3':form3})


@login_required(login_url="/login/")
def home(request):

    post = Post.objects.all()
    a = request.user
    count = 0
    u_id = User.objects.get(username=a).id
    u_post = Post.objects.filter(user=a)
    for i in u_post:
        count += i.amount

    form = PostForm()
    if request.method=='POST':
        form=PostForm(request.POST, None)
        if form.is_valid():
            print("a")
            form.save(commit=False)
            cmd = form.save(commit=False)
            cmd.user = request.user
            print(cmd)
            cmd.save()
            #create_action(cmd, 'has created food')
            return redirect("home")
    return render(request,'home.html',{'form':form,'post':post, 'count':count})




@login_required
def PostCreateView(request):
    form = PostForm()
    if request.method=="POST":
        form = PostForm(request.POST, None)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form':form})



def DeleteView(request,id):

    post = Post.objects.get(id = id)
    post.delete()
    return redirect('home')

#email
def email(request,id):
    post = Post.objects.get(id = id)
    a = request.user
    email_to = User.objects.get(username = a).email
    if email_to:
        Name = post.user
        Name = str(Name)
        Type_of_food = post.type
        
        No_of_person_feed =   post.amount
        No_of_person_feed = str(No_of_person_feed)
        description =  post.description
        ini_time  = post.itime
        final_time =  post.finaltime
        final_time = str(final_time)
        landmark =  post.landmark
        town =  post.town
        dist =  post.dist
        state =  post.state
        mobile = post.mobile
        mobile = str(mobile)
        message = "Hello Ma'am/Sir,\t "+"\n\n"+"Name:\t"+Name+ "\n"+"Type of food:\t"+Type_of_food+"\n"+"No. of person: \t"+ No_of_person_feed + "\n" + "Description: \t" +description + "\n" + "Land: \t "+ landmark + "\n"+"Town: \t"+town+"\n" + "District: \t" + dist +"\n \n" +"For more details contact ......\t" + mobile +"\n"
        print(message)
        send_mail('These are the details you request',message,'abcdef7700000000@gmail.com',[email_to],fail_silently=False)
        return redirect('home')
    else:
        return redirect('home')

def index(request):
    return render(request, 'index.html', {})
