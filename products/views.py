from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone
# Create your views here.


def product_list(request):
	products = Product.objects
	return render(request, 'product_list.html', {'products': products})


def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'detail.html', {'product': product})

# 装饰器，只有登陆用户才看得到
@login_required
def publish(request):
	if request.method == 'GET':
		return render(request, 'publish.html')
	elif request.method == 'POST':
		app_title = request.POST['标题']
		app_intro = request.POST['介绍']
		app_url = request.POST['链接']
		try:
			app_icon = request.FILES['图标']
			app_image = request.FILES['大图']

			product = Product()
			product.title = app_title
			product.intro = app_intro
			product.url = app_url
			product.icon = app_icon
			product.image = app_image

			product.pub_date = timezone.datetime.now()
			product.hunter = request.user

			product.save()
			return redirect('主页')
		except Exception as err:
			return render(request, 'publish.html', {'错误': '上传图片！'})



