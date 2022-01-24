#!/bin/python3

import openai
import json
import random

#### ACCESSING GPT-3 API ########################### 

api_filename = r"/home/me/.apikey"

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


openai.api_key = get_file_contents(api_filename)


## source: https://github.com/dylburger/reading-api-key-from-file/blob/master/Keeping%20API%20Keys%20Secret.ipynb

#### LOADING DICKENS' ENTIRE CORPUS AND SPLITTING INTO SENTENCES ########################### Used bash to concat all cleaned Dickensbooks.txt from the dropbox
#### cat * > dickens_corpus.txt

#from nltk import sent_tokenize

#corpus_file= r"/home/me/gpt3-victoria/dickens_corpus.txt"
#corpus = open(corpus_file,'rt')
#text = corpus.read()
#corpus.close()

#sentences = sent_tokenize(text)

with open(r"/home/me/gpt3-victoria/dickens_sent","r") as fp:
    sent = json.load(fp)

### source: https://machinelearningmastery.com/clean-text-machine-learning-python/

#MAKING PROMPT-COMPLETIONS W/ RANDOM SAMPLING TO FINE-TUNE GPT3
#{"prompt": "<prompt text>", "completion": "<ideal generated text>"}

#sampler: List -> JSONL pair
def sampler(l):
    r = random.randint(0,len(l)-2)
    return({"prompt":l[r],"completion":l[r+1]})

#with open(r"samples.json","w") as outfile:
#    for i in range(1,100):
#        outfile.write(json.dumps(sampler(sent)))
#        outfile.write('\n')

##################USING THE FINETUNED MODEL TO RESURRECT DICKENS#######################

#x=openai.Completion.create(
#    model="davinci:ft-personal-2022-01-24-01-21-08",
#    prompt="The coach lumbered on again, with heavier wreaths of mist closing round it as it began the descent.",
#    max_tokens=20,
#   temperature=.7
#    )
#print(x["choices"][0]["text"])

prompts = []

for i in range(1,20):
    prompts.append(sampler(sent)['prompt'])

completions = []

for j in range(0,19):
    completions.append(openai.Completion.create(
        model="davinci:ft-personal-2022-01-24-01-21-08",
        prompt=prompts[j],
        max_tokens=20,
        temperature=.7)["choices"][0]["text"])



#TODO: CHECK FOR OVERFITTING - ENSURE OUTPUT TEXT IS NOT IN DICKENS' CORPUS
#TODO: strip new lines \n
#TODO: add more authors
#TODO: point AA model at it

#response = openai.Completion.create(engine="text-davinci-001", prompt="Say this is a test", max_tokens=6)
# to print:  print(response["choices"][0]["text"])
