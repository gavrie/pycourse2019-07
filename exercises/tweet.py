#!/usr/bin/env python

import sys
import redis
import time
import json

HOST = "redis-13418.c8.us-east-1-4.ec2.cloud.redislabs.com"
PORT = 13418
PASS = "QCqZr7caZxWcUahORl0ReOg2JvqD8HZ4"
POST_PREFIX = "posts:"
FOLLOWEES_PREFIX = "followees:"
USER = 'user'
MESSAGE = 'message'
TIME = 'time'


def post(user: str, message: str, conn):
    post_to_add = {MESSAGE: message, TIME: time.time()}

    list_name = POST_PREFIX + user
    message = json.dumps(post_to_add)
    conn.rpush(list_name, message)
    result = json.loads(conn.lindex(list_name, -1))

    print(f">{user}:{result.get(MESSAGE)}")


def print_timeline(user: str, conn):
    # Get all my posts
    all_posts = get_posts_by_user(user, conn)

    # Get all my followees posts
    for followee in get_followees(user, conn):
        all_posts += get_posts_by_user(followee, conn)

    sorted_posts = sorted(all_posts, key=lambda k: k.get(TIME), reverse=True)

    for post in sorted_posts:
        print(f"<{post.get(USER)}>: {post.get(MESSAGE)}")


def get_followees(user: str, conn) -> list:
    return conn.smembers(FOLLOWEES_PREFIX + user)


def get_posts_by_user(user: str, conn) -> list:
    users_posts = list()
    for post in conn.lrange(POST_PREFIX + user, 0, -1):
        post_dic = json.loads(post)
        post_dic[USER] = user
        users_posts.append(post_dic)

    return users_posts


def follow(user: str, user_to_follow: str, conn):
    set_name = "followees:" + user
    conn.sadd(set_name, user_to_follow)
    print(f"User: {user} Follow: {user_to_follow}")


def main():
    user = sys.argv[1]
    op_name = sys.argv[2]

    conn = redis.Redis(host=HOST, port=PORT, password=PASS, decode_responses=True)

    if op_name == 'post':
        post(user=user, message=sys.argv[3], conn=conn)
    elif op_name == 'timeline':
        print_timeline(user=user, conn=conn)
    elif op_name == 'follow':
        follow(user=user, user_to_follow=sys.argv[3], conn=conn)

if __name__ == '__main__':
    main()
