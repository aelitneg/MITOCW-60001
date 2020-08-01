# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Andrew Gentile
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid

    def get_title(self): 
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase;

    def is_phrase_in(self, text):
        clean_text = text

        # Replace punctuation with spaces (" ")
        for p in string.punctuation:
            clean_text = clean_text.replace(p, " ")
        
        # Remove spaces
        clean_text = list(filter(lambda c: c != "", clean_text.split(" ")))
        
        # Rejoin into clean string 
        clean_text = ' '.join(clean_text)
        
        if self.phrase.lower() == clean_text.lower():
            return True
        elif clean_text.lower().startswith(self.phrase.lower() + " "):
            return True
        elif clean_text.lower().endswith(" " + self.phrase.lower()):
            return True
        elif (" " + self.phrase.lower() + " ") in clean_text.lower():
            return True
        else:
            return False


# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.title)
        

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.description)


# TIME TRIGGERS

# Problem 3
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.date_time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        self.timezone = pytz.timezone("US/Central")

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    def evaluate(self, story):
        pubdate = story.get_pubdate()
        date_time = self.date_time

        if pubdate.tzinfo:
            date_time = self.timezone.localize(date_time)
        return pubdate < date_time

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    def evaluate(self, story):
        pubdate = story.get_pubdate()
        date_time = self.date_time

        if pubdate.tzinfo:
            date_time = self.timezone.localize(date_time)

        return story.pubdate > date_time


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        return not self.T.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1;
        self.T2 = T2;

    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    remove_list = []

    for story in stories:
        remove = True
        for trigger in triggerlist:
            if trigger.evaluate(story):
                remove = False
                break
        if remove:
            remove_list.append(story)

    for story in remove_list:
        stories.remove(story)

    return stories

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    triggers = []
    trigger_defs = {}
    for line in lines:
        cmd = line.split(',')
        
        if cmd[0] != "ADD":
            name = cmd[0]
            trigger_type = cmd[1]

            if trigger_type == "TITLE":
                trigger_defs[name] = TitleTrigger(cmd[2])
            elif trigger_type == "DESCRIPTION":
                trigger_defs[name] = DescriptionTrigger(cmd[2])
            elif trigger_type == "BEFORE":
                trigger_defs[name] = BeforeTrigger(cmd[2])
            elif trigger_type == "AFTER":
                trigger_defs[name] = AfterTrigger(cmd[2])
            elif trigger_type == "AND":
                trigger_defs[name] = AndTrigger(trigger_defs[cmd[2]], trigger_defs[cmd[3]])
            elif trigger_type == "OR":
                trigger_defs[name] = OrTrigger(trigger_defs[cmd[2]], trigger_defs[cmd[3]])
            elif trigger_type == "NOT":
                trigger_defs[name] = NotTrigger(trigger_defs[cmd[2]])
        elif cmd[0] == "ADD":
            for i in range(1, len(cmd)):
                triggers.append(trigger_defs[cmd[i]])
    return triggers

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # 2020-07-31 Yahoo breaks provided feedparser
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

