# Telegram Notifications for Available Vaccination Appointments
This application includes a web scraper that checks the site of a vaccination center for available vaccination appointments and sends a notification to a user via a Telegram bot if new appointments were added.

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Instructions](#instructions)
4. [Licensing, Authors, Acknowledgements](#licensing)

## Installation
The code requires Python versions of 3.* and general libraries available through the Anaconda package. In addition, it uses:
* `schedule==0.6.0`
* `requests==2.25.1`
* `beautifulsoup4==4.9.3`

## Project Motivation <a name="motivation"></a>
In Germany, it is currently still difficult to get vaccinated because there aren't enough appointments and doses available for all the people that want to get vaccinated. I kept checking the site of the vaccination center near me multiple times a day manually. So I decided to create a small web scraper that checks the site every 30 minutes to see whether new appointments were added.

## Instructions
You can take the code and add your own environment variables for your own telegram bot, chat id, url, and div class whose content should be checked on the website. The code was deployed to Heroku, but it can also be run locally. However, it only makes sense to run it locally for testing purposes.

**But please make sure you do not overwhelm the site of the vaccination center.** First, make sure that the robots.txt page allows crawling. Second, use a relatively wide interval - such as 30 minutes or once an hour - to access the site.

## Licensing, Authors, Acknowledgements <a name="licensing"></a>
The code was created by Julia Nikulski. Feel free to use it for your own project. This project is published under the [MIT License](https://github.com/julianikulski/vaccination-info-bot/blob/main/LICENSE.md).
