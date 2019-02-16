import json
import data_access.wave_manipulations as w_man
import data_access.users_manipulations as u_man
from models.wave import WaveFactory
from consts.statuses import Status
from helpers.insta_helper import InstaHelper
from consts.wave_states import WaveStates


class WaveService:
    @staticmethod
    def register_for_wave(user, insta_username):
        def get_user_to_work(user_v):
            if u_man.user_exists_with_user_id(user_v.user_id):
                return u_man.get_by_user_id(user_v.user_id)
            else:
                u_man.insert_user(user_v)
                return user_v

        if not InstaHelper.profile_exists(insta_username):
            return Status.InstagramProfileDoesNotExist

        if InstaHelper.is_profile_private(insta_username):
            return Status.InstagramProfileIsPrivate

        user = get_user_to_work(user)
        wave = w_man.get_wave_in_state(WaveStates.CREATED)

        if wave is None:
            return Status.NoWaveForRegistration

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

    @staticmethod
    def create_wave():
        try:
            new_wave = WaveFactory.get_new_wave()
            w_man.insert_wave(new_wave)
            return Status.NewWaveCreated
        except:
            return Status.InternalError

    @staticmethod
    def start_bidding():
        wave = w_man.get_wave_in_state(WaveStates.CREATED)
        usernames = json.loads(wave.users_profiles).values()
        posts, links = InstaHelper.get_posts_for_wave(usernames)
        post_dict = {'posts': posts}
        wave.posts = json.dumps(post_dict)
        wave.wave_state = WaveStates.BIDDING
        w_man.update_wave(wave)
        return Status.WaveBiddingStarted, links

    @staticmethod
    def start_assuring_step():
        return

    @staticmethod
    def finish_wave():
        return
