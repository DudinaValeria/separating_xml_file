#!/usr/bin/env python

import xml.etree.ElementTree as xml
import xml.etree.ElementTree as ET
import urllib


path= urllib.request.urlopen("https://files.sima-land.ru/mav.xml")

tree = ET.ElementTree(file=path)
root = tree.getroot()
a_s=[]
for child_of_root in root:
    a_s=child_of_root.getchildren()
    #print(a_s)

s=[]
s_names=[]
for child_of_root in a_s[4]:

        s.append(child_of_root.attrib)
        
        s_dict={"category_id":child_of_root.attrib.get("id"),"name":child_of_root.text}
        s_names.append(s_dict)

level1=[]
for i in s:
    if i.get('parentId') is None:
        
        level1.append(i.get('id'))
        
        


level2=[]
j=0
l=0
no=0
cat_all=len(level1)
num=int(cat_all/4)
no=0


for no in range(num):
    
    a_root=xml.Element("catalog")
    categ=xml.SubElement(a_root,"categories")
    
   
    if len(level1)<4:
        num_range=len(level1)
    else :
        num_range=4
    for j in range(num_range):
        level2.append(level1[j])
        for child_of_root in a_s[4]:
            
            if (child_of_root.attrib.get('parentId')==level1[j]) :
                of=xml.SubElement(categ,"categoty",child_of_root.attrib)
                
                for ind in range(len(s_names)):
                    if child_of_root.attrib.get("id")==s_names[ind].get('category_id'):
                        
                        of.text=str(s_names[ind].get('name'))
                        s_names.pop(ind)
                        break
        
        level1.pop(j)
                    
    for k in s:
        
        if k.get('parentId') is not None:
            for val in level2:
                if (k.get('parentId')==val) :
                    level2.append(k.get('id'))
                    of=xml.SubElement(categ,"categoty",attrib=k)
                    for ind in range(len(s_names)):
                        if k.get("id")==s_names[ind].get('category_id'):
                        
                            of.text=str(s_names[ind].get('name'))
                            s_names.pop(ind)
                            
                            break
                                
    root2 = a_s[5]
    off2=xml.SubElement(a_root,"offers")
    root3=root2.getchildren()
    
    for q in root3:
        
        for w in level2:  
            
            if q.getchildren()[4].text==w: 
                
                item=xml.SubElement(off2,"offer",q.attrib)
                item.append(q)
                    
                root3.remove(q)

    file_name="/home/bitrix/www/upload/partners/simaland/simaland_"+str(no)+".xml"
    
   
    a_tree = xml.ElementTree(a_root)
    
    a_tree.write(file_name, encoding='utf-8',xml_declaration=True)  
    level2.clear()
    a_root.clear()     
    print("done",no)
     
    
    
    
