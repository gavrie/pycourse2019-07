# Exercise: Twitter clone

In this exercise, you will write a simple command line Twitter clone.
It does _not_ connect to the real Twitter API. Instead, it stores all data in your own Redis database.

## Step 1: Posting tweets and showing the timeline

Implement the ability to post new tweets as a specific user.
Assuming your program is named `tweet`, it should be run as follows:

    $ tweet @gavrie post Hello
    
This will post the message `Hello` as the user `@gavrie`.

Now, implement the `timeline` command that will show all tweets that are posted by people followed by the user (at this point, this is only the user himself):

    $ tweet @gavrie timeline
    <@gavrie> Hello

Since `@gavrie` has posted one tweet, it shows up on his timeline.

## Step 2: Following others

Implement the `follow` command that will cause tweets from others to show up on the user's timeline.

    $ tweet @gavrie follow @moshe
     
    $ tweet @moshe post "Just saying a few things"
    
    $ tweet @gavrie timeline
    <@gavrie> Hello
    <@moshe> Just saying a few things
      
## Guidelines

- To handle command line arguments, import the standard module `sys` which provides the arguments in the `argv` list ([see here for details](https://docs.python.org/3/library/sys.html#sys.argv)).  
- Be sure to install the `redis` module with `pip install redis` ([see the documentation](https://pypi.org/project/redis/)).
- You can either install Redis locally on your computer, or use a free [Redis Cloud](https://app.redislabs.com/#/login) database.