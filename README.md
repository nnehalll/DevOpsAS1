# DevOps Assignment 1: Git Branching and Workflow

<b>Objective: </b> Implement and manage a branching strategy in Git.<br>
<br>
<b>Tasks:</b><br>
1. Repository Setup-<br>
    Create a new Git repository or use an existing one with a sample Python project (e.g., a simple Flask or FastAPI application).<br>
    ```git
    echo "# DevOpsAS1" >> README.md
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/nnehalll/DevOpsAS1.git
    git push -u origin main
    ```

2. Feature Branch- <br>
    - Create a new branch named <code>feature/new-feature</code> from the main branch.
    - Implement a new feature in this branch, such as adding a new endpoint to the API.
    - Commit the changes and push the branch to the remote repository.<br>
    ```git
    git checkout -b feature/new-feature
    git commit -m "Add new endpoint to the API"
    git push -u origin feature/new-feature
    ```

3. Release Branch-<br>
    - Create a release branch named <code>release/v1.0.0</code> from the main branch.
    - Merge the <code>feature/new-feature</code> branch into the <code>release/v1.0.0</code> branch.
    - Tag the release branch with <code>v1.0.0</code>.
    ```git
    git checkout -b release/v1.0.0
    git merge feature/new-feature
    git commit -m "Update file with new changes"
    git tag v1.0.0
    git push -u origin release/v1.0.0
    git push -u origin v1.0.0
    ```
