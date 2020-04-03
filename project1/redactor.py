# Azadeh Gilanpour / 113338068 /Project1 / Redator/ Spring 2020

#packages ------------------------------------------------------------
from optparse import OptionParser
import glob
import re
import nltk
import sys
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.tree import Tree
import spacy
from nltk.corpus import wordnet as wn
nltk.download('punkt')
#nltk.download('all')
# Functions:  ------------------------------------------------------------------
# Convert redacted word:  -----------------------------------------------------
def block_char (Word):
    item = ''
    for i in Word:
        if i  == ' ':
            item  += ' '
        else:
            item  += '\u2588'
    return item

# Reading file functions:  -----------------------------------------------------

def read_text_file (target_file):
    with open(target_file,'r', encoding='utf-8') as file:
        target_file = file.read()
        file.close()
    return target_file

# Read the input files  --------------------------------------------------------

def getText (options, target_file):
    if options.stats:
        print ('Operation on {} is in progress ...'.format(target_file))

    if re.search(r'.*txt$', target_file):
         text = read_text_file (target_file)

    elif re.search(r'otherfiles/.*md$', target_file):
        text = read_text_file (target_file)
    else:
        print (target_file + "format is not supported!")
    return text
# Parse the target files  ------------------------------------------------------

def downloadFiles (options, inputFile_list=[]):
    #inputFile_list = list()
    if options.inputFile is None:
        print ("There is no file to redact.")
    else:
        for file_mask in options.inputFile:
            inputFile_list += glob.glob(file_mask)
    if inputFile_list == '':
        print ("There is no file to redact.")


    return inputFile_list



#redact name -----------------------------------------------------------------------
def redact_names (text):
    names = []
    nlp = spacy.load('en_core_web_sm') # language model
    doc= nlp(text)
    for ee in doc.ents:
        if ee.label_ =="PERSON":
            names.append(ee)

    count = 0
    for found_name in names:
        count += len(re.findall(str(found_name), text))
        #print (found_name)
        text = text.replace (str(found_name), block_char(str(found_name)))

    return text,names,count
#redact gender ---------------------------------------------------------------------
def redact_genders (text):
    gender = {'she', 'he', 'She', 'He', 'Him', 'Her', 'His', 'Her', 'Hers','herself', 'himself','him', 'Himself', 'Herself','her', 'his', 'hers','female','male','Female',
              'Male','women','men','Women','Men','ms','mr','miss','Ms.','Mr.','Miss','boy','Boy','girl','Girl','father','Father','mother','Mother','sister','Sister','brother','Brother','husband','Husband','wife','Wife'}
    words = nltk.word_tokenize(text)
    genders = gender & set(words)
    count = 0
    for found_gender in genders:
        count += len(re.findall(' '+found_gender+' ', text))
        text = text.replace (' '+found_gender+' ', block_char(' '+found_gender+' '))
    return text,genders,count

#redact date--------------------------------------------------------------------------------------------------
def redact_dates(text):
    dates= list()
    a = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}", text)
    b = re.findall(r"([\d]{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December)\s[\d]{4})", text)
    c = re.findall(r"(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{2})", text)
    d = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", text)  #10/10/2015
    e = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", text)  #10-10-2015
    f = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}", text)  #0 OCT 2015
    g = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4}", text)  #0-OCT-2015
    h = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{2}", text)  #0-OCT-15
    j = re.findall(r"([\d]{1,2}\s(?:JAN|NOV|OCT|DEC)\s[\d]{4})", text)
    k = re.findall(r"([\d]{1,2}\s(?:JAN|NOV|OCT|DEC)\s[\d]{4})", text) #1 NOV 2010
    l = re.findall(r'[0-9]+(?:st|[nr]d|th) [ADFJMNOS]\w*',text)
    k = re.findall(r'[ADFJMNOS]\w*. [0-9]+(?:st|[nr]d|th)',text)
    n = re.findall(r"[\d]{1,2}/[\d]{1,2}", text) #10/22
    m = re.findall(r"[ADFJMNOS]\w* [\d]{2}", text)  #OCT 15
    p =  re.findall(r"[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}", text)  # OCT 20 2015
    w = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", text)  #10-10-15
    z = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,2}", text)  #10/10/15
    u = re.findall(r"[ADFJMNOS]\w*-[\d]{1,2}-[\d]{4}", text)  #0-OCT-2015
    q=  re.findall(r"[ADFJMNOS]\w* [\d]{1,2} [\d]{4}", text)  # OCT 20 2015
    month=['january','february','march','april','june','july','august','september','october','november','december','January','February','March','April','May','June','July','August','September','October','November','December']
    day_complete=['monday','tuesday','thursday','wednesday','friday','saturday','sunday','today','tomorrow','Monday','Tuesday','Thursday','Wednesday','Friday','Saturday','Sunday','Today','Tomorrow']
    day_short=['mon','tue','thu','wed','fri','sat','sun','Mon','Tue','Thu','Wed','Fri','Sat','Sun']
    for i in a:
        dates.append(i)
    for i in b:
        dates.append(i)
    for i in c:
        dates.append(i)
    for i in d:
        dates.append(i)
    for i in e:
        dates.append(i)
    for i in f:
        dates.append(i)
    for i in g:
        dates.append(i)
    for i in h:
        dates.append(i)
    for i in j:
        dates.append(i)
    for i in k:
        dates.append(i)
    for i in n:
        dates.append(i)
    for i in l:
        dates.append(i)
    for i in m:
        dates.append(i)
    for i in p:
        dates.append(i)
    for i in w:
        dates.append(i)
    for i in z:
        dates.append(i)
    for i in q:
        dates.append(i)
    for i in word_tokenize(text):
        if i.lower() in month:
            dates.append(i)
    for i in word_tokenize(text):
        if i.lower() in day_complete:
            dates.append(i)
    for i in word_tokenize(text):
        if i.lower() in day_short:
            dates.append(i)
    count = 0
    total_found = list()
    total_found += dates
    count = count + len(dates)
    dates.sort (key =len, reverse=True)
    for found_date in dates:
        text = text.replace (found_date, block_char(found_date))
    return text,dates,count

