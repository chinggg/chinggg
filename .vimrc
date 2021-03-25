" If you open this file in Vim, it'll be syntax highlighted for you.

set nocompatible
autocmd BufWritePost $MYVIMRC source $MYVIMRC
set shortmess+=I

set number
set relativenumber
set ruler
set cursorline
set cursorcolumn

set hlsearch
set wildmenu
set showmatch

syntax on
filetype on
let python_highlight_all = 1
set background=dark
colorscheme industry

set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
au BufNewFile,BufRead *.cu set ft=cu

" Always show the status line at the bottom, even if you only have one window open.
set laststatus=2

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

" This setting makes search case-insensitive when all characters in the string
" being searched are lowercase. However, the search becomes case-sensitive if
" it contains any capital letters. This makes searching more convenient.
set ignorecase
set smartcase

" Enable searching as you type, rather than waiting till you press enter.
set incsearch

" Unbind some useless/annoying default key bindings.
nmap Q <Nop> " 'Q' in normal mode enters Ex mode. You almost never want this.

" Disable audible bell because it's annoying.
set noerrorbells visualbell t_vb=

set mouse+=a

set fileencodings=ucs-bom,utf-8,utf-16,gbk,big5,gb18030,latin1
"set clipboard=unnamedplus

"" vim-plug section
"call plug#begin('~/.vim/plugged')
"" list plugins with Plug commands
"Plug 'tpope/vim-surround'
"Plug 'ervandew/supertab'
"Plug 'preservim/nerdcommenter'
"Plug 'preservim/nerdtree'
"Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
"call plug#end()

" NERDTree
map <C-n> :NERDTreeToggle<CR>

" Run Programs
noremap <F5> :call RunProgram()<CR>

func! RunProgram()
    exec "w"
    if &filetype == 'c'
        exec '!gcc % -fopenmp -O2 -o %<'
        exec '!time ./%<'
    elseif &filetype == 'cpp'
        exec '!g++ % -O2 -o %<'
        exec '!time ./%<'
    elseif &filetype == 'go'
        exec '!time go run %'
    elseif &filetype == 'java'
        exec '!javac %'
        exec '!time java %<'
    elseif &filetype == 'javascript'
        exec '!time node %'
    elseif &filetype == 'php'
        exec '!time php %'
    elseif &filetype == 'python'
        exec '!time python3 %'
    elseif &filetype == 'sh'
        :!time bash %
    endif
endfunc
