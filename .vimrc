set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

"code comlpetion engine
Plugin 'Valloric/YouCompleteMe'
"a tree explorer plugin for vim
Plugin 'scrooloose/nerdtree'
Plugin 'Lokaltog/vim-powerline'
Plugin 'Yggdroot/indentLine'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"NERD tree
let NERDChristmasTree = 0
let NERDTreeWinSize = 35
let NERDTreeChDirMode = 2
let NERDTreeIgnore = ['\~$','\.pyc$','\.swp$']
let NERDTreeShowBookmarks = 1
let NERDTreeWinPos = "left"
"Automatically open a NERDTree if files where if no files where specified
autocmd vimenter * if !argc() | endif
"Close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
"open a NERDTree
nmap <F5> :NERDTreeToggle<cr>

"indent Line setting"
let g:indentLine_char = '|'
let g:indentLine_enabled = 1


let g:molokai_original = 1
set number
