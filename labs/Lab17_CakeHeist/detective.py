"""
detective.py  -  catch the cake thief

STEP 4  sets                        senders_between(), who_mentioned(), find_culprit()
STEP 5  arguments + scope           search(), count_words(), add_drama()
"""


# -------------------------------------------------------------------
# STEP 4: sets
# -------------------------------------------------------------------
def senders_between(messages, start, end):
    """Return a SET of critters who sent a message between start and end (both included).

    start and end are (hour, minute) tuples, e.g. (15, 0) and (15, 30).
    """
    # TODO 4a: ONE line with a SET comprehension  { ... for ... if ... }
    #   Keep the sender of every message whose time is between start and end.
    #   Tuples compare like clock times:  (15, 0) <= (15, 18) <= (15, 30)  is True
    #   so you can write:   start <= time <= end
    return {sender for time, sender, text in messages if start <= time <= end}


def who_mentioned(messages, phrase):
    """Return a SET of critters whose message contains phrase (ignore upper/lower case)."""
    # TODO 4b: ONE line with a set comprehension.
    #   Keep the sender if  phrase  appears in the text.
    #   Ignore upper/lower case: compare  phrase.lower()  with  text.lower()
    #   (Pixel shouts "CREAM CHEESE", and that must count too!)
    return {sender for time, sender, text in messages if phrase.lower() in text.lower()}


def find_culprit(online, knew_secret, alibis):
    """Return the set of critters who were online AND knew the secret, minus anyone with an alibi."""
    # TODO 4c: ONE line with set operators:
    #   &  keeps names that are in BOTH sets      -  removes names that are in the second set
    return (online & knew_secret) - alibis

# -------------------------------------------------------------------
# STEP 5: arguments
# -------------------------------------------------------------------
def search(messages, word, sender=None, ignore_case=True):    # TODO 5a (part 1): add 2 parameters with default values
    """Return a list of message tuples whose text contains word.

    sender       (default None)  -> if given, only that critter's messages
    ignore_case  (default True)  -> if True, "CAKE" also matches "cake"
    """
    # TODO 5a (part 2):
    #   1. add the parameters  sender=None  and  ignore_case=True  to the def line above
    #   2. loop over the messages and keep the WHOLE tuple (time, who, text) when:
    #        - sender is None, OR who == sender
    #        - AND word is in text  (if ignore_case is True, compare both in lower case)
    #   3. return the list of matching tuples
    results = []
    for time, who, text in messages:
        if sender is not None and who != sender:
            continue
        if ignore_case:
            found = word.lower() in text.lower()
        else:
            found = word in text
        if found:
            results.append((time, who, text))
    return results


def count_words(messages, *words):    # TODO 5b (part 1): make this take ANY number of words
    """Return a dictionary: for each word, how many messages contain it (ignore case).

    count_words(messages, "cake", "nap")  ->  {"cake": 6, "nap": 2}
    """
    # TODO 5b (part 2):
    #   1. change  words  to  *words  in the def line, so you can call
    #      count_words(messages, "cake", "nap", "dream")  with as many words as you like
    #      (inside the function, words is then a TUPLE of all those words)
    #   2. build a dictionary  {word: number of messages that contain it}
    #      Reuse your search() function:   len(search(messages, word))
    counts = {}
    for word in words:
        counts[word] = len(search(messages, word))
    return counts


# -------------------------------------------------------------------
# STEP 5: scope
# -------------------------------------------------------------------
total_drama = 0          # a GLOBAL variable: it lives outside every function


def add_drama(text):
    """Add drama points for one message to the global total_drama. Return the points."""
    # TODO 5c: this function has a SCOPE BUG. Run main.py (or check_my_work.py 5) to see it:
    #   UnboundLocalError: cannot access local variable 'total_drama'...
    #   Fix it by adding ONE line at the top of this function that tells Python
    #   total_drama is the GLOBAL variable, not a new local one.
    points = text.count("!")
    global total_drama
    if text.isupper():
        points += 5
    total_drama = total_drama + points
    
    return points
