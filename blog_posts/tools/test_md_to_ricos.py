#!/usr/bin/env python3
"""Tests for the markdown-to-Ricos converter.

Stdlib unittest, no dependencies::

    python -m unittest discover blog_posts/tools
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from md_to_ricos import (
    PostError,
    build_payload,
    markdown_to_nodes,
    parse_front_matter,
    parse_inline,
    reset_ids,
    slugify,
    space_blocks,
)

MEMBER = "e00ee638-af7f-4aac-aa2b-c99d795ecf78"


def text_of(nodes):
    """Flatten the visible text out of a node tree."""
    out = []
    for node in nodes:
        if node["type"] == "TEXT":
            out.append(node["textData"]["text"])
        out.extend(text_of(node.get("nodes", [])))
    return "".join(out)


def decorations_for(nodes, needle):
    for node in nodes:
        if node["type"] == "TEXT" and needle in node["textData"]["text"]:
            return {d["type"] for d in node["textData"]["decorations"]}
        found = decorations_for(node.get("nodes", []), needle)
        if found is not None:
            return found
    return None


class FrontMatterTests(unittest.TestCase):
    def test_parses_scalars_lists_and_body(self):
        meta, body = parse_front_matter(
            "---\n"
            "title: Hello World\n"
            "slug: hello-world\n"
            "tags: [ai, smb]\n"
            "featured: true\n"
            "---\n"
            "Body text.\n"
        )
        self.assertEqual(meta["title"], "Hello World")
        self.assertEqual(meta["slug"], "hello-world")
        self.assertEqual(meta["tags"], ["ai", "smb"])
        self.assertIs(meta["featured"], True)
        self.assertIn("Body text.", body)

    def test_parses_block_lists(self):
        meta, _ = parse_front_matter(
            "---\ntitle: T\ntags:\n  - one\n  - two\n---\nbody\n"
        )
        self.assertEqual(meta["tags"], ["one", "two"])

    def test_strips_quotes(self):
        meta, _ = parse_front_matter('---\ntitle: "A: colon title"\n---\nbody\n')
        self.assertEqual(meta["title"], "A: colon title")

    def test_rejects_missing_block(self):
        with self.assertRaises(PostError):
            parse_front_matter("title: no fence\n")

    def test_rejects_unclosed_block(self):
        with self.assertRaises(PostError):
            parse_front_matter("---\ntitle: T\nbody\n")

    def test_rejects_unknown_key(self):
        with self.assertRaises(PostError) as ctx:
            parse_front_matter("---\ntitle: T\nauthor: Ry\n---\nbody\n")
        self.assertIn("author", str(ctx.exception))

    def test_rejects_missing_title(self):
        with self.assertRaises(PostError):
            parse_front_matter("---\nslug: s\n---\nbody\n")

    def test_rejects_empty_title(self):
        with self.assertRaises(PostError):
            parse_front_matter('---\ntitle: ""\n---\nbody\n')


class InlineTests(unittest.TestCase):
    def test_bold_and_italic(self):
        nodes = parse_inline("plain **bold** and *italic* end")
        self.assertEqual(text_of(nodes), "plain bold and italic end")
        self.assertEqual(decorations_for(nodes, "bold"), {"BOLD"})
        self.assertEqual(decorations_for(nodes, "italic"), {"ITALIC"})

    def test_nested_bold_italic(self):
        nodes = parse_inline("**bold *both* bold**")
        self.assertEqual(decorations_for(nodes, "both"), {"BOLD", "ITALIC"})

    def test_strikethrough(self):
        nodes = parse_inline("~~gone~~")
        self.assertEqual(decorations_for(nodes, "gone"), {"STRIKETHROUGH"})

    def test_inline_code_is_literal_and_undecorated(self):
        # Wix strips FONT_FAMILY on save, so inline code carries no decoration.
        # What must hold is that its contents stay verbatim.
        nodes = parse_inline("use `a **b** c` here")
        self.assertEqual(text_of(nodes), "use a **b** c here")
        self.assertEqual(decorations_for(nodes, "a **b** c"), set())

    def test_link(self):
        nodes = parse_inline("see [the rates](https://example.com/r) now")
        self.assertEqual(text_of(nodes), "see the rates now")
        decorations = decorations_for(nodes, "the rates")
        self.assertIn("LINK", decorations)
        link = next(
            d for n in nodes if n["type"] == "TEXT"
            for d in n["textData"]["decorations"] if d["type"] == "LINK"
        )
        self.assertEqual(link["linkData"]["link"]["url"], "https://example.com/r")

    def test_link_label_keeps_its_own_decorations(self):
        nodes = parse_inline("[**bold link**](https://example.com)")
        self.assertEqual(decorations_for(nodes, "bold link"), {"BOLD", "LINK"})

    def test_snake_case_underscore_is_literal(self):
        nodes = parse_inline("call verify_facts_now please")
        self.assertEqual(text_of(nodes), "call verify_facts_now please")
        # One undecorated run -- the underscores never opened an emphasis span.
        self.assertEqual(len(nodes), 1)
        self.assertEqual(decorations_for(nodes, "facts"), set())

    def test_escapes(self):
        nodes = parse_inline(r"literal \*not italic\* here")
        self.assertEqual(text_of(nodes), "literal *not italic* here")


class BlockTests(unittest.TestCase):
    def setUp(self):
        reset_ids()

    def test_headings(self):
        nodes = markdown_to_nodes("# One\n\n### Three\n")
        self.assertEqual([n["type"] for n in nodes], ["HEADING", "HEADING"])
        self.assertEqual(nodes[0]["headingData"]["level"], 1)
        self.assertEqual(nodes[1]["headingData"]["level"], 3)

    def test_paragraph_joins_wrapped_lines(self):
        nodes = markdown_to_nodes("one line\ncontinues here\n\nsecond para\n")
        self.assertEqual([n["type"] for n in nodes], ["PARAGRAPH", "PARAGRAPH"])
        self.assertEqual(text_of(nodes[0]["nodes"]), "one line continues here")

    def test_paragraph_breaks_at_next_block(self):
        nodes = markdown_to_nodes("some text\n# Heading\n")
        self.assertEqual([n["type"] for n in nodes], ["PARAGRAPH", "HEADING"])

    def test_bulleted_list(self):
        nodes = markdown_to_nodes("- alpha\n- beta\n")
        self.assertEqual(nodes[0]["type"], "BULLETED_LIST")
        self.assertEqual(len(nodes[0]["nodes"]), 2)
        self.assertEqual(nodes[0]["nodes"][0]["type"], "LIST_ITEM")
        self.assertEqual(text_of(nodes[0]["nodes"]), "alphabeta")

    def test_ordered_list(self):
        nodes = markdown_to_nodes("1. first\n2. second\n")
        self.assertEqual(nodes[0]["type"], "ORDERED_LIST")
        self.assertIn("orderedListData", nodes[0])
        self.assertEqual(len(nodes[0]["nodes"]), 2)

    def test_blockquote(self):
        nodes = markdown_to_nodes("> quoted line\n> and more\n")
        self.assertEqual(nodes[0]["type"], "BLOCKQUOTE")
        self.assertEqual(text_of(nodes[0]["nodes"]), "quoted line and more")

    def test_code_block_is_verbatim(self):
        nodes = markdown_to_nodes("```python\nx = **1**\n# not a heading\n```\n")
        self.assertEqual(nodes[0]["type"], "CODE_BLOCK")
        self.assertEqual(text_of(nodes[0]["nodes"]), "x = **1**\n# not a heading")

    def test_divider(self):
        nodes = markdown_to_nodes("above\n\n---\n\nbelow\n")
        self.assertEqual([n["type"] for n in nodes], ["PARAGRAPH", "DIVIDER", "PARAGRAPH"])

    def test_image_collects_and_resolves(self):
        images = []
        nodes = markdown_to_nodes("![a cat](cat.png)\n", {"cat.png": "wix123"}, images)
        self.assertEqual(nodes[0]["type"], "IMAGE")
        self.assertEqual(nodes[0]["imageData"]["image"]["src"]["id"], "wix123")
        self.assertEqual(nodes[0]["imageData"]["altText"], "a cat")
        self.assertEqual(images, ["cat.png"])

    def test_image_without_alt_is_decorative(self):
        nodes = markdown_to_nodes("![](x.png)\n", {"x.png": "id"}, [])
        self.assertTrue(nodes[0]["imageData"]["decorative"])

    def test_image_missing_from_media_map_raises(self):
        with self.assertRaises(PostError):
            markdown_to_nodes("![a](missing.png)\n", {"other.png": "id"}, [])

    def test_html_comments_are_stripped(self):
        nodes = markdown_to_nodes("before\n\n<!-- a note\nspanning lines -->\n\nafter\n")
        self.assertEqual([n["type"] for n in nodes], ["PARAGRAPH", "PARAGRAPH"])
        self.assertEqual(text_of(nodes[0]["nodes"]), "before")
        self.assertEqual(text_of(nodes[1]["nodes"]), "after")

    def test_ids_are_deterministic(self):
        reset_ids()
        first = markdown_to_nodes("# H\n\npara\n\n- item\n")
        reset_ids()
        second = markdown_to_nodes("# H\n\npara\n\n- item\n")
        self.assertEqual(json.dumps(first), json.dumps(second))


class SlugTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello, World! Part 2"), "hello-world-part-2")
        self.assertEqual(slugify("Café Déjà Vu"), "cafe-deja-vu")
        self.assertEqual(slugify("!!!"), "post")


class PayloadTests(unittest.TestCase):
    def _post(self, md: str, files=()):
        tmp = Path(tempfile.mkdtemp())
        (tmp / "post.md").write_text(md, encoding="utf-8")
        for name in files:
            (tmp / name).write_bytes(b"\x89PNG\r\n")
        return tmp

    def test_builds_full_payload(self):
        post = self._post(
            "---\n"
            "title: The Model Is Your Beacon\n"
            "excerpt: Why the model comes first.\n"
            "cover: cover.png\n"
            "cover_alt: A beacon\n"
            "tags: [finance, smb]\n"
            "---\n"
            "## Opening\n\nSome **strong** copy.\n",
            files=["cover.png"],
        )
        payload, images, tags = build_payload(
            post, MEMBER, {"cover.png": "wixcover"},
            {"finance": "tag-fin", "smb": "tag-smb"},
        )
        draft = payload["draftPost"]
        self.assertEqual(draft["title"], "The Model Is Your Beacon")
        self.assertEqual(draft["memberId"], MEMBER)
        self.assertEqual(draft["excerpt"], "Why the model comes first.")
        self.assertEqual(draft["tagIds"], ["tag-fin", "tag-smb"])
        self.assertNotIn("hashtags", draft)
        self.assertEqual(draft["seoSlug"], "the-model-is-your-beacon")
        self.assertEqual(draft["media"]["wixMedia"]["image"]["id"], "wixcover")
        self.assertEqual(draft["media"]["altText"], "A beacon")
        self.assertIs(payload["publish"], False)
        self.assertEqual(images, ["cover.png"])
        self.assertEqual(tags, ["finance", "smb"])

    def test_tags_without_a_map_are_listed_not_sent(self):
        post = self._post("---\ntitle: T\ntags: [alpha, beta]\n---\nbody\n")
        payload, _, tags = build_payload(post, MEMBER)
        self.assertNotIn("tagIds", payload["draftPost"])
        self.assertEqual(tags, ["alpha", "beta"])

    def test_tag_missing_from_map_raises(self):
        post = self._post("---\ntitle: T\ntags: [alpha, beta]\n---\nbody\n")
        with self.assertRaises(PostError) as ctx:
            build_payload(post, MEMBER, tag_map={"alpha": "id-a"})
        self.assertIn("beta", str(ctx.exception))

    def test_explicit_slug_wins(self):
        post = self._post("---\ntitle: A Long Title\nslug: short\n---\nbody\n")
        payload, _, _ = build_payload(post, MEMBER)
        self.assertEqual(payload["draftPost"]["seoSlug"], "short")

    def test_publish_flag(self):
        post = self._post("---\ntitle: T\n---\nbody\n")
        payload, _, _ = build_payload(post, MEMBER, publish=True)
        self.assertIs(payload["publish"], True)

    def test_missing_cover_file_raises(self):
        post = self._post("---\ntitle: T\ncover: nope.png\n---\nbody\n")
        with self.assertRaises(PostError) as ctx:
            build_payload(post, MEMBER)
        self.assertIn("nope.png", str(ctx.exception))

    def test_empty_body_raises(self):
        post = self._post("---\ntitle: T\n---\n\n")
        with self.assertRaises(PostError):
            build_payload(post, MEMBER)

    def test_missing_post_md_raises(self):
        with self.assertRaises(PostError):
            build_payload(Path(tempfile.mkdtemp()), MEMBER)

    def test_oversize_post_raises(self):
        post = self._post("---\ntitle: T\n---\n" + ("word " * 120000))
        with self.assertRaises(PostError) as ctx:
            build_payload(post, MEMBER)
        self.assertIn("409,600", str(ctx.exception))


class SpacingTests(unittest.TestCase):
    """Wix renders butted-together PARAGRAPH nodes with no gap. See space_blocks."""

    def setUp(self):
        reset_ids()

    def _post(self, text, files=()):
        d = Path(tempfile.mkdtemp())
        (d / "post.md").write_text(text, encoding="utf-8")
        for name in files:
            (d / name).write_bytes(b"x")
        return d

    def test_spacer_between_every_pair(self):
        nodes = space_blocks(markdown_to_nodes("one\n\ntwo\n\nthree\n"))
        self.assertEqual(
            [n["type"] for n in nodes],
            ["PARAGRAPH"] * 5,
        )
        self.assertEqual([bool(n["nodes"]) for n in nodes],
                         [True, False, True, False, True])

    def test_spacer_is_an_empty_paragraph(self):
        nodes = space_blocks(markdown_to_nodes("one\n\ntwo\n"))
        self.assertEqual(nodes[1]["type"], "PARAGRAPH")
        self.assertEqual(nodes[1]["nodes"], [])
        self.assertEqual(nodes[1]["paragraphData"], {})

    def test_no_leading_or_trailing_spacer(self):
        nodes = space_blocks(markdown_to_nodes("only\n"))
        self.assertEqual(len(nodes), 1)
        self.assertTrue(nodes[0]["nodes"])

    def test_spacing_separates_mixed_blocks(self):
        nodes = space_blocks(markdown_to_nodes("# H\n\npara\n\n- item\n"))
        self.assertEqual(
            [n["type"] for n in nodes],
            ["HEADING", "PARAGRAPH", "PARAGRAPH", "PARAGRAPH", "BULLETED_LIST"],
        )

    def test_empty_input_stays_empty(self):
        self.assertEqual(space_blocks([]), [])

    def test_build_payload_applies_spacing(self):
        post = self._post("---\ntitle: T\n---\nfirst\n\nsecond\n")
        payload, _, _ = build_payload(post, MEMBER)
        nodes = payload["draftPost"]["richContent"]["nodes"]
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1]["nodes"], [])

    def test_spacing_is_deterministic(self):
        post = self._post("---\ntitle: T\n---\nfirst\n\nsecond\n\nthird\n")
        a, _, _ = build_payload(post, MEMBER)
        b, _, _ = build_payload(post, MEMBER)
        self.assertEqual(json.dumps(a), json.dumps(b))


class TemplateTests(unittest.TestCase):
    """The shipped template is the first thing anyone runs. Keep it working."""

    def test_template_converts(self):
        template = Path(__file__).resolve().parent.parent / "_template"
        payload, images, tags = build_payload(template, MEMBER)
        nodes = payload["draftPost"]["richContent"]["nodes"]
        types = {n["type"] for n in nodes}
        # The template demonstrates every block the converter supports.
        self.assertTrue(
            {"HEADING", "PARAGRAPH", "BULLETED_LIST", "ORDERED_LIST",
             "BLOCKQUOTE", "IMAGE", "DIVIDER"} <= types,
            f"template stopped exercising every block type; got {sorted(types)}",
        )
        self.assertIn("cover.png", images)
        self.assertEqual(tags, ["ai", "smb"])
        # The trailing author-notes comment must not leak into the post.
        self.assertNotIn("Reminders, per CLAUDE.md", json.dumps(payload))


if __name__ == "__main__":
    unittest.main()
