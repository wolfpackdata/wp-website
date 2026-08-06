528 commits across nine repositories in thirty days.

That number sounds like the story. It is not.

A commit is bookkeeping, not value. My workflow also creates more commits than some teams because one issue becomes one branch and one pull request. Line counts were left out because generated builds would have distorted the comparison.

The useful story is the system behind the output.

I personally built five projects with Claude and OpenAI agents as implementation partners. I wrote the specifications, constraints, architecture, and verification rules. The agents handled implementation inside those boundaries.

Two practices mattered most.

First, I used an expensive reasoning model only as the orchestrator, then pinned subagents to a less expensive model at two separate levels. I verified the routing on a small slice of work before letting the full run spawn.

Second, merging never meant verified. A merged issue received a `fixed-on-develop` label and stayed open until human testing confirmed the result. That separated the development backlog from the verification queue.

The lesson is not that AI can produce a large commit count. The lesson is that engineering judgment can be moved into specifications, controls, tests, and review systems that make higher output easier to trust.

For technical leaders already using coding agents, which part of your engineering judgment still lives only in your head?

Read the full version linked in Wolfpack profile.