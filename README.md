Open Guelph Hackathon - February 22nd-23rd, 2014
===

Saturday, 12:00 AM
---
  This repo contains my work for the Open Guelph hackathon, taking place over 24 hours from the morning of February 22nd until that of the 23rd.

  I plan to use the Flask framework to create a web application that will give directions to local parks and attractions. Here's to a productive weekend!

Saturday, 12:00 PM
---
  And we're off! 

  Fairly slow start. Created a `scripts` directory to hold the Python scripts I'm using to parse data. At present it holds one script: `parseRoutes`, which parses the `stop_times.txt` file, converting the data into `Route` classes and storing it in a pickled file.

Saturday, 3:00 PM
---
  Well, five hours in and my head is starting to hurt. :P

  I've been focussing on the bus stops themselves now, using the data in `stops.txt`. I spent a bunch (probably too much) time fixing `stops.txt`, since it had a bunch of typos and different naming conventions and I had to wrap my head around a few things. Currently, I am assuming stops longitude and latitude data is 100% correct, and that is how I am differentiating stops. The `stops.txt` file being used currently has been modified, the original is saved as `old_stops.txt.`

  Having done all of that, there is now a new parsing script called `parseStops` (which takes bus stop data and puts sorts it with `Stop` classes, containing the stop's name, latitude, longitude, and routes that use it) and a scriptcalled `stopExperiments` which I use to play with the data.

Saturday, 4:30 PM
---
  After a brief but terrifying episode featuring a non-functional computer, I've added a `parseParks` script.

Saturday, 7:15 PM
---
  Whew! There's light at the end of the tunnel!

  I have started working through bus route calculations in the `calculations` script. At present, I can locate the nearest bus stop to a latitude/longitude pair and determine when the next bus leaves from a specified stop. (Any stop, in theory, but I only care about the UC and Guelph Central)

Saturday, 10:45 PM
---
  Past the halfway point, beginning to feel it. A bit behind schedule, but the back-end is close enough to done I can justify starting the front end.

  At present I can find the closest bus stop to a co-ordinate, find a bus route that reaches it, say when the next bus leaves, and determine what stops are along the way. However, the data my code generates at present is correct but often far from efficient. I'll have to go back and fix that later.

  I reverted the bus stop information to the official file, and tweaked my code to work around it.

Sunday, 2:30 AM
---
  I feel like I haven't accomplished much in the last four hours, but I haven't stopped working so I must have done something.

  Created generic `Place` class and converted `Park`s into `Place`s. Also made some headway on the webapp front-end.
