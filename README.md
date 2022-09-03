# AI Musings
A Python Twitter bot that generates and posts random musings using a series of APIs.

### Random word generator
The script first gets a couple of random words by making calls to an API @ https://random-word-api.herokuapp.com. It then inserts these words into a predetermined prompt which will be fed to the AI.

### Sumbit input to AI
The script then calls the Davinci Completion API at https://beta.openai.com/ using the constructed input prompt.

### Output cleanup
Next the script extracts the 'text' property from the json return of the AI API and cuts off anything after the last period to try and account for any sentences the AI might not have been able to finish in the provided token length. This was set to try and keep the AI's response within the character limiation of a standard Tweet.

### Tweet submission
Finally, the script uses the Tweepy library to authenticate to the Twitter account and make a post using the generated content.

### Necessary packages
- python-decouple
- openai
- tweepy
