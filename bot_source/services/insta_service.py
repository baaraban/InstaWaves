import json
import data_access.users_manipulations as u_man
import data_access.wave_manipulations as w_man
from consts.wave_states import WaveStates
from consts.statuses import Status
from instaparser.agents import Agent
from instaparser.entities import Account, Media


class InstaService:
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
            tmp, pointer = agent.get_likes(post, pointer=pointer)
            comments += tmp

        return [x.owner for x in comments]

    @staticmethod
    def get_posts_for_wave(usernames):
        result = []
        agent = Agent()
        for user in usernames:
            result.append(InstaService._get_last_post_link(agent, user))
        return result

    @staticmethod
    def _get_last_post_link(agent, username):
        account = Account(username)
        media1, _ = agent.get_media(account, count=1)
        post = media1[0]
        return InstaService.BASE_INSTAGRAM_POST_LINK.format(post)

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
    def is_profile_private(username):
        agent = Agent()
        account = Account(username)
        agent.update(account)
        return account.is_private

    @staticmethod
    def register_for_wave(user, insta_username):
        def get_user_to_work(user_v):
            if u_man.user_exists_with_username(user_v.user_id):
                return u_man.get_by_user_id(user_v.user_id)
            else:
                u_man.insert_user(user_v)
                return user_v

        if InstaService.profile_exists(insta_username):
            return Status.InstagramProfileDoesNotExist

        if InstaService.is_profile_private(insta_username):
            return Status.InstagramProfileIsPrivate

        user = get_user_to_work(user)
        wave = w_man.get_wave_in_state(WaveStates.CREATED)

        to_work_with = json.loads(wave.users_profiles)
        if user.user_id in to_work_with.keys():
            return Status.AlreadyRegisteredForWave

        to_work_with[user.user_id] = insta_username
        wave.users_profiles = json.dumps(to_work_with)
        w_man.update_wave(wave)

        profiles = json.loads(user.profiles)
        if insta_username not in profiles.keys():
            profiles[insta_username] = insta_username
            user.profiles = json.dumps(profiles)
            u_man.update_user(user)

        return Status.RegisteredForWave
