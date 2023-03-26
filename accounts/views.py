from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, UsernameAuthenticationForm, SectionForm, TableForm
from django.contrib.auth.decorators import login_required
from venues.models import Venue, Section, Table
from .models import Profile


def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    return render(request, 'registration_login/landing.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add these lines to create a Venue instance
            venue_name = request.POST.get('venue_name')
            venue_address = request.POST.get('venue_address')
            venue = Venue(user=user, name=venue_name, address=venue_address)
            venue.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration_login/register.html', {'registration_form': form})

@login_required
def create_section_and_table(request, section_id=None):
    venue = Venue.objects.get(user=request.user)
    sections = Section.objects.filter(venue=venue)

    if request.method == "POST":
        if 'create_section' in request.POST:
            section_form = SectionForm(request.POST)
            table_form = TableForm()
            if section_form.is_valid():
                section = section_form.save(commit=False)
                section.venue = venue
                section.save()
                section_form = SectionForm()  # Reset section_form after successful submission
        elif 'create_table' in request.POST:
            section = Section.objects.get(id=section_id)
            section_form = SectionForm()
            table_form = TableForm(request.POST)
            if table_form.is_valid():
                table = table_form.save(commit=False)
                table.section = section
                table.save()
                table_form = TableForm()  # Reset table_form after successful submission
    else:
        section_form = SectionForm()
        table_form = TableForm()

    return render(request, 'registration_login/create_section_table.html', {'section_form': section_form, 'table_form': table_form, 'sections': sections})


def user_login(request):
    if request.method == 'POST':
        form = UsernameAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:index')
    else:
        form = UsernameAuthenticationForm()
    return render(request, 'registration_login/login.html', {'login_form': form})


def user_logout(request):
    logout(request)
    return redirect('landing')
