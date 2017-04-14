"""
input
5 
Delhi, is a metropolitan and the capital region of India which includes the national capital city, New Delhi. It is the second most populous metropolis in India after Mumbai and the largest city in terms of area.

Mumbai, also known as Bombay, is the capital city of the Indian state of Maharashtra. It is the most populous city in India, and the fourth most populous city in the world, with a total metropolitan area population of approximately 20.5 million.

New York is a state in the Northeastern region of the United States. New York is the 27th-most extensive, the 3rd-most populous, and the 7th-most densely populated of the 50 United States.

The Indian Rebellion of 1857 began as a mutiny of sepoys of the East India Company's army on 10 May 1857, in the town of Meerut, and soon escalated into other mutinies and civilian rebellions largely in the upper Gangetic plain and central India, with the major hostilities confined to present-day Uttar Pradesh, Bihar, northern Madhya Pradesh, and the Delhi region.

The Boston Tea Party (referred to in its time simply as "the destruction of the tea" or by other informal names and so named until half a century later,[2]) was a political protest by the Sons of Liberty in Boston, a city in the British colony of Massachusetts, against the tax policy of the British government and the East India Company that controlled all the tea imported into the colonies. On December 16, 1773, after officials in Boston refused to return three shiploads of taxed tea to Britain, a group of colonists boarded the ships and destroyed the tea by throwing it into Boston Harbor. The incident remains an iconic event of American history, and other political protests often refer to it.

"""

from collections import Counter
import re
import string

n = int(input())*2
re_pun = re.compile('[%s]' % re.escape(string.punctuation))
def find_regex(test_str):
    regex = r"(\d{1,2}(th|rd|nd) \w{2,12} \d{1,4}|\d{1,2}(th|rd|nd) of \w{2,12}, \d{2,4}|\d{2} \w{2,12} \d{2,4}|\d{1,4}\/\d{1,4}\/\d{1,4}|\w{2,12} \d{1,2}(th|rd|nd) \d{2,4}|\w{2,12}, \d{1,2}(th|rd|nd) \d{2,4}|\d{1,2} \w{2,12} \d{1,4}|\w{2,12} \d{1,2}, \w{2,4}|\w{2,12}, \d{1,2}, \w{2,4})"
    matches = re.finditer(regex, test_str, re.IGNORECASE)
    t = 0
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        t = matchNum
    print(t)

    
def find_all(sent):
    sent = sent.lower()
    sent = re_pun.sub(" ",sent)
    article = Counter(sent.split())
    print(article["a"])
    print(article['an'])
    print(article["the"])
    find_regex(sent)


for i in range(n):
    try:
        s = input().strip()
    except EOFError:
        continue
    if s == "":
        continue
    find_all(s)
#print(e)
