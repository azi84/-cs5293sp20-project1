
# Azadeh Gilanpour
 
Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.

# Project Description:

In this project, I  used my  knowledge of Python and Text Analytics to design a system that accept plain text documents then detect and redact “sensitive” items like names/gender/dates/phones and emails.

## Github :

First I made GitHub repository with the name of cs5293sp20-project1. This one would be use at the end of project when are done we need to push every directory and file we made in our cloud instance. All directory and file was created in the cloud SSH can use $git clone + you GitHub URL of the project repository to get access to GitHub and following code would be used after we done with project to have them in our GitHub:
 1. $git status (at first time it is red before adding the files/directories to GitHub) 
2. $git add filename 
3. $git status (turn to green after adding) 
3. $git commit -m "your comment" 
4. $git push origin master

## Directory :

We need to make a blow directory in our cloud instance (SSH):

cs5293p20-project1/
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── project1
│   ├── __init__.py
│   └── project1.py
│   └── ... 
├── docs/
├── setup.cfg
├── setup.py
└── tests/
    ├── test_names.py
    └── test_genders.py
    └── ...
### Directory and files:

For starting to make your directory such as ##project1/docs/test... with the command: mkdir "name of directory"

### Pipfile and Pipfile.lock :

For these two file we need the other kind of command for them like : Pipfile ==> $pipenv --python python3 Pipfile.lock ==> $pipenv install requests

### Setup.py:

 This file is contain below codes which you can write into it by using Vim setup.py command :
 from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='You Name',
	authour_email='your ou email',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)

### Setup.cfg:

[aliases]
test=pytest

[tool:pytest]
norecursedirs = .*, CVS, _darcs, {arch}, *.egg, venv

## Packages:

Following the packages were used in this projects that for having them in your SSH you need to use the pipenve install filename.
           1:glob
           2:re
           3:nltk
           4:sys
           5:spacy
           6.optparse    
           7:nltk.corpus
           8:nltk.tree
           9:sent_tokenize
           10:word_tokenize
           11: pos_tag
           12: ne_chunk
           13: Tree
           14:wordnet
           15:nltk.download(“punk”)

##Function Description:

In this project we have different function to help us to read the .txt and .md file and then redact the sensitive information. I tried to cover names, genders, dates, emails and phones information in this project. I wrote all the project in the one .py and I do not have a main function because it was easier for me to handle it. I will go through each function I made it one by one in below:

####def block_char (Word):

This function is use to redacted characters in the document by Unicode (U+2588). This function use through code whenever you want to redacted a word you just need to call this function. 

####def read_text_file (target_file):

This function reading the file which in our project most text. I used simple way of reading the file with the help of the “with open” and the file that read would be my targets file.

####def getText (options, target_file):

This function read the input files. In this project we have to read .txt files and .md files. I used the RE package to find everything end up to .txt and .md and used my def read_text_file (target_file) and said if you find these two in target find read them.

####def downloadFiles (options, inputFile_list=[]):

This function parses the target files and checked it. I used glob as the professor suggested. And the put the condition if it couldn’t find any file print out that    print ("There is no file to redact.")

####def redact_names (text):

This function is one of the main thing we have to do redact the name. There is two package for doing that, the one is the NLTK and the other one is SPACY. I worked with both of them and make function with both and compare my result and I understood that my SPACY function work better than the NLTK. Because NLTK function with any criteria I consider for that try to read every word which start with capital letter. In spacy function I load (“en_core_web_sm”) language model [ I couldn’t load (“en”) for my Jupiter but I did for my instance and compare with this one and couldn’t find any differences] and used the PERSON labels to detect the person’s name and then redacted them by calling my def block_char (word) function. Also I count the number of the name the function found for the stats.

#### def redact_genders (text):

In this function we have to redact the gender. First I made a list of the word that are common in gender in both lower case and upper case and then tokenized by word_tokenize. And call my redacted function to redact the text based on my gender list and count them for stats.

####def redact_dates(text):

In this function we have to redact the dates. I worked with so many different packages for this function and my problem with them was they only consider some type of the date. Therefore, I decided to use RE packages and write all the different type of the date to cover each type of the date. I know it is a really long list but I wants to consider each type of the date. Again after finding them I used my redacted function to redact the date it found in the text by this function and count them for stats.

####def redact_phones (text):

I decided to redact the people phones number because it is part of the private information and it is sensitive. I follow the instruction I used for dates and used RE packages to find phone style and redacted them and count them for stats

####def redact_emails (text):

Another extra thing that I did was for email. Again I used the RE packages to find the email in the text and redacted them by my redacted function and count them for stats.

####def redact_concepts (text, word):

This function was one of the main part of the things we have to do for the project. We need to takes one word and represents a concept. And then any section of the input files that refer to this concept should be redacted. I used this package (from nltk.corpus import wordnet as wn) and called wn.synset which help us to find the group of the synonymous word that express the same concept. Some words have only one synset but some have several. And then I used the tokenize word and sentences to extract the same word from the text that equal with sysnet . Again after that called the redacted function to redacted the word the function found and count them for stats.


####def findFlag ():

This function is my flag recognition function. As explained in the project we need to have a flag for each argument. So I used OptionParser packges to make flag for –input/--output/--names/--genders/--dates/--emails/--phones/--concepts/--stats.

####def stats (options, text):

This function redacts the target files and whenever it is on (that means when we call the –stats) prints the count that each function has. As explained in the project this Stats takes either the name of a file, or special files (stderr, stdout), and writes a summary of the redaction process. Some statistics to include are the types and counts of redacted terms and the statistics of each redacted file. And count the number of the time each function redacted.

####def expo (text, destination): and def export (options, text):

