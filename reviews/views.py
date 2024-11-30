from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect



def review(request):
    if request.method == 'POST':
        # Handle the form submission
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect('reviews/thank_you')  # Redirect to the thank you page
    return render(request, 'reviews/review.html')  # Render the review form

def submit_review(request):
    if request.method == "POST":
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        # You can process or save the data here
        print(f"Username: {username}, Comment: {comment}")  # Debugging or logging
        return render(request, 'thank_you.html')
    return redirect('review')  # Redirect to the form page if accessed via GET

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
