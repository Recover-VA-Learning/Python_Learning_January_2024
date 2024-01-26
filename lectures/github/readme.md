# GitHub Commands Cheat Sheet

### MOST USED COMMANDS
- `git clone [repository_url]`: Clone a remote repository to your local machine.
- `git push`
- `git pull`

> VS Code has a built-in UI for Git. You can access it by clicking on the Git icon in the left sidebar.

## Repository Commands

- `git init`: Initialize a new Git repository in the current directory.
- `git clone [repository_url]`: Clone a remote repository to your local machine.
- `git remote add origin [repository_url]`: Add a remote repository as the origin.
- `git remote -v`: List all remote repositories.
- `git pull origin [branch_name]`: Fetch and merge changes from a remote repository.
- `git push origin [branch_name]`: Push local changes to a remote repository.

## Branch Commands

- `git branch`: List all branches in the repository.
- `git branch [branch_name]`: Create a new branch.
- `git checkout [branch_name]`: Switch to a different branch.
- `git merge [branch_name]`: Merge changes from a different branch into the current branch.
- `git branch -d [branch_name]`: Delete a branch.

## Commit Commands

- `git status`: Show the status of the repository.
- `git add [file_name]`: Add a file to the staging area.
- `git commit -m "[commit_message]"`: Commit changes with a descriptive message.
- `git log`: Show the commit history.
- `git diff`: Show the differences between the working directory and the staging area.

## Collaboration Commands

- `git fetch`: Fetch changes from a remote repository.
- `git pull`: Fetch and merge changes from a remote repository.
- `git push`: Push local changes to a remote repository.
- `git branch -r`: List all remote branches.
- `git branch -a`: List all local and remote branches.

## Miscellaneous Commands

- `git config --global user.name "[your_name]"`: Set your name for Git commits.
- `git config --global user.email "[your_email]"`: Set your email for Git commits.
- `git remote show origin`: Show information about the remote repository.
- `git stash`: Stash changes in a dirty working directory.
- `git stash apply`: Apply the most recent stash.
