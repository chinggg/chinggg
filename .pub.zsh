# global env
export EDITOR=vim

# colorful less
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'
export LESSCHARSET=utf-8

alias ls="ls --color"
alias l="ls -lah"
alias o="xdg-open"
alias p="python"

alias dcbuild="docker-compose build"
alias dcup="docker-compose up"
alias dcdown="docker-compose down"
alias dps='docker ps --format "{{.ID}} {{.Names}}"'
alias dockps='docker ps --format "{{.ID}} {{.Names}}"'
docksh() { docker exec -it $1 bash; }
alias http="systemctl start httpd"

export _JAVA_OPTIONS="-Dsun.java2d.uiScale=1.5"
