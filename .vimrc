" vim
autocmd BufWritePost $MYVIMRC source $MYVIMRC
set nocompatible
set shortmess=F
set fileencodings=ucs-bom,utf-8,utf-16,gbk,big5,gb18030,latin1
set ttimeoutlen=100

" line
set number
set relativenumber
set ruler
set cursorline
set cursorcolumn

" space
set tabstop=4
set shiftwidth=3
set expandtab
set autoindent

" search
set hlsearch
set incsearch
set ignorecase
set smartcase
set showmatch
set wildmenu

" color
syntax on
filetype on
filetype plugin on
set background=dark
colorscheme desert

" mouse
set mouse+=a
set ballooneval
set balloonevalterm
"set clipboard=unnamedplus

" Run Programs
func! RunProgram()
    exec "w"
    if &filetype == 'c'
        exec '!gcc % -O2 -o %<.out'
        exec '!time ./%<.out'
    elseif &filetype == 'cpp'
        exec '!g++ % -O2 -o %<.out'
        exec '!time ./%<.out'
    elseif &filetype == 'go'
        exec '!time go run %'
    elseif &filetype == 'java'
        exec '!javac %'
        exec '!time java %<'
    elseif &filetype == 'javascript'
        exec '!time node %'
    elseif &filetype == 'typescript'
        exec '!time ts-node %'
    elseif &filetype == 'php'
        exec '!time php %'
    elseif &filetype == 'python'
        exec '!time python3 %'
    elseif &filetype == 'sh'
        :!time bash %
    endif
endfunc
noremap <F5> :call RunProgram()<CR>

" download vim-plug if missing
if empty(glob("~/.vim/autoload/plug.vim"))
  silent! execute '!curl --create-dirs -fsSLo ~/.vim/autoload/plug.vim https://raw.fastgit.org/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * silent! PlugInstall
endif

" declare plugins
silent! if plug#begin()
  if filereadable(expand("~/.vimrc.plugins"))
    source ~/.vimrc.plugins
  endif
  call plug#end()
endif

" The backspace key has slightly unintuitive behavior by default. For example,
" by default, you can't backspace before the insertion point set with 'i'.
" This configuration makes backspace behave more reasonably, in that you can
" backspace over anything.
set backspace=indent,eol,start

" By default, Vim doesn't let you hide a buffer (i.e. have a buffer that isn't
" shown in any window) that has unsaved changes. This is to prevent you from "
" forgetting about unsaved changes and then quitting e.g. via `:qa!`. We find
" hidden buffers helpful enough to disable this protection. See `:help hidden`
" for more information on this.
set hidden

" Unbind some useless/annoying default key bindings.
nmap Q <Nop> " 'Q' in normal mode enters Ex mode. You almost never want this.

" Disable audible bell because it's annoying.
set noerrorbells visualbell t_vb=

iab cinit #include <bits/stdc++.h><CR>
         \using namespace std;<CR>
         \<CR>
         \int main() {<CR>
            \return 0;<CR>
         \}<CR>

autocmd InsertLeave * :silent !fcitx5-remote -c
autocmd BufCreate *  :silent !fcitx5-remote -c
autocmd BufEnter *  :silent !fcitx5-remote -c
autocmd BufLeave *  :silent !fcitx5-remote -c
