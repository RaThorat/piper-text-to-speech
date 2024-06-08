# piper-text-to-speech
Running a local Piper TTS server with Python on ubuntu 24.04

# Youtube source / Thorsten Mueller
https://www.youtube.com/watch?v=pLR5AsbCMHs&t=219s 
https://github.com/thorstenMueller/youtube/tree/main/TTS/PiperTTS 

# Download requied voices from Piper:
[https://github.com/rhasspy/piper/blob/master/README.md ](https://github.com/rhasspy/piper/blob/master/README.md#voices)

# To activate virtual environment from terminal:
source name_of_environment/bin/activate

# To run the model in server:
(.venv) (base) gebruiker@N141ZU:~/anaconda3/envs/piper/models$ python3 -m piper.http_server --model nl_NL-mls-medium.onnx


# terminal outside virtual environment, to check if the server is working:
(base) gebruiker@N141ZU:~/anaconda3/envs/piper$ curl -G --data-urlencode 'text=Dit is een tekst.' -o test.wav 'localhost:5000'

# run the python script with the text:
(base) gebruiker@N141ZU:~/anaconda3/envs/piper$ python3 test.py
