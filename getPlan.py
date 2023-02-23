import os
import openai
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

openai.api_key = ("ENTER YOUR OPENAI API KEY HERE")

gpt_prefix = "using the following things to do, "
gpt_prefix2 = " and the following restaurants, "
gpt_for = " create a vacation plan for  "
gpt_suffix2 = " days. Create a plan for a vacation with the output being the form of a python string. The output should have a similar format as this: 'Day 1: \nWalk around Central Park. Eat at Gramercy Cavern.\nDay 2:\netc."

@app.route("/getPlan", methods=["POST"])
def getRecs():
    body = request.get_json()
    logging.info("received request body: ")
    logging.info(body)
    gpt_thingsToDo = ""
    gpt_restaurants = ""
    if not (numDays := body.get("numDays")):
        return "numDays is a required field", 404
    if not (thingsToDo := body.get("thingsToDo")):
        return "thingsToDo is a required field", 404
    if not (restaurants := body.get("restaurants")):
        return "restaurants is a required field", 404
    for thingToDo in thingsToDo:
        gpt_thingsToDo += thingToDo
    for restaurant in restaurants:
        gpt_restaurants += restaurant
    
    gpt_prompt = gpt_prefix + gpt_thingsToDo + gpt_prefix2 + gpt_restaurants + gpt_in + str(numDays) + gpt_suffix
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    gpt_response = response['choices'][0]['text']
    return jsonify({"vacationPlan": gpt_response}), 200

if __name__ == "__main__":
    app.run()