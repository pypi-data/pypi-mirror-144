# Dark Fusion - UserBot
# Copyright (C) 2022 TeamFussion
# This file is a part of < https://github.com/TeamFussion/Fusion/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamFussion/pyFussion/blob/main/LICENSE>.

from .. import udB


def get_stuff():
    a = udB.get("MUTE")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        udB.delete("MUTE")
    return {}


def mute(chat, id):
    ok = get_stuff()
    if ok.get(chat):
        if id not in ok[chat]:
            ok[chat].append(id)
    else:
        ok.update({chat: [id]})
    udB.set("MUTE", str(ok))


def unmute(chat, id):
    ok = get_stuff()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    udB.set("MUTE", str(ok))


def is_muted(chat, id):
    ok = get_stuff()
    return bool(ok.get(chat) and id in ok[chat])
