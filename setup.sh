source ./resources/bash_colors.sh

echo -e "\n\n${CYAN}Welcome to Sagaxus.${NC}"
echo -e "${CYAN}Brought to you by @herereadthis.${NC}\n\n"

VENV_ACTIVATE="venv/bin/activate"

if command -v python3 &>/dev/null; then
    if [ -e $VENV_ACTIVATE ]
    then
        echo -e "${B_CYAN}Virtual environment exist.${NC}"
    else
        echo -e "${B_CYAN}Set up virtual environment.${NC}"
        python3 -m venv venv
    fi

    source $VENV_ACTIVATE
    echo -e "${B_CYAN}Virtual environment is now ./venv directory.${NC}"

    echo -e "\n\n${B_CYAN}Installing packages.${NC}"
    pip install -r requirements.txt
    echo -e "${B_CYAN}Packages installed.${NC}"

    # Download student data
    echo -e "\n\n${B_GREEN}Grab student data.${NC}"
    DESTINATION="demos/bayesian-linear-regression/temp"
    FILE="student.zip"
    URL="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"

    if [ -e "$DESTINATION/student.txt" ]
    then
        echo -e "\n\n${B_GREEN}Student data already exists.${NC}"
    else
        echo -e "\n\n${B_GREEN}Downloading student data.${NC}"
        wget $URL -P $DESTINATION
        unzip "$DESTINATION/$FILE" -d "demos/bayesian-linear-regression/temp"
        rm "$DESTINATION/$FILE"
    fi
    echo -e "\n\n${B_GREEN}Finished grabbing student data.${NC}"

    echo -e "\n\n${BG_GREEN}Ready to go!${NC}\n\n"
else
    echo -e "${B_RED}Please install Python3 before continuing.${NC}"
fi



