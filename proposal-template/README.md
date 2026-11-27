# Wolfpack proposal page template

A client-neutral, single-page proposal you fill in and read top to bottom. It uses the
Wolfpack design system (navy and coral, Roboto headings, Montserrat body) and is fully
self-contained: local fonts, one local image, no scripts, and nothing loaded from another
host.

The template holds **no client content**. A filled-in proposal is client material and is
**never committed to this repository** (wp-website, which is public). Copy the whole folder
into the client's private workspace **first**, and fill it in only there.

The template is never deployed from this repository, so the site's OG-card / social-preview
rule does not apply to it. It deliberately carries `<meta name="robots" content="noindex,
nofollow">` and **no** Open Graph or Twitter card tags: a proposal has no business in a
search index or in a preview card in somebody else's feed. Keep it that way in every copy.

## Files

| File | What it is |
|---|---|
| `index.html` | The page: every section, with placeholders |
| `css/proposal.css` | The design system: tokens, components, the coral ration |
| `css/fonts.css` | `@font-face` rules for the local font files |
| `fonts/*.woff2` | Montserrat 400/500/600 and Roboto 700, subset by script |
| `fonts/Montserrat-OFL.txt`, `fonts/Roboto-OFL.txt` | SIL Open Font License 1.1 for each family. Keep them with the font files whenever the fonts are copied or redistributed |
| `img/wolfpack-logo.png` | Wolfpack logo: favicon, nav mark, hero watermark |

## Placeholders

There are two kinds:

- **`{{TOKEN}}`**: a single value, sometimes used more than once. Listed below.
- **`[Bracketed instruction]`**: prose to write in place, such as "[One sentence: the outcome
  the client gets]". Replace the brackets along with the text inside them. Table cells such
  as `[N]` and `[$0]` work the same way.

| Token | Meaning |
|---|---|
| `{{PROPOSAL_TITLE}}` | Short page title, used in `<title>`. **Never the client's name** |
| `{{CLIENT_DISPLAY_NAME}}` | Who the proposal is addressed to, in the hero kicker only (page body) |
| `{{DRAFT_NUMBER}}` | Draft number shown in the hero kicker, such as `1` |
| `{{HERO_HEADLINE}}` | The hero `<h1>`: one sentence naming the outcome |
| `{{PREPARED_DATE}}` | Month and year the proposal was prepared |
| `{{ENGAGEMENT_NAME}}` | Name of the proposed engagement, used as the proposal section heading |
| `{{SCOPE_TOTAL}}` | One-line total for the scope table, such as "~N hours over N weeks" |
| `{{LEAD_ROW_CHIP}}` | Chip label on lifted scope rows, such as "Stage 1" |
| `{{PRICING_CAPTION}}` | Caption of the pricing ledger, such as "Estimate, first 30 days" |
| `{{STEP_1}}`, `{{STEP_2}}`, `{{STEP_3}}` | Labels for the three boxes in the placeholder figure (optional approach section). Keep each to about ten characters so it fits its box at phone width |
| `{{VIDEO_URL}}` | Link to the recorded walkthrough (optional video section) |
| `{{VIDEO_HOST}}` | Name of the video host, shown under the play button (optional video section) |
| `{{CTA_URL}}` | Booking link used by both the nav CTA and the closing CTA |
| `{{NAV_CTA_LABEL}}` | Nav button text, such as "Book a call" |
| `{{CLOSING_CTA_LABEL}}` | Closing button text, such as "Book a 30-minute call" |
| `{{CONTACT_EMAIL}}` | Footer contact address (used as link text and in the `mailto:`) |
| `{{WEBSITE_URL}}` | Footer website link |
| `{{WEBSITE_LABEL}}` | Footer website link text |

The instructions comment at the top of `index.html` (the first comment in the file, before
`<html>`) mentions `{{TOKEN}}`,
`{{`, `[bracketed instruction]` and `[` by name. Those are descriptions, not placeholders, so a
search for `{{` or `[` always hits that comment. Ignore hits there, or delete the comment once
the page is filled.

## Sections

