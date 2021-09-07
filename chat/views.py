import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer

# This class sole job is the render a template, 
# hence the inheretance from TemplateView.
class ChatterBotAppView(TemplateView):
    template_name = 'chat/app.html'

# This class does not have to handle a templete, 
# therefore you only need for it to dispatch get/post operations,
# hence the inheretance from View.
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """


    chatterbot = ChatBot(**settings.CHATTERBOT)
    #print(settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))
        print(input_data)

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)
        #print(type(response))

        response_data = response.serialize()
        #print(type(response_data))

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

