# Configuration Status Accounting (Lab 3)

## Branch Structure
- `main` — stable production branch
- `dev` — active development branch (Lab 3)
- `feature/add-grade` — feature branch (Lab 1)
- `maint/v1.1-updates` — maintenance branch (Lab 2)

## Commit → Maintenance Task Mapping
| Commit | Task | Lab |
|--------|------|-----|
| Initial commit | Baseline setup | Lab 1 |
| Lab 2: Corrective, adaptive... | All maintenance types | Lab 2 |
| Lab 3: Add inventory module | New inventory feature | Lab 3 |
| Lab 3: Add generated changelog | Status accounting | Lab 3 |

## Releases
- v1.0 — Lab 1 baseline
- v1.1 — Lab 2 maintenance release
- v1.0-lab3 — Lab 3 accounting release

## Git Commands Used
- `git log --oneline --graph` — visualize history
- `git tag` — mark releases
- `git branch -a` — list all branches