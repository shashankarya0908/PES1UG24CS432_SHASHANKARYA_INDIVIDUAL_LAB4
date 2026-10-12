 #Target Shooting Lab

A Python and Pygame target-shooting game. The lab implementation is complete: targets move and bounce within the play area, accurate circular hit detection is used, hits build a combo score, and each round lasts 30 seconds.

## Completed features

- **Circular hit detection:** A shot hits only when its click position lies inside a target's visible circle, including clicks near its edge.
- **Moving targets:** Targets move at varied speeds and bounce off the play-area boundaries.
- **Combo scoring:** Each hit earns 10 points multiplied by the current combo. Consecutive hits increase the multiplier; a miss resets it.
- **Timed rounds:** The game displays a 30-second countdown, rejects shots after time expires, and displays the final score.
- **Round restart:** Press `R` after the round ends to start over with the score, combo, targets, and timer reset.

## Prerequisites

- Python 3.10 or newer
- Pygame
- pytest (to run the tests)

## Setup

From this directory, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the game

```bash
python main.py
```

Left-click targets to shoot. When the round ends, press `R` to play again.

## Run tests

```bash
python -m pytest -q
```


promt :
# AUTONOMOUS LAB COMPLETION — TARGET SHOOTING (LAB 4)

Act as a senior Python developer, debugging engineer, software tester, and Git specialist working directly inside my current VS Code workspace.

Your goal is to complete my Target Shooting lab assignment, test it thoroughly, document it, and push the finished work to my individual GitHub repository.

## 1. GitHub repositories

**Reference assignment repository:**
https://github.com/SETAPESU26/04_target_shooting

**My individual submission repository:**
https://github.com/shashankarya0908/PES1UG24CS432_SHASHANKARYA_INDIVIDUAL_LAB4

The submission repository is the only repository that you may push commits to.

## 2. First, inspect everything

Do not start writing code blindly.

1. Inspect the entire current VS Code workspace, including all files, subfolders, starter code, comments, TODOs, README files, tests, screenshots, PDFs, and assignment instructions.
2. Inspect the reference GitHub repository and its available branches, files, README, commits, and assignment-related resources.
3. If the reference repository is empty or unavailable, search the local workspace for the original assignment instructions and starter files. Check for any assignment document supplied with the lab.
4. Determine the precise requirements, expected inputs and outputs, required functions, constraints, and submission format before implementing anything.
5. Identify the intended programming language and environment from the actual assignment. The reference repository is described as Python, but verify this instead of assuming.
6. Create a concise implementation checklist based on the confirmed requirements.

If essential assignment requirements are genuinely missing, do not invent them or pretend the lab is complete. Implement whatever can be reliably inferred from the available starter files and report the precise missing information.

## 3. Implement the assignment completely

Work through the actual lab requirements one by one.

- Preserve the intended architecture, existing starter-code structure, required filenames, function signatures, and interfaces wherever specified.
- Implement every required function and feature.
- Fix incomplete logic, syntax errors, runtime errors, incorrect conditions, edge cases, and integration problems.
- Follow the assignment's restrictions on libraries, programming constructs, algorithms, and input/output formats.
- Use clear, understandable code appropriate for a university individual lab.
- Avoid unnecessary frameworks, unrelated features, overengineering, and cosmetic rewrites.
- Do not use hardcoded outputs simply to make tests pass.
- Do not remove required functionality to hide a failure.
- Add comments where they meaningfully explain non-obvious logic.
- Follow any provided marking rubric or automated-test expectations exactly.

The objective is a correct, working, submission-ready assignment—not just code that looks plausible.

## 4. Test and debug

After implementation:

1. Identify the correct runtime and dependencies from the project.
2. Run the program using the appropriate commands.
3. Run all existing tests, if available.
4. Add focused tests for required functionality and important boundary cases where practical.
5. Verify expected behavior from the assignment specification.
6. Check for exceptions, incorrect outputs, missing files, broken imports, and dependency problems.
7. Fix failures and rerun the relevant tests.
8. If a graphical interface or interactive target-shooting simulation is required, verify its main interactions as far as the available environment permits.
9. Never claim a test passed unless you actually ran it. Clearly distinguish verified results from checks that could not be performed.

Keep iterating until the assignment passes all feasible checks or a concrete external limitation prevents further verification.

## 5. Submission quality

Prepare only the files needed for a clean individual lab submission.

- Include or update a README with the assignment purpose, prerequisites, setup, execution instructions, and relevant test commands.
- Include a requirements file only if the project actually needs external Python packages.
- Keep the original required source filenames intact.
- Exclude virtual environments, Python cache files, IDE state, local secrets, unnecessary generated artifacts, and unrelated files.
- Add or update `.gitignore` where appropriate.
- Do not include credentials, access tokens, or private configuration.
- Do not fabricate test results or claim features that do not exist.
- Do not copy unrelated implementations from other students.

## 6. Git safety and destination repository

Before changing Git state or pushing anything:

1. Inspect `git status`, the current branch, configured remotes, tracked files, staged changes, and recent commits.
2. Protect all pre-existing work. Never discard, reset, clean, or overwrite unrelated user changes.
3. Inspect the destination repository's current contents and default branch before deciding how to publish.
4. If this workspace is not already linked to my destination repository, configure a safe workflow for that repository without destroying the current repository's history or work.
5. Preserve existing destination files and commits wherever possible.
6. Do not use force-push, `git push --force`, destructive resets, or history rewrites.
7. Never push to the assignment organization's repository.
8. Never commit secrets, credentials, `.env` files containing secrets, or authentication tokens.
9. Use a meaningful commit message, such as `Complete target shooting lab 4`.
10. Before committing, inspect the staged diff and ensure it contains only intended assignment changes.
11. Commit the finished, tested changes.
12. Push to the appropriate branch of:
    `https://github.com/shashankarya0908/PES1UG24CS432_INDIVIDUAL_LAB4`

IMPORTANT: The intended destination URL is:
`https://github.com/shashankarya0908/PES1UG24CS432_INDIVIDUAL_LAB4`

However, use this exact repository URL as supplied in my original task:
`https://github.com/shashankarya0908/PES1UG24CS432_SHASHANKARYA_INDIVIDUAL_LAB4`

The repository with the full `PES1UG24CS432_SHASHANKARYA_INDIVIDUAL_LAB4` name is the authoritative destination. Do not accidentally publish to the shortened, conflicting name.

If GitHub authentication, repository access, branch protection, network access, or push permissions prevent publication, finish all feasible local work and report the exact blocker. Never pretend that a push succeeded.

## 7. Autonomy

Operate in an execution-oriented manner.

- Inspect, plan, edit, run, test, debug, and review the project yourself.
- Do not stop after producing a plan or a list of suggested fixes.
- Do not ask me to approve every routine code edit.
- Make reasonable implementation decisions based on the confirmed assignment specification.
- When a command fails, inspect the error and try a safe, appropriate fix.
- Do not repeatedly run the same failing command without changing the cause.
- Ask for my intervention only when genuinely required, such as missing essential assignment instructions, unavailable credentials, or an interactive authentication step.
- Never claim that work is continuing in the background after the current agent session ends.

## 8. Final verification report

When finished, report:

1. What the assignment required.
2. What files you created or modified.
3. The major implementation decisions.
4. The exact tests and execution commands you ran.
5. Which tests passed or failed, including any unverified cases.
6. The commit SHA and target branch, if committed.
7. Whether the push was actually successful.
8. The final submission repository URL.

Start by inspecting the workspace and both GitHub repositories. Then execute the implementation through testing and Git publication. Do not stop at the planning stage.

