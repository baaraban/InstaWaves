from models.wave import Wave, WaveFactory
import data_access.wave_manipulations as w_man


class WaveService:
    @staticmethod
    def create_wave():
        new_wave = WaveFactory.get_new_wave()
        w_man.insert_wave(new_wave)