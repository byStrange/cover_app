
from urllib.parse import parse_qs
from urllib.parse import urlparse
def get_id(url):
    url = urlparse(url)
    video_id  = parse_qs(url.query)['v'][0]
    return video_id