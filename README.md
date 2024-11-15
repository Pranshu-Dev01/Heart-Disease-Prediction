# Heart Disease Prediction

## Description
A Regression type prediction model using *Random Forest Regression* algorithm. It uses accuracy score and classification report as the metric for prediction.

## Steps

### Building Files
1) train_model.py: which has regression model code
2) requirements.txt: which has the required library names
3) heart disease.csv: .csv dataset which includes the data regarding counsumer forcast prediction
4) Dockerfile: which contains the commands to be run in docker

### Git & Other Commands used in Command Prompt
1) `mkdir <file_name>` to create the folder
2) `cd <file name>` to go inside the folder
3) `git init`, initializing folder as git repository
4) manually add all the files
5) `git add .` to add all the files into git track
6) `git commit -m "<message>"`, it commits whatever is there in the track
7) `git remote add origin <GitHub repository link>`, builds connection between git and github
8) `git push --set-upstream origin master`, sends all the files from git to github.


### Jenkins
1) created a new item with item name as **9. Counsumer forcast prediction**
2) selected *Freestyle project* as the item type
3) selected *Git* in **Source Code Management**
4) added *Execute Windows batch command* step in **Build Steps**
5) Saved the Configurations
6) Clicked build now


#### Output
  ![image](https://github.com/user-attachments/assets/d16be8a0-71bb-4c37-99a1-239d0fb0a6f3)


### Dockers
1) used `cd` to go forward and `cd..` to do backward, to get to the correct path in command prompt (i.e. the folder where all the files including docerfile is located.
2) executed the command `docker build -t <docker_image_name> .` to build the docker image.
3) executed the command `docker run <docker_image_name>` to run the docker image.


#### Output
  ##### Command Prompt
![image](https://github.com/user-attachments/assets/d11bc0d8-22f9-443f-a885-c9c9b8c1112d)


  
  ##### Docker Hub 
![image](https://github.com/user-attachments/assets/691bae14-71eb-43a1-958d-7a0ab64538ce)


