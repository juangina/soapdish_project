# regex for removing punctuation!
import re
# nltk preprocessing magic
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

def index(request):
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
        }
        return render(request, "chatbot/home.html", context)

    sample_text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."
    context = {
        'chatbot': 'Welcome to the Soapdish Chatbot',
        'sample_text': sample_text
        }
    return render(request, 'chatbot/home.html', context)
