from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Products
# Create your views here.
import requests
from bs4 import BeautifulSoup

def add_show(request):
    
    data=(Products.objects.filter().order_by('-rating'))[:5]
    return render (request,'top_product/top_product.html',{'products':data,}) 
    # print(alls)

def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=Products.objects.filter(name__icontains=query)
        data=(Products.objects.filter().order_by('-rating')) 
    return render(request,'top_product/top_product.html',{'query':query, 'results':results ,'products':data,})

def searched(request,id):
       item=Products.objects.get(pk=id)
       return render(request,'top_product/searched_item.html',{'item':item,})

def scrapdata(request):
    url = "https://www.amazon.in/s?i=electronics&bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc&qid=1628231459&rnid=3837712031&ref=sr_pg_1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    #Step 2 :parse the html
    soup = BeautifulSoup(htmlcontent,"html.parser")   
    for d in soup.findAll('div', attrs={'class':'a-section a-spacing-medium'}):
        name = d.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        image = d.find('img', attrs={'class':'s-image'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        user_rated = d.find('span', attrs={'class':'a-size-base'})
        price = d.find('span', attrs={'class':'a-price-whole'})
        
        nm=name.get_text()
        img=image.get('src')
        rat=float(rating.text[slice(3)])
        users_rat=user_rated.get_text()
        pric=price.get_text()

        pro_data = Products(name=nm,image=img,rating=rat,user_rated=users_rat,price=pric)
        pro_data.save()
    return HttpResponseRedirect('/') 

