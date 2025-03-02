# 🎓 Quiz Question Generator

A simple App that creates a set of questions for a specific learning objective. It uses LLMs in order to provide the set of questions.

## 🚀 Quick Start

```bash
# Build the Docker image
docker build -t quiz-question-generator .

# Run the Docker container
docker run -it --rm \
   -p 8000:8000 \
   -e OPENAI_API_KEY="your_openai_api_key" \
   quiz-question-generator
```

**🎉 You can now go to http://localhost:8000/docs** to try the API

> [!NOTE]
> You can find more configurable parameters in the [Parameters section](#parameters)

You can also use code to check the API

```python
import requests

url = "http://localhost:8000/generate-quiz"
payload = {
   "learning_objective": "Understand the basics of Python programming",
   "n_questions": 5
}
headers = {
   "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
quiz = response.json()
```


## ⚙️ Configuration

The application can be configured using a `.env` file or environment variables. Parameters set in the .env file will have preference over the ones set using env variables.

- [Set the configuration using a .env file](#using-env-file)
- [Set the configuration using env variables](#using-env-variables)

### Parameters

Alternatively, you can set the configuration options using environment variables:

| Variable         | Description                              | Default                        |
|------------------|------------------------------------------|--------------------------------|
| `OPENAI_API_KEY` | Your OpenAI API key                      |                                |
| `API_HOST`       | The host for the API                     | `0.0.0.0`                      |
| `API_PORT`       | The port for the API                     | `8000`                         |
| `API_DEBUG`      | Enable or disable debug mode             | `True`                         |
| `LLM_MODEL`      | The LLM model to use. This API uses [AISuite](https://github.com/andrewyng/aisuite) where models from multiple providers can be used, so this variable uses a `<provider>:<model>` format. Refer to that project for more info. | `openai:gpt-4o-mini-2024-07-18` |

### Using .env File

Create a `.env` file in the root directory with the following content:

```plaintext
# .env file
OPENAI_API_KEY="your_openai_api_key"
```

### Using env variables

You could also pass environment variables directly when running the Docker container or in your console session.

```bash
# in console
export OPENAI_API_KEY="your_openai_api_key"
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
