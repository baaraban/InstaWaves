from instaparser.agents import Agent
from instaparser.entities import Account, Media


BASE_INSTAGRAM_POST_LINK = 'https://www.instagram.com/p/{0}'


def get_who_liked_post(agent, media):
    post = Media(media)

    likes, pointer = agent.get_likes(post)

    while pointer is not None:
        tmp, pointer = agent.get_likes(post, pointer=pointer)
        likes += tmp

    return [x.login for x in likes]


def get_who_commented_post(agent, media):
    post = Media(media)

    comments, pointer = agent.get_comments(post)

    while pointer is not None:
        tmp, pointer = agent.get_likes(post, pointer=pointer)
        comments += tmp

    return [x.owner for x in comments]


def get_posts_for_wave(usernames):
    result = []
    agent = Agent()
    for user in usernames:
        result.append(_get_last_post_link(agent, user))
    return result


def _get_last_post_link(agent, username):
    account = Account(username)
    media1, _ = agent.get_media(account, count=1)
    post = media1[0]
    return BASE_INSTAGRAM_POST_LINK.format(post)


def profile_exists(username):
    try:
        agent = Agent()
        account = Account(username)
        agent.update(account)
        return True
    except:
        return False


def is_profile_private(username):
    agent = Agent()
    account = Account(username)
    agent.update(account)
    return account.is_private
