# UOttaHack2019-BreadCrumbz

This was our final project for UOttaHacks 2019 which placed 4th overall.

Inspiration

We were inspired to find a way to serve the community while rewarding the good samaritans, resulting in a win-win situation.

What it does

When the user enters their final route destination, our program utilizes many different google maps APIs to calculate the most efficient route to pickup leftover food from a restaurant that broadcasted their availability via a webpage and nearby homeless shelters from the final destination. Our algorithm optimizes the route to reduce driving time to make it as convenient as possible. Twilio's API then contacts both the driver and homeless shelter to determine if the package was actually delivered (or stolen). Since it was built using RESTful APIs and micro-services, it is highly scalable and can respond to increase in demands seamlessly.

How we built it

We created a web application using express.js that employs Restful APIs allowing us to connect the community with restaurants, supermarkets and homeless shelters. Restaurants are able to post their location when they have excess food through a post request. Then, a notification is sent to all registered drivers who are within a specified range. A Google Maps API then calculates the most efficient route and whoever has the shortest route takes the delivery request by utilizing Nearby Searches and Directions API. Then, Twilio's API waits for a keyword "Delivered " and obtained order number. This order number is then confirmed by calling the shelter on file and asking them if they did receive that specific order.

Challenges we ran into

When we were planning our project, we were attempting to use Solaces API, however their services were blocked by the school's network. They were unable to provide a reasonable solution, so we had to find other alternatives. Upon realizing this, team morale dropped drastically and one of our team members decided to leave and stay at home instead. In the end, we followed through with the idea and have succeeded in overcoming the obstacle.

Accomplishments that we're proud of

All of us have tackled problems that we are not familiar with which helped us learn a lot about how API's work, different languages, and algorithms. We also learned how to make codes compatible from different languages and how to read/parse json files.

What we learned

We have all learned different languages while reinforcing our python knowledge. Now, we are more familiar with the syntax and understand how the language is structured.
