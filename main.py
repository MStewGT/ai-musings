#Retrieve API token from environment variable
from decouple import config
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
    import requests
    url = 'https://api.openai.com/v1/engines/davinci/completions'
    headers = {
        'Authorization': 'Bearer {}'.format(OPENAI_TOKEN),
    }
    data = {
    'prompt': input,
    'max_tokens': 69,
    'temperature': 0.7,
    'top_p': 0.9,
    'n': 10
    }
    response = requests.post(url, headers=headers, json=data)
    json_response = response.json()
    return json_response

#Get words, generate input, submit to AI
words = random_words(),random_words()
input = "What are your thoughts on " + words[0] + " and " + words[1] + "?"
output = submit_to_ai(input)
print (words,output)