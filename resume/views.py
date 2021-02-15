from django.core.mail import send_mail
from django.shortcuts import render
from .models import About, Social, \
    Skill_category, \
    Training, \
    Project, \
    Port_Filter, Port_Column, Port_Item, \
    Contact
from .forms import ContactForm
from django.contrib import messages


def resumeView(request):
    about = About.objects.get()
    social = Social.objects.all()

    skill_categories = Skill_category.objects.all()

    training_list = Training.objects.all()

    project_list = Project.objects.all()

    port_filters = Port_Filter.objects.all()
    port_columns = Port_Column.objects.all()
    port_items = Port_Item.objects.all()

    contacts = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail(subject, message, sender_email, ['sarthak1998singh@gmail.com'])

            form = ContactForm()
            messages.success(request, 'Thanks for contacting me.')
    else:
        form = ContactForm()

    context = {
        'about': about,
        'social_list': social,

        'skill_categories': skill_categories,

        'training_list': training_list,

        'project_list': project_list,

        'port_filters': port_filters,
        'port_columns': port_columns,
        'port_items': port_items,

        'contacts': contacts,

        'form': form
    }
    return render(request, 'resume/base.html', context)
