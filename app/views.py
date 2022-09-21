from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import pickle
import json
from keras.models import load_model
from .bot import predict_class, get_response

intents = json.loads(open('resources/job_intents.json').read())
words = pickle.load(open('resources/words.pkl', 'rb'))
classes = pickle.load(open('resources/classes.pkl', 'rb'))
model = load_model("resources/chatbot_model (3).h5")

def index(request):
    return render(request, "build/index.html")
# Create your views here.
class DekutViewset(viewsets.ViewSet):
    def requestbot(self,request):
        if request.method == "POST":
            question = request.data["question"]
            ints = predict_class(question)
            res = get_response(ints, intents)
            return Response({'answer':res})
