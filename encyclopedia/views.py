from django.shortcuts import render
from .util import get_entry
import markdown2
import os
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_detail(request, title):
    entry_content = get_entry(title)
    return render(request, 'entry_detail.html', {'title': title, 'content': entry_content})
''' def pages():
        util.get_entry(title)
    '''

def content_page(request,filename):
    file_path = os.path.join('entries', filename + '.md')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown2.markdown(content)
    except FileNotFoundError:
        html_content = "<p>File Not Found.</p>"

    return render(request, 'encyclopedia/contents.html', {'html_content': html_content})
        