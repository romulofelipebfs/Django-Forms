from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
from django.views import View
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        review = Review.objects.all()
        print(review)
        return render(request, "reviews/review.html", {
            "form":form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-you')
    
'''    
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-you')
    else:
        form = ReviewForm()
    review = Review.objects.all()
    print(review)
    return render(request, "reviews/review.html", {
        "form":form
    })
'''
def thanks_you(request):
    return render(request, "reviews/thanks-you.html")
