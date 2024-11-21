from AmritaXMusic.core.bot import RAUSHAN
from AmritaXMusic.core.dir import dirr
from AmritaXMusic.core.git import git
from AmritaXMusic.core.userbot import Userbot
from AmritaXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()