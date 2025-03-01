# 🎓 Quiz Question Generator

A simple App that creates a set of questions for a specific learning objective. It uses LLMs in order to provide the set of questions.

## 🚀 Quick Start

To start this project simply run:

```bash
# Build the Docker image
docker build -t quiz-question-generator .

# Run the Docker container
docker run -it --rm -p 8000:8000 quiz-question-generator
```

## 🏗️ Development

### 🐋 Devcontainer Environment

The fastest way to quickly start developing is to build a **development environment** up an ready **[using Docker and vscode](https://code.visualstudio.com/docs/remote/containers)**:

![devcontainer_gif](https://microsoft.github.io/vscode-remote-release/images/remote-containers-readme.gif)

1. Install [remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in **VSCode**.
   1. Press `Ctrl+P`
   2. Paste `ext install ms-vscode-remote.remote-containers`
   3. Press `Enter`

2. VSCode automatically searches for the `.devcontainer/devcontainer.json` file in the root folder. So and Run the **docker** in development in **VSCode** *(wait, first time takes some time to run)*.

   ```console
   F1 > Rebuild and reopen in container
   ```

👍 After the docker has successfully built it will add all the [pre-commit hooks](.pre-commit-config.yaml) along all the tools correctly configured for a correct development: black, isort, pylint, pytest...

### 🧑‍⚖️ Pre-Commit

In order to **keep code and commits quality** we enforce the use of pre-commit by doing:

```console
pre-commit install
```

This will install a bunch of hooks that will check staged files (only the `*.py` staged files) to check that they stick to black, autopep8, isort and some other standards.