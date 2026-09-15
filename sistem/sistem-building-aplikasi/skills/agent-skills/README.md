# agent-skills hub catalog (from Input-Pengguna/agent-skills-main.zip 6.6M, 248 skills)
Source zip kept at Input-Pengguna/agent-skills-main.zip - full content available via unzip
Install selective: unzip -q Input-Pengguna/agent-skills-main.zip -d /tmp && cp -r /tmp/agent-skills-main/<skill> skills/
# Agent Skills

Shared skill catalog for GitHub Copilot, Claude Code, and Codex.

This workspace is the main branch for maintained skills, cross-client
portability guidance, host-aware routing, and MCP fallback rules.
Install or import new maintained skills here first, then sync them outward to the downstream targets.

## Session Start Rule

Every AI agent working in this workspace, including Codex, Claude Code, and
GitHub Copilot, must read
[`LESSON.md`](c:\Users\LOQ\.copilot\skills\LESSON.md) at the start of each new
session before analysis, planning, edits, validation, reviews, or advisory
work.

## Completion, Sync, and Publish Rule

For every user-requested mutation task in this workspace, finish the requested
work in `C:\Users\LOQ\.copilot\skills` first, then validate, sync outward to
the approved skill folders, and commit and push to GitHub when
the result is satisfactory.

Treat the work as satisfactory only when validation passes, sync completes,
no requested step was skipped, no required command was rejected, no unresolved
secret/security/privacy issue remains, and the final diff matches the user's
request. Escalate to the user instead of committing or pushing when those
conditions are not met. For read-only or advisory tasks with no file changes,
do not create empty sync, commit, or push churn.

