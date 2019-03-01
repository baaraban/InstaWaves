from instaparser.agents import Agent
from instaparser.entities import Account, Media


class InstaHelper:
    BASE_INSTAGRAM_POST_LINK = 'https://www.instagram.com/p/{}'

    @staticmethod
    def get_who_liked_post(agent, media):
        post = Media(media)

        likes, pointer = agent.get_likes(post)

        while pointer is not None:
            tmp, pointer = agent.get_likes(post, pointer=pointer)
            likes += tmp

        return [x.login for x in likes]

    @staticmethod
    def get_who_commented_post(agent, media):
        post = Media(media)

        comments, pointer = agent.get_comments(post)

        while pointer is not None:
            tmp, pointer = agent.get_comments(post, pointer=pointer)
            comments += tmp

        return [x.owner.login for x in comments]

    @staticmethod
    def get_posts_for_wave(usernames):
        links = []
        posts = []
        agent = Agent()
        for user in usernames:
            post, link = InstaHelper._get_last_post_link(agent, user)
            posts.append(post)
            links.append(link)
        return [str(x) for x in posts], links

    @staticmethod
    def _get_last_post_link(agent, username):
        account = Account(username)
        media1, _ = agent.get_media(account, count=1)
        post = media1[0]
        return post, InstaHelper.BASE_INSTAGRAM_POST_LINK.format(post)

    @staticmethod
    def profile_exists(username):
        try:
            agent = Agent()
            account = Account(username)
            agent.update(account)
            return True
        except:
            return False

    @staticmethod
    def has_post(username):
        agent = Agent()
        account = Account(username)
        media1, _ = agent.get_media(account)
        return len(media1) != 0

    @staticmethod
    def is_profile_private(username):
        agent = Agent()
        account = Account(username)
        agent.update(account)
        return account.is_private

    @staticmethod
    def get_warned_by_post(agent, post, users_profiles):
        media = Media(post)
        comments = InstaHelper.get_who_commented_post(agent, media)
        likes = InstaHelper.get_who_liked_post(agent, media)
        warned = {}
        for user_id, profile in users_profiles.items():
            if str(media.owner) == profile:
                continue
            if profile not in likes:
                warned[user_id] = profile
                continue
            if profile not in comments:
                warned[user_id] = profile
        return warned

    @staticmethod
    def get_wave_warned(posts, users_profiles):
        agent = Agent()
        warned = {}
        for post in posts:
            warned.update(InstaHelper.get_warned_by_post(agent, post, users_profiles))
        return warned

