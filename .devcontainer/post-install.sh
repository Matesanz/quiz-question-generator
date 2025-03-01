# Description: This script is run after the devcontainer is built.
# It installs the packages defined in pyproject.toml and the local package.

GREEN='\033[92m'
BLUE='\033[94m'
END='\033[0m'

# install packages defined in pyproject.toml and the local package
echo -e "${BLUE}🔧  Installing python dependencies using Poetry..${END}\n"
if [ ! -f "poetry.lock" ]; then
    echo -e "${BLUE}ℹ️  No poetry.lock file found, resolving dependencies, this may take a while, please wait..${END}\n"
fi
poetry install --all-groups --no-interaction --no-ansi --no-root
pip3 install -e . --no-deps 
echo -e "${GREEN}✅  Python dependencies installed!${END}\n"

# install pre-commit hooks
echo -e "${GREEN}✅  Project correctly configured!${END}\n"
echo -e "${BLUE}🔧  Installing pre-commit hooks...${END}\n"
pre-commit install
