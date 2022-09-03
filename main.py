#Retrieve API token from environment variable
from decouple import config
from post_twitter import tweet
OPENAI_TOKEN = config('OPENAI_TOKEN')

#Function to get a random word from an api
def random_words():
    import requests
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    data = response.json()
    word = data[0]
    return word

#Function to submit the input to the AI
def submit_to_ai(words):
    import openai
    openai.api_key = OPENAI_TOKEN
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="What are your thoughts on space and synthwave.",
        temperature=0.7,
        max_tokens=69,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

#Get words, generate input, submit to AI
words = random_words(),random_words()
input = "What are your thoughts on " + words[0] + " and " + words[1] + "?"
output = submit_to_ai(input)
#Cutoff 'output' string after the last period
#output = output.rsplit('.', 1)[0]
print (words,output)


#Tweet the output
#tweet(output)