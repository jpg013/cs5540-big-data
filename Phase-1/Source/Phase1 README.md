# CS 5540 Principles of Big Data Management Project

Repository and source code for CS-5540 Principles of Big Data Management, Spring 2019. 
Project Phase 1 Submission
Due Date - Feb 22, 2019

Justin Graber, Poonam Kankariya, Vidyullatha Lakshmi Kaza

Scripts and data at:

https://github.com/jpg013/cs5540-big-data/tree/master/Phase-1

This archive contains python programs for downloading tweets using Twitter's API, for parsing URLs and hashtags from the downloaded tweets, and the output of a Spark JavaWordCount program that counts occurrences of hashtags and tweets.  The following files are included:

Collect Tweets using Twitter's Streaming APIs
--- gettweets.py ---
Python script to download tweets with keyword 'Trump' in them.


--- hashtags.py ---
Python script to parse downloaded tweets and print hashtags.


--- urls.py ---
Python script to parse downloaded tweets and print URLs.


Run the WordCount example in Apache Hadoop and Apache Spark on the extracted hashtags/URLs and collected the output files from Hadoop. 

--- hashtags_sparkop.txt --- & --- urls_sparkop.txt ---  
Output of Spark JavaWordCount file that counts URL and hashtag occurrences in input file.  


--- hashtags_out --- & --- urls_out ---  
Output of hadoop JavaWordCount file that counts URL and hashtag occurrences in input file.  

