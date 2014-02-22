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
