from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.
def scraper(request):
    if request.method == 'POST':
        site_url = request.POST.get('site_url','')
        page = requests.get(site_url)
        soup = BeautifulSoup(page.text,'html.parser')

        # link_address=[]
        
        for link in soup.find_all('a'):
            # link_address.append(link.get('href'))
            link_address = link.get('href')
            link_name = link.string

            Link.objects.create(name = link_name, link=link_address)
            return redirect('scraper')
    else:
        data =  Link.objects.all()

    return render(request,'myapp/result.html',{'link_address':data})

def delete_data(request):
    Link.objects.all().delete()
    return redirect('scraper')