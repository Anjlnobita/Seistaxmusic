from Seistaxmusic.core.bot import NOBI
from Seistaxmusic.core.dir import dirr
from Seistaxmusic.core.git import git
from Seistaxmusic.core.userbot import Userbot
from Seistaxmusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NOBI()
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