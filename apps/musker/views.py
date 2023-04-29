from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from apps.musker.forms import MeepForm
from apps.musker.models import Profile, Meeps


def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, ("Your Meep has been Posted!"))
                return redirect('home')
        meeps = Meeps.objects.all().order_by('-created_at')
        return render(request, 'home.html', {"meeps": meeps, "form": form})
    else:
        meeps = Meeps.objects.all().order_by('-created_at')
        return render(request, 'home.html', {"meeps": meeps})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meeps.objects.filter(user_id=pk).order_by('-created_at')

        # Post Form logic
        if request.method == 'POST':
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # Save th profile
            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile, "meeps": meeps})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')