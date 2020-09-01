from django.shortcuts import render
from scholarly import scholarly


def home(request):
    return render(request, 'homepage.html')


def results(request):
    if request.method == "POST":
        search_word = request.POST['search']

    searchquery = scholarly.search_pubs(search_word)
    data = next(searchquery)
    # print(data.bib['url'])
    title = data.bib['title']
    author = data.bib['author']
    url = data.bib['url']

    return render(request, "homepage.html", {'title': title, 'url': url, 'author': author})
