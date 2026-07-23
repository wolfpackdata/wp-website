<!--
  Wolfpack GitHub SOP — Pull Request template.
  Squash-merges into `develop`. See docs/sop/02-commits-and-prs.md.
-->

## Summary

<!-- What does this PR change, and why? One or two sentences. -->

## Related issues

<!--
  Reference issues PLAINLY — `#N` or `Refs #N`.
  NEVER use closing keywords (Closes / Fixes / Resolves #N): issues stay open until
  Ry verifies against real data. See docs/sop/03-issues-and-labels.md.
-->

Refs #

## Local verification results

<!--
  Repos generally have no CI — the merge gate is local verification.
  Paste the actual commands you ran and their results (or "N/A — docs only").
-->

```
# e.g. npm test, npm run build, lint — with their output/summary
```

## Checklist

- [ ] Conventional Commit title with an area scope (e.g. `feat(matrix): …`, `fix(compare): …`).
- [ ] Branch is `prefix/issue-number-kebab-slug`, cut from `develop`.
- [ ] No closing keywords — issues referenced with `#N` / `Refs #N` only.
- [ ] Full local suites run and results pasted above (or explicitly N/A).
- [ ] After merge: add `fixed-on-develop` to every issue this PR addresses.
