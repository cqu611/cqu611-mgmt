# version 0.1.1
# editor: Ekira Welkea
# date: 2016/09/30
# update: 2017/10/19

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -lh --color=auto'
alias lla='ls -lah --color=auto'
export GPG_TTY=`tty`
export http_proxy='http://172.24.170.90:65523/'
export https_proxy='http://172.24.170.90:65523/'
export ftp_proxy='http://172.24.170.90:65523/'

function git_branch {
    branch="`git branch 2>/dev/null | grep "^\*" | sed -e "s/^\*\ //"`"
    if [ "${branch}" != "" ];then
        if [ "${branch}" = "(no branch)" ];then
            branch="(`git rev-parse --short HEAD`...)"
        fi
        echo "($branch)"
    fi
}

PS1='\e[1;35mxxiong\e[m\e[1;34m@CQU611\e[m\e[0;35m_\e[m\e[1;32m<\w>\e[m\e[0;31m$(git_branch)\e[m'
