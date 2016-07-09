from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import ContactForm
from ..utils.slack import send_to_slack


class HomeView(TemplateView):
    template_name = 'index.html'

def contact(request):
    '''
    Contact us form POST
    '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            contact_details = "*Name*: {}\n *Email*: {}\n *Phone*: {}\n *Message*: {}".format(name, email, phone, message)
            send_to_slack(contact_details)

            return HttpResponseRedirect('/')
        else:
            print("form not valid")
        return HttpResponseRedirect('/')