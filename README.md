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
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
     Add Homebrew to your PATH and to your bash shell profile script, either ~/.profile on Debian/Ubuntu or ~/.bash_profile on CentOS/Fedora/Red Hat.
    ```sh
    $ test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
    $ test -d /home/linuxbrew/.linuxbrew && eval$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
    $ test -r ~/.bash_profile &&echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~/.bash_profile
    $ echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~/.profile
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
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

    #### Installing pyenv
    Install pyenv binary-
    ```sh
    $ brew update
    $ brew install pyenv
    ```
    Enable pyenv in your profile-
    ```sh
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zprofile
    ```
    1. The first line sets an environment variable (PYENV_ROOT) that points to the pyenv directory.
    2. The second line puts pyenv first in your search path so that the OS will find pyenv’s Python(s) before any other Pythons.
    3. The last line initializes pyenv each time you open a terminal.

        After All these steps close the terminal and reopen it for the changes to take effect.

    ### Windows Installation-
    #### pyenv installation- 
    1. Download pyenv-win project from github
    ```sh
    git clone https://github.com/pyenv-win/ pyenv-win.git $HOME/.pyenv
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

    ### After successfull installation of pyenv and python clone the repository into your local machine.
    




















    


