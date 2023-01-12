from django.shortcuts import render, redirect

from random import sample, shuffle

from .models import *

from django.http import HttpResponse

from userapp.models import CustomUser


# Create your views here.
def Home(request):
        
    comet = Comment.objects.all()
    quotes = Quote.objects.all()
    cate = Category.objects.all()
    pre_quote = sample(list(quotes), 6)
    latest_comment = list(comet)[-1:-4:-1]
    post = Post.objects.all()
    postitems = list(post)[-1:-11:-1]
    sect = {}
    for p in cate:
        sect[str(p.category)] = [k.title for k in post if str(k.category) == str(p.category)]

    if request.method == "POST":
        if request.user != "AnonymousUser":
            comm = request.POST["comm"]
            if list(comet)[-1].writer.username != str(request.user.username):
                if comm != "":
                    Comment.objects.create(comment=comm, writer=request.user)
            comet = Comment.objects.all()
            latest_comment = list(comet)[-1:-4:-1]
    if request.method == "GET":
        y = request.GET.get("submail")
        if y != None:
            for rebec in post:
                if str(rebec.title).lower().__contains__(y.lower()):
                    return redirect("post", rebec)
    return render(request, "home.html", {"post": postitems, "quotes": pre_quote, "comments": latest_comment, "category": cate, "mathematics": sect["mathematics"], "physics": sect["physics"], "programming": sect["programming"], "web_development": sect["web_development"],"personality": sect["personality"],"politics": sect["politics"],"football": sect["football"], "sect": sect})

def PostDetail(request, title):
    title = title.lower()
    j = Post.objects.filter(title = title)
    post = Post.objects.all()
    if len(j) == 1:
        relatedpost = Post.objects.filter(category = j[0].category)
        k = PostComment.objects.filter(postitem = j[0])
        if len(list(relatedpost)) >= 3:
            relatedpost = list(relatedpost)[0:3]
        if request.method == "GET":
            if len(list(k)) > 3:
                k = list(k)[-1:-4:-1]
            return render(request, 'post.html', {'post':j[0], 'relatedpost':relatedpost, 'postitem':k, 'seen': True})
        if request.method == "POST":
            if request.user.is_authenticated:
                print(request.user.email)
                cum = request.POST["comet"]
                if cum != "":
                    PostComment.objects.create(writer=request.user, postitem=j[0], postcomment=cum)
            k = PostComment.objects.filter(postitem = j[0])
            if len(list(k)) > 3:
                k = list(k)[-1:-4:-1]
            return render(request, 'post.html', {'post':j[0], 'relatedpost':relatedpost, 'postitem':k, 'seen': True})
    else:
        relatedpost = list(post)[0:3]
        return render(request, 'post.html', {'post':{'posturl': "Sorry No Post For The this Search", "postimg": "oops.png"}, 'relatedpost': relatedpost,"seen": False})
