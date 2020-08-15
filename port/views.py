from .models import Contact, Posts, BlogComment
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .templatetags import extras

# HTML Pages Render
def index(request):
    return render(request, "index.html")


def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

    return render(request, "about.html")


def blog(request):
    allPosts = Posts.objects.all()
    context = {
        "posts":allPosts
    }
    return render(request, "blog.html", context)


def portfolio(request):
    return render(request, 'portfolio.html')


def blogPost(request, slug):
    post = Posts.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {
        "post": post,
        "comments": comments,
        "user": request.user,
        "replies": replyDict
    }
    return render(request, 'blogPost.html', context)


def postcomment(request):
    try:
        if request.method == 'POST':
            comment = request.POST.get("comment")
            user = request.user
            postsno = request.POST.get("postSno")
            post = Posts.objects.get(sno=postsno)
            parentSno = request.POST.get("parentSno")
            if parentSno == "":
                comment = BlogComment(comment=comment, user=user, post=post)
            else:
                parent = BlogComment.objects.get(sno=parentSno)
                comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            return redirect(f'/blog/{post.slug}/')
    except Exception as e:
        return redirect(f'/blog/{post.slug}/')


def search(request):
    query = request.GET.get('search')
    if len(query) > 30:
        allPosts = []
    else:
        allPosts = Posts.objects.filter(title__icontains=query)
    params = {"posts": allPosts}
    return render(request, 'search.html', params)


# Authentication APIs
def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['emailS']
        pass1 = request.POST['passwordS']
        pass2 = request.POST['confirmpassword']
        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "SignUp Successful.")
        else:
            messages.error(request, "Password does not match. Please try again.")
    return redirect('/')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST['usernamel']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful.")
            return redirect('/')
        else:
            messages.error(request, "Sorry the username or password does not match.")
            return redirect('/')
    return HttpResponse("404 - Page Not Found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('/')


def forgotpass(request):
    if request.method == 'POST':
        email = request.POST['emailID']
        username = request.POST['usernameforgot']

        user = User.objects.get(email=email)
        context = {
            "user": user
        }
        return render(request, 'index.html', context)
    return HttpResponse("404 - Page not found")