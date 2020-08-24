syntax enable
set tabstop=4
set shiftwidth=4
set expandtab
set number
filetype indent on
set autoindent

"python
augroup pythonbindings
    autocmd! pythonbindings
    autocmd Filetype python nnoremap <buffer> <localleader>cm 0i#<esc>
    autocmd Filetype python nnoremap <buffer> <localleader>nocm 0x
    autocmd Filetype python command Wr w | !python %

"    autocmd Filetype python nnoremap <buffer> mab %%<right>i
"    autocmd Filetype python nnoremap <buffer> mbb %i
augroup end


"java
augroup javabindings
    autocmd! javabindings
    autocmd Filetype java nnoremap <buffer> <localleader>cm 0i//<esc>
    autocmd Filetype java nnoremap <buffer> <localleader>nocm 0xx
    autocmd Filetype java command Wc w | !javac %


"    autocmd Filetype java inoremap <buffer> { {<enter>}<up><esc>A<enter>
"    autocmd Filetype java inoremap <buffer> {{ {
"    autocmd Filetype java inoreabbrev <buffer> psvm public static void main(String[] argv){<enter><enter>}<left><up><tab>
"    autocmd Filetype java nnoremap <buffer> dun :w<enter>:!javac %<enter>
augroup end

"javascript
augroup jsbindings
    autocmd! jsbindings
    autocmd Filetype javascript nnoremap <buffer> <localleader>cm 0i//<esc>
    autocmd Filetype javascript nnoremap <buffer> <localleader>nocm 0xx
    autocmd Filetype javascript command Wc w | !node %
augroup end

"html
augroup htmlbindings
    autocmd! htmlbindings
    "autocmd Filetype html inoreabbrev <buffer> html:5 
    autocmd Filetype html inoremap <buffer> > <esc>yiwea></<esc>pa><esc>b<left><left>i
    autocmd Filetype html inoremap <buffer> >> >
    autocmd Filetype html inoremap <buffer> <C-l> <enter><up><esc>o
augroup end


:map <C-n> :NERDTreeToggle<enter>
:inoremap jk <Esc>

" tab 
nnoremap th  :tabfirst<CR>
nnoremap tj  :tabnext<CR>
nnoremap tk  :tabprev<CR>
nnoremap tl  :tablast<CR>
nnoremap te  :tabedit<Space>
nnoremap tn  :tabnext<Space>
nnoremap tm  :tabm<Space>
nnoremap tq  :tabclose<CR>
""""""""""""""""""""""""""""""




call plug#begin()
"        Plug 'valloric/youcompleteme'       
        Plug 'scrooloose/nerdtree'
        Plug 'neoclide/coc.nvim', {'branch':'release'}
        Plug 'neoclide/coc.nvim', {'do':'yarn install --frozen-lockfile'}
        Plug 'jiangmiao/auto-pairs'
"        Plug 'ryanoasis/vim-devicons' 
call plug#end()

