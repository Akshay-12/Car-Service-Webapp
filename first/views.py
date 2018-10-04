from django.shortcuts import render,redirect
from .models import Company
from .models import Cars
from .models import Parts
from .forms import TheForm
from .forms import TheFormRe
from django.views.decorators.http import require_POST

def index(request):
	#post_company=Company.objects.all()
	#post_car=Cars.objects.filter()
	form = TheForm()
	formr= TheFormRe()
	'''a=request.GET.get('id1')
	cname=request.POST.get('company')

	 i in 	print('Here !!! '+a)'''
	return render(request,'first/front.html',{'form':form,'formr':formr})

@require_POST
def getData(request):
	form = TheForm(request.POST)
	cname=request.POST['name']
	print(cname)
	#post_car=Cars.objects.filter(company__exact='id1')
	return redirect('index')

@require_POST
def getDataRe(request):
	form = TheFormRe(request.POST)
	cname=request.POST['name']
	print(cname)
	post_car=Cars.objects.all()
	post_parts=Parts.objects.all()
	ans="temp"
	for i in post_car:
		if i.id==int(cname):
			ans=i.name
	MY_CHOICES_RT = []
	for j in post_parts:
		if ans==str(j.model):
			MY_CHOICES_RT.append([j.name,j.price,j.garage_name,j.model])		

	result_string = """<HTML><head><style>{body{background-color:yellow;}}</style></head><body><h1>Dealer list</h1><table border=1>
	<tr><b> <td>Parts</td> <td>Price</td><td>Garage Name</td><td>Model</td></b></tr>\n"""

	for k in MY_CHOICES_RT:
		result_string += "<tr>\n"
		for l in k:
			result_string += "<td>%s</td>"%l 
		result_string += "\n</tr>\n" 
	result_string += """</table></body></HTML>"""
	display = open("first/templates/first/Onsubmit.html", 'w')
	display.write(result_string)
	display.close()

	#post_car=Cars.objects.filter(company__exact='id1')
	return render(request,'first/Onsubmit.html')