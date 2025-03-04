# 🎓 Quiz Question Generator

A simple App that creates a set of questions for a specific learning objective. It uses LLMs in order to provide the set of questions.

> [!TIP]
> * 🎉 **Try out the UI [here](https://quiz-question-generator-front-418010332670.us-central1.run.app/)!** 👈
> 
> * 🎉 **Or check the API docs [here](https://quiz-question-generator-418010332670.us-central1.run.app/docs#)!** 👈

![assets](assets/quiz-generator-demo.mp4)

## 🔎 Table of contents

- [🎓 Quiz Question Generator](#-quiz-question-generator)
  - [🔎 Table of contents](#-table-of-contents)
  - [🚀 Quick Start](#-quick-start)
  - [📝 How to use the API](#-how-to-use-the-api)
  - [☁️ How to deploy to the cloud](#️-how-to-deploy-to-the-cloud)
    - [Option 1: Using Google Cloud Run](#option-1-using-google-cloud-run)
    - [Option 2: Using Azure Container Instances](#option-2-using-azure-container-instances)
    - [Option 3: Using AWS Elastic Container Service (ECS)](#option-3-using-aws-elastic-container-service-ecs)
  - [⚙️ Configuration](#️-configuration)
    - [Parameters](#parameters)
    - [Using .env File](#using-env-file)
    - [Using env variables](#using-env-variables)
  - [🏗️ Development](#️-development)
    - [🐋 Devcontainer Environment](#-devcontainer-environment)
    - [🧑‍⚖️ Pre-Commit](#️-pre-commit)
  - [🔙 Project Retrospective](#-project-retrospective)
  - [🌟 Next Steps](#-next-steps)

## 🚀 Quick Start

1. First, **clone** the repository:

```bash
git clone https://github.com/Matesanz/quiz-question-generator.git
cd quiz-question-generator
```

2. Then **add** the `OPENAI_API_KEY` in a **`.env` file** in the root folder.

```plaintext
# .env file
OPENAI_API_KEY="sk-proj-123"
```

3. Then use **docker compose** to launch the front and back services

```bash
docker compose up
```

4. **🎉 Enjoy!**
- **👉 You can now go to http://localhost:8000/docs** to try the API
- **👉 You can now go to http://localhost:8501/** to try the streamlit quiz generator

> [!NOTE]
> You can find more configurable parameters in the [Parameters section](#parameters)

## 📝 How to use the API

You can use the API through python:

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

## ☁️ How to deploy to the cloud

Deploy the API to the cloud using:

- [Google Cloud Run](#option-1-using-google-cloud-run)
- [Azure Container Instances](#option-2-using-azure-container-instances)
- [AWS Elastic Container Service](#option-3-using-aws-elastic-container-service-ecs)

### Option 1: Using Google Cloud Run

1. Authenticate with Google Cloud:

   ```bash
   gcloud auth configure-docker
   ```

2. Deploy the image to Google Cloud Run, ensuring it listens on port 8080 and includes the `OPENAI_API_KEY`:
   ```bash
   gcloud run deploy quiz-question-generator \
      --image=matesanz/quiz-question-generator:latest \
      --platform=managed \
      --region=us-central1 \
      --allow-unauthenticated \
      --port=8000 \
      --set-env-vars OPENAI_API_KEY=<your-api-key>
   ```

### Option 2: Using Azure Container Instances

1. Login to Azure:

   ```bash
   az login
   ```

2. Deploy the container, ensuring the `OPENAI_API_KEY` environment variable is set:

   ```bash
   az container create --resource-group myResourceGroup \
      --name quiz-question-generator \
      --image matesanz/quiz-question-generator:latest \
      --dns-name-label quiz-generator \
      --ports 8000 \
      --environment-variables OPENAI_API_KEY=<your-api-key>
   ```

### Option 3: Using AWS Elastic Container Service (ECS)

1. Create an Elastic Container Repository (ECR) and push the image:
    ```bash
    aws ecr create-repository --repository-name quiz-question-generator
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
    docker tag matesanz/quiz-question-generator:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/quiz-question-generator:latest
    docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/quiz-question-generator:latest
    ```

2. Deploy the image using AWS ECS Fargate or EC2 with a task definition, ensuring the `OPENAI_API_KEY` environment variable is set.

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

## 🔙 Project Retrospective

Before diving into the specific tasks, it is important to outline the structured approach we took to ensure a well-organized and efficient development process. Each step was designed to build upon the previous one, ensuring seamless integration and optimal performance.

1. **Repository Setup**: We initialized a new repository to manage the project efficiently.
2. **Basic File Structure**: Essential files such as `README.md`, `pyproject.toml`, and `.gitignore` were included to ensure a well-documented and organized codebase.
3. **CI/CD Principles**: We implemented the foundational elements of CI/CD using GitHub Actions to manage API releases.
4. **Dockerization**: The solution was containerized to enhance portability and ease of deployment.
5. **Business Logic Development**: We validated the connection with the LLM and ensured proper quiz generation functionality.
6. **API Development**: The business logic was encapsulated within an API to allow structured access and interaction.
7. **CI/CD Pipelines for Testing and Linting**: Additional pipelines were integrated to enforce code quality through automated testing and linting.
8. **Basic UI with Streamlit**: A simple interface was built using Streamlit to enhance usability.
9. **Docker Image Deployment**: The process for building and pushing a Docker image to Docker Hub was implemented to facilitate cloud deployment.
10. **Continuous Documentation and Testing**: Throughout all phases of the project, thorough documentation and test coverage were maintained to ensure clarity and reliability.

The easiest/most difficult parts of the project:

- **Easiest (or Most Enjoyable) Part**: The development of the API was relatively straightforward and enjoyable once the business logic was fully implemented. Having a well-defined structure allowed for a smooth encapsulation of the core functionalities.
- **Hardest (or Most Tedious) Part**: The configuration of CI/CD pipelines was the most challenging aspect. The feedback loop for error correction in CI/CD is inherently slow, making debugging and refinement a time-consuming process.

## 🌟 Next Steps

One of the most important parts regarding the next steps is to **guarantee the quality and scientific correctness of the questions generated**. We could tackle this problem in two ways:

1. First step would be to evaluate the LLM model on the provided objective, it would require to create a dataset to measure the affinity of the model to the expected results. This would be possible using tools like [llm-eval](https://github.com/EleutherAI/lm-evaluation-harness) (the tool behing [open-llm-leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/)).

2. The Second step would require adding traceability to the outcomes of the model. A well known tool to do so is [MLFlow, that allows different options to enable tracing of the GenAI applications](https://mlflow.org/docs/latest/llms/tracing/index.html).
