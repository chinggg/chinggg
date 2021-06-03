export HISTFILE=~/.zsh_history
export HISTSIZE=65535
export SAVEHIST=65535
setopt HIST_FIND_NO_DUPS
setopt INC_APPEND_HISTORY

[[ -f ~/.pub.zsh ]] && source ~/.pub.zsh
