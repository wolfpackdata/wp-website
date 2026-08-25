---
title: What Every New Client Gets When Working With Wolfpack
slug: working-with-wolfpack
excerpt: "What a new client gets from a Wolfpack engagement: an AI-safety mentality before any tool connects, a day-one technology stack in accounts you own, transparent delivery, and an ROI measured in dollars."
cover: cover.jpg
cover_alt: A wolf's head drawn as a glowing constellation of nodes and lines, hovering above a luminous diamond at the center of a dark blue circuit-board landscape dotted with small lit data structures.
date: 2026-08-25
tags: [AI engineering, project management, client engagement, AI safety]
featured: false
---

This post is about what every client receives when working with Wolfpack.

That includes the technical tools and processes I bring into an engagement, but it also includes something less tangible that is on everyone's mind: a data-quality and AI-safety mentality, and a practical understanding of what AI is capable of, what it is not capable of, and where it should and should not be allowed to operate.

The technology matters. The mentality around how you deploy it matters just as much.

## A Safety Mentality Before Any Tool Touches Your Systems

Part of that mentality is knowing how to dive deeply into the technical workings of an organization and first identifying all the places where you want to restrict AI — just as you would with a new employee or development partner.

That discovery process happens before an AI model is allowed to start interacting with the system.

For example, we can map out the services, connections, ports, and access points, then design AI guardrails that allow visibility only where it is explicitly needed. Other areas can be restricted and audited so the AI does not infer or gradually gain access to things it was never intended to touch.

Another example is how AI chatbots are allowed to respond to incoming customer email.

My standard operating procedure at the inception of that kind of system is simple: **the agents are not allowed to send messages. Period.**

They can draft responses, but a human must ultimately send them.

The guardrail is not merely an instruction telling the chatbot, "Don't send email." The agent layer itself does not have the send-message tool in its arsenal, and it cannot access that tool through the email provider's MCP connection. For an AI chatbot to get around that restriction would require human intervention rather than the model simply deciding to exceed its role.

Other guardrails can take the form of auditing agents.

I think of these as anonymous check bots, not finger-pointing blame machines. An auditing bot may look across communication and activity throughout a company to identify vulnerabilities, but it can also uncover opportunities:

- A customer who deserves a follow-up.
- An opportunity for an upsell.
- A recurring operational issue showing up across several conversations.
- A connection between two vendors, customers, or projects that individual employees may never have the bandwidth to notice.

The idea is not to give AI unlimited visibility because it is useful. The idea is to deliberately decide where that visibility creates value, then engineer the boundaries around it.

## The Technology You Get on Day One

Let's talk about the technology I bring into a client engagement right away.

### A Secure Wolfpack Processing Environment

On the internal Wolfpack side, every client is given their own secure processing environment with an individual client ID. Their name is anonymized inside the Wolfpack system, and their work remains isolated within its own environment.

The underlying client-separation system has been part of how I operate for roughly 15 years. The AI layer follows the same philosophy: AI sessions running inside one client's folder have no visibility into another client's data.

It is similar to using a client ID inside a data warehouse, where customer data is never allowed to commingle.

That separation is established from the beginning rather than added after development has already started.

### A Private Client Subdomain

The client also receives their own secure subdomain of the Wolfpack web environment, where we can host deliverables in a password-protected space.

I've found this makes collaboration substantially easier. Instead of sending increasingly confusing versions of files back and forth, we can host things like:

- Proposals
- Statements of work
- SOPs
- Research
- Reports
- Prototype interfaces
- Other web-based deliverables

I can send the client a link, and both teams have a convenient place to return to throughout the engagement.

### A BigQuery Analytics Environment

Another thing the client gets is the BQL command-line product, which creates their own BigQuery analytics environment.

The client owns the data on their side. Their raw data remains in their environment, and they retain the audit trail around it.

The basic environment can be provisioned from the command line in roughly five to ten minutes.

That also gives us a Looker environment where I can immediately begin prototyping:

- Tables
- Charts
- Data workflows
- Dashboards
- Exploratory analytics

Instead of spending the beginning of an engagement debating where analytics work will eventually live, we can start working with the data.

### Wolfpack AI Command

The client will also receive Wolfpack AI Command: the system I use to tie together Notion and GitHub through a Python-based agent layer.

The purpose is to connect the business and development sides of the work so that AI project manager and assistant agents can operate across otherwise separate project silos, on a centralized platform isolated from production data.

With the right permissions and guardrails in place, the AI can become a bespoke project-management layer and a developer's best friend: understanding tasks, repositories, project context, documentation, and the relationship between what the business requested and what is being built.

