from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription
from django.views.generic import DetailView



new = EmailCreateView.as_view(model = Subscription,
                              form_class = SubscriptionForm,
                              email_subject = 'Confirmacao de inscricao')

detail = DetailView.as_view(model=Subscription)