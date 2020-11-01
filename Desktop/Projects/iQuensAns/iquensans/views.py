from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import SignUpForm, AccountAuthenticationForm, PostCreateForm
from django.http import JsonResponse




# Create your views here.
from .models import Post, User


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.gender = user_form.cleaned_data['gender']
            new_user.birth_day = user_form.cleaned_data['date_of_birth']
            # Save the User object
            new_user.save()
            return redirect('iquensans:index')
    else:
        user_form = SignUpForm()
    return render(request, 'iquensans/signup.html', {'user_form': user_form})


def login_view(request):
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('iquensans:index')

    else:
        form = AccountAuthenticationForm()

    context = {"form": form}

    # print(form)
    return render(request, "iquensans/login.html", context)


@login_required
def index(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostCreateForm()
    else:
        # Post data submitted; process data.
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            print(request.GET.get('image'))
            new_post.save()
            return redirect('iquensans:index')

    user = request.user.username
    profile_pic = User.objects.get(username=request.user.username)
    profiles_pic = profile_pic.profile_pic.url
    print(profile_pic.profile_pic.url)
    posts = Post.objects.all()
    print(posts[0].author.profile_pic.url)
    context = {"posts": posts, "user": user, "profile_pic": profiles_pic, "form": form}
    return render(request, 'iquensans/index.html', context)


def fetchPosts(request):
    # Filter emails returned based on mailbox
    posts = Post.objects.all()
    # Return emails in reverse chronologial order
    posts = posts.order_by("-created").all()
    list = []
    for post in posts:
        list.append(post.serialize())
    return JsonResponse(list, safe=False)


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            print("called")
            image = Post.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})
