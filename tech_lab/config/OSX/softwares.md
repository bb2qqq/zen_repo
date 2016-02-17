# Other Bash tools
`jq`: A JSON doc file Query tool

# Install Seil(Key Swap/Mapping)
[Discussion](http://stackoverflow.com/questions/127591/using-caps-lock-as-esc-in-mac-os-x)

# Install Karabiner(Key and Mouse Manipulation)
[Discussion on stackoverflow](http://apple.stackexchange.com/questions/132564/how-can-i-remap-caps-lock-to-both-escape-and-control)  
[Download Link](https://pqrs.org/osx/karabiner/)  
> By using this, you can map `Caps` to both `Esc` and `control`.  
> Note the possible conflict with other key-map softwares, such as `Seil`.

# Install Python Modules
* [matplotlib](http://matplotlib.org/downloads.html)
* nltk

# Install Python Tools
* pylint (代码检查简直太好用）

# Install ipython3
Install ipython3 on OSX is a bit tricky.  
Theoratically we just need use `pip3 install ipython[all]`, then you can use `ipython3` to use ipython.  
But it didn't work on my OSX. So we need to install anaconda first.  
Anarconda is a set of integrated packages. This is the [download link](https://www.continuum.io/downloads)  
After installed anarconda with `bash Anaconda3-2.4.1-MacOSX-x86_64.sh`, you may need to set something in your bashrc to trigger anaconda, like  
`alias conda="~/miniconda2/bin/conda"`  
Then, use `conda create -n py3k python=3 ipython` to install an ipython3 in conda path.  
Put this alias in your .bashrc then you can use ipython3!  
`alias ipython3="source ~/miniconda2/bin/activate py3k; ipython; source ~/miniconda2/bin/deactivate;"`



# Install macdown(A updated version of Mou)
    http://macdown.uranusjr.com/

# Intall licecap(capturing screen)
    http://www.cockos.com/licecap/
> Quicktime can record screen too, it will generate files with better quality but much bigger size.

# Install MPlayerX as an alternative of QuickTime
    http://mplayerx.org/download.html#sthash.G87N4t4Y.AplIDo4Z.dpbs
    # To change MPlayerX as default player, do this:
    Get the menu of a file -> Get Info -> Open with -> Choose app, change all

# Install Picture Documentation tool
    https://www.yinxiang.com/skitch/

# Install Mou
    http://25.io/mou

# Install ulysses-iii
    search "ulysses" in your bookmark manager

# Install Calibre to convert epub
    http://www.calibre-ebook.com/download_osxf

# Install Xmind on OS X
    http://www.xmind.net/download/mac/

# Install and config Adobe Reader
    install abode reader:
        http://get.adobe.com/reader/

    color set:
        Preferences -> Accessibility -> Document Colors Options -> Replace Document Colors -> ( Background: light-grey, Font: deep dark brown, like black )

    enable scrolling:
        View -> Page Display -> Enable Scrolling

    memorize last view page:
        Preferences -> Documents  -> Restore last view setting when reopening documents √

# Install kindle previewer
    http://www.appinn.com/kindle-previewer/

# Adobe Reader Color Config
    BackGround: Mercury, Front: blue-116 red-0 green-0
    Front font color: R-104, G-208, B-245

# Build git-sites with gitlab
    https://about.gitlab.com/downloads/
