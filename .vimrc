" Comments in Vimscript start with a `"`.

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
colorscheme desert

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

" Enable mouse support. You should avoid relying on this too much, but it can
" sometimes be convenient.
set mouse+=a
set ballooneval
set balloonevalterm
"set clipboard=unnamedplus

set fileencodings=ucs-bom,utf-8,utf-16,gbk,big5,gb18030,latin1

" Run Programs
func! RunProgram()
    exec "w"
    if &filetype == 'c'
        exec '!gcc % -fopenmp -O2 -o %<.out'
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

iab cinit #include <bits/stdc++.h><CR>
         \using namespace std;<CR>
         \<CR>
         \int main() {<CR>
            \return 0;<CR>
         \}<CR>


call plug#begin('~/.vim/plugged')
Plug 'tpope/vim-surround'
Plug 'ervandew/supertab'
Plug 'preservim/nerdcommenter'
Plug 'preservim/nerdtree'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'oblitum/youcompleteme'
Plug 'w0rp/ale'
call plug#end()

map <C-n> :NERDTreeToggle<CR>

let g:ale_linters = {
        \   'python': ['pyls', 'flake8', 'mypy', 'pycodestyle'],
        \   'shell': ['shellcheck'],
        \}

let g:ale_set_balloons=1

"if executable('clangd')
    "augroup lsp_clangd
        "autocmd!
        "autocmd User lsp_setup call lsp#register_server({
                    "\ 'name': 'clangd',
                    "\ 'cmd': {server_info->['clangd']},
                    "\ 'whitelist': ['c', 'cpp', 'objc', 'objcpp'],
                    "\ })
        "autocmd FileType c setlocal omnifunc=lsp#complete
        "autocmd FileType cpp setlocal omnifunc=lsp#complete
        "autocmd FileType objc setlocal omnifunc=lsp#complete
        "autocmd FileType objcpp setlocal omnifunc=lsp#complete
    "augroup end
"endif

"if executable('pyls')
    "au User lsp_setup call lsp#register_server({
        "\ 'name': 'pyls',
        "\ 'cmd': {server_info->['pyls']},
        "\ 'whitelist': ['python'],
        "\ })
"endif

