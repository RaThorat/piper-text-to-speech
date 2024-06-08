# Script for my "Thorsten-Voice" step-by-step tutorial on "Running a local Piper TTS server and use it with Python on Linux"
# https://youtu.be/pLR5AsbCMHs

import requests

textToSpeak = "Ondanks een verhoging van budgetten met bijna een derde sinds 2013, slaagt justitie er minder goed in witteboordencriminelen veroordeeld te krijgen, blijkt uit FD-onderzoek."
urlPiper = "http://localhost:5000"
outputFilename = "output.wav"

payload = {'text': textToSpeak}

r = requests.get(urlPiper,params=payload)

with open(outputFilename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
