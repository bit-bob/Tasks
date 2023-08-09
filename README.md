# Initial setup

1. Create virtual environment
   ```
   python3 -m venv env
   ```

   **_DO NOT run this again if you already have env, this causes this error later on. the fix was to fully delete the env and start again_**

   ```
   zsh: <path>/sarajevo/env/bin/pip: bad interpreter: /Users/helinaberhane/Documents/Projects/sarajevo/env/bin/python3: no such file or directory
   ```

2. Activate the environment

   ```
   source ./env/bin/activate
   ```

   **_this needs to be done before running pip so it doesn't install the dependencies on the system environment_**
