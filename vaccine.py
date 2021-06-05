from bs4 import BeautifulSoup
import requests
import schedule
import os


def crawling(website_link, link_class):
    '''
    Function to crawl content from website
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for the relevant text
    Returns: vaccine_list = list
    '''
    # link of website to be crawled
    website_link = website_link

    # get content of website and parse it
    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')

    # extract the message on the vaccination site
    vaccine_message = website_content.find_all(class_ = link_class)

    # create a list to save all messages
    vaccine_list = []

    # iterate through the found content
    for item in vaccine_message:
        vaccine_item = item.get_text()
        vaccine_list.append(vaccine_item)

    return vaccine_list


def send_message(chat_id, text, bot):
    '''
    Takes the chat id of a telegram bot and the text that was crawled from the
    website and sends it to the bot
    Args: chat_id = chat id of the telegram bot,
          text = crawled text to be sent
    Returns: None
    '''
    parameters = {'chat_id': chat_id, 'text': text}
    message = requests.post('https://api.telegram.org/bot' + bot + '/sendMessage', data=parameters)


def check_message(test=False):
    '''
    Function to check whether the message displayed still mentions that
    there are no new vaccination appointments available
    Args: test = boolean; used to send a test message after script was run
    Returns: None
    '''

    try:
        # the website to crawl
        crawled_content = crawling(os.environ['CRAWL_URL'], 'text-c2')
    except:
        send_message(os.environ['CHAT_ID'], 'Der Crawler ist kaputt', os.environ['API_KEY'])

    # the message to be checked
    no_vaccines = os.environ['MESSAGE']

    if test:
        send_message(os.environ['CHAT_ID'], 'Keine neuen Termine', os.environ['API_KEY'])

    # messages to send if message_to_check disappeared from website
    if no_vaccines in crawled_content:
        pass
    else:
        send_message(os.environ['CHAT_ID'], 'Es könnte neue Termine geben!', os.environ['API_KEY'])


def summary_message():
    '''
    Function that sends content confirming that the crawler is still
    running correctly
    Args: None
    Returns: None
    '''

    send_message(os.environ['CHAT_ID'], 'Der Crawler läuft noch', os.environ['API_KEY'])


# send a one time initialization message
check_message(test=True)

# schedule crawler
schedule.every(30).minutes.do(check_message)
schedule.every().day.at('08:00').do(summary_message)

# run script infinitely
while True:
    schedule.run_pending()
