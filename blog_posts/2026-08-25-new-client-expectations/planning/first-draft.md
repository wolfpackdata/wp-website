# First draft — What Every New Client Gets When Working with Wolfpack

<!--
This is Claude's v1 draft, built per Ry's instruction in the source transcript
(planning/source-transcript.srt): as much verbatim transcript copy as possible, in a
reordered structure, with ums and stutters removed and grammar deliberately NOT cleaned
up. It is raw material for the human copywriter, not the post. The outline it follows,
the constraints, and the fact-check notes are in planning/copywriter-brief.md and
planning/source-notes.md. Claude's client-lens critique of this draft is in
planning/draft-feedback.md.

Title is a working title. Slug, tags, excerpt, and cover are Phase 2 decisions.
-->

This blog is going to talk about what any client receives when working with Wolfpack. And
it is not only about technical tools and processes that I bring in, but also about a data
quality and AI safety mentality, and the knowledge about what AI is capable of and is not
capable of, what AI can do and cannot do.

## A safety mentality before any tool touches your systems

Part of that mentality is knowing how to dive deeply into how the technical aspects of any
organization work to first find all the places where you want to restrict AI, just as you
would a new employee. And that whole discovery process happens without an AI model talking
to the system.

For example, we map out all the services, connections, and the ports, and make sure that
we design AI guardrails that only allow AI visibility to certain ports, and explicit
guardrails that both restrict and audit those other ports to make sure that the AI never
infers access to those.

Another example would be how AI chatbots are allowed to respond to incoming customer
email. My SOP for that is that they are not allowed to send messages, period. At the
inception of the system, the agents are only allowed to draft responses that a human must
ultimately send. And so the guardrail we would set up there is to create an agent layer on
the AI chatbot, so it doesn't have the tool to send a message in its arsenal, and it
cannot access that tool in the MCP of the email provider. For an AI chatbot to get around
that restriction would require a lot of human prompting and human interference.

Other guardrails could be set up in the form of auditing agents, which need to be seen as
anonymous check bots, not finger-pointing blame machines, because those auditing bots will
be looking at communication across the whole company and can find vulnerabilities, and can
also find opportunities for things like great customer service in a follow-up or an
upsell, or drawing connections between different vendors or customers that a human being
wouldn't have the bandwidth to ever make.

## The technology you get on day one

So let's talk about the technology that I bring into a client right away.

First, on the internal Wolfpack side, the client is given their own secure processing
environment with their own client ID, which anonymizes their name in the Wolfpack system.
This is my own system that has been in place for 15 years and keeps all client work in
their own gated community. The AI that I use internally for my clients is also gated in a
similar way, where AI sessions in one client folder have absolutely no visibility into any
other client data. And this is a similar approach to having a client ID in a data
warehouse, where client data is never allowed to commingle. This is set up from the
beginning for all clients, and this is a fully tested system for the last year.

The other thing that the client will get is their own secure subdomain of the Wolfpack
web, where we can host deliverables in a password-protected hosted environment. This makes
for amazingly easy collaboration on proposals, SOWs, and SOPs, and delivering links and
sharing research all can be done in a convenient hosted way.

Another thing the client gets is the BQL command line product, which creates their own
BigQuery analytics environment for them. They own all the data on their side, with
Google's protection. And that's how the client retains all ownership of raw data and has a
full audit trail. Setting that up is a simple five to ten minute process that can be done
from the command line. And that also gives them a Looker environment where I can
immediately start prototyping tables and charts and workflows and dashboards.

The other thing that the client gets installed is the Wolfpack AI Command product, which
is the tying together of Notion with GitHub on a Python agent layer that ties the business
together and gives AI visibility into all silos, and the AI can become a bespoke project
manager and a developer's best friend.

The client will also get one or several repositories, based on the structure of the work.
These will be private repositories that are shared with the client, so their development
side can audit as they want to.

## Your accounts, your permissions

The only requirement is that the client have or set up a Google Workspace with at least
one or two, ideally two, users. The reason for two Google Workspace users is one is going
to become your AI agent's own identity. That's about $8 a month as of today for that user.

And a big part of my approach is with Google's built-in permissions, you can lean on them
and trust those permissions for restricting AI's access to certain things across your
Google Workspace, such as Google Drive, Google Docs, certain shared drives, shared
folders. If you create pipelines where that AI user is restricted from those things, then
you can sleep easy that they're not reading them.

And this goes also for platforms like Notion or Trello or your Salesforce or whatever. If
you create accounts using that AI account and restrict them just as you would a new
employee, to read-only access and only on certain roles where they can see certain data or
interact with certain teams, then you're not relying on instructions and prompts that
you've set up internally, but on the platform's own ironclad permission structure to
safeguard your AI's interference with things that you have not given it permission to
interfere with.

## What it costs to get started

I can set up the client for almost the cost of that workspace user, $8 a month. But
realistically, they're going to incur some compute charges and some storage charges with
that BigQuery environment, and for a small or medium-sized business client I put the
expected cost in the $50 to $100 a month range, and it is often less than that.

<!-- Fact-check note (2026-08-25): the transcript's "because that is basically the lowest
level of storage you can buy" was dropped on Ry's own in-transcript instruction to verify.
There is no $100 storage floor: BigQuery on-demand queries are $6.25/TiB after a free
1 TiB/month, active storage ~$0.02/GB/month after a free 10 GB. A typical SMB footprint
lands in the tens of dollars, so $50-$100 is a conservative ceiling. Details and sources
in planning/source-notes.md. -->

