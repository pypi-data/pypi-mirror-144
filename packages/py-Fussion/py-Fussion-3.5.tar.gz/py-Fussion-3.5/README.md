# py-Fussion Library
A stable userbot base library, based on Telethon.

[![PyPI - Version](https://img.shields.io/pypi/v/py-Fussion?style=for-the-badge)](https://pypi.org/project/py-Fussion)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-Fussion?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/py-Fussion)

## Installation
`pip install py-Fussion`

## Usage
=> Create folders named `plugins`, `addons`, `assistant` and `resources`.<br/>
=> Add your plugins in the `plugins` folder and others accordingly.<br/>
=> Create a `.env` file with `API_ID`, `API_HASH`, `SESSION`, `REDIS_URI` & `REDIS_PASSWORD` as mandatory environment variables. Check
[`.env.sample`](https://github.com/TeamFussion/Dark-Fusion/blob/main/.env.sample) for more details.<br/>
=> Run `python -m pyFussion` to start the bot.<br/>

### Creating plugins
- To work everywhere

```python
@ultroid_cmd(
    pattern="start",
)   
async def _(e):   
    await eor(e, "Fussion Started")   
```

- To work only in groups

```python
@ultroid_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "Fussion Started")   
```

- Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("Fussion Started")   
```

Made with 💕 by [@TeamFussion](https://t.me/DarkFussion). <br />

# Credits
* [![TeamFussion](https://img.shields.io/static/v1?label=TeamFussion&message=devs&color=critical)](https://t.me/DarkFussion)
* [![TeamUltroid-Devs](https://img.shields.io/static/v1?label=Teamultroid&message=devs&color=critical)](https://t.me/UltroidDevs)
* [![Lomani](https://img.shields.io/static/v1?label=Lomani&message=devs&color=critical)](https://github.com/LonamiWebs/Telethon)
