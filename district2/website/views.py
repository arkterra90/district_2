from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactForm, blogPost

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def handle_form_submission(request):
    if request.method == 'POST':
        try:
            # Get data from the request
            data = json.loads(request.body.decode('utf-8'))
            name = data.get("name", "")
            email = data.get("email", "")
            phone = data.get("phone", "")
            message = data.get("message", "")
            volunteer = data.get("volunteer", False)
            yard_sign = data.get("yardSign", False)
            door_hangers = data.get("doorHangers", False)
            large_sign = data.get("largeSign", False)
            meet_and_greet = data.get("meetAndGreet", False)

            # Create a new instance of the kuehnForm model
            new_form_entry = ContactForm(
                formName=name,
                formEmail=email,
                formPhone=phone,
                formMessage=message,
                formVolunteer=volunteer,
                formYardSign=yard_sign,
                formDoorHangers=door_hangers,
                formLargeSign=large_sign,
                formMeetAndGreet=meet_and_greet,
            )

            # Save the new entry to the database
            new_form_entry.save()

            return JsonResponse({'message': 'Data received successfully.'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Error decoding JSON: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    

def blogHome(request):
# Query for all blog posts, ordering them by publication date (newest first)
    blog_entries = blogPost.objects.all().order_by('-dateMade')
    # Pass the blog entries to the template context
    context = {'blog_entries': blog_entries}
    return render(request, "website/bloghome.html", context)

def blogEntry(request, postID):

    post = blogPost.objects.get(id=postID)

    other_entries = blogPost.objects.exclude(id=postID).order_by('-dateMade')[:10]

    context = {
        'post': post,
        'other_entries': other_entries,  # Add the other entries to the context
    }   
     
    return render(request, 'website/blogpost.html', context)