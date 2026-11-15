"""Build the claude.ai Artifact version of index.html.

The Artifact host wraps the page in its own <!doctype>/<head>/<body>, so this
keeps the page's <title>, font links and <style> and the body content, drops
the outer document tags, and adds the side-safe-area meta the host expects.

Usage: python3 scripts/build-artifact.py index.html OUT.html
"""
import re, sys

src = open(sys.argv[1], encoding="utf-8").read()
head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", src, re.S).group(1)
head = re.sub(r'\s*<meta (charset|name="viewport"|name="theme-color")[^>]*>', "", head)
title = re.search(r"<title>.*?</title>", head, re.S).group(0)
head = head.replace(title, "", 1)
out = (title + '\n<meta name="claude:viewport-fit-sides" content="cover">' + head.rstrip() + "\n" + body.strip() + "\n")
open(sys.argv[2], "w", encoding="utf-8").write(out)
print("wrote", sys.argv[2], len(out), "bytes")
