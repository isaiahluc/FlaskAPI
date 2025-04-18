# How to call API



1. Open browser and go to
http://34.66.193.111:5002/api/hello

Receive:
{"message":"Hello, world!"}






2. Open browser and go to
http://34.66.193.111:5002/api/secure-data

Include the line:
Authorization: Bearer bviurwbrvuijv1256

If done correctly, you’ll see:
{"secret":"This is protected info!"}





3. Pick one of the cities I set up (London, New York, Tokyo, Sydney, Paris…)

Open browser and go to
http://34.66.193.111:5002/api/time/London
(swap “London” for whichever city you want)

Include token header:
Authorization: Bearer bviurwbrvuijv1256

If in list, you get back:

“capital”: *the name you asked for*

“local_time”: *what time it is there right now*

“utc_offset”: *how many hours ahead or behind UTC that place is*

If you ask for a city we don’t know, you’ll get back an error telling you which capitals we do support
