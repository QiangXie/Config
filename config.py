#-*- coding: utf-8 -*-
import os
import subprocess
import shutil
import getpass

#get user name
username = getpass.getuser()

#htop
print("Check htop...")
if not os.path.exists("/usr/bin/htop"):
    print("htop hasn't been installed, please install htop first.")
    exit(1)
print("Done.")

print("Check git...")
if not os.path.exists("/usr/bin/git"):
    print("git hasn't been installed, please install git first.")
    exit(1)
print("Done.")

print("Check zsh...")
if not os.path.exists("/usr/bin/zsh"):
    print("zsh hasn't been installed, please install zsh first.")
    exit(1)
print("Done.")

print("Check tmux...")
if not os.path.exists("/usr/bin/tmux"):
    print("tmux hasn't been installed, please install tmux first.")
    exit(1)
print("Done.")

#config git
print("Config git...")
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
if not os.path.exists("/home/{}/.zshrc".format(username)):
    subprocess.call("cp ./.zshrc /home/{}/".format(username), shell = True)

shell_string = "cat /etc/passwd | grep \"^" + username +"\\>\" | awk -v FS=: '{print $7}'"
p = subprocess.Popen(shell_string, shell=True, stdout=subprocess.PIPE)
shell_type = p.stdout.readlines()[0].decode('utf-8').strip()
if not shell_type == "/bin/zsh":
    print("Default shell is {}, change default shell to zsh, please input your password:".format(shell_type))
    subprocess.call("chsh -s /bin/zsh", shell = True)
print("Config zsh done.")

#config tmux
print("Config tmux...")
if not os.path.exists("/home/{}/tmux.conf".format(username)):
    subprocess.call("cp ./.tmux.conf /home/{}/".format(username), shell = True)
print("Config tmux done.")

#config vim 
print("Config vim...")
subprocess.call("cp ./.vimrc /home/{}/".format(username), shell = True)
if not os.path.exists("/home/{}/.vim/bundle/Vundle.vim".format(username)):
    subprocess.call("git clone https://github.com/VundleVim/Vundle.vim.git  /home/{}/.vim/bundle/Vundle.vim".format(username),
            shell = True)
else:
    shutil.rmtree("/home/{}/.vim/bundle/Vundle.vim".format(username))
    subprocess.call("git clone https://github.com/VundleVim/Vundle.vim.git  /home/{}/.vim/bundle/Vundle.vim".format(username), 
            shell = True)
subprocess.call("vim +BundleInstall +qall", shell = True)
subprocess.call("python /home/{}/.vim/bundle/YouCompleteMe/install.py".format(username), shell = True)
if not os.path.exists("/home/{}/.vim/colors".format(username)):
    os.mkdir("/home/{}/.vim/colors".format(username))
subprocess.call("cp /home/{}/.vim/bundle/vim-colors-solarized/colors/solarized.vim /home/{}/.vim/colors/".format(username, username), shell=True)
subprocess.call("cp /home/{}/.vim/bundle/molokai/colors/molokai.vim /home/{}/.vim/colors/".format(username, username), shell=True)
print("Config vim done." )
