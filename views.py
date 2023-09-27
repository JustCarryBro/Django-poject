from django.shortcuts import render
from tkinter import *
from tkinter import ttk

def index(requests):
    return render(requests,'main/index.html')


def about(requests):
    return render(requests,'main/about.html')