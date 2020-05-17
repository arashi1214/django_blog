from django.shortcuts import render, redirect
from django.http import HttpResponse
from trips.models import Post, Img
from django.utils import timezone

def home(request):
	post_list = Post.objects.all()

	return render(request, 'home.html', {
			'post_list': post_list,
		})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post':post})

def showImg(request):
	imgs = Img.objects.all()
	context = {
		'imgs' : imgs
	}
	return render(request, 'showImg.html', context)