**Core sections, always present:** hero · where things stand (`#stand`) · the proposal, what
it is and what it is not (`#proposal`) · scope table (`#scope`) · outcomes (`#outcomes`) · out
of scope (`#outside`) · terms and pricing (`#pricing`) · working together (`#working`) · next
steps CTA (`#next`) · footer.

**Optional sections.** Each is wrapped in a single-line opening marker
`<!-- OPTIONAL: <name> -->` and a closing marker `<!-- /OPTIONAL -->`. Any guidance for the
block sits in a separate comment just inside it, so it goes when the block goes:

| Section | id | Nav link? |
|---|---|---|
| Video walkthrough | `#video` | no |
| Approach (placeholder figure + teaser callout) | `#approach` | yes |
| Next phase teaser | `#next-phase` | no |
| Running costs | `#costs` | yes |

When an optional section has a nav link, the link sits in its own `OPTIONAL` block inside
the `<nav>`. **Delete both blocks together**, so every nav link still points at a section that
exists. Deleting any optional block leaves the layout intact.

**Deleting optional blocks.** By hand: delete from the `<!-- OPTIONAL: <name> -->` line
through the next `<!-- /OPTIONAL -->` line, then do the same for the matching
`<name> (nav link)` block, if there is one. With a regex (any editor with regex
find-and-replace, replacing with nothing):

- All optional blocks at once: `<!-- OPTIONAL:[^>]*-->[\s\S]*?<!-- /OPTIONAL -->`
- One section and its nav link, by name, for example the approach section:
  `<!-- OPTIONAL: approach[^>]*-->[\s\S]*?<!-- /OPTIONAL -->`
  (the name prefix also catches `approach (nav link)`)

The blocks do not nest, so the lazy match always stops at the block's own closing marker.
The instructions comment at the top of the file writes the markers with spaced dashes
(`<!- - … - ->`), so the regex never touches it. The replacement leaves a blank line where
each block was, which is harmless. After deleting, the "Every nav link resolves" check
below still applies.

Below 1000px wide the nav's in-page links are hidden on purpose, so a phone shows only the
logo and the CTA button. That is expected, not a bug.

The video section is a link only. The template ships no embed and no script. Any video host
is a third-party reference: list it in the publishing manifest, and keep iframe embeds off a
gated page. The approach figure is a neutral three-box placeholder. Replace it with your own
**inline SVG**, never an iframe or a remote image.

## Making a new proposal

1. Copy the whole folder (`index.html`, `css/`, `fonts/`, `img/`) into the client's own
   private workspace. Never fill it in inside the template repository.
2. Fill every `{{TOKEN}}` and replace every `[bracketed instruction]`.
3. Add or remove scope rows, ledger rows and list items as needed. The scope table
   (`~Hrs`, `Week`) and the pricing ledger assume hourly, week-based work. For a fixed-fee or
   milestone-priced project, rename those columns (for example `Milestone` and `Due`) and use
   one ledger row per milestone or fee. The layout does not depend on the column names.
4. Delete the optional blocks you don't use, along with their nav links (see Deleting
   optional blocks).
5. Run the pre-ship checklist.

## Pre-ship checklist

- [ ] **No leftover placeholders:** searching `index.html` for `{{` and for `[` finds nothing
      left to fill outside the instructions comment at the top (see Placeholders).
- [ ] **`noindex` present:** `<meta name="robots" content="noindex, nofollow">` is still in
      `<head>`.
- [ ] **Title has no client name:** `<title>` is seen out of context (tabs, history).
- [ ] **No social-preview tags:** no Open Graph or Twitter card meta tags.
- [ ] **No third-party references:** no CDN scripts, hosted fonts, remote images, analytics or
      embeds. Any outbound link (such as a booking or video link) is listed in the publishing
      manifest.
- [ ] **Served filenames are neutral:** no client name in any file or folder name that becomes
      a URL path.
- [ ] **Every nav link resolves** to a section id that still exists.
- [ ] **Publish only through the gated flow:** a manifest is cleared first, then the page goes
      out behind the access gate, and only after the gate has been verified. Never serve the
      page from the workspace it was built in.
