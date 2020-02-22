import time
import leveldb

# �e�X�g�f�[�^�F750�o�C�g
inputData = '{"_id" : "ObjectId(\5e3b4dd825755df3f15a2d17\")","coediting" : False,"comments_count" : 0,"created_at" : "2020-02-05T20:20:10+09:00","group" : None,"id" : "6ed1eec1d6fba127a863","likes_count" : 0,"private" : False,"reactions_count" : 0,"tags" : [{"name" : "Python","versions" : [ ]},{"name" : "MongoDB","versions" : [ ]},{"name" : "Python3","versions" : [ ]},{"name" : "pymongo","versions" : [ ]}],"title" : "Python��mongoDB�𑀍삷��`���̂U�Faggregate�ҁ`","updated_at" : "2020-02-05T20:20:10+09:00","url" : "https://qiita.com/bc_yuuuuuki/items/6ed1eec1d6fba127a863","page_views_count" : 96,"tag1" : "Python","tag2" : "MongoDB","tag3" : "Python3","tag4" : "pymongo","tag5" : "","tag_list" : ["Python","MongoDB","Python3","pymongo"],"stocks_count" : 0}'

start = time.time()

db = leveldb.LevelDB("measurement_test")

start = time.time()

for i in range(1,1000001):
    db.Put(i.to_bytes(4, 'little'), inputData.encode('utf-8'))
    if i % 100 == 0:
        end = time.time()
        print("{0}:{1}".format(i,end-start))
        start = end