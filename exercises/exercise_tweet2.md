    
## Step 3: Mentions

On Twitter, if you mention another user in a tweet by including his handle (username), it will show up in that user's timeline.

Implement mentions in your program. It should work as follows:

    $ tweet @gavrie post "Let's see what @danny says"
    
    $ tweet @danny timeline
    ...
    <@gavrie> Let's see what @danny says
    ...
    
## Step 4: Streaming timeline

The timeline functionality can be improved by making it update automatically when new tweets are added.
Instead of printing the current tweets and exiting, your program should wait for new tweets and print them as they arrive.
This is similar to how the [`tail -f`](https://linux.die.net/man/1/tail) command works.

Implementation hints:

- Look at the blocking Redis commands, such as [BLPOP](https://redis.io/commands/blpop)
- You may want to consider using Redis Streams, but it's more complicated 

## Step 5: Additional features
    
Some ideas for further features:
- Direct Messaging (DMs) with other users
- Likes
- Threading
- Replies
