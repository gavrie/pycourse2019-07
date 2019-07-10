#!/usr/bin/env python

import redis
import sys

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print("wrong number of parameters. got {} arguments expecting 2 or 3".format(len(sys.argv) - 1))
    exit(1)

user = sys.argv[1]
command = sys.argv[2]
# print(f"user:{user} is executing {command} command")
if len(sys.argv) == 4:
    content = sys.argv[3]
    # print(f"content is {content}")

try:
    conn = redis.Redis()
    conn.ping()
except:
    print("tweeter server is down, please try again later")
    exit(1)

if command == "post":
    if conn.exists(f"{user}_followers") != 1:
        conn.rpush(f"{user}_followers", f"{user}")
    followers_list = [follower.decode("utf-8") for follower in conn.lrange(f"{user}_followers",0,-1)]
    # print(followers_list)
    for follower in followers_list:
        conn.rpush(f"{follower}_timeline", f"<{user}> {content}")

elif command == "follow":
    if conn.exists(f"{content}_followers") != 1:
        conn.rpush(f"{content}_followers", f"{content}")
    conn.rpush(f"{content}_followers", f"{user}")

elif command == "timeline":
    timeline = conn.lrange(f"{user}_timeline", 0, -1)
    if timeline:
        for message in timeline:
            print(message.decode("utf-8"))
    else:
        print("timeline is empty")
