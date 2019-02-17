import json
import datetime
import data_access.wave_manipulations as w_man
import data_access.users_manipulations as u_man
from models.wave import WaveFactory
from models.wave_summary import WaveSummary
from consts.application_level_consts import *
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

        if not InstaHelper.has_post(insta_username):
            return Status.InstagramProfileHasNoPosts

        user = get_user_to_work(user)
        wave = w_man.get_wave_in_state(WaveStates.CREATED)

        if wave is None:
            return Status.NoWaveForRegistration

        to_work_with = json.loads(wave.users_profiles)
        if user.user_id in to_work_with.keys() or insta_username in to_work_with.values():
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
    def delete_user_from_wave(user):
        def get_user_to_work(user_v):
            if u_man.user_exists_with_user_id(user_v.user_id):
                return u_man.get_by_user_id(user_v.user_id)
            else:
                u_man.insert_user(user_v)
                return user_v

        user = get_user_to_work(user)
        wave = w_man.get_wave_in_state(WaveStates.CREATED)

        if wave is None:
            return Status.NoWaveForRegistration

        to_work_with = json.loads(wave.users_profiles)
        if user.user_id not in to_work_with.keys():
            return Status.NotRegisteredInWave

        del to_work_with[user.user.user_id]
        wave.users_profiles = json.dumps(to_work_with)
        w_man.update_wave(wave)

        return Status.UnregisteredFromWave

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
        wave.bidding_start = datetime.datetime.utcnow()
        w_man.update_wave(wave)
        return Status.WaveBiddingStarted, links

    @staticmethod
    def start_assuring_step():
        wave = w_man.get_wave_in_state(WaveStates.BIDDING)
        wave.wave_state = WaveStates.ASSURING
        wave.assuring_start = datetime.datetime.utcnow()
        w_man.update_wave(wave)
        return Status.AssuringStepStarted

    @staticmethod
    def finish_wave():
        wave = w_man.get_wave_in_state(WaveStates.ASSURING)
        posts = json.loads(wave.posts)['posts']
        users_profiles = json.loads(wave.users_profiles)
        warned = InstaHelper.get_wave_warned(posts, users_profiles)
        warned_username = []
        banned = []
        for warned_user_id, insta_profile in warned.items():
            user = u_man.get_by_user_id(warned_user_id)
            user.warnings += 1
            warned_username.append(user.username)
            if user.warnings >= WARNINGS_LIMIT:
                user.is_banned = True
                banned.append(user.username)
            u_man.update_user(user)
        summary = WaveSummary(warned_username, banned)
        wave.finish = datetime.datetime.utcnow()
        wave.wave_state = WaveStates.FINISHED
        w_man.update_wave(wave)
        return Status.WaveIsFinished, summary
