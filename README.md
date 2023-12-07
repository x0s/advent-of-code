# Advent-of-code

[![](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![](https://github.com/x0s/advent-of-code/actions/workflows/action_cov.yml/badge.svg)]()
[![](https://coveralls.io/repos/github/x0s/advent-of-code/badge.svg?branch=main)](https://coveralls.io/github/x0s/advent-of-code?branch=main)
[![](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Here is a project where you can find the python scripts I imagined to solve the [advent-of-code](https://adventofcode.com/) games. Feel free to open an [Issue](https://github.com/x0s/advent-of-code/issues) if you want to discuss the algorithms or ask for help. Have fun!

## Install guidance
### 1. First, create virtual environment
We use mamba because it enables us to use python 3.11 as of november 2022 and it is a very powerful dependency solver. If you already use conda, please see [Troubleshooting](#troubleshooting)
```
$ mamba create --name advent python=3.11
$ mamba activate advent
```

### 2. Clone and Install package
```
(advent)$ git clone git@github.com:x0s/advent-of-code.git
(advent)$ make install
```
If you want to contribute and/or see your changes reflected, you may prefer to install in editable mode with `make install EDIT=1`

### 3. Set token to be able to retrieve your game inputs
[Here](https://github.com/wimglenn/advent-of-code-wim/issues/1) is a nice explanation how to get the token. Then, generate the config file, replacing `<YOUR_TOKEN>`:

```
(advent)$ make config TOKEN=<YOUR_TOKEN>
Token saved in advent_of_code/config.toml
```

This file is ignored by git, preventing to push your personal token online ;)

### 3.Optional. Build Docker image and run commands
From this moment, you can build the docker image and forward any `make` commands to the container 
replacing `make` by `make_in_container`

```
(advent) make build
(advent) make_in_container help
```

### 4. Launch a game
There are games in two parts every day of the advent for a given year.
For instance, the following command will launch part 1 of the game issued the 13th, December 2022:
```
(advent)$ make game WHEN=2022/13-1
```
To run it inside the container:
```
(advent)$ make_in_container game WHEN=2022/13-1
```

For now, the available games are:

- 2023: days=[01, 02, 03]
- 2022: days=[01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16-1, 17, 18, 19, 20, 21, 22-1(wip)]
- 2021: days=[01, 02]


### 5. Launch the tests
Launch the test and choose if you want the details of the test suite
```
(advent)$ make test
(advent)$ make test VERBOSE=1
```
or testing only one day (in verbose mode)
```
(advent)$ make test_this DAY=2022/02
```

In case of doubt `make help` will cover you.

## Troubleshooting
### Mamba asking you to `mamba init`
If you already have conda environments, mamba may ask you to `mamba init` in order to take over the conda `base` env.
If you do so, we will have to set it back. Nothing will be lost.

- Check the environments you have (for ie):
```
(base)$ conda info --envs
base                  *  /home/user_name/anaconda3
test-env                 /home/user_name/anaconda3/envs/test-env
```
- Then we init mamba (the conda envs are no longer reachable by their name)
```
  (base)$ mamba init
  (base)$ mamba create --name advent python=3.11
  (base)$ mamba activate advent
(advent)$ conda info --envs
                         /home/user_name/anaconda3
                         /home/user_name/anaconda3/envs/test-env
base                     /home/user_name/mambaforge
advent                *  /home/user_name/mambaforge/envs/advent
```
- Let's rehabiliate the conda envs:
```
(advent)$ conda config --append envs_dirs /home/user_name/anaconda3/envs/
base                     /home/user_name/anaconda3
test-env                 /home/user_name/anaconda3/envs/test-env
base                     /home/user_name/mambaforge
advent                *  /home/user_name/mambaforge/envs/advent
```
Now the problem is solved and you can activate/deactivate any of the mamba/conda envs like this:
```
  (base)$ conda activate advent
(advent)$ conda deactivate
  (base)$
  ```