These two function are used for output. As explain in the project we need to store all the redacted file regardless of their input type should be written to text files Each file should have the same name as the original file with the extension. redacted appended to the file name. The first function make file for save the file that add .redacted extension in the second one. And finally I call the function at end.
###Check the project result:

After we wrote the whole project we need to run in to make sure that it gives us all desirable output we want for this part we need the blow code that we use it in our SSH and we need to add the URL to it to see the final result : 
pipenv run python project1/redactor.py --input texts/'*.txt' \
                    --input 'otherfiles/*.md' \
                    --names –-dates -–genders -–emails --phones  \
                    --concept 'crime' \
                    --output 'files/' \
                    --stats stderr
## Test
 After we are done with our real code we need to test them to see that they are work correctly or not. So in this part we have to create our own test file to check each function. I checked all features and make test function for each of them. I also import following packages for this part:
                            1.import project1

                            2.import pytest
                               
                            3.from project1 import redactor 
####Test names

For this part I just called my function and then checked it works correctly or not by checking the number of the name was redacted in my new text.
 s = " William Bradley Pitt on December 18th, 1963, in Shawnee, Oklahoma, and was raised in Springfield, Missouri. He is the son of Jane Etta (Hillhouse), a school counselor, and William Alvin Pitt, a truck company manager. He has a younger brother, Douglas (Doug) Pitt, and a younger sister, Julie Pitt."
def test_names():
             t,n,c= redactor.redact_names (s) 
 # there is 7 name in this file [William Bradley Pitt, Jane Etta, William Alvin Pitt, Douglas, Doug, Pitt, Julie Pitt]     
             assert len(n) == 7

####Test Genders

For this part I checked the number of the gender found in the sample text and the number of redacted. As you see they are different because the redacted just shows the word the found and ignore repetition. 
text = 'Gender is the state of being male or female in relation to the social and cultural roles that are considered appropriate for men and women.Gender is the state of being male or female in relation to the social and cultural roles that are considered appropriate for men and women.’
def test_gender(): 
      (t,g,c) = redactor.redact_genders (text)
       assert c == 6
        assert len(g) == 4

####Test Dates

For this part I checked the function is work perfectly or not by checking the number of the redactor and also I checked that the number I found in the text is the same as the one found in the function. 
d = """Tom Cruise is an American actor known for his roles in iconic films throughout the August 2 1980, as well as his high profile marriages to actresses Nicole Kidman and Katie Holmes.After developing an interest in acting during high school, he rocketed to fame with his star turns in Risky Business and Top Gun. Cruise later earned acclaim for his work in the hit film Jerry Maguire and the Mission: Impossible franchise. Early Life Thomas Cruise Mapother IV, better known as Tom Cruise, was born on July 3, 1962, in Syracuse, New York, to Mary and Thomas Mapother. Cruise's mother was an amateur actress and schoolteacher, and his father was an electrical engineer. His family moved around a great deal when Cruise was a child to accommodate his father's career."""

def test_date(): 
         (t, da, c) = redactor.redact_dates (d)
         assert c ==4 
         assert ['August 2 1980', 'July 3, 1962', 'August', 'July'] == da

####Test emails
 
In this part for checking the function I checked is the number of the email is found is correct and then checked is the email is same it is in the text and finally I checked that the text redacted correctly.  
e = "The general format of an email address is local-part@domain, and a specific example is jsmith@example.com. An address consists of two parts."
def test_emails(): 
      (t, em,c) = redactor.redact_emails (e) 
       assert c == 1 
       assert em == [' jsmith@example.com'] 
       assert t == '''The general format of an email address is local-part@domain, and a specific example is ██████████████████. An address consists of two parts.'''~

####Test Phones

In this Test part again as before I checked the number of the phone the function can find is correct and is the same as the one they are in the text and finally I checked the text redacted correctly or not.:wq
p = '''Education Abroad Contact InformationOffice HoursMonday - Friday 8:00 AM to 5:00 PMMailing AddressEducation AbroadUniversity of Oklahoma729 Elm Ave. Room 144Norman, OK 73019PhoneMain Phone (405) 325-1693Fax (405) 325-7387Emergencies While Abroad (405) 630-5392EmailOffice Email: ea@ou.eduEmergency Email: helpabroad@ou.eduBuilding Location'''
def test_phones(): 
        (t, ph,c) = redactor.redact_phones (p) 
                print (ph)
                assert c == 3 
                assert ph == ['(405) 325-1693', '(405) 325-7387', '(405) 630-5392'] 
                 assert t == '''Education Abroad Contact InformationOffice HoursMonday - Friday 8:00 AM to 5:00 PMMailing AddressEducation AbroadUniversity of Oklahoma729 Elm Ave. Room 144Norman, OK 73019PhoneMain Phone █████ ████████Fax █████ ████████Emergencies While Abroad █████ ████████EmailOffice Email: ea@ou.eduEmergency Email: helpabroad@ou.eduBuilding Location''

####Test concepts

For this part I checked that the number of the word the function chooses as the same concept or the child is equal the one I can see in the samples text. 
c="""Biologically, a child is a person between birth and puberty,[1][2] or between the developmental period of baby and puberty.Common meanings for kid is young baby how can talk and walk """
def test_concept(): 
         (t, con, co) = redactor.redact_concepts (c, ['child'])
         assert co == 4

####Test Download 

For the last thing I checked that my function can I download the file correctly or not.
options, args = redactor.findFlag ()
def test_downloadText(): 
     inputFile_list = redactor.downloadFiles (options, inputFile_list='my.txt') 
      assert inputFile_list == 'my.txt'

##Check the test result:

For checking the test result in SSH we need to install pytest first. I install pytest with the ##pip install pytest.  I run my test with pipenv run python -m pyest
                                         