[Read the Wolfpack AI Command case study](https://intake.wolfstrategyllc.com/wolfpack-ai-command/)

### Private Development Repositories

The client will also receive one or several repositories, depending on the structure of the work.

These are private repositories shared with the client so their development team can inspect and audit the work whenever they want.

I don't believe a consulting engagement should require the client to take my word for what is happening inside the technical work.

## Your Accounts, Your Permissions

There is one basic infrastructure requirement I generally recommend: the client should have, or set up, Google Workspace with at least one or two users — ideally two.

The reason for the second Google Workspace user is that one account can become the AI agent's own identity.

That is important.

A major part of my approach is to lean on the permissions already built into platforms rather than trusting a prompt to enforce every security boundary.

Within Google Workspace, for example, that AI identity can be restricted from:

- Google Drive
- Specific Google Docs
- Shared Drives
- Shared folders
- Other sensitive resources

If the AI user's account does not have access to something, then we are not relying solely on an instruction buried inside a prompt telling the model not to look at it.

The same philosophy applies to platforms such as Notion, Trello, Salesforce, and other business systems.

Create an account for the AI just as you would for a new employee. Give it read-only access where appropriate. Restrict it to the teams, roles, databases, and information it genuinely needs.

Then your security model is supported by the platform's own ironclad permission structure, rather than depending entirely on instructions we have written for the AI.

## What It Costs to Get Started

The infrastructure itself can start very inexpensively.

A small client may initially be paying little more than the cost of an additional Workspace user. Realistically, however, there will also be some compute and storage charges associated with the BigQuery environment.

For a typical small or medium-sized business client, I generally budget roughly **$50 to $100 per month** for that infrastructure, and it is often less; development-heavy months can approach $100, while months under normal operation are (optimized to be) less than $50.

On top of that, I generally recommend at least a Claude Max 5x subscription so the client can use the skills and AI products I deliver without constantly worrying about hitting low usage limits.

For organizations making heavy use of these systems, I recommend Max 20x for better usage economics.

In many cases, one account should suffice. A development-heavy firm may already have this infrastructure in place.

My own system also uses Codex as an independent code and document reviewer, but a top-tier subscription there is generally not required.

## ROI Is Part of Every Statement of Work

An ROI calculator is part of every statement of work.

Together with the client, I want to figure out how the project's ROI is going to be measured **in dollars**.

Then I want to measure it over time.

The work I am doing should connect as directly as possible to that path.

For example, "followers gained" is not quite enough for me. If followers are the KPI, eventually I want to understand how those followers monetize. What is a follower worth? How does that translate into revenue? How do we justify the project economically?

Conversion is another common example.

If improving conversion is part of the project's goal, we can calculate the value of each incremental increase. Using order volume and average order value, we can estimate something like:

> Every 0.1 percentage-point increase in conversion is worth approximately $X in additional revenue.

Now the project has a scoreboard.

Ideally, I like to look at two ROI measurements:

- **Revenue-based ROI**
- **Profit-based ROI**

Why two? Because one isn't enough.

Profit ROI can become nonlinear and difficult to nail down because once direct and indirect expenses are backed out of revenue, reasonable people can arrive at several different conclusions about the project's exact contribution.

So I prefer to calculate profit ROI within an agreed set of assumptions while also tracking gross revenue ROI over time.

The client can then compare both numbers against what they're paying Wolfpack and make their own judgment about the return the engagement has produced.

In general, if I cannot figure out how to measure the economic return of the work I'll be doing, I'm hesitant to take the project until we can establish a more direct relationship between my fee and the client's expected return.

Otherwise, it isn't a win-win.

## What to Expect When Working With Ryan

A Wolfpack engagement is designed to be transparent.

The statement of work and project management live in Notion, where the client can see what is happening rather than waiting for a weekly status presentation to find out.

In general, clients can expect:

- **Transparent project management in Notion.** The work against the statement of work remains visible throughout the engagement.
- **Weekly meetings.** Usually around 30 minutes, although they can run longer when we are discussing deliverables or a new statement of work.
- **Hosted statements of work.** SOWs can live on the client's Wolfpack subdomain so both teams always know where the current version resides and amendments remain visible.
- **Secure file sharing.** I can provide secure file-sharing links through Google Cloud Storage, and I'm also comfortable working with client-provided FTP or other existing infrastructure.
- **Questions instead of assumptions.** I work very autonomously, but I'm extremely detail-oriented. If something materially affects the quality of a deliverable, I will ask rather than quietly guessing.
- **Loom videos.** I love using Loom for questions, debugging walkthroughs, demonstrations, and tours of deliverables.
- **AI coaching.** Clients also have access to me as an AI coach when they want to bring tools, advice, or best practices to other members of the team alongside the primary statement of work.
- **Self-tested and self-audited deliverables.** I use adversarial agents to judge and test my own work, deliberately looking for weaknesses, edge cases, and scenarios I may not have considered.

I'm very delivery-focused, and I analyze every deliverable from Python through the P&L.

## Where to Start

If the work you're picturing sounds like it's inside the Wolfpack wheelhouse — analytics, AI enablement, operational systems, product thinking, or connecting messy business data into something powerful — let's have a call.

[Book a 30-minute intro call](https://calendar.app.google/zHNd1NA9wzb4VRLw5)

[See recent projects in the portfolio](https://intake.wolfstrategyllc.com/portfolio/)
