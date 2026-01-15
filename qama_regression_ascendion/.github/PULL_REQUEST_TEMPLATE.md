# Pull Request Template

## Summary
- **What does this PR do?**
- **Why is this change needed?**

## Type of Change
- [ ] Feature
- [ ] Bug Fix
- [ ] Refactor / Cleanup
- [ ] Documentation Update
- [ ] Test Automation Update
- [ ] CI/CD / Config Change

## Related Tickets / References
- JIRA / Azure / QC ID(s):
- Test Case IDs (if applicable):

## What Was Done
- Describe key changes
- List updated flows, methods, locators, resources, configs

## Test Coverage
- [ ] Unit tests updated/added
- [ ] Automation scripts updated
- [ ] Manual test cases covered
- [ ] Platform-specific validations considered (Windows/Mobile/Cloud)

## Evidence / Logs
(Add screenshots, video recordings, execution logs if applicable)

##  Breaking Changes (if any)
- Does this PR introduce breaking changes? If yes, explain impact.

##  Developer Self‑Review Checklist
- [ ] Code compiles without warnings
- [ ] Code follows naming conventions (methods, flows, page objects)
- [ ] Proper use of FlowContainer & reusable flows
- [ ] Page methods mapped to correct flow files
- [ ] Assertions are complete and no validations missed
- [ ] Image/layout validations added (if needed)
- [ ] Proper error handling & return values implemented
- [ ] No hardcoded waits (replaced with explicit waits)
- [ ] No sensitive data / credentials in code
- [ ] Locators added to UIMAP with correct region mapping
- [ ] Logs, prints, and comments are meaningful
- [ ] Dependencies updated safely

##  Reviewer Checklist
- [ ] Code readable and maintainable
- [ ] No duplicate logic / reusable flows exist
- [ ] Naming conventions followed
- [ ] No dead code or commented-out blocks
- [ ] Test coverage sufficient
- [ ] Platform dependency handled (skip/fail logic)
- [ ] No assertion gaps
- [ ] Potential risks identified

##  Deployment Notes
- Any steps needed after merging? (e.g., rebuild pipelines, update config files)

## Additional Notes
(Anything else relevant for reviewers)
