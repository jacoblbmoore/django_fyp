from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from venues.models import Section
from .forms import SectionForm, TableForm
from accounts.decorators import has_section_table
from venues.models import Section, Venue, Table
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, 'user_dashboard/dashboard.html')


@login_required
def bookings(request):
    return render(request, 'user_dashboard/bookings.html')


@login_required
def floor_plan(request):
    return render(request, 'user_dashboard/floor_plan.html')


@login_required
def staffroom(request):
    return render(request, 'user_dashboard/staffroom.html')


@login_required
def contacts(request):
    return render(request, 'user_dashboard/contacts.html')


def settings(request):
    user_venue = Venue.objects.get(user=request.user)
    sections = Section.objects.filter(venue=user_venue)
    tables = Table.objects.filter(section__venue=user_venue)
    table_forms = {table.id: TableForm(instance=table) for table in tables}
    # Instantiate the forms
    section_form = SectionForm()
    table_form = TableForm()

    context = {
        'sections': sections,
        'section_form': section_form,
        'table_form': table_form
    }

    return render(request, 'user_dashboard/settings.html', context)


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

    return render(request, 'user_dashboard/settings.html',
                  {'section_form': section_form, 'table_form': table_form, 'sections': sections})


@login_required
def delete_section_or_table(request, section_id=None, table_id=None):
    venue = Venue.objects.get(user=request.user)

    # Delete the section if section_id is provided
    if section_id:
        section = get_object_or_404(Section, id=section_id, venue=venue)
        section.delete()
        messages.success(request, f"The section '{section.name}' was deleted successfully.")
        return redirect('dashboard:settings')

    # Delete the table if table_id is provided
    if table_id:
        table = get_object_or_404(Table, id=table_id, section__venue=venue)
        section = table.section
        table.delete()
        messages.success(request, f"The table '{table.name}' in section '{section.name}' was deleted successfully.")
        return redirect('dashboard:settings')

    # If neither section_id nor table_id is provided, show an error message
    messages.error(request, "Invalid request: either section_id or table_id must be provided.")
    return redirect('dashboard:settings')


@login_required
def update_table(request, table_id=None):
    table_instance = get_object_or_404(Table, id=table_id)

    if request.method == 'POST':
        form = TableForm(request.POST, instance=table_instance)
        if form.is_valid():
            table = form.save(commit=False)
            table.save()
            messages.success(request, 'Table updated successfully.')
            return redirect('dashboard:settings') # Redirect to the settings page or any other page you'd like to go after updating the table
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TableForm(instance=table_instance)

    context = {
        'form': form,
        'table_id': table_id,
    }

    return render(request, 'user_dashboard/update_table.html', context)


@login_required
def get_calendar_data(request):
    try:
        venue = Venue.objects.get(user=request.user)
        sections = Section.objects.filter(venue=venue)
        tables = Table.objects.filter(section__in=sections)

        data = []
        for table in tables:
            data.append({
                'id': table.id,
                'section': table.section.name,
                'title': f'Table {table.name}({table.min_seats}-{table.max_seats})',
            })

        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': 'An error occurred.'})
