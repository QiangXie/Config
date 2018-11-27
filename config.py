#-*- coding: utf-8 -*-
import os
import subprocess
import shutil
import getpass

#htop
if not os.path.exists("/usr/bin/htop"):
    print("htop hasn't been installed, please install htop first.")
    exit(1)

#config git
print("Config git...")
if not os.path.exists("/usr/bin/git"):
    print("git hasn't been installed, please install git first.")
    exit(1)
subprocess.Popen("git config --global user.name \"QiangXie\"", shell=True)
subprocess.Popen("git config --global user.email \"happyxieqiang@qq.com\"", shell=True)
subprocess.Popen("git config --global alias.lg \"log --graph --pretty=format:\'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset\' --abbrev-commit --date=relative\"", shell=True)
subprocess.Popen("git config --global alias.ci commit", shell=True)
subprocess.Popen("git config --global alias.co checkout", shell=True)
subprocess.Popen("git config --global alias.st status", shell=True)
subprocess.Popen("git config --global alias.br branch", shell=True)
subprocess.Popen("git config --global alias.psm \"push origin master\"", shell=True)
subprocess.Popen("git config --global alias.plm \"pull origin master\"", shell=True)
subprocess.Popen("git config --global core.editor \"vim\"", shell=True)
subprocess.Popen("git config --global color.ui true", shell=True)
print("Config done.")

#config zsh
print("Config zsh...")
if not os.path.exists("/usr/bin/zsh"):
    print("zsh hasn't been installed, please install zsh first.")
    exit(1)
if not os.path.exists("~/.zshrc"):
    subprocess.call("cp ./.zshrc ~/", shell = True)

username = getpass.getuser()
shell_string = "cat /etc/passwd | grep " + username +" | awk -v FS=: '{print $7}'"
p = subprocess.Popen(shell_string, shell=True, stdout=subprocess.PIPE)
shell_type = p.stdout.readlines()[0].decode('utf-8').strip()
if not shell_type == "/bin/zsh":
    print("Change default shell to zsh, please input your password:")
    subprocess.call("chsh -s /bin/zsh", shell = True)
print("Config zsh done.")

#config tmux
print("Config tmux...")
if not os.path.exists("/usr/bin/tmux"):
    print("tmux hasn't been installed, please install tmux first.")
    exit(1)
if not os.path.exists("~/.tmux.conf"):
    subprocess.call("cp ./.tmux.conf ~/", shell = True)
print("Config tmux done.")

#config vim 
print("Config vim...")
subprocess.call("cp ./.vimrc ~/", shell = True)
if not os.path.exists("~/.vim/bundle/Vundle.vim"):
    subprocess.call("git clone https://github.com/VundleVim/Vundle.vim.git  ~/.vim/bundle/Vundle.vim", shell = True)
else:
    shutil.rmtree("~/.vim/bundle/Vundle.vim")
    subprocess.call("git clone https://github.com/VundleVim/Vundle.vim.git  ~/.vim/bundle/Vundle.vim", shell = True)
subprocess.call("vim +BundleInstall +qall", shell = True)
subprocess.call("python ~/.vim/bundle/YouCompleteMe/install.py", shell = True)
print("Config vim done." )
