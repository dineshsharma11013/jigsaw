from datetime import datetime
from flask import jsonify, current_app
import os
from app.helper import Helper
from datetime import datetime

hl = Helper()

class BlogMdl():
    def __init__(self):
        try:
            current_time = datetime.now()
            self.formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            #print("connected successfully")
        except Exception as e:
            print("error - ",e)
            
            
    def getBlogs(self):
        return hl.getAllData('blogs')    
            
    
    def save_blog(self, data, rem_addr, fl):
            
        img_path = current_app.config['file_dir']
        if 'img' in fl:
            file = hl.make_unique(fl['img'].filename)
            #print("file name ", img_path)
            fl['img'].save(img_path+'/blogs/'+file)
        else:
            file = ''    
        #print("res ",res)
        print("data ", current_app, img_path)
        
        res = {
            'title':data['title'],
            'img':file, #data.get('img', 'sdf'),
            'msg':data['msg'],
            'url':hl.create_slug(data['title']),
            'tags':data['tags'],
            'rem_addr':rem_addr,
            'created_at':datetime.now(),
            'updated_at':''
        }
        return hl.insertData(res, 'blogs')
        
    def getSelectedData(self, id):
        return hl.getSingleRow('blogs', id)            
    
    def updateSelectedData(self, data, rem_addr, fl, id):
        cat, status_code = self.getSelectedData(id)
        if status_code == 200:
            print(cat['payload']['title'])
            old_img = cat['payload']['img']
        #return cat
        img_path = current_app.config['file_dir']
        if 'img' in fl:
            if old_img != '':
                if os.path.exists(img_path+'/blogs/'+ old_img):
                    os.unlink(img_path +'/blogs/'+ old_img)
            
            file = hl.make_unique(fl['img'].filename)
            fl['img'].save(img_path+'/blogs/'+file)
        else:
            file = old_img    
        print("data ", current_app, img_path)
        
        res = {
            'title':data.get('title', cat['payload']['title']),
            'img':file, #data.get('img', 'sdf'),
            'msg':data.get('msg', cat['payload']['msg']),
            'url':hl.create_slug(data['title']),
            'tags':data.get('tags', cat['payload']['tags']),
            'rem_addr':rem_addr,
            'updated_at':datetime.now()
        }
        
        return hl.updateData(res, 'blogs', id)        
            
    def deleteSelected(self, id):
        return hl.deleteSelectedData('blogs', id)        
            
            
            
            
            
            
            
            
            
            