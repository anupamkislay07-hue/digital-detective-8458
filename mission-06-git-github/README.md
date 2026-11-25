# Mission 06 — Git, GitHub, branches and Pull Requests

## 1. Task / objective

Understand version control and the basic Git workflow: inspect the status, stage specific changes, commit them with a meaningful message and review the history. Then create a branch named `update-about`, add a "My Learning" section to the root README, publish the branch, and open a Pull Request from that branch into `main`. Finally, explain the core Git operations in my own words.

## 2. Work completed

### Task 6.1 — The basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| Check repository status (`git status`) | Reports which files are untracked, modified or already staged, and which branch I am on. It changes nothing — it only tells me what Git currently sees. |
| Stage selected changes (`git add <file>`) | Moves chosen changes into the staging area, the holding list that the next commit will capture. Staging a single file keeps unfinished work in other files out of the commit. |
| Create a commit (`git commit -m "..."`) | Records everything in the staging area as one permanent snapshot with a message describing why the change was made. |
| View commit history (`git log --oneline`) | Lists past commits newest first, each with its short hash and message, so I can follow how the project evolved. |

**Staging vs. committing.** Staging is *selecting* what should be saved: the changes are still only in the working directory plus an index entry, and I can keep editing or unstage them. Committing is *saving* the selected changes as a permanent snapshot that becomes part of the project history. A commit cannot be created without something staged; the staging area is the boundary that lets one commit contain exactly the work I mean, rather than everything that happens to be on disk.

### Task 6.2 — The `update-about` branch

1. Created a branch from `main` and switched to it:

   ```bash
   git checkout -b update-about
   ```

2. Added a short **"My Learning"** section to the root `README.md` describing three things learned during the assignment.
3. Inspected the status, staged only that one file and committed it:

   ```bash
   git status
   git add README.md
   git commit -m "Add My Learning section to root README"
   ```

   Commit: `6662b9f` — *Add My Learning section to root README*.
4. Published the branch to GitHub:

   ```bash
   git push -u origin update-about
   ```

   The first push created the branch on the remote and set it to track `origin/update-about`.

### Task 6.3 — The Pull Request

- Opened a Pull Request from `update-about` into `main`:

  **PR #1 — "Add My Learning section to root README"**
  <https://github.com/anupamkislay07-hue/digital-detective-8458/pull/1>

- Description written on the PR: the README change, and that the branch was created for Mission 06 tasks 6.2 and 6.3 so the change can be reviewed before reaching `main`.
- Compared and reviewed the changed file: one addition, eleven lines, only `README.md` touched (the "My Learning" section and its heading), no other files affected.
- **Merge status: the Pull Request was MERGED into `main`.** Merge commit: **`2d76846`** — *Merge pull request #1 from anupamkislay07-hue/update-about*.
- Before the merge, GitHub reported a conflict because the root README had gained a "Running the Number Converter" section on `main` while this branch added "My Learning" at the same place. I resolved it locally by merging `main` into `update-about` and keeping both sections (commit `e710e25`), then pushed and merged the PR, so nothing was overwritten.
- After merging, the local `main` was updated and the change confirmed on the computer:

  ```bash
  git checkout main
  git pull
  ```

  `git rev-parse HEAD origin/main` then showed the same commit, and the "My Learning" section was present in the root `README.md` on `main`.

**What a branch is and why it is useful.** A branch is a separate line of development that shares the project's history but records its own new commits, so work in progress can exist without changing what is on `main`. If the change is wrong, `main` is untouched and the branch can simply be deleted.

**What a Pull Request is and why it is useful.** A Pull Request is a request to merge one branch into another, together with a diff, a description and a place to discuss it. It makes a change reviewable before it lands, shows exactly which lines moved, and leaves a record of why the change was accepted. When several people work on the same repository, branches plus Pull Requests are what stop everyone's unfinished edits from colliding on `main`.

### Task 6.4 — Git command glossary

