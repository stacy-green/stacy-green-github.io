"""
Co-conspirators:
Stacy, Adrian, Wesley, Leigh, Randall
"""

from audioop import reverse
from textwrap import shorten
from django.shortcuts import redirect, render
from django.urls import reverse
from earlshorten.models import ShortenedURL
import random
import string 

valid_characters = string.ascii_letters + string.digits
def create_code():
    code = ''
    for x in range (6):
        code += random.choice(valid_characters)
    return code
# Create your views here.


def index(request):
    """
    View 1 returns a page for entering in a url to be shortened, and a list of urls that have been shortened (localhost:8000/shortener/)
    """
    urls = ShortenedURL.objects.all()
    context = {
        'urls': urls
    }

    return render(request, 'earlshorten/index.html', context)

def save(request):
    """
    View 2 for receiving the form submission containing the long url, generating a random string, and saving it to the database (localhost:8000/shortener/save/)
    """
    if request.method == 'POST':
        form = request.POST
        shortened_url = ShortenedURL()
        shortened_url.url = form.get('long_url')
        taken = True
        while taken:
            new_url = create_code()
            length = len(ShortenedURL.objects.filter(code=new_url))
            if not length:
                taken = False
                shortened_url.code = new_url
                shortened_url.save()
    return redirect('earlshorten:index')

def yeet(request, url_code):
    """
    View 3 performs the redirecting, which takes a code as a parameter (localhost:8000/shortener/pEc4vt/). Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.
    url_shortener
    """

    '''
    take shortened url, look up associated url, redirect to original url
    '''    
    try:
        original_url = ShortenedURL.objects.get(code=url_code)
        original_url.counter += 1
        original_url.save()
        if 'https' in original_url.url:
            return redirect(original_url.url)
        else:
            return redirect('https://' + original_url.url)
    except ShortenedURL.DoesNotExist:
        return redirect('earlshorten:index')

"""
Part 1
A url shortener is a web service that can take long urls (https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url) and create a short url (goo.gl/pEc4vt). Some examples are bitly, TinyURL, and RB.GY. These are used to put short, easily typed links onto flyers, twitter posts, etc.

When the short url is accessed, the view will take the code associated with that url (pEc4vt) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL. You could use the ID in the url, instead of some code, but that then exposes some details about your database to the public.

Your app should contain the following:

Model: a model ShortenedURL which has the following fields code (CharField), url (URLField)
View 1 returns a page for entering in a url to be shortened, and a list of urls that have been shortened (localhost:8000/shortener/)
View 2 for receiving the form submission containing the long url, generating a random string, and saving it to the database (localhost:8000/shortener/save/)
View 3 performs the redirecting, which takes a code as a parameter (localhost:8000/shortener/pEc4vt/). Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.
url_shortener

Part 2
Add an IntegerField counter to the ShortenedUrl model, increment the counter every time the short url is accessed. Show the counter of each shortened url in the template.

"""