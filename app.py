import os
import openai
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

openai.api_key = ("YOUR API KEY HERE")


@app.route("/getRecommendations", methods=["POST"])
def getRecs():

    gpt_thingsToDo = "Give three recommendations for "
    gpt_restaurants = "Give three restaurant recommendations for "
    gpt_in = " in "
    gpt_suffix = ". The recommendations should be given in a numbered list, with each recommendation on a new line. It should like the following: 1. Recommendation 1\n2. Recommendation 2\n 3. Recommendation 3"

    gpt_responseList = []

    body = request.get_json()
    logging.info("received request body: ")
    logging.info(body)

    if not (location := body.get("location")):
        return "location is a required field", 404
    if not (recommendationType := body.get("recommendationType")):
        return "recommendationType is a required field", 404
    
    if recommendationType == "thingsToDo":
        gpt_prompt1 = gpt_thingsToDo + recommendationType + gpt_in + location + gpt_suffix
        logging.info(f"prompt: {gpt_prompt1}")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=gpt_prompt1,
            temperature=0.5,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
    
    elif recommendationType == "restaurants":
        gpt_prompt1 = gpt_restaurants + recommendationType + gpt_in + location + gpt_suffix
        logging.info(f"prompt: {gpt_prompt1}")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=gpt_prompt1,
            temperature=0.5,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
    
    else:
        return "not a valid recommendationType", 404
    
    logging.info(f"response: {response}")
    gpt_responseList = response['choices'][0]['text'].split('\n')
    logging.info(f"response list: {gpt_responseList}")
    gpt_responseList.remove("")
    gpt_responseList.remove("")
    return jsonify({"recs": gpt_responseList}), 200
    

@app.route("/getPlan", methods=["POST"])
def getPlan():

    gpt_prefix = "using the following things to do, "
    gpt_prefix2 = " and the following restaurants, "
    gpt_for = " create a vacation plan for  "
    gpt_suffix2 = " days. Create a plan for a vacation with the output being the form of a python string. The output should have a similar format as this: 'Day 1: \nWalk around Central Park. Eat at Gramercy Cavern.\nDay 2:\netc."

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
    
    gpt_prompt = gpt_prefix + gpt_thingsToDo + gpt_prefix2 + gpt_restaurants + gpt_for + str(numDays) + gpt_suffix2
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