# Redact Phone Numbers:  -------------------------------------------------------
def redact_phones (text):
    count = 0
    found = list()
    telephone = r'(?:\s+(?:\+|00)?[1-9]\d{,2}(?:\s+|\-|\.)?)?\(?\d{2,4}\)?(?:\s|\-|\.)+(?:(?:\d{3,4}(?:\s|\-|\.)+\d{4})|[a-zA-Z0-9]{3}\-[a-zA-Z0-9]{4})'
    phones= re.findall (telephone, text)
    found += phones
    count = count + len(phones)
    phones.sort (key =len, reverse=True)
    for item in phones:
        text = text.replace (item, block_char(item))
    return text,phones,count

# Redact Emails:  --------------------------------------------------------------
def redact_emails (text):
    count = 0
    found = list()
    e = r'\s*(?:\w|\d|[\!#\%\$&_\.])*@(?:\w|\d)*\.(?:\w|\d){1,4}'
    emails = re.findall (e, text)
    found += emails
    count = count + len(emails)
    found.sort (key =len, reverse=True)
    for item in emails:
        text = text.replace (item, block_char(item))
    return text,emails,count

# Redact Concepts:  ------------------------------------------------------------
def redact_concepts (text, word):
    concepts = list(word)
    for concept in word:
        for synset in wn.synsets(concept):
            for i in synset.lemma_names():
                concepts.append(i)
    concepts = set(concepts)
    concepts = concepts & set(nltk.word_tokenize(text))
    #print (concepts)
    sentences = nltk.sent_tokenize(text)
    count = 0
    concept_found = list()
    for concept in concepts:
        count += len(re.findall(concept, text))
        for i in range(len(sentences)):
            if sentences[i].lower().find(concept) != -1:
                concept_found.append (sentences[i])
                #print (sentences[i])
                sentences[i] = block_char(sentences[i])
    text = ''
    for sent in sentences:
        text += sent
    return text,concept_found,count


# Parse the Command-line Options  ---------------------------------------------

def findFlag ():

    parser = OptionParser()

    parser.add_option("--input", type="string", dest="inputFile",  action="append", help="Input file name", metavar="FILES")
    parser.add_option("--output",type="string", dest="outputFile", help="Output filename/destination")
    parser.add_option("--names",action="store_true", dest="names", default=False, help="Redact names")
    parser.add_option("--genders", action="store_true", dest="genders", default=False, help="Redact genders")
    parser.add_option( "--dates", action="store_true", dest="dates", default=False, help="Redact dates")
    parser.add_option("--emails", action="store_true", dest="emails", default=False, help="Redact emailss")
    parser.add_option("--phones", action="store_true", dest="phones", default=False, help="Redatt phones")
    parser.add_option( "--concept", type="string", dest="concepts",  action="append",help="Redact concepts")
    parser.add_option( "--stats", type="string", dest="stats",  action="append", help="Count")

    (options, args) = parser.parse_args()
    return options, args


# Redact the target files and count -----------------------------------------------------
def stats (options, text):
    if options.names:
        (text, stats, items) = redact_names (text)
        if options.stats:
            print ('{} names redacted. The redacted names are:'.format(stats))
            print (items)
    if options.genders:
        (text, stats, items) = redact_genders (text)
        if options.stats:
            print ('{} genders redacted. The redacted genders are:'.format(stats))
            print (items)
    if options.dates:
        (text, stats, items) = redact_dates (text)
        if options.stats:
            print ('{} dates redacted. The redacted dates are:'.format(stats))
            print (items)
    if options.phones:
        (text, stats, items) = redact_phones (text)
        if options.stats:
            print ('{} phone numbers redacted. The redacted phones re:'.format(stats))
            print (items)
    if options.emails:
        (text, stats, items) = redact_emails (text)
        if not options.stats is None:
            print ('{} emails redacted. The redacted emails are:'.format(stats))
            print (items)
    if not options.concepts is None:
        (text, stats, items) = redact_concepts (text, options.concepts)
        if options.stats:
            print ('{} concepts redacted. The found items are:'.format(stats))
            print (items)
    return text
# make file for output:  --------------------------------------------------

def expo (text, destination):
    with open(destination, 'w', encoding = "utf-8")as file:
        e=file.write(text)
        file.close()
    return e

#export to .redacted ----------------------------------------------------
def export (options, text):
    if options.outputFile is None:
        output_path = ''
    else:
        output_path = options.outputFile
    file_name = target_file.split('/')
    file_name = file_name [-1]
    file_name = output_path + file_name
    file_name = file_name.replace('.txt','.redacted')
    file_name = file_name.replace('.md','.redacted')
    ex = expo (text, file_name)
# Main part --------------------------------------------------------------------
options, args = findFlag ()
inputFile_list = downloadFiles (options)
for target_file in inputFile_list:
    text = getText (options, target_file)
    text = stats (options, text)
    export (options, text)
