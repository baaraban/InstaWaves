from models.wave import WaveFactory
import data_access.wave_manipulations as w_man
from consts.statuses import Status


class WaveService:
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
        return

    @staticmethod
    def start_assuring_step():
        return

    @staticmethod
    def finish_wave():
        return
