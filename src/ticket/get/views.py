# coding=utf-8

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from ticket.models import Sponsor
from ticket.models import Ticket
from ticket.get.forms import TicketFormSet


def index(request, token):
    sponsor = get_object_or_404(Sponsor, token=token)
    tickets = sponsor.tickets.all()

    formset = TicketFormSet(queryset=tickets)
    if request.method == "POST":
        formset = TicketFormSet(request.POST, queryset=tickets)
        if formset.is_valid():
            formset.save()

            return redirect("get_ticket", token=token)

    context = {
        "sponsor": sponsor,
        "formset": formset
    }
    return render(request, "get/index.html", context)


def download(request, token):
    sponsor = get_object_or_404(Sponsor, token=token)
    tickets = sponsor.tickets.all()
