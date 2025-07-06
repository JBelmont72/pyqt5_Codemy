

## 🏁used UV
* uv pip list | grep PyQt5

python -c "import PyQt5.QtWidgets; import PyQt5.QtGui; print('PyQt5 imports successful')"

uv pip install --force-reinstall pyqt5


uv init to rev it all up ( first i rm -rf the old .git that came with)
uv add for adding packages

## Cloned from author:
* [John ELder](https://github.com/flatplanet/pyqt5_youtube_playlist)

import sys
print(sys.executable) to confirm we are in a virtual environment

## to run a file
* use:    uv run filename/path
## if we accidentally delete .venv
* no problem, all our info and dependencies are in the uv.lock and pyroproject.toml and the .venv will be reconstituted
with a simple:   uv run filename

## uv sync
*. will recreate the virtual enviroment using the uv.lock

## to migrate project 
 use  uv init
 to add packages from the 
 uv add -r requirements.txt. afterthat you are not using the requirements.txt

 ## pipX 
 to install rust across the system
 uv tool install ruff (for example)
 can check ' which ruff' and 'ruf check
  uv tool uninstall ruff   to remove

  uv tool run ruff check to run once but not installed in the whole system

  uvx ruff check is a shortcut

  uv tool list to get a list of all tools

  uv help

## install uv with brew install uv
# ArjanCodes. for the info below
## uv tree to see the dependencies

## uv python list
* shows versions of python on the computer

## uv python intall.  3.12.0

uv venv --python 3.13.0     this sets the virtual envirinment version to whatever desired






## References
Corey Schafer
ArjanCodes. 'UV for Python ...(Almost) all batteries included)

## .gitignore 
* Ignore everything in any directory named temp
Example
# ignore ALL .log files
*.log

# ignore ALL files in ANY directory named temp
temp/

Below is my .gitignore I use in my ‘practiceOPENCV’ folder which I will add to git hub

*.venv
.DS_Store
*.mov
*.avi
*.csv
.venv
*.mp4
*.mpeg
.DS_Store
*.DS_Store
**.DS_Store

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
.pytest_cache



*.log
temp/
*.venv
.DS_Store
*.mov
*.avi
*.csv
.venv
*.venv
**.venv
*.mp4
*.mpeg
.DS_Store
*.DS_Store
**.DS_Store
dlib
*dlib


# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
.pytest_cache

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# dotenv
.env

# virtualenv
.venv/
venv/
ENV/

# Spyder project settings
.spyderproject

# Rope project settings
.ropeproject

# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio and Webstorm
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff:
.idea/guizero.iml
.idea/misc.xml
.idea/modules.xml
.idea/vcs.xml
.idea/workspace.xml
.idea/tasks.xml

# Sensitive or high-churn files:
.idea/dataSources/
.idea/dataSources.ids
.idea/dataSources.xml
.idea/dataSources.local.xml
.idea/sqlDataSources.xml
.idea/dynamic.xml
.idea/uiDesigner.xml

# Gradle:
.idea/gradle.xml
.idea/libraries

# Mongo Explorer plugin:
.idea/mongoSettings.xml

## File-based project format:
*.iws

## Plugin-specific files:

# IntelliJ
/out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor detritus
*.vim
*.swp
tags
.vscode
.idea

# MKDocs build
site/

*.pyc

**/.idea
*~
*.swp
*.o
*.so
*.pyc
build
build2
dist
*.egg-info/
docs/release/
docs/docs/web/
docs/docs/chm/
docs/docs/cache/
docs/docs/git-logs.xml
docs/docs/python/classes.txt
docs/docs/python/functions.txt
docs/docs/python/constants.txt
**/.vscode
**/vent







