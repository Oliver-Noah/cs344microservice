How to request data:

The microservice accepts HTTP Post requests to both the /getPlan and getRecommendations endpoint, depending on which service is being called. In this example, the URL is http://localhost:5000/getPlan and http://localhost:5000/getRecommendations.

For the getRecommendations endpoint, the body of the request must be in the form of the following:

{
    "location": "New York City",
    "recommendationType": "thingsToDo"
}

Note that the recommendation type must be either thingsToDo or restaurants.

An example call to this using the fetch API would look as follows:

const data = {
    "location": "New York City",
    "recommendationType": "restaurants"
}

//note this should be an absolute url
const resp = await fetch(url/totalTime, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        "Content-Type": "application/json",
    },
})

For the getPlan endpoint, the body of the request must be in the form of the following:

{
    "numDays": 3,
    "thingsToDo": [
        "Walk around Central Park",
        "Go to the Empire State Building",
        "Go to Times Square"
    ],
    "restaurants": [
        "Gramercy Tavern",
        "abc cafe"
    ]
}

thingsToDo and restaurants should be an array, and there is no limit or minimum on how many indexes need to be in that array. numDays should be an int.

An example call to the getPlan endpoint will be as follows

const data = {
    "numDays": 3,
    "thingsToDo": [
        "Walk around Central Park",
        "Go to the Empire State Building",
        "Go to Times Square"
    ],
    "restaurants": [
        "Gramercy Tavern",
        "abc cafe"
    ]
}

//note this should be an absolute url
const resp = await fetch(url/totalTime, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        "Content-Type": "application/json",
    },
})

How to receive data:

When receiving data from getRecommendations endpoint, a json object titled "recs" will be received. The recs object will be an array with three recommendations that pertain to the inputted location. 

When receiving data from getPlan endpoint, a json object titled "vacationPlan" will be received. This object will just contain a string with the generated vacatin plan.

UML Diagram:

In repo under "UML Sequence Diagram.jpg