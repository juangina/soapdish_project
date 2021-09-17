import re
import random
import nltk

from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from .nltk_utils.part_of_speech import get_part_of_speech
from .nltk_utils.tokenize_words import word_sentence_tokenize
from .nltk_utils.chunk_counters import np_chunk_counter, vp_chunk_counter

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

import json
from django.http import JsonResponse
from django.views.generic import View

from .models import Conversation_Meta, Conversation_Dialog
from store.utils import cookieCart, cartData, guestOrder

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        chat_text = request.POST['chat_text']
        cleaned = re.sub('\W+', ' ', chat_text)
        tokenized = word_tokenize(cleaned)
        stemmer = PorterStemmer()
        stemmed = [stemmer.stem(token) for token in tokenized]
        lemmatizer = WordNetLemmatizer()
        lemmatized = lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

        # sentence and word tokenize text here
        word_tokenized_text = word_sentence_tokenize(chat_text)
        # create a list to hold part-of-speech tagged sentences here
        pos_tagged_text = []
        # create a for loop through each word tokenized sentence here
        for each_sentence in word_tokenized_text:
        # part-of-speech tag each sentence and append to list of pos-tagged sentences here
            pos_tagged_text.append(pos_tag(each_sentence))
        # define noun phrase chunk grammar here
        chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
        # create noun phrase RegexpParser object here
        np_chunk_parser = RegexpParser(chunk_grammar)
        # define verb phrase chunk grammar here
        chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"
        # create verb phrase RegexpParser object here
        vp_chunk_parser = RegexpParser(chunk_grammar)
        # create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
        np_chunked_text = []
        vp_chunked_text = []
        # create a for loop through each pos-tagged sentence here
        for item in pos_tagged_text:
            # chunk each sentence and append to lists here
            np_chunked_text.append(np_chunk_parser.parse(item))
            vp_chunked_text.append(vp_chunk_parser.parse(item))
        # store and print the most common NP-chunks here
        most_common_np_chunks = np_chunk_counter(np_chunked_text)
        # store and print the most common VP-chunks here
        most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)

        # if request.user.is_authenticated:
        #     user_id = request.user.id
        messages.success(request, 'Your request has been submitted.  Here are the results of your submission.')
        context = {
            'chatbot': 'Welcome to the Soapdish Chatbot',
            'chat_text': chat_text,
            'cleaned': cleaned,
            'tokenized': tokenized,
            'stemmed': stemmed,
            'lemmatized': lemmatized,
            'word_tokenized_text' : word_tokenized_text,
            'pos_tagged_text': pos_tagged_text,
            'np_chunked_text': np_chunked_text,
            'vp_chunked_text': vp_chunked_text,
            'most_common_np_chunks': most_common_np_chunks,
            'most_common_vp_chunks': most_common_vp_chunks,
            'cartItems': cartItems
        }
        return render(request, "chatbot/home.html", context)

    sample_text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."
    context = {
        'chatbot': 'Welcome to the Soapdish Chatbot',
        'sample_text': sample_text,
        'cartItems': cartItems
        }
    return render(request, 'chatbot/home.html', context)


class ChatBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
            "Let's get this chat going.  What is your query?\n>> ",
            "I am looking forward to our chat.  What do you want to know?\n>> ",
            "I am ready to talk about Soapdish.  What can we start with?\n>> "
        )
    continue_chat = ('That was a good query.  This is fun.  Keep asking.\n>> ', 'That was a good query.  This is interesting.  Keep it coming.\n>> ', 'That was a good question.  This is exciting.  What else you want to know?.\n>> ', 'This explains a lot I hope.  This is fantastic.  Hope you have more quetions.\n>> ')

    def __init__(self):
        self.alienbabble = {'describe_soapdish_intent': r'.*what.*soapdish.*', 'answer_why_intent': r'.*why.*soapdish.*', 'cubed_intent': r'.*number (\d+)'
                                }
        self.chatted = False
    
    # Define .make_exit() here:
    def make_exit(self, reply):
        for negative_response in self.negative_responses:
            if negative_response in reply:
                if self.chatted == False:
                    print("Okay, thanks for visiting Soap Talk.  Come back anytime to catch the latest news from Soap Dish!")
                else:
                    print("Okay, thanks for chatting with Soap Dish.  Looking forward to our next chat.  Have a nice day!")
                return True
        for exit_command in self.exit_commands:
            if exit_command in reply:
                if self.chatted == True:
                    print("Okay, thanks for chatting with Soap Dish.  Looking forward to our next chat.  Have a nice day!")
                else:
                    print("Okay, thanks for visiting Soap Talk.  Come back anytime to catch the latest news from Soap Dish!")
                return True
            return False

    # Define .greet() below:
    def greet(self, will_help):
        self.name = input("Hi, I'm am a chatbot for Soapdish.  Welcome to Soap Talk.  Before we can chat, I would like some information from you.  What is your first name?\n>> ")
        
        will_help = input(f"Hi {self.name}.  I am looking forward to our chat.  Want to know the latest news in Soap Talk?\n>> ")
        
        if self.make_exit(will_help):
            return
        
        self.chatted = True  
        self.chat(will_help)

    # Define .chat() next:
    def chat(self, reply):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            print(self.match_reply(reply))
            reply = input(random.choice(self.continue_chat))

    # Define .match_reply() below:
    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            #print(regex_pattern) #debug printing
            found_match = re.match(regex_pattern, reply.lower())
            if found_match and intent == 'describe_soapdish_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])
        return self.no_match_intent()

    # Define .describe_planet_intent():
    def describe_planet_intent(self):
        responses = ('Soapdish is a home project to create vegetable-based soap', 'Soapdish create a variety of vegetable-based soap products.')
        return random.choice(responses)

    # Define .answer_why_intent():
    def answer_why_intent(self):
        responses = ('Soap ingredients are easy to find.', 'Soap is fun to make.', 'Everyone uses soap, so it is easy to share with people.')
        return random.choice(responses)
        
    # Define .cubed_intent():
    def cubed_intent(self, number):
        cubed_number = int(number)*int(number)*int(number)
        return f"The cube of {number} is {cubed_number}. Isn't that cool?"

    # Define .no_match_intent():
    def no_match_intent(self):
        return "Inside .no_match_intent()"                                                              


