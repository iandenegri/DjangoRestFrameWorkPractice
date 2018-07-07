from django.http import JsonResponse, HttpResponse

class HttpResponseMixin(object):
    is_json=False
    def render_to_response(self, data, status=200):
        content='text/html'
        if self.is_json:
            content= 'application/json'
        return HttpResponse(data, content_type=content, status_code=status)


#####################################

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        # we need to make sure context will work as a JsonResponse
        return JsonResponse(self.get_data(context), **response_kwargs)

    # This function will verify or convert the data to a format that will work
    # with the JsonResponse
    def get_data(self, context):
        return context
