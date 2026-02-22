# DEVTOOLS-105: Find the Breaking Change Using Git Bisect

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 30 · **Story Points:** 5
**Reporter:** Raj Patel (Senior Dev) · **Assignee:** You (Intern)
**Labels:** `git`, `bisect`, `debugging`, `python`
**Task Type:** Debugging

---

## Description

The `DataProcessor` class was working 5 commits ago but is now broken. The function
`process_records()` returns wrong results. We have 5 versions of the file representing
5 commits. Your job: figure out which commit introduced the bug.

Each version is in `src/` named `v1_dataProcessor.py` through `v5_dataProcessor.py`.
v1 is the oldest (known good), v5 is the latest (known broken).

This simulates `git bisect` — binary search through commits to find the breaking one.

## Strategy (like git bisect)

1. Test v1 (good) and v5 (bad) — confirm the range
2. Test v3 (middle) — is it good or bad?
3. Based on the result, test v2 or v4
4. Identify the exact version that introduced the bug
5. Write your finding in `src/bisect_result.txt`

## Acceptance Criteria

- [ ] Identify the exact version that broke `process_records()`
- [ ] Explain what changed in that version
- [ ] Fix the bug in `src/dataProcessor.py` (copy the correct version + fix)
- [ ] Tests pass
