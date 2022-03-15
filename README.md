<h1 align="center">Clean Code</h1>
<h4 align="center">Challenge</h4>
<center><img src="https://miro.medium.com/max/1280/1*YSYhINS70gJpvT6ZeI09UA.jpeg" width="300px"/><br/></center>

## Introduction

A clean way of working is at the basis of productivity. Decluttering your mind helps you to focus, and a 
clean desk helps you to stay organized. Similarly, clean code results in a higher productivity, because it ensures 
efficient collaboration and is easy to maintain. So in other words, code should be easy to understand and easy to change. 

We all know that the reality is different. Especially in the field of Data Science where specialists not always have a
background in software engineering. Even more so because some aspects of coding are more like a style and there is no 
arguing about taste.

During your career you might have stumbled upon (or created?) dirty code bases. Now we want to challenge to you to clean
up a pretty sever case. Time is limited, so let's see how far you can come!


## The task

The code base you're looking at is from an old BDR-employee Bob. You might have never seen him because for some reason 
he was unable to come to the office. But, as we all know, once in a while you're responsible for filling the dishwasher. 
Because Bob was never there, he tried to help by creating a model that predicts the number of times the dishwasher has
to run on a particular day at the office.

For the input of the model Bob used two things.
1. He hacked into our key tag system and found a log file: "key_tag_logs.csv". This file logs every time a colleague 
arrives and leaves the office, so in particular we know who was there for lunch. A colleague only contributes to extra 
dishes, if they are present at 12:00.
2. Every day a lunch is served. Bob scraped the recipe from the internet to determine which supplies were used. You can 
assume that only the words ["pan", "rasp", "kom"] contribute to extra dishes. It doesn't matter how many times the word 
is mentioned in the recipe. The recipes are in "lunch_recipes.csv"

For the labels, he asked Nieke to install an arduino in the dishwasher. The results are in "dishwasher_log.csv".


## Instructions

- Do whatever you think is necessary to make it maintainable software.
- We highly recommend working in pairs.
- Make your own branch, or fork this repo.
- Send (a link to) your code before 12.00.
- The file "clean_code_guidelines.md" is a reference for what the jury will judge your task on.
