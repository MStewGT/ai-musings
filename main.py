import random
#Retrieve API token from environment variable
from decouple import config
from post_twitter import tweet
openai_token = config('OPENAI_TOKEN')

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
    openai.api_key = openai_token
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=input,
        temperature=0.7,
        max_tokens=69,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

#Get words, generate input, submit to AI
prompts = [
    "Write a Shakespearean sonnet about ",
    "Write a poem in the style of Edgar Allen Poe about ",
    "Write a love song about ",
    "Write a haiku about ",
    "Write a story in pig latin about "
    ]
input = random.choice(prompts) + random_words() + "."
output = submit_to_ai(input)

#Extract 'text' property and split string after the last period
text = output['choices'][0]['text']
text = text.split('\n', 1)[1]
text = text.rsplit('.', 1)[0]

#Debugging
print(input)
print (text)

#Tweet the output
tweet(text)