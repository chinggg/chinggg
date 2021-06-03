#!/usr/bin/env python3
import os

softs = 'zsh curl wget vim git'

dic = {
    "vim-plug": "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
    "oh-my-zsh": "bash install_omz.sh",
    "nvm": "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash",
    "zsh-autosuggestions": "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
    ".vimrc": "cp ~/.vimrc ~/.vimrc.bak \ cp ../.vimrc ~",
    ".gitconfig": "cp ~/.gitconfig ~/.gitconfig.bak \ cp ../.gitconfig ~"
}

os.system('sudo apt install '+ softs)

for k, v in dic.items():
    print("Will install", k)
    os.system(v)
