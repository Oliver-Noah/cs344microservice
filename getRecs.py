import os
import openai
import logging
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

openai.api_key = ("ENTER YOUR OPENAI API KEY HERE")

gpt_thingsToDo = "Give three recommendations for "
gpt_restaurants = "Give three restaurant recommendations for "
gpt_in = " in "
gpt_suffix = ". The recommendations should be given in the form of an array within a json object titled recs. The json object should not have any newline operators, and should all be on the same line"

@app.route("/getRecommendations", methods=["POST"])
def getRecs():
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
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt1,
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        gpt_responseList = response['choices'][0]['text'].split(",")
        return jsonify({"recs": gpt_responseList}), 200
    if recommendationType == "restaurants":
        gpt_prompt1 = gpt_restaurants + recommendationType + gpt_in + location + gpt_suffix
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt1,
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        gpt_responseList = response['choices'][0]['text'].split(",")
        return jsonify({"recs": gpt_responseList}), 200
    else:
        return "not a valid recommendationType", 404

if __name__ == "__main__":
    app.run()

