
# IBM Generative AI Development Guide

<!-- vscode-markdown-toc -->
* [Setup the Development Environment](#SetuptheDevelopmentEnvironment)
	* [Pre-requisites](#Pre-requisites)
		* [Using Venv](#UsingVenv)
	* [Clone repo and checkout dev branch](#Clonerepoandcheckoutdevbranch)
	* [Install requirements](#Installrequirements)
	* [Setup your IBM Gen AI token](#SetupyourGenAItoken)
* [Make Changes](#MakeChanges)
* [Commit Changes and Make a Pull Request](#CommitChangesandMakeaPullRequest)
* [Logging](#Logging)
	* [Enabling Logs](#EnablingLogs)
* [Deployment Process](#DeploymentProcess)
	* [Automated Release Process](#AutomatedReleaseProcess)
	* [Manual Release Process](#ManualProcess)


<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='SetuptheDevelopmentEnvironment'></a>Setup the Development Environment

### <a name='Pre-requisites'></a>Pre-requisites

- Python version >= 3.9.
- Setup a virtual environment (using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)) and activate it.
- You need to **activate this environment every time** before you want to make changes to this repository.

#### <a name='UsingVenv'></a>Using Venv
```bash
python -m venv .venv # Create your Virtual environment
source .venv/bin/activate # Activate and use your virtual environment


# And once you're all done..
deactivate
```


### <a name='Clonerepoandcheckoutdevbranch'></a>Clone repo and checkout dev branch

```bash
git clone <repository-link>
git checkout dev
```

### <a name='Installrequirements'></a>Install requirements

Minimal pip version is 22.0.1. Check your pip version with `pip --version` and if needed run the following command to upgrade pip.
```bash
pip install --upgrade "pip>=22.0.1"
```
Following should install regular package dependencies as well as the dependencies required for development.
```bash
pip install -e ".[dev]"
```
Install pre-commit setup
```bash
pre-commit install
```

### <a name='SetupyourIBMGenAItoken'></a>Setup your IBM Generative AI token
Login to [workbench.res.ibm.com/](https://workbench.res.ibm.com/) and get your IBM Generative AI API key. Then, create a `genai/.env` and assign the `GENAI_KEY` value as:
```
GENAI_KEY=<your key here>
```

Once done, you and genai can use your key using `os.getenv("GENAI_KEY")` and you will not
have to worry about committing it to GitHub.

## <a name='MakeChanges'></a>Make Changes
Create a branch for making changes
```bash
git checkout -b <my_awesome_branch>
```
Make your changes and add any unit tests. Run tests as
```bash
python -m pytest
```

## <a name='CommitChangesandMakeaPullRequest'></a>Commit Changes and Make a Pull Request
Once you are done making changes, run `flake8` for linting and try fixing for as many messages as possible.
```bash
flake8 .
```
**Add only specific files to your commit** instead of doing something like `git commit -am`. This is recommended so as not to push unwanted files to the repo.
```bash
git add src/xyz.py tests/test_xyz.py
```
Commit your changes. If your code is not well-formatted then our scripts will format it for you. In that case, you may need to add the files again and commit.
```bash
git commit -m <my_commit_message>  ## *NOTE* black should auto-format through hooks.
```
Push your changes
```bash
git push origin HEAD
```
Raise a pull request from your `<my_awesome_branch>` containing changes to `dev` branch by going to github page of the repo.
- Add a description for your PR.
- Link any issues.
- Wait for tests to pass. If they fail then try to fix issues. Get in touch with the core team if needed. They will get back to you for anything that needs to be addressed.

## <a name='Logging'></a>Logging

GenAI uses the standard python logging module for logging debug messages within the module. Unless the consuming application explicitly enables logging, no logging messags from GenAI should appear in stdout or stderr e.g. no `print` statements, we should also always log to the `genai` namespace so that logs are easily identifiable.

The python standard logging module is documented [here](https://docs.python.org/3/library/logging.html).

Below is an example template file showing how logging can be added to a GenAI class.

```python
# Import the logging module
import logging

# Configure the logger to be named genai.xxx (where xxx is the current file or class)
logger = logging.getLogger(__name__)

logger.debug("This is some debug.")
logger.info("This is some info.")
logger.warning("This is a warning.")
logger.error("This is an error.")
logger.critical("This is a critial message.")
```
