from django.shortcuts import render
from . import download_trailers as dl
import os.path

homedir = os.path.expanduser("~") + '/Downloads/'


def download_trailer(request):
    template_name = 'imovie/index.html'
    context = {}
    if request.method == 'POST':
        page_url = str(request.POST.get('url'))
        print(page_url)
        if page_url.startswith('http://trailers.apple.com/') or page_url.startswith('https://trailers.apple.com/'):
            download_all_urls = page_url
            hg_trailers = dl.get_trailer_file_urls(
                page_url, '480', 'trailers', download_all_urls)

            for trailer in hg_trailers:
                print(trailer)
                if trailer['type'] == 'Trailer':
                    context['message'] = 'downloading'
                    filename = dl.get_trailer_filename(
                        trailer['title'], trailer['type'], trailer['res'])
                    dl.download_trailer_file(
                        trailer['url'], homedir, filename)
        else:
            context['message'] = 'error'
            print(context)

    print(context)
    return render(request, template_name, context)
