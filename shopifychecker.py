#!/python2.7
#Follow me on twitter @_ajnicolas
import requests
from bs4 import BeautifulSoup


# While true to get a actual link
def linkfriendly():
    global url
    global r
    global soup
    while True:
        # Get user shopify link
        try:
            url = raw_input('PASTE LINK HERE: ')
            r = requests.get(url + '.xml')
            soup = BeautifulSoup(r.content, 'html.parser')
            if r == False:
                print 'Link not supported!'
            elif r == True:
                print '\n' + 'Link found!'
            break
            # Handle exceptions
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL, requests.exceptions.ConnectionError,
                NameError) as e:
            print 'link no bueno '


# Grabs handle text
def grabhandle():
    try:
        for handL in soup.findAll("handle"):
            return 'Handle: ' + handL.text
    except NameError:
        print 'Could not find text!'


# Sets up the link formating and grabs date link was created
def grabdate():
    for created in soup.findAll("created-at"):
        return 'created: ' + created.text


# Function names pretty self explanitory!
def grabsku():
    for sku in soup.findAll("sku"):
        return 'sku: ' + sku.text


def grabprice():
    for price in soup.findAll("price"):
        return 'Price: ' + price.text


# Parses stock,sz name, and variants from shopify site
def grabszstk():
    sz = []
    for size in soup.findAll("title")[1:]:
        # append to list
        sz.append(size)

    stk = []
    for stock in soup.findAll("inventory-quantity"):
        stk.append(stock)

    variants = []
    for variant in soup.findAll("id"):
        variants.append(variant)

    # formats the data
    fmt = '{:<8}{:<10}{:<10}{}'

    print(fmt.format('', 'size', 'stock', 'variant'))
    # zips the for lists together
    for i, (sz, stk, variants) in enumerate(zip(sz, stk, variants)):
        print(fmt.format(i, sz.text, stk.text, variants.text))


# Also bad formatting
def formattext():
    print '--------------------------------------' * 2
    print url
    print '                                      ' * 2
    try:
        print grabhandle() + ' ' + grabdate() + ' \n' + grabprice() + ' \n' + grabsku()
        print grabszstk()
    except TypeError:
        print "Try copying everything before before the '?variant' \n or before the '?' in the link!".upper()


# While true statment for multiple link checks!
while True:
    if linkfriendly() == True:
        print linkfriendly()
    elif formattext() == True:
        print formattext()
