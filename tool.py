import os
import re
import json
import urllib
import urllib.request
import urllib.parse
import urllib.error
import socket
import time
import json
import MySQLdb


def connectionCreate():
    try:
        conn = MySQLdb.connect("localhost",sqlIP,sqlpassword,sqlName, charset='utf8' ) #参数依次：数据库IP、数据库用户名、数据库密码、数据库名
        cur = conn.cursor()
        return conn,cur
    except MySQLdb.Error as e:
        print ('connect'+sqlName+' failed:'+e.args[0])
        pass

def searchByKeyword(keyword):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}    
    # 对要搜索的关键字进行URL编码
    search = urllib.parse.quote(keyword)
    # 图片页码 int类型 用来标明从第几张图片开始下载
    pn = 0
    url = "http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=" + search + "&cg=girl&pn=" + str(pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
    print(url)
    try:
        print("开始获取搜索关键字为：" + keyword)
        time.sleep(0.5)
        res = urllib.request.Request(url=url, headers=headers)
        page = urllib.request.urlopen(res)
        response_json_data = page.read().decode('unicode_escape')
    except UnicodeDecodeError as e:
        print(e)
        print('-----UnicodeDecodeErrorurl:', url)
    except urllib.error.URLError as e:
        print(e)
        print("-----urlErrorurl:", url)
    except socket.timeout as e:
        print(e)
        print("-----socket timout:", url)
    except Exception as e:
        print(e)
        print("未知错误")
    else:
        json_data = json.loads(response_json_data)
        #with open("test_json.json", "w") as f:
            #json.dump(json_data, f)
        save_imgs(json_data, keyword)
    finally:
        #page.close()
        print("关键字为:" + keyword + "的top10图片下载结束")
        print("-----------------------------------------")
    return None



def get_suffix(name):
    suffix = re.search(r"\.[^\.]*$", name).group()
    #print("suffix:", suffix)
    if suffix:
        return suffix
    else:
        return ".jpeg"


def save_imgs(json_data, word):
    if not os.path.exists(word):
        os.mkdir(word)
    conn,c = connectionCreate()
    insert_sql1 = "insert into "+ getImagesTable +" (name) values (\'%s\')"%(str(word))
    try:
        c.execute(insert_sql1)
        conn.commit()
    except MySQLdb.Error as e:
        print ('Insert data failed:'+e.args[0])
        pass
    conn.close()
    __counter = len(os.listdir(word)) + 1
    for image_info in json_data['imgs']:
    #for image_info in json_data['objURL']:
        if __counter <= 12:
            try:
                print("正在获取第" + str(__counter) + "张图片")
                # 间歇爬取
                time.sleep(0.5)
                print("objURL:", image_info['objURL'])
                img_suffix = get_suffix(image_info['objURL'])
                filename = str(word)+str(__counter) + str(img_suffix)
                filename_xdpath = str(word) + '/' + filename
                urllib.request.urlretrieve(image_info['objURL'], filename=filename_xdpath)
                filename_jdpath = str(os.getcwd())+'/'+str(filename_xdpath)
                conn,c = connectionCreate()
                insert_sql2 = "insert into "+ getPathTable +" (name,filename,image_path) values (\'%s\',\'%s\',\'%s\')"%(word,filename,filename_jdpath)
                try:
                    c.execute(insert_sql2)
                    conn.commit()
                except MySQLdb.Error as e:
                    print ('Insert data failed:'+e.args[0])
                    pass
                conn.close()
            #捕获网络访问错误并输出
            except urllib.error.HTTPError as urllib_err:
                print(urllib_err)
                continue
            except Exception as err:
                time.sleep(1)
                print(err)
                print("产生未知错误，未保存该图片")
                continue
            else:
                print("第" + str(__counter) + "张图片获取成功")
                __counter += 1
    return None

def isKeyWordExist(word):
    if not os.path.exists(word):
        os.mkdir(word)
        return False
    else:
        return True

def tableCreateForImages():
    try:
        conn,c = connectionCreate()
        c.execute('create table %s(name varchar(20)) default character set utf8'%(getImagesTable))
        conn.commit()
        print("C su!")
    except:
        pass
    conn.close()

def tableCreateForPath():
    try:
        conn,c = connectionCreate()
        c.execute('create table %s(name varchar(20),filename varchar(50),image_path varchar(150)) default character set utf8'%(getPathTable))
        conn.commit()
    except:
        pass
    conn.close()

def getUrls(keyword):
    try:
        conn,c = connectionCreate()
        sql = "select * from "+ getPathTable + " where name = \'%s\'"%(keyword)
        c.execute(sql)
        results = c.fetchall()
        paths = []
        #c.execute("PRAGMA busy_timeout = 30000")
        for row in results:
            path = row[2]
            paths.append(path)
        return paths
    except MySQLdb.Error as e:
        print ('Search data failed:'+e.args[0])
        pass
    conn.close()

def getHistoryKeyword():
    try:
        conn,c = connectionCreate()
        sql = "select * from "+ getImagesTable
        c.execute(sql)
        results = c.fetchall()
        images = []
        #c.execute("PRAGMA busy_timeout = 30000")
        for row in results:
            image = row[0]
            images.append(image)
        return images
    except MySQLdb.Error as e:
        print ('Search data failed:'+e.args[0])
        pass
    conn.close()


# tableCreateForImages()
# tableCreateForPath()
# words = input("请输入内容(单独输入':w'保存退出):")
# while words != 'tui':
#     searchByKeyword(words)
#     words = input()

#get_json_info("南京大学 12345")
