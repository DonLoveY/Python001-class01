# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from week2.assignment.maoyanSpiderToMySql.maoyanSpiderToMySql.utils.mysql import ConnDB
import random

class MaoyanspiderPipeline:
    # def process_item(self, item, spider):
    #     with open('mysql_maoyan_movie_top10.csv', 'a+', encoding='utf-8') as file:
    #         line = "{title},{category},{date}\n".format(
    #             title=item['title'],
    #             category=item['category'],
    #             date=item['date'])
    #         file.write(line)
    #     return item

    def process_item(self, item, spider):
        dbInfo = {
            'host': 'cnode01',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'kkb'
        }
        a = random.randint(0,100)
        sql = "INSERT INTO user (username, nickName,password,sex, birthday, job, email, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (item['title']+str(a), item['category'], "123", "1", item['date'], "管理员", "admin@test.com.cn", "18187654321")

        db = ConnDB(dbInfo, sql, val)

        db.save2MySql()

        return item
