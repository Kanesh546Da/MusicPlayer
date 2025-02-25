"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "13303918")
        self.API_HASH: str = os.environ.get("API_HASH", "24f473f4478796b9a416e4e68b49ab25")
        self.SESSION: str = os.environ.get("SESSION", "BQDLAG4AXMbnSpqwA3JXNhnQR99UcpLQUWd8TZH68BNJw6VZOefq78Bpn3EK5apDin65PM62X5Sb5bArhJF_n0DfPNmTEi4duvLLn4AZ-65XzkBGkbbth8FYLmm7vofr1pFZErPWJPVWzTgtPEnJ8TSVYNE_XnR38VXUjxsvWDIPcw1q4KUsMWHVo16I0wwNnt-2NxujDB-idUPYlrIKNeIPCTdC24T80jJkcIC7eA9LRQemHRUBT-KwUD28MIgAd8Qo6Wr9sCzq5loiYJdGRtSgWfcd6m6pxYK9VG7I_f8oCfUZti2q86gqkz31OG3YWm1AGfu_2PP-mSheE4qJudpA7-M6egAAAAA2mX5BAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6839471362:AAEejQnQ3wxuRsMy18FKfq-pplEzO5G9d4U")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5094761774 8092453704").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
