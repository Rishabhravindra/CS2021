## Lists, Dictionaries ##

#########
# Lists #
#########

# Q5
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    new,num = [],0
    while num < len(lst):
        new = [lst[num]] + new
        num += 1
    return new



# Q6
def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    if not lst:
        return []
    return reverse_recursive(lst[1:]) + [lst[0]] 


# Q7
def map(fn, seq):
    """Applies fn onto each element in seq and returns a list.

    >>> map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    res = []
    for arr in seq:
        res += [fn(arr)]
    return res

def filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    res = []
    for arr in seq:
        if pred(arr):
            res += [arr]
    return res

def reduce(combiner, seq):
    """Combines elements in seq using combiner.

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> reduce(lambda x, y: x * y, [4])
    4
    """
    total = seq[0]
    for elem in seq[1:]:
        total = combiner(total, elem)
    return total


################    
# Dictionaries #
################

# Q10
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

# Q11
def construct_tweet(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
        result += word
    return result + word

# Warning: do NOT try to print the return result of this function
def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def trump_tokens(path='trumptweets.txt', url='http://pastebin.com/raw/nWvFKcH7'):
    """Return the words found in tweets of Trump as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('trumptweets.txt', encoding='ascii').read().split()
    else:
        trump = urlopen(url)
        return trump.read().decode(encoding='ascii').split()
        
# Uncomment the following lines
shakestokens = shakespeare_tokens()
shakestable = build_successors_table(shakestokens)
trumptokens = trump_tokens()
trumptable = build_successors_table(trumptokens)

def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)