from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import logging
import datetime


class PwnClock(plugins.Plugin):
    __author__ = "https://github.com/LoganMD"
    __version__ = "1.0.4"
    __license__ = "GPL3"
    __description__ = "Clock/Calendar for pwnagotchi"

    def on_loaded(self):
        logging.info("Pwnagotchi Clock Plugin loaded.")

    def on_ui_setup(self, ui):
        memenable = False

        with open("/etc/pwnagotchi/config.toml", "r") as f:
            config = f.read().splitlines()

        if "main.plugins.memtemp.enabled = true" in config:
            memenable = True
            logging.info("Pwnagotchi Clock Plugin: memtemp is enabled")

        if ui.is_waveshare_v2():
            pos = (130, 80) if memenable else (200, 80)

        elif ui.is_waveshare1in54V2():
            pos = (150, 110)

        else:
            pos = (100, 100)

        ui.add_element(
            "clock",
            LabeledValue(
                color=BLACK,
                label="",
                value="-/-/-\n-:--",
                position=pos,
                label_font=fonts.Small,
                text_font=fonts.Small,
            ),
        )

    def on_ui_update(self, ui):
        now = datetime.datetime.now()
        time_rn = now.strftime("%m/%d/%y\n%I:%M%p")
        ui.set("clock", time_rn)
