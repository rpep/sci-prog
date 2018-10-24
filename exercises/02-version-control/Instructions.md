# Git Tutorial

1) Open your terminal, or Git Bash.

2) Set your name and username with Git. This labels things you do and associates them with you!

```bash
  git config --global user.name "Ryan Pepper"
  git config --global user.email "ryan.pepper@soton.ac.uk"
```

3) Set your favourite text editor by running the appropriate command below:

```
# Atom   
git config --global core.editor "atom --wait"

# nano
git config --global core.editor "nano -w"

# Sublime Text (Mac) 
git config --global core.editor "/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl -n -w"

# Sublime Text (Win, 64-bit install)
git config --global core.editor "'c:/program files/sublime text 3/sublime_text.exe' -w"

# Notepad++ (Win, 64-bit install)	
git config --global core.editor "'c:/program files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

# Emacs
git config --global core.editor "emacs"

# Vim
git config --global core.editor "vim"
```

4) We're going to create a folder. 

> cd ~
> mkdir project
> cd project

5) Now, we make the folder a git repository

> git init

6) "ls" shows the directories contents. "ls -a" - the "-a" flag means that we see hidden files, shows us that a new folder called ".git" has been created.

7) We can run

> git status

to show that everything has worked correctly. You should see something like:

```
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```

8) Let's create a file; open the text editor you chose earlier, and save a file called "workshop.txt" in the directory you're in.

Write something in the file:

```
I'm learning how to use Version Control in Oxford!
```

and save it.

9) Now, let's try running 'git status' again. What you should see is that now, changes you've made show up.

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  workshop.txt

nothing added to commit but untracked files present (use "git add" to track)
```

An untracked file is just a file that we haven't told Git to watch in any way.
To track a file, we use the command:

> git add workshop.txt

Doing "git status" again:

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

  new file:   workshop.txt
```

10) Now, we're going to 'commit' our changes - basically, take a snapshot of them at this particular time.

You have two options

i) Run the command

> git commit

This will bring up the text editor you chose earlier. Type a message about the changes you have made so that the file looks something like this:

```
Added text to workshop.txt
```

Now save the file.

ii) Alternatively, skip opening the text editor with:

git commit -m "Added text to workshop.txt"

11) Now make some more changes - add another line of text to the file workshop.txt, and commit them again.

12) Now we're going to look at the record we've made so far. Try runningt the command:

> git log









