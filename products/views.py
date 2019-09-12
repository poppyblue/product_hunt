from django.shortcuts import render

# Create your views here.


def product_list(request):
	return render(request, 'product_list.html')

def publish(request):
	if request.method == 'GET':
		return render(request, 'publish.html')
	elif request.method == 'POST':
		app_name = request.POST['名称']
		app_intro = request.POST['介绍']
		app_url = request.POST['链接']
		app_icon = request.FILES['图标']
		app_image = request.FILES['大图']
		return render(request, 'publish.html')
		