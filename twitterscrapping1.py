#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:53:18 2021

@author: clement_lfb
"""

from tweepy import *
import pandas as pd
import csv
import re
import string
import os
import tweepy as tw
from textblob import TextBlob



consumer_key= 'atv6oQxfVY5vtMsDDM2Ko23Ac'
consumer_secret= '30Y2Z48jWQaHrQDh9jSPxlqCJ9ni9ejwdbQdAP2aYMWQ3sxrvh'
access_token= '1380468207052537858-23uQsqgt77ZYuayueudeBn7U4HwOJk'
access_token_secret= 'XbPhjRTEB1Uu8x11a7CmDQeaFA92TKIuiWIHw447X5MIc'



auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# Define the search term and the date_since date as variables
search_words = "#corona virus"
date_since = "2020-11-16"


# Collect tweets
tweets = tw.Cursor(api.search,
q=search_words,
lang="en",
since=date_since).items(5)
print(tweets)


# Iterate and print tweets
for tweet in tweets:
    Text=tweet.text
    print(tweet.text)
    polarity = TextBlob(Text).sentiment.polarity
    
    
### fonction pour créer les CSV 

def csv_creation(file_name, columns):
    #this function creates the CSV
    ### We are supposed to call this function later in the main program
    csvFile = open(file_name + ".csv", "w", newline='', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    col = ['id'] + columns
    #print('liste des col', col)
    csvWriter.writerow(col)
    csvFile.close()
    #print('CSV fully created')
    csvFile2 = open("erreur_" + file_name +".csv", "w", newline='', encoding="utf-8")
    csvWriter2 = csv.writer(csvFile2)
    col2 = ['id, url, periode_du, periode_au, ville']
    #print('liste des col', col)
    csvWriter2.writerow(col2)
    csvFile2.close()
    
    
### pour le remplissage
# we need to fill in the CSV
csvFile = open(file_name + ".csv", "a", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(gather_values_components(id, Publish_date, Content, Comments, Retweet, Likes, ImageURL, VideoURL, TweetURL))
csvFile.close()
print('Données enregistrées dans le CSV')
