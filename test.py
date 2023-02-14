import os
import openai

openai.api_key = ("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")

gpt_thingsToDo = "Give three recommendations for thingsToDo in London. The recommendations should be given in the form of an array within a json object titled recs. The json object should not have any newline operators, and should all be on the same line. Each array index should be separated by a comma and space"
gpt_restaurants = "Give three restaurant recommendations for restaurants in New York City. The recommendations should be given in the form of an array within a json object titled recs. The json object should not have any newline operators in it, and should all be on the same line"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_thingsToDo,
  temperature=0.5,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


print(response['choices'][0]['text'])
