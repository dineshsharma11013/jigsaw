from app.models import cur
from flask import jsonify, current_app
from uuid import uuid4
import os
import re

class Helper():
        def make_unique(self, filename):
                ident = uuid4().__str__()
                extension = filename.split('.')[-1]
                return f"{ident}.{extension}"
    
        def getSingleRow(self, tbl, id):
                try:
                        cur.execute(f'SELECT * FROM {tbl} WHERE id = %s', (id,))
                        check = cur.fetchone()
                        if check:
                                return {'payload': check}, 200
                        else:
                                return {'msg': 'There is no data'}, 204
                except Exception as e:
                        print(e)
                        return {'error': 'Server Error'}, 500         
    
        def getAllData(self, tbl):
                try:
                        cur.execute(f"SELECT * FROM {tbl}")
                        data = cur.fetchall()  
                        if len(data)>0:
                                return {'payload':data}, 200
                        else:
                                return {'msg':'There is no data'}, 200
                except Exception as e:
                        return {'error':'Failed to save data'}, 500     
                
        def deleteSelectedData(self, tbl, id):
                try:
                        query = f"select * from {tbl} where id = %s"
                        cur.execute(query, (id,))
                        check = cur.fetchone()
                        if check:
                                print(check)
                                img_path = current_app.config['file_dir']
                                old_img = check['img']
                                if os.path.exists(img_path+'/blogs/'+ old_img):
                                        os.unlink(img_path +'/blogs/'+ old_img)
                                
                                query2 = f"delete from {tbl} where id = %s"
                                cur.execute(query2, (id,))
                                return {'msg':'data available'}, 200
                        else:
                                return {'msg':'there is no data'}, 200
                except Exception as e:
                        print(e)
                        return {'error':'Server Error'}, 500        
                        
        def insertData(self, data, tbl):
                try:
                        keys = ', '.join(data.keys()) # This retrieves all the keys from the dictionary data.
                                # For example, if data is {'name': 'Alice', 'age': 30}, then data.keys() will be dict_keys(['name', 'age']).
                                # ', '.join(...): This joins the keys into a single string, separated by commas and spaces. Using the example above, it results in 'name, age'.        
                                
                        placeholders = ', '.join(['%s'] * len(data))
                        # ['%s'] * len(data): This creates a list where '%s' (a placeholder for a value in SQL) is repeated for each key in the data dictionary. If data has 2 keys, the list would be ['%s', '%s'].        
                        
                        values = tuple(data.values())
                        
                        #data.values(): This retrieves all the values from the dictionary data. For example, if data is {'name': 'Alice', 'age': 30}, then data.values() will be #dict_values(['Alice', 30]).
                        #tuple(...): This converts the values into a tuple. So dict_values(['Alice', 30]) becomes ('Alice', 30).        

                        query = f"INSERT INTO {tbl} ({keys}) VALUES ({placeholders})"
                        
                        print("query is", query)
                        print("values are", values)
                        
                        cur.execute(query, values)
                        
                        return {'msg': 'Data saved successfully'}, 201       
                except Exception as e:
                        print("error ", e)
                        return {'error':'Failed to save data'}, 500
        
        
        # def create_slug(self, title):
        #         slug = title.lower()
        #         slug = re.sub(r'\s+', '-', slug)  # Replace spaces with hyphens
        #         slug = re.sub(r'[^\w-]', '', slug)  # Remove non-alphanumeric characters
        #         return slug    
        
        
        def create_slug(self, title):
                return title.lower().replace(' ', '-')    
        
        
        def updateData(self, data, tbl, id):
                try:
                        query = f'update {tbl} set'
                        for key in data:
                                query += f" {key} = '{data[key]}',"
                                #print("loop ",key, data[key])
                        query = query[:-1] + f" WHERE id = {id}"        
                        print(query)
                        cur.execute(query)
                        if cur.rowcount>0:
                                return jsonify({'msg': 'Data updated successfully'}), 200       
                        else:
                                return jsonify({'msg': 'Data not updated'}), 204          
                except Exception as e:
                        print("error ", e)
                        return jsonify({'msg': 'Failded to update'}), 500       