from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Penguin, Clothes, Photo
from .forms import SwimmingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-ca-central-1.amazonaws.com/'
BUCKET = 'penguincollector'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def penguins_index(request):
  penguins = Penguin.objects.filter(user=request.user)
  return render(request, 'penguins/index.html', { 'penguins': penguins })

@login_required
def penguins_detail(request, penguin_id):
  penguin = Penguin.objects.get(id=penguin_id)
  clothes_penguin_doesnt_have = Clothes.objects.exclude(id__in = penguin.clothes.all().values_list('id'))
  swimming_form = SwimmingForm()
  return render(request, 'penguins/detail.html', { 
    'penguin': penguin,
    'swimming_form': swimming_form ,
    'clothes': clothes_penguin_doesnt_have
  })

class PenguinCreate(LoginRequiredMixin, CreateView):
    model = Penguin
    fields = '__all__'

    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

    success_url = '/penguins/'

class PenguinUpdate(LoginRequiredMixin, UpdateView):
    model = Penguin
    fields = ['breed', 'description', 'age']

class PenguinDelete(LoginRequiredMixin, DeleteView):
    model = Penguin
    success_url = '/penguins/'

def add_swimming(request, penguin_id):
    form = SwimmingForm(request.POST)
    if form.is_valid():
        new_swimming = form.save(commit=False)
        new_swimming.penguin_id = penguin_id
        new_swimming.save()
    return redirect('detail', penguin_id=penguin_id)

@login_required
def assoc_clothes(request, penguin_id, clothes_id):
  Penguin.objects.get(id=penguin_id).clothes.add(clothes_id)
  return redirect('detail', penguin_id=penguin_id)

@login_required
def unassoc_clothes(request, penguin_id, clothes_id):
  Penguin.objects.get(id=penguin_id).clothes.remove(clothes_id)
  return redirect('detail', penguin_id=penguin_id)

@login_required
def add_photo(request, penguin_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, penguin_id=penguin_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', penguin_id=penguin_id)

class ClothesList(LoginRequiredMixin, ListView):
  model = Clothes

class ClothesDetail(LoginRequiredMixin, DetailView):
  model = Clothes

class ClothesCreate(LoginRequiredMixin, CreateView):
  model = Clothes
  fields = '__all__'

class ClothesUpdate(LoginRequiredMixin, UpdateView):
  model = Clothes
  fields = ['name', 'color']

class ClothesDelete(LoginRequiredMixin, DeleteView):
  model = Clothes
  success_url = '/clothes/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)