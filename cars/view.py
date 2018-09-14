from .models import Comment

def index(request):
	return render(request,'first/Car.html')