#!/bin/sh


#Giving the bash script execute privileges for our Python script, this is necessary for the script to run the file
chmod +x SHIsing.py

#Informing the user that the Python script will run now
echo 'The Ising Model will now run'

#This executes the Python script, in which the variables are already defined
python ./SHIsing.py


#Informing the user the script has finished, and where outputs can be found
echo 'Complete'
echo 'Outputted data can be found in the data.txt file'