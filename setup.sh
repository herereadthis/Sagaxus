source ./resources/bash_colors.sh

echo -e "\n\n${CYAN}Welcome to Sagaxus.${NC}"
echo -e "${CYAN}Brought to you by @herereadthis.${NC}\n\n"

if command -v python3 &>/dev/null; then
    echo -e "${B_CYAN}Set up virtual environment.${NC}"
    python3 -m venv venv
    source venv/bin/activate
    echo -e "${B_CYAN}Virtual environment is now ./venv directory.${NC}"

    echo -e "\n\n${B_CYAN}Installing packages.${NC}"
    pip install -r requirements.txt
    echo -e "${B_CYAN}Packages installed.${NC}"
    echo -e "\n\n${BG_GREEN}Ready to go!${NC}\n\n"
else
    echo -e "${B_RED}Please install Python3 before continuing.${NC}"
fi



