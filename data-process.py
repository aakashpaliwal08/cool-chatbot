import numpy as np
import pandas as pd
import config 
import os
import re

lines=open('movie_lines.txt').read().split('\n')
def get_line() :
  id_idvalueline = {}
  for i in lines:
        new_line = line.split(' +++$+++ ')
          if len(new_line) == 5:
            id2line[new_line[0]] = new_line[4]
    return id_idvalueline 
    
 def get_dir (): 
    lines=open('movie_lines.txt').read().split('\n')
    onv_lines = open('movie_conversations.txt').read().split('\n')
    return get_idr
    
    
conv_lines = open('movie_conversations.txt').read().split('\n')
def get_conversation(): 
    convs = [ ]
    for j in conv_lines[:-1]:
        new2_line = j.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
        convs.append(new2_line.split(','))
    return convs

 def split_dataset(convs, id2line):
    questions = []; answers = []
    for conv in convs:
        if len(conv) %2 != 0:
            conv = conv[:-1]
        for i in range(len(conv)):
            if i%2 == 0:
                questions.append(id2line[conv[i]])
            else:
                answers.append(id2line[conv[i]])

    return questions, answers    

   def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"n't", "not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,']", "", text)
    return text
   
# Cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))

# Cleaning the answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
