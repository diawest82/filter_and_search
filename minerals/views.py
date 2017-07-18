from django.shortcuts import render, get_object_or_404

from .models import Mineral

import random

# Create your views here.


def mineral_list(request):
    """
    Get all the minerals from the database inside a list
    """
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals, 'random_mineral': random_mineral})


def mineral_detail(request, pk):
    """Details about each mineral"""
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html', {
        'mineral': mineral, 'random_mineral': random_mineral})


def mineral_letter_list(request, letter):
    """Allows a search by alphabet"""
    minerals = Mineral.objects.filter(name__istartswith=letter)
    random_mineral = random.choice(Mineral.objects.all())
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals,
        'active_letter': letter,
        'random_mineral': random_mineral,
    })


def search(request):
    """search by group name"""
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    random_mineral = random.choice(Mineral.objects.all())
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals,
        'random_mineral': random_mineral,
    })


def search_group(request, group):
    minerals = Mineral.objects.filter(group__icontains=group)
    random_mineral = random.choice(Mineral.objects.all())
    return render(request, 'minerals/mineral_list.html', {
            'minerals': minerals,
            'random_mineral': random_mineral
        })
