# creat-repos.sh

## Description
Create and push to a new github repo from the command line. This will use the ssh interface for updates and it puts the repos under origin.

Grabs sensible defaults from the containing folder and `.gitconfig`. Make sure you set the github.user to your prefered GitHub user ID. The script will allow you to override that setting but that's where the script gets the default from.

I found Rob Wierzbowski's original code here: [https://gist.github.com/robwierzbowski/5430952/] (https://gist.github.com/robwierzbowski/5430952/)

## Usage
You can add your GIT User ID with (replace "githubID" with your GIT Hub User ID):
```
    git config --gobal github.user "githubID"
```
then check it to see if it's set:

git config github.user

```
    mkdir *ReposName*
    cd *ReposName*
    creat-repos.sh # Reply to the prompts
```
Now start adding your files and performing normal git functions.

## Todo
- clean up the terminology
- I'm not happy with the initial setup of the script. I'll need to think about the next step but this works and that's a start.
# mqtt-ser Readem
