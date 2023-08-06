import json
import os
import random
import re
from datetime import datetime
from pathlib import Path

from nonebot.adapters.onebot.v11 import Bot, Message, Event, MessageSegment
from nonebot.log import logger
from nonebot.plugin import on_regex

from .create_file import Config
from .dao.groupcd_dao import GroupCdDao
from .dao.image_dao import ImageDao
from .dao.usercd_dao import UserCdDao
from .getPic import get_url, down_pic

setu = on_regex("^涩图$|^setu$|^无内鬼$|^色图$|^涩图tag.+$")
downLoad = on_regex(r"^下载涩图[1-9]\d*$")
user_cd = on_regex(r"^\[CQ:at,qq=[1-9][0-9]{4,10}\] cd\d+$")
group_cd = on_regex(r"^群cd0$|^群cd[1-9]\d*$")
online_switch = on_regex(r"^开启在线发图$|^关闭在线发图$")
proxy_switch = on_regex(r"^开启魔法$|^关闭魔法$")

Config.create_file()
Config.create_table()
super_user = Config().super_users


@setu.handle()
async def _(bot: Bot, event: Event):
    img_path = Path("loliconImages").resolve()
    images = os.listdir(img_path)
    file_name = images[random.randint(0, len(os.listdir('loliconImages'))) - 1]
    pid = re.sub(r'\D+', '', file_name)
    remain_time = 0 if event.get_user_id() in Config().super_users else UserCdDao().get_user_remain_time(
        event.get_user_id(), event.group_id)
    if remain_time == 0:
        try:
            msg = event.get_plaintext()
            tag_flag = 0
            if bool(re.search(r"^涩图tag.+$", msg)):
                tag_flag = 1
                tags = re.sub(r'^涩图tag', '', msg).split('和')
                if len(tags) > 3:
                    await setu.send('涩图tag最多只能有三个哦', at_sender=True)
                    UserCdDao().delete_user_cd(event.get_user_id())
                    return
                else:
                    file_name = await get_url(num=1, tags=tags, online_switch=Config().online_switch)
                    if Config().online_switch == 0:
                        pid = re.sub(r'\D+', '', file_name)
                    if file_name == "":
                        await setu.send('没有找到相关涩图，请更换tag', at_sender=True)
                        UserCdDao().delete_user_cd(event.get_user_id())
                        return
            if Config().online_switch == 1:
                if tag_flag == 0:
                    img = await get_url(num=1, online_switch=1, tags="")
                else:
                    img = file_name
                await setu.send(MessageSegment.image(img['base64']) +
                                f"https://www.pixiv.net/artworks/{img['pid']}", at_sender=True)
                return
            await setu.send(MessageSegment.image(f"file:///{img_path.joinpath(file_name)}") +
                            f"https://www.pixiv.net/artworks/{pid}", at_sender=True)
        except Exception as e:
            logger.error(f'机器人被风控了{e}')
            await setu.send(message=Message('机器人被风控了,本次涩图不计入cd'), at_sender=True)
            UserCdDao().delete_user_cd(event.get_user_id())
    else:
        hour = int(remain_time / 3600)
        minute = int((remain_time / 60) % 60)
        await setu.send(f'要等{hour}小时{minute}分钟才能再要涩图哦', at_sender=True)


@downLoad.handle()
async def _(bot: Bot, event: Event):
    num = int(re.search(r"\d+", event.get_plaintext()).group())
    if event.get_user_id() in super_user:
        try:
            await downLoad.send(f"开始下载...")
            await get_url(num=num, online_switch=0, tags="")
            await downLoad.send(f"下载涩图成功,图库中涩图数量{len(os.listdir('loliconImages'))}", at_sender=True)
        except Exception as e:
            logger.error(f'下载时出现异常{e}')
            await downLoad.send(str(e), at_sender=True)
    else:
        await downLoad.send('只有主人才有权限哦', at_sender=True)


@user_cd.handle()
async def _(bot: Bot, event: Event):
    msg = event.get_message()
    user_id = event.get_user_id()
    if user_id in super_user:
        user_id = msg[0].get('data')['qq']
        cd = int(event.get_plaintext().replace(' cd', ''))
        user = UserCdDao().get_user(user_id)
        if user is None:
            UserCdDao().add_user_cd(user_id, UserCdDao.datetime_to_seconds(datetime.now()), cd)
        else:
            UserCdDao().update_user_cd(user_id, '', cd)
        await user_cd.send(f'设置用户{user_id}的cd成功,cd时间为{cd}s', at_sender=True)
    else:
        await user_cd.send('只有主人才有权限哦', at_sender=True)


@group_cd.handle()
async def _(bot: Bot, event: Event):
    user_id = event.get_user_id()
    if user_id in super_user:
        cd = int(event.get_plaintext().replace('群cd', ''))
        group_id = GroupCdDao().get_group_cd(event.group_id)
        if group_id is None:
            GroupCdDao().set_group_cd(event.group_id, cd)
        else:
            GroupCdDao().update_group_cd(event.group_id, cd)

        await group_cd.send(f'设置群{event.group_id}的cd成功,cd时间为{cd}s', at_sender=True)
    else:
        await group_cd.send('只有主人才有权限哦', at_sender=True)


@online_switch.handle()
async def _(bot: Bot, event: Event):
    msg = event.get_plaintext()
    switch = 1 if msg == "开启在线发图" else 0
    if event.get_user_id() in super_user:
        with open('data/setu_config.json', 'r') as file:
            configs = json.load(file)
            configs['ONLINE_SWITCH'] = switch
            with open('data/setu_config.json', 'w') as f:
                json.dump(configs, f)
                await online_switch.send(f'{msg}成功')
    else:
        await online_switch.send('只有主人才有权限哦', at_sender=True)


@proxy_switch.handle()
async def _(bot: Bot, event: Event):
    msg = event.get_plaintext()
    switch = 1 if msg == "开启魔法" else 0
    if event.get_user_id() in super_user:
        with open('data/setu_config.json', 'r') as file:
            configs = json.load(file)
            configs['PROXIES_SWITCH'] = switch
            with open('data/setu_config.json', 'w') as f:
                json.dump(configs, f)
                await proxy_switch.send(f'{msg}成功')
    else:
        await proxy_switch.send('只有主人才有权限哦', at_sender=True)
