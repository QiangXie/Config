import os
import subprocess

#config zsh
print "Config zsh..."
subprocess.call("cp ./.zshrc ~/", shell = True)
print "Please input your password."
subprocess.call("chsh -s /bin/zsh", shell = True)
print "Config zsh done."

#config tmux
print "Config tmux..."
subprocess.call("cp ./.tmux.conf ~/", shell = True)
print "Config tmux done."

#config vim 
print "Config vim..."
subprocess.call("cp ./.vimrc ~/", shell = True)
subprocess.call("git clone https://github.com/gmarik/vundle.git  ~/.vim/bundle/Vundle.vim", shell = True)
subprocess.call("vim +BundleInstall +qall", shell = True)
subprocess.call("cd ~/.vim/bundle/YouCompleteMe & python install.py", shell = True)
print "Config vim done." 
