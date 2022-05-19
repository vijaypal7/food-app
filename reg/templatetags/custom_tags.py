from django import template
from django.contrib.auth.models import User
from reg.models import Organisation, Post
register=template.Library()

def check(value):
    name = User.objects.get(username = value).id
    # print(name)
    return name
register.filter('check',check)

def check_donor(value):
    a = Organisation.objects.get(user = value).organisations
    # print(a)
    if a == "D":
        a = "None12"
        return a
    else:
        a = None
        return a
register.filter('check_donor',check_donor)

def ftype(value):
    if value=="0":
        a = "Raw Food."
    elif value=="1":
        a = "Fresh Food with validity 1 Day."
    else:
        a = "Stale Food."
    return a
register.filter('ftype',ftype)

def add(value):
    username = value
    add = Post.objects.filter(user=username)
    print("a",add)
    return add
register.filter('add',add)
