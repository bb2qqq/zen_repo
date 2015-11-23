# I'd better use rsync instead of cp one day
cp ~/.bash_profile  ~/zen/zen_repo/tech_lab/config/OSX/bash_profile

# filter
grep -v "ssh" ~/.bashrc | grep -v "admin" > ~/tmp
cp ~/tmp ~/zen/zen_repo/tech_lab/config/OSX/bashrc
cp ~/.vimrc ~/zen/zen_repo/tech_lab/config/CrossPlatform/vimrc
cp ~/.vimrc ~/zen/zen_repo/tech_lab/config/OSX/vimrc
cp ~/local_vim_scripts.vim ~/zen/zen_repo/tech_lab/config/OSX/local_vim_scripts.vim
cp ~/.vim/plugin/* /Users/zen1/zen/zen_repo/tech_lab/vim_skill/my_plugin

# Universal code
cp /Users/zen1/zen/automation/General/new_system/general_gadget/* /Users/zen1/zen/zen_repo/tech_lab/my_work/zen_system/
