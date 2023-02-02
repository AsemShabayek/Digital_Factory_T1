# URDF to JSON Converter

This project is aiming to convert URDF files to JSON files, to be able to use them in [The Virtual Learning Factory Toolkit (VLFT)]('https://virtualfactory.gitbook.io/vlft/') visualizing the robots using [VEB.Js]('https://virtualfactory.gitbook.io/vlft/tools/vebjs').\
![VEB.js](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/a%20robot%20inside%20the%20VEB.js.png)

## How to use the URDFtoJSON Converter
In this section the Steps of using the URDFtoJSON converter will be explained.
### Workflow Required Inputs
to work with the URDF to JSON Converter, you need to have and prepare the following:-\
1- URDF file\
2- Mesh files of the robot

### Workflow Outputs
after working with the URDFtoJSON converter you will have the following:-\
1-JSON file\
2-GLB file\
these files will be used in the VEB.js environment to be able to visualize the robot.
### Steps to have the required output files.
In the following steps we will use the input files obtained from the URDF package (URDF & Mesh files) to have the output files (JSON & GLB files)
___
#### I. XML file preparation
The URDF file should be saved as xml, this can be done by opening the file using Visual Studio Code and use Save as and select .xml\
Or it can be done by simply renaming the file and change the extension to be .xml
___
#### II. GLB and Blend File preparation
In this step we need to use Blender 3D\
After Importing all the file/files to an empty blender workspace, we need to organize the heirarchy of the meshes, without changing anything related to positions, rotations and locations, making sure that the cursor is located on the world origin (as default).\

The organizing of the heirarchy can be done by:-

1- Adding an empty plain axis for each link. \
2- Making it the parent for the link's mesh/meshes. \
3- Organizing the heirarchy of the plain axes by making each link's plain axis a parent for the following link's plain axis to look like the following screenshots.\
![single meshes for each link](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Parents%20Heirarchy%20single%20meshes.png)
![multiple meshes for each link](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Parents%20Heirarchy%20multiple%20meshes.png)\
4- after this step we need to export the glb file and the blend file with the same name.\
the Glb file needs to have the Y+ up (as default export options)\
![exporting the glb file options](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/GLB%20export%20options.png)
___
#### III. JSON file Preparation
From the steps I & II we should have now an XML file, a GLB file and a Blend file.
All the files should be added to the same folder along with the 2 python code files [URDFtoJSON_V02.py](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/URDFtoJSON_V02.py) and [supportive_functions.py](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/supportive_functions.py), as shown in the following screenshot. \
![Folder contents example](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/folder%20contents.png)\
1- We should open the command prompt and run the python code.\
![JSON 1st step](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Json%201st%20step.png)\
2- After running the code, you will be required to write the files names, as discussed before, all the files should be with the same name, if they are not exactly the same (case sensitive) the generator will not work properly.\
so we will write `Example` without any extensions\
![JSON 2nd step](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Json%202nd%20step.png)\
3- A pop-up window will show up requiring you to select the euler convention of the input file.\
It can be found in the documentation of the file, it’s very important step, as VEB.js is requiring the angles to be with YXZ convention in the JSON file.\
In the previous trials we have found out that ZYX is working well most of the times.\
but some other times it might be XYZ.\
![JSON 2nd step](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Json%203rd%20step.png)\
4- After selecting the Euler convention, a similar pop up window will show up requiring you to select the object name that resembles certain links from the URDF.\
it will show up N times, N = number of links, one time for each link, and each time you should select the object name representing the link written in the message of the pop-up window.\
![JSON 2nd step](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/JSON%204th%20Step.png)\
5- After finalizing this process of the objects names selection.The process of generating the JSON file is done.\
You will find a JSON file with the same name added to the same file directory where you added the previous files in the first step of the JSON file preparation.\
![JSON 2nd step](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/JSON%205th%20STep.png)
___
#### IV. Visualizing the Robot Using VEB.js
1- Uploading the JSON & the GLB to a GitHub repository.\
2- using this link to test the file replacing the indicated space with the raw link of the JSON file and the raw link of the path where the GLB file is located.\

http://ec2-54-174-51-194.compute-1.amazonaws.com/vebjs/?inputscene=INSERT_THE_RAW_LINK_OF_THE_JSON_HERE&&?inputenv=https://wterkaj.github.io/RepoExample/example_robot/Robot_env.json&repoMod3d= INSERT_THE_RAW_LINK_OF_THE_GLB_LOCATION_HERE\
in our case this will be the link\
http://ec2-54-174-51-194.compute-1.amazonaws.com/vebjs/?inputscene=https://raw.githubusercontent.com/AsemShabayek/URDFtoJSON/main/Example.json&&?inputenv=https://wterkaj.github.io/RepoExample/example_robot/Robot_env.json&repoMod3d=https://raw.githubusercontent.com/AsemShabayek/URDFtoJSON/main/\
3- we should see the robot visualized\
![VEB.js](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/a%20robot%20inside%20the%20VEB.js.png)

### In case there is no URDF available
In case of no URDF file available for a required robot, we need at least a .STEP file or any similar file for the robot, mostly it will be available at the manufacturer website, then we can generate the URDF and the meshes in the previous steps using [SW2URDF](http://wiki.ros.org/sw_urdf_exporter/Tutorials/Export%20an%20Assembly)

#### SW2URDF

It works by defining the objects representing each link and exporting them in one part, so the total number of the exported parts equals the number of links.\
It also adds joints, it can be done by two methods:-\
1- by manually inserting axes in the desired places, it will not be so efficient and can make some errors.\
2- by firstly making all the mates correctly then work on the add-in which will be able to define the joints’ locations and type, as long as there is only one degree of freedom for each link.\
There is a good tutorial for how to use it on [this link](http://wiki.ros.org/sw_urdf_exporter/Tutorials/Export%20an%20Assembly)

###### *Important notes on SW2URDF.*
there are three things needs to be taken care of to have a smoother and easier process.\
1- to assemble the parts correctly and having only one degree of freedom at maximum for each part, except the first part, it should better be fixed.\
2- at the last step before exporting, we can change the roll, pitch, yaw for the joints, it will be much easier to make their original values as Zeros, as it will reduce the confusion about which Euler Angle convention should be selected.\
3- to make the assembly standing on the top plan to be in a normal orientation if we are looking at it from an isometric view as shown in the image.\
![Isometric view](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Isometric.png)
___

## A deeper look into the code
In This section we will take a deeper look on the code we are using.\
we are using two python files [URDFtoJSON_V02.py](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/URDFtoJSON_V02.py) and [supportive_functions.py](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/supportive_functions.py).\
the 1st file includes the main code, the 2nd one includes some supportive functions to have more organized python code.

### Used Libraries
- XML.etree Library, used for parsing and manipulating xml data.
- JSON in python, used to work with Json data.
- Mathutils, used for Euler angles convention conversion.
- Blender in python, used in reading the plain axes names.
- Tkinter in python, Used for making GUI pop-up lists.

#### A previous version of the code
there is an outdated version of the code before adding the pop up lists of selecting the Euler angles convention and the links names
[URDFtoJSON.py](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/URDFtoJSON.py)

___
## Possible future enhancements
-	A full GUI interface to generate the files without the need to run the python code from the command prompt.
-	The ability to extract the colors and textures, either from the blend file or the STEP file.
-	Using Bpy library to generate the GLB files from the mesh files without downloading them manually.

___

# Useful links
- Youtube [link](https://youtu.be/HKN9jsmgTvI) of tutorial video.
- PDF documentation of the project, [link](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/DF-01.pdf)