| Operation | One-line explanation |
|---|---|
| Initialise a repository (`git init`) | Turns an ordinary folder into a Git repository by creating the hidden `.git` directory that stores all history. |
| Check status (`git status`) | Shows the current branch and which files are modified, staged or untracked. |
| Stage changes (`git add <file>`) | Marks chosen changes to be included in the next commit. |
| Commit changes (`git commit -m "..."`) | Saves the staged changes as a permanent snapshot with a descriptive message. |
| View history (`git log --oneline`) | Lists previous commits with their short hashes and messages. |
| Create or list branches (`git branch`) | Lists local branches, or creates a new one when given a name. |
| Switch branches (`git checkout`, `git switch`) | Moves the working directory onto another branch so its commits and files become current. |
| Publish changes (`git push`) | Uploads local commits on a branch to the remote repository. |
| Retrieve remote changes (`git pull`) | Downloads commits from the remote and merges them into the current branch. |

### Local vs. remote repository

A **local repository** lives inside my project folder on the computer: it is fast, works offline, and is where I edit, stage and commit. A **remote repository** (GitHub) is the copy hosted online — a backup, a sync point between machines, and the place where branches and Pull Requests are reviewed.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git init` | Start version control in the project folder. |
| `git status` | Inspect staged, modified and untracked files before every commit. |
| `git add <file>` | Stage a specific file so the commit contains only that work. |
| `git commit -m "..."` | Save a meaningful snapshot of the staged changes. |
| `git log --oneline` | Review the commit history of the repository. |
| `git checkout -b update-about` | Create and switch to the new branch. |
| `git push -u origin update-about` | Publish the branch and set its upstream. |
| `git branch`, `git switch`, `git pull` | List branches, change branch, retrieve remote changes. |
| GitHub Pull Request | Review the branch change and request its merge into `main`. |

## 4. My understanding

Git is the record; GitHub is where that record is hosted and reviewed. Every commit is a snapshot of the staged changes only, which is why `git add` matters: it decides what goes into the snapshot. Staging and committing are therefore two separate decisions — *what* to save, then *saving* it — and keeping them separate is what makes clean, per-mission commits possible instead of one large unexplained change.

Branches let me work without touching `main`, and a Pull Request is the review step that turns a branch into a proposed change. The `update-about` work showed the whole cycle: branch, edit, stage, commit, push, compare, review and merge. PR #1 was merged into `main`; the open-PR screenshot currently in `evidence/` shows a different request with the branches reversed, so it is not evidence of that merge.

## 5. Difficulties faced

- The first `git push` of the new branch failed with `could not read Username for 'https://github.com'`, because no credential helper was configured and Git fell back to asking for a password.
- Keeping track of which branch I was on, since committing the README on the wrong branch would have put the "My Learning" section straight onto `main`.
- Understanding that a published branch does not change `main` — the files on GitHub's `main` stay the same until the Pull Request is merged.

## 6. How I resolved them

- I checked how Git was authenticating, configured the GitHub CLI as the credential helper with `gh auth setup-git`, and re-ran the same `git push`. It succeeded without any password, using the existing GitHub login.
- I ran `git branch --show-current` and `git status` before every commit, and staged only `README.md` so nothing else could slip into the branch commit.
- I compared the two branches on GitHub after pushing and confirmed PR #1 lists only the README change, which made the difference between "pushed" and "merged" concrete.

## 7. Evidence / files

- Root `README.md` — the "My Learning" section added on the `update-about` branch (commit `6662b9f`).
- Branch `update-about`, pushed to `origin`.
- **PR #1**: <https://github.com/anupamkislay07-hue/digital-detective-8458/pull/1> — **merged** into `main` as commit `2d76846`.
- Root `README.md` on `main` after the merge contains both the "My Learning" section and the number-converter instructions.
- Commit history visible on GitHub for every mission.

## 8. Commit details

Commit message: **Complete Git and GitHub collaboration mission**

Branch commit: `6662b9f` — *Add My Learning section to root README* (on `update-about`).

Both the branch and this README were pushed to GitHub and verified on the repository page.
