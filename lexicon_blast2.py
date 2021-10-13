import random
import csv
import twitter
import datetime
import time
import sqlite3
import json
import sys

database_path = sys.argv[2]
user = sys.argv[1]

def extractContexts(user):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    results = cur.execute("select * from contexts where user=:user", {"user": user})
    r = cur.fetchone()
    con.close()
        
    return r


def runCapture(when, status, term):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    results = cur.execute("insert into run_results VALUES(:when,:str_id,:term)", {"when": when,"str_id":status,"term":term})
    con.commit()
    con.close()


def extractLexiconDefinition():
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    count = cur.execute("SELECT COUNT(*) FROM lexicon")
    r = cur.fetchone()
    

    my_number = random.randint(1,r[0])

    definition = cur.execute("SELECT Lex,Def from lexicon where ID=" + str(my_number))
    s = cur.fetchone()

    con.close()

    return s

    


def tweetLexicon(term_and_definition, contexts):

    ## pip install python-twitter is needed to import the twitter module
    api = twitter.Api()

    api = twitter.Api(consumer_key=contexts[0],
                      consumer_secret=contexts[1],
                      access_token_key=contexts[2],
                      access_token_secret=contexts[3])

    current_date=datetime.datetime.date(datetime.datetime.now())

    day = current_date.day
    month = current_date.month
    year = current_date.year
    twitter_status = "SUCCESS"

    try:
        status = api.PostUpdate(str(term_and_definition[0]) + ": " + str(term_and_definition[1]) + '  ##f3nation #lexicon (' + str(month) + '/' + str(day) + ').')

        runCapture(current_date,twitter_status,term_and_definition[0])
    except twitter.error.TwitterError:
        twitter_status="FAILURE"
        runCapture(current_date,twitter_status,term_and_definition[0])
        print("I have failed")

    



### MAIN ####


print("argument is " + user)
print("database path arg is " + database_path)

contexts = extractContexts(user)

term_and_definition = extractLexiconDefinition()

tweetLexicon(term_and_definition,contexts)



