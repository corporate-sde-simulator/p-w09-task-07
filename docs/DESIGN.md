# Learning Guide — Git Bisect

## What is Git Bisect?
Binary search through commits to find which one introduced a bug.

## The Process
1. Mark a known GOOD commit and a known BAD commit
2. Git checks out the middle commit — you test it
3. Tell git if it's good or bad
4. Repeat until the exact breaking commit is found

## In This Task
You have v1-v5. v1 is good, v5 is bad.
- Test v3 (middle). If bad -> bug is in v1-v3. If good -> bug is in v3-v5.
- Continue halving until you find the exact version.

## How to Test Each Version
`python
from v3_dataProcessor import DataProcessor
dp = DataProcessor()
dp.add_record('A', 10)
dp.add_record('B', 20)
result = dp.process_records()
print(result['average'])  # Should be 15.0, not 1.0
`
"@ | Set-Content "c:\Users\DINESH VA\Desktop\SDE tivor\Product-Track\Week-9\Task-7\docs\GUIDE.md" -Encoding UTF8

@"
# ADR-024: Debugging Strategy - Git Bisect
**Decision:** Use binary search through versions to find breaking change.
**Expected:** 3 tests to find the bug among 5 versions (log2(5) = ~2.3).
