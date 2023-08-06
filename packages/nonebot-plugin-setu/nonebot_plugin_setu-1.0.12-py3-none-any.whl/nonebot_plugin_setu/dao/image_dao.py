import json
import sqlite3


class ImageDao:
    def __init__(self):
        self.db_path = 'data/lolicon.db'

    def add_images(self, datas):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for data in datas:
            pid = data['pid']
            uid = data['uid']
            title = data['title']
            author = data['author']
            r18 = data['r18']
            width = data['width']
            height = data['height']
            ext = data['ext']
            urls = json.dumps(data['urls'])
            upload_date = data['uploadDate']
            sql = "INSERT OR IGNORE INTO lolicon_images(pid, uid, title, author, r18, width, height, ext, urls, upload_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (pid, uid, title, author, r18, width, height, ext, urls, upload_date))
            tags = data['tags']
            for tag in tags:
                sql = "INSERT OR IGNORE INTO lolicon_tags(pid, tags) VALUES (?, ?)"
                cursor.execute(sql, (pid, tag))
        conn.commit()
        conn.close()

    def get_images(self, pid):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = f"select * from lolicon_images where pid='{pid}'"
        cursor.execute(sql)
        img_info = cursor.fetchone()
        data = {}
        for idx, col in enumerate(cursor.description):
            if col[0] == 'urls':
                data[col[0]] = json.loads(img_info[idx])
            else:
                data[col[0]] = img_info[idx]
        conn.close()
        return data

    def get_tags(self, tags):
        tags = tags.split('&')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql = f"select * from lolicon_tags where tags like '%{tags[0]}%'"
        if len(tags) > 1:
            for tag in tags[1:]:
                sql += f" or tags like '%{tag}%'"
        cursor.execute(sql)
        img_list = []
        for pid in cursor.fetchall():
            img = self.get_images(pid[1])
            img_list.append(img)
        conn.close()
        return img_list






