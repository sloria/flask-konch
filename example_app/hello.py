import typing

from flask import Flask

BANNER = """
           ╓É^▄
           ╙▓▓▓
            ▄▓▓▓▀▓▓
          ▐▓▓▓▓▓▀▀█▓▓▄▄▄
          ▄▓▓▓▓▓▓▄4▀▀▓▓▓▓▄▄
       ▓▓▓▓▓▓▓▓▓▓▓▓▄╓██▀▓▀▀▀▀^▄▄,
      ▄▓▓▓▓▓▓██▀▀▀      └   ,▄█▓▓▓Σ,
    ]▓█▀▌▀▓▓   ▄  ▄▄▄▄▄▄██▀▀▓     └.
    █▓ ▓▄  ▓▓▄▄▓▓▓▓▀▀ ▀`    ▐
     █▓▓▓▓▓▓▓██▓▀▀        ▓ƒ▓
      ▓▓▓▓▓▓▓▓▓▓   ▄`     └ ▐─
      ▐▓▓▓▓▓▓▀    ▓▄─       ▐▌
       ▓▓▓▓▓▓▄k▄▓▌           ▌
       ▐▓▀▓▓▓▄ ▓.  ,▌▄   ▓▄ ,▓
        █▓▐▓▓▓█ ▄▌▓▓▄██   ▀ └▐▄
         ▓▌█▓▓▓▓ ▓▓█          ▓
          ▓▀▓▓▓▓▌ ▀`▓          ▌
           ▓▓▓▓▓▓▓▓▄▄▓▓▓▓▀▄   `▓▌
            █▄█▓▓▓▓▓` ╠▓▓▓█    É█▌
             ▀▓▀▓▓▓▓▌ `▓▓▓▓▄▄    ╕╙▄
               ▓▄▓▓▓▓▓▓▄▓▓▓▓█▓     ^█▄
                ▀▓▀▓▓▓▓▀▀█▓▓█▓k▄   ╙ ╙▓▄
                  ▀▄▀▓▓▓▓▓▓▓▓▓▓▓▓▓▄    █▓▄
                    ▀▌▀▀▓▓▓▓▓▓▓▓▓▄▓██    ▀▀█▌▄              ,
                      ╙▀▓▓▓▓▓▓▓▓▓▓▓▓▓▌        ▀▓▓▄▄      ,▄▓▓▀
                         ▀█▓▓▓█▓▓▓▓▓▓▓▓▓▄▄▓▓▓▀ÿ▄▄.╙▀█▓▓▓▓██▓▄▄▄▄▄,▄▌▄▄▄▄▄
                             ▀▀█▄▌▀█▓▀██▓▓▓▓▓▓▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                                 . ╙²█████▓▓▓▓▀▀▀▀▀▀▀▀▓▓▓▓▓▓▓▓██▀▀▀▀▀
                                              .    .   .
"""


class User:
    pass


db: dict[str, typing.Any] = {}


class Config:
    SERVER_NAME = "hello.test"
    KONCH_CONTEXT = {"User": User, "db": db}
    KONCH_BANNER = BANNER


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "Hello"
