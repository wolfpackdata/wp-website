---
title: How to Restrict What Your IC Can Touch
slug: how-to-restrict-what-your-ic-can-touch
excerpt: "You hired a contractor to build something. Here is how to make sure they can only reach the parts of your company you meant to hand them. I am the contractor, and this is the lockout I ask for."
cover: cover.jpg
cover_alt: A dark navy grid of locked cells seen from above at an angle, with one corridor of cells lit in icy blue running from the left edge to a single bright destination panel, and small amber points marking the turns.
date: 2026-09-10
tags: [governance, AI safety, engineering leadership, client engagement]
featured: false
---

You run a technical company. You are not the engineer. And you have just hired an independent contractor, an IC, to build something that matters.

Somewhere around the second week, a question shows up that nobody wants to ask out loud: **what can this person actually touch?**

I am that contractor. Twenty years on the other side of that question have landed me on a position that surprises some clients. **I want you to lock me out.** Not out of the work. Out of everything that is not the work.

This post is the list I hand a founder before we start. Each item comes in plain language, then one level down, the engineering mechanism that makes it real. You need to know it exists, so you can ask whether it is on.

One more thing. "Contractor" now includes the AI. An agent that writes code for you is an independent contractor with a very fast typing speed and no sense of consequence. Every rule below applies to it too, and the last section is about that.

## 1. Nobody ships to production alone. Including me.

Your codebase has a main branch. Whatever is on it is, by definition, what your customers get. The single most valuable restriction you can put on a contractor is that **they cannot change main by themselves.** Not once, not for a hotfix, not because it was "just a one-liner."

**How it is executed:** GitHub has a feature called branch rulesets. A ruleset on main says: no direct pushes, every change arrives as a pull request, and that pull request needs an approving review from a named code owner before it can merge. The code owner is you, or whoever stands in for you. In my own organization the rule is written once at the org level and applies to every repository, so a new project is born with the lock already on. A second ruleset on the integration branch requires a pull request but no approval.

The tell that it is working: the contractor can open a pull request into main, and nobody, including the contractor, can click merge until an owner approves.

## 2. Give me a sandbox, not the keys

A contractor needs somewhere to work that is not your live system. Ask for two things.

**A sandbox repository.** A separate repository where the contractor can experiment, break things, and push freely. Nothing in the sandbox reaches customers. Anything worth keeping moves into the real repository as a pull request, under the rules in section one.

**A non-production database.** The most expensive mistake a contractor can make is not bad code. It is a good query run against the wrong database. Ask for a development copy of your data: same structure, scrubbed or synthetic, on a separate connection. The contractor's tools should point at that copy by default, and switching to production should be a deliberate act that someone authorizes.

**How it is executed:** separate repositories or forks on GitHub, a development database with its own connection string, and configuration in which production is never the default. In my own tools, anything that writes to real infrastructure runs as a dry run unless someone explicitly turns the dry run off.

## 3. Your data lives in your accounts, and you can turn me off in under a minute

When a contractor builds you a data system, ask one question: **whose account is it in?**

If the answer is the contractor's account, you have a problem you will not feel until the engagement ends. Your data and dashboards are sitting on somebody else's bill, and getting them back is a migration project.

The version I run is the opposite. Everything gets provisioned inside a cloud project you own. I work inside it as a guest. When we are done, or if you decide tomorrow that you would rather I were not there, you remove one permission and I am out. The data does not move. Nothing ever left, so there is nothing to claw back.

**How it is executed:** on Google Cloud, the client creates a service account in their own project and grants the contractor the ability to act as that account, and nothing else. No key files are ever downloaded, so there is no file to leak. Revocation is deleting one IAM binding, a single line in a console the client already controls. I also refuse a short list of roles by name, the ones that would let a contractor grant themselves more access later. A permission that can escalate is not a small permission.

## 4. My tokens are short, narrow, and never in your code

When a contractor's tools talk to GitHub or to your cloud, they use a token, a long password that a program can present. The restriction is simple to state: **every token is scoped to the least it needs, expires on a schedule, and lives outside the repository.**

**How it is executed:** GitHub's fine-grained personal access tokens can be limited to specific repositories and specific permissions. The token my automated reviewer uses has exactly four: read the code, read and write pull requests, read and write issues, read metadata. It cannot push or merge. It expires, and for the tokens my automation depends on, a reminder opens thirty days before expiry. It lives in the user's own profile on the machine, never in a tracked file, and every repository ignores `.env` files from day one.

The rule that binds everyone: no credential in an issue, a pull request, a commit, a log excerpt, a screenshot, or an AI prompt. Not redacted-ish. Not temporarily. If one ever gets out, it is rotated first and written up second. I have done that twice. Both times a token reached a terminal it should not have, and both times it was rotated before anything else. That is not a confession. That is the system working.

## 5. The AI is a contractor, and it needs a rulebook it cannot argue with

Whether your contractor uses an AI coding agent or you do, every restriction above still applies. Two more are specific to the AI.

**It gets its own identity.** My automated reviewer has its own GitHub account, on its own team, with the lowest permission level that can still post a review. It cannot push, merge, change settings, or close an issue. It signs everything it writes with a prefix, so a reader can tell a program's comment from a person's at a glance. The agent that writes code has no identity of its own. It works as the human running it and inherits exactly that human's permissions. No more. The short version is in [what every new client gets when working with Wolfpack](https://www.wolfstrategyllc.com/post/working-with-wolfpack): create an account for the AI just as you would for a new employee, and restrict it to what it genuinely needs.

**It runs under a written SOP with hard stops.** Every repository carries a rulebook the agent loads at the start of every session. Most of it is preference. A handful of lines are not. They are numbered: never commit or merge to main, never write outside the working directory, never run a command on any machine but this one, never close an issue. The document itself says that repeating the request does not unlock them.

**How it is executed:** the rulebook is a file in the repository. The hard stops are backed by hooks, small programs that intercept the agent's commands and refuse the ones that break a rule, so "remember not to" becomes "the call does not go through." When the AI reviewer runs, its only writable location is one folder inside its own run directory. A write anywhere else fails instead of asking. I treat all of this as a forcing function rather than a security boundary. The security boundary is the ruleset on main, which is why section one comes first.

## Why I ask for this

Because it makes me faster, not slower. A contractor who can reach everything has to be careful about everything. One who can only reach the work can move at full speed inside it. And when the engagement ends, you are left with the work, not a stranger's fingerprints on production and a token you forgot to revoke.

## The checklist to hand your contractor

Nobody merges to main without an owner's approval. A sandbox and a non-production database are the default. Everything is provisioned in accounts the company owns, with contractor access one person can revoke in under a minute. Every token is scoped, expiring, and stored outside the code. Any AI agent runs under its own identity, with a written rulebook and hard stops a human cannot talk it out of.

If your current contractor already does all of this, keep them. If you would like to talk through what it would look like in your company, [book a 30-minute intro call](https://calendar.app.google/zHNd1NA9wzb4VRLw5). I will bring the lock.
