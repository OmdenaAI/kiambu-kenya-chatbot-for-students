# import pickle
# from autocorrect import Speller
# import string
# import pandas as pd
# import json
# import string
# import random
# import nltk
# import numpy as num
# import nltk #Natural languange Processing tool
# from nltk.stem.lancaster import LancasterStemmer #model for stemming words
# from nltk.stem import WordNetLemmatizer 

# nltk.download('punkt')
# nltk.download('omw-1.4')

# stemmer = LancasterStemmer()
# # load saved model
# with open('resources/models_pkl' , 'rb') as f:
#     model = pickle.load(f)
# # Create your views here.
# lm = WordNetLemmatizer() 
# ourData = json.loads(open('resources/job_intents.json').read())
# print(ourData)

# def _lowercase(obj):
#     """ Make dictionary lowercase """
#     if isinstance(obj, dict):
#         return {k.lower():_lowercase(v) for k, v in obj.items()}
#     elif isinstance(obj, (list, set, tuple)):
#         t = type(obj)
#         return t(_lowercase(o) for o in obj)
#     elif isinstance(obj, str):
#         return obj.lower()
#     else:
#         return obj.translate(str.maketrans('', '', string.punctuation))


# def ourText(text):
#   spell = Speller()
#   newtkns = nltk.word_tokenize(spell(text.translate(str.maketrans('', '', string.punctuation))))
#   newtkns = [lm.lemmatize(word) for word in newtkns]
#   return newtkns

# def wordBag(text, vocab):
#   newtkns = ourText(text)
#   bagOwords = [0] * len(vocab)
#   for w in newtkns:
#     for idx, word in enumerate(vocab):
#       if word == w:
#         bagOwords[idx] = 1
#   return num.array(bagOwords)

# def Pclass(text, vocab, labels):
#   bagOwords = wordBag(text,vocab)
#   ourResult = model.predict(num.array([bagOwords]))[0]
#   newThresh = 0.2
#   yp = [[idx, res] for idx, res in enumerate(ourResult) if res > newThresh]

#   yp.sort(key=lambda x: x[1], reverse=True)
#   newList = []
#   for r in yp:
#     newList.append(labels[r[0]])
#   return newList

# def get_response(intents_list, intents_json):
#     tag = intents_list[0]
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if i['tag'] == tag:
#             ourResult = random.choice(i['responses'])
#             break
#     return ourResult

# def getRes(firstlist, fJson):
#   tag = firstlist[0]
#   listOfIntents = fJson["intents"]
#   for i in listOfIntents:
#     if i["tag"] == tag:
#       ourResult = random.choice(i["responses"])
#       break
#   return ourResult

# def predict_class(sentence):
#     # bow = wordBag(sentence)
#     # res = model.predict(num.array([bow]))[0]
#     ourClasses = []
#     newWords = []
#     documentX = []
#     documentY = []

#     for intent in ourData["intents"]:
#         for pattern in intent["patterns"]:
#             ournewTkns = nltk.word_tokenize(pattern)
#             newWords.extend(ournewTkns)
#             documentX.append(pattern)
#             documentY.append(intent["tag"])


#         if intent["tag"] not in ourClasses:
#             ourClasses.append(intent["tag"])

#     newWords = [lm.lemmatize(word.lower()) for word in newWords if word not in string.punctuation] 
#     newWords = sorted(set(newWords))
#     ourClasses = sorted(set(ourClasses))
#     intents = Pclass(sentence, newWords, ourClasses)
#     ourResult = getRes(intents, ourData)

#     return ourResult




# while True:
#     newMessage = input("")
#     ourClasses = []
#     newWords = []
#     documentX = []
#     documentY = []

#     for intent in ourData["intents"]:
#         for pattern in intent["patterns"]:
#             ournewTkns = nltk.word_tokenize(pattern)
#             newWords.extend(ournewTkns)
#             documentX.append(pattern)
#             documentY.append(intent["tag"])


#         if intent["tag"] not in ourClasses:
#             ourClasses.append(intent["tag"])

#     newWords = [lm.lemmatize(word.lower()) for word in newWords if word not in string.punctuation] 
#     newWords = sorted(set(newWords))
#     ourClasses = sorted(set(ourClasses))
#     intents = Pclass(newMessage, newWords, ourClasses)
#     ourResult = getRes(intents, ourData)
#     print(ourResult)





# import random
# import json
# import numpy as np
# from nltk.corpus import stopwords
# import pickle
# import nltk
# from nltk.stem import WordNetLemmatizer
# from keras.models import load_model
# from tensorflow.python.keras.backend import reset_uids
# model = load_model('resources/chatbot_model (1).h5')
# intents = json.loads(open('resources/job_intents.json').read())
# words = pickle.load(open('resources/words.pkl', 'rb'))
# classes = pickle.load(open('resources/classes.pkl', 'rb'))
# nltk.download('punkt')
# nltk.download('wordnet')
# stop_words = set(stopwords.words('english'))
# lemmatizer = WordNetLemmatizer()


# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     return sentence_words



# def bow(sentence, words, show_details = True):
#    # tokenize the pattern
#     sentence_words = clean_up_sentence(sentence)
#     # bag of words - matrix of N words, vocabulary matrix
#     bag = [0] * len(words)
#     for s in sentence_words:
#         for i, w in enumerate(words):
#              if w == s:

#                 bag[i] = 1
#                 if show_details:
#                     print("found in bag: %s" % w)
#                 return (np.array(bag))

# def predict_class(sentence, model):
#    # filter out predictions below a threshold
#     p = bow(sentence, words, show_details = False)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [
#     [i, r]
#     for i, r in enumerate(res) if r > ERROR_THRESHOLD
#     ]
# # sort by strength of probability
#     results.sort(key = lambda x: x[1], reverse = True)
#     return_list = []
#     for r in results:
#         return_list.append({
#             "intent": classes[r[0]],
#             "probability": str(r[1])
#         })
#     return return_list

# def getResponse(ints, intents_json):
#     tag = ints[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if (i['tag'] == tag):
#           result = random.choice(i['responses'])
#         break
#     return result


# def chatbot_response(msg):
#     ints = predict_class(msg, model)
#     res = getResponse(ints, intents)
#     return res



import random
import json
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from tensorflow.python.keras.backend import reset_uids
# nltk.download('punkt')
# nltk.download('wordnet')



lemmatizer = WordNetLemmatizer()
intents = json.loads(open('resources/job_intents.json').read())

words = pickle.load(open('resources/words.pkl', 'rb'))
classes = pickle.load(open('resources/classes.pkl', 'rb'))

model = load_model("resources/chatbot_model (3).h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list


# bot_name = "Carebot"

def get_response(intents_list, intents_json):
    try:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    except:
        result = "I do not know the answer to this yet. Perhaps rephrase it or type it differently?"
    return result





# while True:
#     message = input()
#     ints = predict_class(message)
#     res = get_response(ints, intents)
#     print(res)
    
