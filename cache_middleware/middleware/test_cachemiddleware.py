from mock import Mock

from django.test import TestCase
from django.core.cache import cache

from .cache import CacheMiddleware


class CacheMiddlewareTest(TestCase):

    def setUp(self):
        self.request = Mock()
        self.response = Mock()
        self.request.path = "/todos/view_todos/"
        self.cache_data = [
            {
                "task": "recieve test",
                "id": "06c3ab0a-1c7d-42fe-9388-10603f9f39ea",
                "is_completed": True
            },
            {
                "task": "do test project",
                "id": "8521cccb-f683-4824-98f2-fa46c67526f1",
                "is_complete": True
            }
        ]
        self.cache_middleware = CacheMiddleware()

    def test_request_processing_for_not_cached_page(self):
        # Page("/todos/view_todos/") has not been cached yet.
        # process request should return None

        # clear any data that might be in cache
        cache.clear()

        # Process the request of the none cached page
        response = self.cache_middleware.process_request(self.request)

        # Should return None. This means it will hit the view.
        self.assertEqual(response, None)

    def test_request_processing_for_cached_page(self):
        # cache data(self.cache_data) for 25 seconds
        # with the above url (self.request.path)
        cache.set(self.request.path, self.cache_data, 25)

        # request for the page
        response = self.cache_middleware.process_request(self.request)

        # should return the cached data and not none.
        # this means it will not hit the view.
        self.assertEqual(response, self.cache_data)

        cache.clear()