# This class does not have to handle a templete, 
# therefore you only need for it to dispatch get/post operations,
# hence the inheretance from View.
class ChatBotApiView(View):

    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # potential positive responses
    positive_responses = ("yes", "yep", "yeppers", "of course", "sure", "no problem")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    # random starter questions
    random_questions = (
            "Let's get this chat going.  What is your query?",
            "I am looking forward to our chat.  What do you want to know?",
            "I am ready to talk about Soapdish.  What can we start with?"
        )
    continue_chat = ('That was a good query.  This is fun.  Keep asking.', 'That was a good query.  This is interesting.  Keep it coming.', 'That was a good question.  This is exciting.  What else you want to know?.', 'This explains a lot I hope.  This is fantastic.  Hope you have more quetions.')

    soapdish_intent_options = {'describe_soapdish_intent': r'.*what.*soapdish.*', 'answer_why_intent': r'.*why.*soapdish.*'}

    def match_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                return True
        return False
    
    def match_negative(self, reply):
        for negative_response in self.negative_responses:
            if negative_response in reply:
                return True
        return False

    def match_positive(self, reply):
        for positive_response in self.positive_responses:
            if positive_response in reply:
                return True
        return False        

    def match_reply(self, reply, conversation_meta):
        for key, value in self.soapdish_intent_options.items():
            intent = key
            regex_pattern = value
            #print(regex_pattern) #debug printing
            found_match = re.match(regex_pattern, reply.lower())
            if found_match and intent == 'describe_soapdish_intent':
                conversation_meta.conversation_dialog_set.create(intent=intent)
                return self.describe_soapdish_intent(conversation_meta)
            elif found_match and intent == 'answer_why_intent':
                conversation_meta.conversation_dialog_set.create(intent=intent)
                return self.answer_why_soapdish_intent(conversation_meta)
        return self.no_match_intent(conversation_meta)

    # Define .describe_planet_intent():
    def describe_soapdish_intent(self, conversation_meta):
        responses = ('Soapdish is a home project to create vegetable-based soap', 'Soapdish create a variety of vegetable-based soap products.')
        response = random.choice(responses)
        conversation_meta.conversation_dialog_set.create(dialog=response)
        return response

    # Define .answer_why_intent():
    def answer_why_soapdish_intent(self, conversation_meta):
        responses = ('Soap ingredients are easy to find.', 'Soap is fun to make.', 'Everyone uses soap, so it is easy to share with people.')
        response = random.choice(responses)
        conversation_meta.conversation_dialog_set.create(dialog=response)
        return response

    # Define .no_match_intent():
    def no_match_intent(self, conversation_meta):
        response = "No intent.  We are just shooting the breeze!"
        conversation_meta.conversation_dialog_set.create(dialog=response)
        return response

    def post(self, request, *args, **kwargs):
        # get the data from the .ajax post request from JS script
        input_data = json.loads(request.body.decode('utf-8'))
        # print(input_data) # debug print statement
        # data will pbe a json object

        # verify that the key value pair identifier key is "text:"
        # this condition was mainly for the chatterbot app
        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        # extract string from json object for processing
        reply = input_data['text']
        # print(will_help) # debug print statement
        #  print(type(will_help)) # debug print statement

        reply = reply.lower()
        #print(reply) # debug print statment

        if reply == "hi soapdish" or reply == "hi soapdish." or reply == "hi soapdish!":
            conversation_meta, created = Conversation_Meta.objects.get_or_create(user=request.user)
            if created == True:
                response = "Hi, I'm am a chatbot for Soapdish.  Welcome to Soap Talk.  Before we can chat, I would like some information from you.  What is your first name?"
            elif created == False and not conversation_meta.name:
                response = "Welcome to Soap Talk.  Before we can chat, I would like some information from you.  What is your first name?"
            elif created == False and conversation_meta.name:
                    response = response = f"Welcome to Soap Talk {conversation_meta.name}.  You can type something else to continue the conversation."
            else:
                response = "I am sorry, I did not understand.  Please enter your response again."
        elif self.match_exit(reply):
            conversation_meta, created = Conversation_Meta.objects.get_or_create(user=request.user)
            if created == True:
                response = "Please type 'Hi Soapdish' to start the chat."
                Conversation_Meta.objects.filter(user = request.user).delete()
            elif created == False and conversation_meta.name:
                response = f"Okay {conversation_meta.name}, thanks for visiting Soap Talk.  Come back anytime to catch the latest news from Soap Dish!"
                Conversation_Meta.objects.filter(user = request.user).delete()
            else:
                response = "Okay, thanks for visiting Soap Talk.  Come back anytime to catch the latest news from Soap Dish!"
                Conversation_Meta.objects.filter(user = request.user).delete()
        else:
            conversation_meta, created = Conversation_Meta.objects.get_or_create(user=request.user)
            if created == False and conversation_meta.dialog_started == False:
                conversation_meta.name = reply
                conversation_meta.dialog_started = True
                conversation_meta.temp_data = 'query1'
                conversation_meta.save()
                response = f"Hi {conversation_meta.name}.  I am looking forward to our chat.  Want to know the latest news in Soap Talk?"
                conversation_meta.conversation_dialog_set.create(dialog=response)
            elif created == False and conversation_meta.dialog_started == True and conversation_meta.temp_data == 'query1':
                conversation_meta.conversation_dialog_set.create(dialog=reply)
                conversation_meta.temp_data = 'query'
                conversation_meta.save()
                response = f"Great {conversation_meta.name}.  What is your query?"
                conversation_meta.conversation_dialog_set.create(dialog=response)
            elif created == False and conversation_meta.dialog_started == True and conversation_meta.temp_data == 'query':
                conversation_meta.conversation_dialog_set.create(dialog=reply)
                response = self.match_reply(reply, conversation_meta)
                conversation_meta.conversation_dialog_set.create(dialog=response)

        #    response = "I am sorry, I did not understand.  Please type 'Hi Soapdish' to start the chat."

        # setup response from soapdish chatbot for transfer response to client
        # format must be a python dictionary object
        response_dict = {}
        response_dict['text'] = response
        try: 
            Conversation_Meta.objects.get(user=request.user)
            response_dict['chat_status'] = True
        except:
            response_dict['chat_status'] = False
        #print(response_dict) # debug print statement

        return JsonResponse(response_dict, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatbot.name
        })
