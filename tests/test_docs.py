"""Documentation consistency tests. Reads live repo files; excludes .trash/.
Registered in docs/tests/TEST-001-doc-consistency.md.
Run: python3 -m pytest tests/test_docs.py   (or import and call each test_* fn)

The repo has two legitimate line-1 conventions:
  - CONTENT docs (docs/{decisions,specs,plans,philosophy,research,sessions,tests}/*.md,
    excluding READMEs and *-000-template.md): line 1 = <!-- keywords: ... -->, line 2 = bare filename.
  - SKELETON / top-level files (AGENTS.md, ROADMAP.md, READMEs, memory files, rules):
    line 1 = '# Title', line 2 = '<!-- soft: N hard: M -->'. Not checked for the keywords header.
These tests guard the CONTENT convention and the global no-legacy-token invariants."""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _md_files():
    out = []
    for dp, dn, fns in os.walk(ROOT):
        if ".trash" in dp.split(os.sep):
            continue
        dn[:] = [d for d in dn if d != ".trash" and not d.startswith(".git")]
        for fn in fns:
            if fn.endswith(".md"):
                out.append(os.path.join(dp, fn))
    return out

def _content_docs():
    """Numbered/dated content documents that must carry the keywords-comment header.
    Excludes READMEs (skeleton) and *-000-template.md (templates render their own placeholder)."""
    out = []
    for sub in ("decisions", "specs", "plans", "philosophy", "research", "sessions", "tests"):
        for p in glob.glob(os.path.join(ROOT, "docs", sub, "*.md")):
            base = os.path.basename(p)
            if base == "README.md" or base.endswith("-000-template.md"):
                continue
            out.append(p)
    return sorted(out)

def _strip_code_blocks(text):
    """Remove fenced code blocks and inline-backtick spans so doc-type refs inside
    examples are not mistaken for live references."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]*`', '', text)
    return text

def test_no_kw_token_residual():
    """No legacy 'kw:' HEADER token survives outside .trash/.
    Only header forms count: '<!-- kw:' or a 'filename | kw:' line. Prose mentions of the
    word are allowed (a doc may discuss the migration)."""
    offenders = []
    for p in _md_files():
        with open(p, encoding="utf-8") as f:
            txt = _strip_code_blocks(f.read())
        if re.search(r'<!--\s*kw:', txt) or re.search(r'^\S+\.md\s*\|\s*kw:', txt, re.M):
            offenders.append(os.path.relpath(p, ROOT))
    assert not offenders, "legacy 'kw:' header token in: " + ", ".join(offenders)

def test_no_pipe_form_headers():
    """No 'filename | keywords' pipe-form line-1 header survives outside .trash/."""
    offenders = []
    for p in _md_files():
        with open(p, encoding="utf-8") as f:
            line1 = f.readline().rstrip("\n")
        if re.match(r'^#?\s*\S+\.md\s*\|', line1):
            offenders.append(os.path.relpath(p, ROOT))
    assert not offenders, "pipe-form header in: " + ", ".join(offenders)

def test_content_docs_line1_is_keywords_comment():
    """Every numbered/dated content doc: line 1 is <!-- keywords: ... -->, line 2 is the bare filename."""
    offenders = []
    for p in _content_docs():
        with open(p, encoding="utf-8") as f:
            lines = f.read().split("\n")
        l1 = lines[0] if lines else ""
        l2 = lines[1] if len(lines) > 1 else ""
        if not re.match(r'^<!--\s*keywords:.*-->\s*$', l1):
            offenders.append(os.path.relpath(p, ROOT) + " (line1)")
        elif l2.strip() != os.path.basename(p):
            offenders.append(os.path.relpath(p, ROOT) + " (line2=%r)" % l2.strip())
    assert not offenders, "bad content-doc header in: " + "; ".join(offenders)

def test_no_dead_doctype_references():
    """No living doc references an ADR/SPEC/PLAN/DP id (NNN >= 001) whose file is absent.
    Excluded: session logs / CHANGELOG / work-log (history); code blocks and backtick spans
    (examples); -000 template placeholders (NNN==000 never counts)."""
    existing = set()
    for typ, sub in [("ADR", "decisions"), ("SPEC", "specs"), ("PLAN", "plans"), ("DP", "philosophy")]:
        for p in glob.glob(os.path.join(ROOT, "docs", sub, "%s-*.md" % typ)):
            m = re.match(r'(%s-\d+)' % typ, os.path.basename(p))
            if m:
                existing.add(m.group(1))
    pat = re.compile(r'\b((?:ADR|SPEC|PLAN|DP)-(\d+))')
    exempt_files = ("CHANGELOG.md", "work-log.md")
    offenders = []
    for p in _md_files():
        rel = os.path.relpath(p, ROOT)
        if rel.startswith(os.path.join("docs", "sessions")) or os.path.basename(p) in exempt_files:
            continue
        with open(p, encoding="utf-8") as f:
            txt = _strip_code_blocks(f.read())
        for ref, num in pat.findall(txt):
            if num == "000":
                continue
            if ref not in existing:
                offenders.append("%s -> %s" % (rel, ref))
    assert not offenders, "dead doc-type references: " + "; ".join(sorted(set(offenders)))
