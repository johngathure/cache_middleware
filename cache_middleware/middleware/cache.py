from django.conf import settings
from django.core.cache import cache


class CacheMiddleware(object):
    def process_request(self, request):
        """
        All requests go through this method.
        It checks if the page is in cache and returns
        it if it exists, else returns none. The request is 
        then processed in the view
        """
        cached_page = cache.get(request.path)
        if cached_page:
            return cached_page
        return None

    def process_response(self, request, response):
        """
        All responses go through this method.
        It loops through all the urls defined
        in the settings.py file and checks whether
        the one being requested has been cached, if not
        the page is cached.
        ttl - time to live. on the cache
        if the page being requested is not in the cache urls setting,
        then proceed
        """
        cache_settings = settings.CACHE_URLS
        for (url, ttl) in cache_settings:
            if request.path == url and not cache.get(url):
                cache.set(url, response, ttl)
                return response
        return response