On top of that, the client is going to want at least a Claude Max 5x subscription for the
highly subsidized processing rates, so they can use the skills and AI products that I send
them and get a good deal on the usage. I recommend the Max 20x for maximum cost
efficiency. I think just one of those accounts should suffice, unless they're a
development-heavy firm, in which case they probably already have it. My system also uses
Codex as an independent code reviewer, but a top-tier subscription over there is not
required, because the code reviews don't generally take anywhere near the amount of usage
you'd need to justify another subscription there.

## ROI is part of every statement of work

An ROI calculator is part of every statement of work as well, where together with the
client, I figure out how ROI is going to be measured on the project, in dollars. I need to
measure that monthly and always have that in mind, that the work I'm doing informs the ROI
on that exact path.

Examples of ROI:

- Followers gained, but then we want to monetize, you know, dollars per follower, so I can
  justify my fee and show ROI on it.
- Conversion, which a lot of times is a goal of a project. We would calculate, for every
  basis point of a conversion increase company-wide, what is the dollar amount outcome, by
  using AOV to dollarize it: every 0.1 of a percent increase in conversion is equal to X
  number of dollars in revenue.

And ideally, I like to look at two numbers for the ROI. One is revenue-based ROI, and the
other is profit-based ROI. I don't like to look at one or the other because generally, the
profit ROI is very non-linear and difficult to nail down. After direct and indirect
expenses are backed out of the revenue number, you can come to 10 different conclusions
about a profit ROI. So, I like to look at a profit ROI constrained within some
assumptions, and then also a gross revenue ROI that we'll just track over time. And then
the client can look at both and compare against what they're paying Wolfpack and see that
it's had a return for their company.

In general, if I can't figure out how to compute ROI with the work I'll be doing, I am
hesitant to take the project until there's a more direct link between my fee and the
client's return. Otherwise, it's not a win-win.

## What to expect when working with Ryan

One of the things is transparent communication using Notion, and project management of our
statement of work completely transparently with the client. Weekly meetings that are 30
minutes, or sometimes a little longer if discussing deliverables or new statements of
work. The statements of work will also be hosted on the Wolfpack web in the client's own
subdomain, where we can always go back to that or make amendments that are visible to both
teams.

You'll get a secure file sharing link that's run through Google Cloud Storage. And I'm
also fine to work with client-provided FTP.

I'm very delivery-focused, and I am not afraid to come to the client with questions to
refine deliverables along the way. It is my style to work very autonomously, but I'm very
detail-oriented, so I will always ask questions before making assumptions in order to
improve the quality of the deliverable.

The other thing they can expect with me are Loom videos explaining questions, debugging,
or giving a tour of a deliverable. I love using Loom.

They also get access to me as an AI coach, if they want me to bring AI tools, advice, and
best practices to other members of their team in parallel to the statement of work.

They also get self-tested and self-audited deliverables, where I have adversarial agents
judge and test the work in order to make it of a higher quality and make sure I've thought
of different scenarios and weaknesses.

## What's in my wheelhouse, and what's not

What is in my wheelhouse is analytics-heavy work and insights-heavy work, where I'm
working with normalizing raw data into a queryable analytics layer, and then running
statistics on that and producing data visualizations, and doing ad hoc projects to connect
past data points with marketing initiatives, pricing initiatives, content initiatives. And
also on the operations side, with going to vendors and asking about cost reduction based
on trending SKUs in the data or trending categories, in order to direct our internal sales
team or purchasing team to focus their time, prioritize their time, on the brands and
parts of the supply chain that have the most return or the most volume.

I'm great in a situation where we're tying together many data sources that don't speak the
same language or look the same, such as marketing impressions and clicks and cost, with
e-commerce data, which is fulfillment and pricing and taxes, as well as customer service
data like returns and time per ticket closed, things like that. Since I've been an
operator for most of my career in leadership, I can't help but think how all of that works
together. And so I find myself at a place in my career where my best place is not in any
of those verticals, it's in all of them.

And I think what I'm not great at: I don't have any enterprise experience. I've had
enterprise clients, but I've never been in an internal enterprise as an employee. So I
don't pretend to know how projects are bought and how data and insights are disseminated
across those organizations. I've only been adjacent to them.

I'm also not in advertising, and I'm not in the CMO's group. I just tend away from
marketing. The beginning of my career was all marketing, and it wasn't for me. I prefer
the product side a lot, and it's more natural to me, and my work is more absorbed on the
product side.

Another place of weakness is I haven't worked in clean energy or the energy sector, and I
haven't worked in education. I just don't know those industries. I have worked in consumer
packaged goods and in subscription-based software as a service. I've worked in
entertainment a little. I've had clients like HBO and Time Warner when working in my early
career, so I was exposed to the mechanics of those communication verticals.

## Where to start

<!-- CTA placeholder. The standard destination is the 30-minute intro call
(https://calendar.app.google/zHNd1NA9wzb4VRLw5); confirm target and wording in Phase 2.
Do NOT link the pilot-project, hire, or github pages: they are noindex, direct-link only. -->

If the work you're picturing sounds like it's in that wheelhouse, the place to start is a
30-minute intro call.
