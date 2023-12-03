from django.shortcuts import render, redirect
from .util import get_entry, list_entries, save_entry
import markdown2
import os
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_detail(request, title):
    entry_content = get_entry(title)

    if entry_content is None:
        return render(request, 'encyclopedia/404.html', status=404)
    

    return content_page(request, filename=title)


def content_page(request,filename):
    file_path = os.path.join('entries', filename + '.md')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown2.markdown(content)
    except FileNotFoundError:
        html_content = "<p>File Not Found.</p>"

    return render(request, 'encyclopedia/wiki.html', {'html_content': html_content, 'filename': filename})




def search_results(request):
    
    query = request.GET.get('q', '')
    entries = list_entries()

    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

    if matching_entries:
        if len(matching_entries) == 1 and matching_entries[0].lower() == query.lower():
            return entry_detail(request, title=matching_entries[0])
        
        return render(request, 'encyclopedia/search_results.html', {'results': matching_entries, 'query': query})
    
    else:
        return render(request, 'encyclopedia/search_results.html', {'results': entries, 'query': query})


def new_page(request):

    if request.method == 'POST':

        title = request.POST.get('title', "")
        content = request.POST.get('content', "")

        if not title or not content:
            error_message = "Title and Content are both required."
            return render(request, 'encyclopedia/new_page.html', {'error_message': error_message})

        if get_entry(title) is not None:
            error_message = f"Title '{title}' is already in use. Please pick another one."
            return render(request, 'encyclopedia/new_page.html', {'error_message': error_message})
    
        save_entry(title, content)
        return redirect(entry_detail, title=title)

    else:
        return render(request, 'encyclopedia/new_page.html')