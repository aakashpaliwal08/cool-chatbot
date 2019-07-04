import config 
import os

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
