
# py-gtts
================

An unofficial repository for Google Text-to-Speech (gTTS) using subprocess and pydub.

## Requirements
---------------

This project requires the following dependencies:

* certifi==2024.8.30
* charset-normalizer==3.4.0
* click==8.1.7
* gTTS==2.5.3
* idna==3.10
* pydub==0.25.1
* requests==2.32.3
* urllib3==2.2.3

You can install these dependencies using pip:

### Example as module
```bash
pip install -r requirements.txt


from gtts import tts

tts('hello. hi, sir how are you. my name shreya')

Note that I've included the requirements from `requirements.txt` in the README file, as well as a brief description of the project and its usage. I've also included the license and credits information from the `LICENSE` file. Let me know if you'd like me to make any changes!
```

### gTTS doc
for localiz accent use --tld custom
refre this link https://gtts.readthedocs.io/en/latest/module.html#localized-accents
