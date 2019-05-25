<p align="center"><a href="https://github.com/absolum1"
target="_blank"><br><img width="200" src="https://absolum.nl/assets/images/absolum-logo1.svg"></a></p>


<h1 align="center">Client Password Generator</h1>


<p align="center">Easy to remember passphrase that can be used as a master password, we've made this for our clients but anyone is free to use it.</p>

<p align="center">Soon to be Abraxas.</p>

<p align="center"> 
<a href="https://absolum.nl"><img src="https://img.shields.io/badge/website-absolum.nl-lightgrey.svg" alt="Website"></a>
<a href="https://github.com/absolum1"><img src="https://img.shields.io/badge/build-success-lightgrey.svg" alt="Build"></a>
<a href="https://absolum.nl/Licenses"><img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" alt="License"></a>
</p>


## Tags
- :bulb: Easy to remember
- :lock: Secure passphrases
- 🎉 Open source

## How to use it?
#### Notes
Currently CPG is only available on the command-line we are working to create a secure website to generate these
passphrases with multiple functions for example:
- Choosing a wordlist
- Number of words used
- Amount of passphrases to generate
- Time to hack these passphrases*
- Adding a personal wordlist (please add these to the repo to share them)*
We're also converting the python app to a command-line package so everyone can download it from their favorite package manager and generate passphrases with flags like -w 4 to use four words instead of the standard three.

* = not a priority

#### Guide
- Clone the repository: ```git clone https://github.com/Absolum1/CPG.git```
- ```cd``` into the folder ```CPG/python/``` by: ```cd CPG/python```
- Run the script by: ```python cpg.py```
- Tip: use the ```repeat x``` (replace x with the amount of passphrases you want) command before the run script command ```python cpg.py``` to get multiple passphrases, example ```repeat 10 python cpg.py``` (to get 10 generated passphrases)


## Why CPG?
This tool aims to generate secure master passwords according to our standards for our clients.

Some of our clients havent moved on to password managers (like LastPass) yet, and one of the biggest hassles is getting them to pick a secure master password.

They go with an easy unsecure password or one thats really easy to guess.
Here are a few very generous examples (unfortunately they are usually worse) and whats wrong with them:
#### Chantal231!@
- Chantal is a common name so it will likely be in a dictionary already.
- The user's kid is called Chantal.
- 231 is a variation of 123 which is pre baked into any attack.
- !@ are the two first special characters and are most used, using #$%^*()-_=+/?.,<> are a lot more secure because they appear less.
#### Kitchen731#!
- Kitchen is in the top 10000 English words used so it could appear in a dictionary, although usually hackers prefer 1000-5000 words because they yield more results and work faster.
- The user who created this password, loves cooking and she happens to be very open about that on social media.
#### BaseballLawyerChuck1271999!@
- The words "Baseball" and "Lawyer" are both in the top 10000 English words used so they could appear in a dictionary, although usually hackers prefer 1000-5000 words because they yield more results and work faster.
- The user is a proud member of a lawyers baseball team.
- The user's kid "Chuck" is born on 12-Juli-1999.
- !@ are the two first special characters and are most used, using #$%^*()-_=+/?.,<> are a lot more secure because they appear less.

Most of the passwords I see or hear of being used are terrible, some appear to be good like BaseballLawyerChuck1271999!@ but could be hacked quite quickly.

To leave all the mathematics out of it we've set a standard for our own master passwords and those of our clients that should keep them secure for the following years, and most likely any password will be better than the one they use already you can see it below.

## Absolum master password guideline
A "secure" password has to be 3-5 words of uncommon nonesence words with special character split, with atleast 1 uppercase letter, 1 lowercase letter, 3 numbers without any variation of 123 or 123456/123456789 , and 2 special characters not including !@.

Tip!: Special characters are all special characters on the keyboard not just!@#$%^&*()-_=+
when possible be sure to use all of the ones possible `~[]{}\|;:'",.<>/? and anymore if you might use a different keyboard than querty.

### Summary guideline
- 3-5 words of uncommon nonesence words with a special character split
- 1 uppercase letter
- 1 lowercase letter
- 3 numbers without any variation of 123 or 123456/123456789
- 2 special characters not including !@

### Nonesence words
- Hooey, Bushwa, Trumpery (words with a meaning, that are uncommon in natural conversation)
- Crumpsey, Mundle, Vargle (English dialect, or Old English)
- Fiawa, Scremptula, Wequlious (made up words with no meaning)

Tip!: if you speak a dialect or any other language than English use words in that language they will be less likely to be in a dictionary
- Krissie, Slaoij, Drekbak (Dialect in Maastrichts)

### Examples
- Ve%logoofiekrissiesjeng831#$
- Bushw*ayYAOURTvargle239&*
- Zielowva~lmaandJaar(,721
- beh_indlagvarinlus';008

### Explanation
The goal of these rules is to create an easy to remember secure master password.
To reach the goal it has to be:
#### Long
- 3-5 words (12+ characters)
#### Dictionary safe
- The words have to be nonesense or uncommon (we prefer nonesense because it's usually funny and thus easier to remember)
- Splitting of words with a special character (this makes dictionairy attacks almost useless)
#### Varius
- Uppercase
- Lowercase
- Numbers
- Special characters
