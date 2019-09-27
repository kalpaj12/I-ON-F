#!/bin/bash

user=$(whoami)
Path="/home/$user"
FolderName="I-ON-F-kalpaj12"
FileName="do_not_delete.txt"

COLOR_GREEN='\033[0;32m'
NC='\033[0m'

# Make run.sh single run throughout system lifetime
if [ ! -e "$Path/$FolderName/$FileName" ]; then

    mkdir "$Path/$FolderName"
    touch "$Path/$FolderName/$FileName"

    cp -R . "$Path/$FolderName"

    # Save init date
    currentDate=`date`
    echo $currentDate >> "$Path/$FolderName/$FileName"


    cd "$Path/$FolderName"

    # install python requirements
    pip install delegator.py


    # make python file executable, to add to crontab
    chmod +x main.py

    # (crontab -l ; echo "*/5 * * * * $Path/$FolderName/main.py") | crontab -

    echo "${COLOR_GREEN}Prelim Init successful${NC}"

    # init for testing purposes
    ./main.py

else
    echo Instance already installed on
    cat $Path/$FolderName/$FileName

    echo Updating repo
    cd "$Path/$FolderName"
    git pull origin master

fi