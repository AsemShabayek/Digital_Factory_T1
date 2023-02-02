a link for the youtube video explaining the process https://youtu.be/HKN9jsmgTvI


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

#### I. XML file preparation
The URDF file should be saved as xml, this can be done by opening the file using Visual Studio Code and use Save as and select .xml\
Or it can be done by simply renaming the file and change the extension to be .xml

#### II. GLB File preparation
In this step we need to use Blender 3D\
After Importing all the file/files to an empty blender workspace, we need to organize the heirarchy of the meshes, without changing anything related to positions, rotations and locations, making sure that the cursor is located on the world origin (as default).\

The organizing of the heirarchy can be done by:-

1- Adding an empty plain axis for each link. \
2- Making it the parent for the link's mesh/meshes. \
3- Organizing the heirarchy of the plain axes by making each link's plain axis a parent for the following link's plain axis to look like the following screenshots.\
![single meshes for each link](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Parents%20Heirarchy%20single%20meshes.png)
![multiple meshes for each link](https://github.com/AsemShabayek/Digital_Factory_T1/blob/main/Screenshots/Parents%20Heirarchy%20multiple%20meshes.png)

#### III. JSON file Preparation
