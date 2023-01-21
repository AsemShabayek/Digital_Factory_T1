#initiating the libraries
xmlfile = input("Please insert the name of the xml file (including the .xml): ")
#xmlfile = input("Please insert the name of the xml file (including the .xml):")
#xmlfile = xmlfile or "ABB.xml"
import json
import xml.etree.ElementTree as ET
import bpy
import mathutils
tree = ET.parse(xmlfile)
root = tree.getroot()

main_filename = input("Please insert the name of the GLB file (including the .glb): ")
main_filename = main_filename or "7amada.glb"
euler_convention = input("Please insert the Euler Convention of the used file in capital: ")
euler_convention = euler_convention or "ZYX"

def add_word_to_list_items(lst, word):
    return [word+"." + item for item in lst]


#RepoPath=input("Please Enter the raw link of the glb's folder")

#lists for saving links and joints
links =[]
joints=[]

#finding all robots names
robotname = root.attrib.get("name", main_filename[:-4])

#finding all the links names
for elm in root.findall(".//link"):
    linkname=elm.attrib["name"]
    links.append(linkname)

#finding all the joints names
for elm in root.findall(".//joint"):
    jointname=elm.attrib["name"]
    joints.append(jointname)

y=len(links)
assets=[0]*(y+1)

#looking for the data of each link name

x=1
for link in links:
    fname=0
    parent=0
    child=0
    assets[x]={"id":(robotname+"."+link)}
    #finding the file name
    for elm in root.findall(f".//link[@name='{link}']/visual/geometry/mesh"):
        #filenames[x]=(elm.attrib["filename"])
        fname=(elm.attrib["filename"])
    if fname!=0:
        #print (fname)
        assets[x]["representations"]=([{"file":(main_filename+fname),"unit":1}])
        for joint in joints:
            #finding if there are any parents for the link
            for elm in root.findall(f".//joint[@name='{joint}']/child[@link='{link}']"):
                child=1
                #finding the parent name
                for elm in root.findall(f".//joint[@name='{joint}']/parent"):
                    parent=(elm.attrib["link"])
                #finding position and rotations of the link
                for elm in root.findall(f".//joint[@name='{joint}']/origin"):
                    rpy=(elm.attrib["rpy"])
                    xyz=(elm.attrib["xyz"])
                if xyz!=0:
                    xyz_list = [float(num) for num in xyz.split()]
                    assets[x]["position"]=(xyz_list)
                if rpy!=0:
                    rpy_list = [float(numz) for numz in rpy.split()]
                    #print (rpy_list)
                    xs, ys, zs = rpy_list[0], rpy_list[1], rpy_list[2]
                    rot_ZYX = mathutils.Euler((xs, ys, zs), euler_convention)
                    rot_mat = rot_ZYX.to_matrix()
                    rot_YXZ = rot_mat.to_euler('YXZ')
                    new_rpy_list=[(round((rot_YXZ.x),4)),(round((rot_YXZ.y),4)),(round((rot_YXZ.z),4))]
                    #print(new_rpy_list)
                    assets[x]["rotation"]=(new_rpy_list)
                if parent!=0:
                    assets[x]["placementRelTo"]=(robotname+"."+parent)
                    assets[x]["parentObject"]=(robotname+"."+parent)
            if child ==0:
                    assets[x]["placementRelTo"]=(robotname)
                    assets[x]["parentObject"]=(robotname)
    x=x+1

assets[0]={"id":(robotname)}
assets[0]["representations"]=([{"file":main_filename,"unit":1}])
my_list = ['item1', 'item2', 'item3']
links = add_word_to_list_items(links, robotname)
links.insert(0, robotname)
data=dict()
data['context']={"UnitOfMeasureScale": 1,"Zup": True,"RepoPath":''}
data ['scene']=links
data['assets']=assets

output_filename = xmlfile.replace(".xml", ".json")
x= json.dumps(data, indent=4)
with open(output_filename, "w") as outfile:
    outfile.write(x)
#print (json.dumps(data,indent=4))
