from ast import parse
from django.shortcuts import render
from django.views.generic import View
from requests import request
from app.utils import get_id

# url = 'https://www.youtube.com/watch?v=TSPGlIkTsVk'
# parsed_url = urlparse(url)
# captured_value = parse_qs(parsed_url.query)['v'][0]
# Create your views here.


class HomeView(View):

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        video_id = get_id(request.POST.get("video_url"))
        cover_image_url = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"

        return render(request, "result.html", context={"image": cover_image_url})
