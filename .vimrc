syntax on "grammar highlighting
set number "display the number of lines
set autoindent "automatic indentation
set cindent "c indent
set tabstop=4 
set backspace=indent,eol,start

"bracket automatic completion
:inoremap ( ()<ESC>i
:inoremap ) <c-r>=ClosePair(')')<CR>
:inoremap { {}<ESC>i
:inoremap } <c-r>=ClosePair('}')<CR>
:inoremap [ []<ESC>i
:inoremap ] <c-r>=ClosePair(']')<CR>
:inoremap " ""<ESC>i
:inoremap ' ''<ESC>i
function! ClosePair(char)
	if getline('.')[col('.') - 1] == a:char
		return "\<Right>"
	else
		return a:char
	endif
endfunction

"file type detection plugin indent on
filetype plugin indent on 

set completeopt=longest,menu

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
Plugin 'tpope/vim-surround'
Plugin 'scrooloose/nerdtree'
"Plugin 'Lokaltog/vim-powerline'
Plugin 'Yggdroot/indentLine'
Plugin 'luochen1990/rainbow'
Plugin 'altercation/vim-colors-solarized'
Plugin 'tomasr/molokai'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

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

"NERD tree setting
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
nmap <F4> :NERDTreeToggle<cr>

"indent Line setting
let g:indentLine_char = '|'
let g:indentLine_enabled = 1
let g:rainbow_active = 1


"Quickly Run py file
map <F5> :call ComileRunGcc()<CR>

func! ComileRunGcc()
	exec "w"
	if &filetype == "c"
		exec "!g++ % -o %<"
		exec "!time ./%<"
	elseif &filetype == 'cpp'
		exec "!g++ % -o %<"
		exec "!time ./%<"
	elseif &filetype == 'python'
		exec "!time python %"
	endif
endfunc

"color scheme setting
if has('gui_running')
		set background=light
else
		set background=dark
endif

"use solarized
set t_Co=256
syntax enable
colorscheme solarized
let g:solarized_termcolors=256

"use molokai
"colorscheme molokai
"let g:molokai_original = 1
"let g:rehash256 = 1

highlight Normal ctermbg=NONE
highlight nonText ctermbg=NONE
highlight LineNr ctermfg=grey ctermbg=None
