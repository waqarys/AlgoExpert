"""Turn terse notes into speakable sentences."""
import re
def clean(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t); t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", t)
    return t.strip()
def sentences(t):
    t = t.replace("...", "…")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", t) if s.strip()]
SUBS = [(r"(?<=\w)/(day|s|sec|second|month|year|user|hour|min)\b", r" per \1"), (r"\.\.\.|…", " "),(r"\s*(->|→|=>)\s*", " to "), (r"<->|↔", " and "), (r"~\s*", "about "), (r"≈", " about "), (r"(\d)\s*x\s*(\d)", r"\1 times \2"),
        (r"\be\.g\.", "for example"), (r"\bi\.e\.", "that is"), (r"\bvs\.?\b", "versus"), (r"\betc\.", "and so on"),
        (r"\bw/", "with "), (r"&", " and "), (r"\+", " plus "), (r"(?<=\w)/(?=\w)", " or "), (r"\bQPS\b", "Q P S"),
        (r"<", " under "), (r">", " over "), (r"\s*=\s*", " equals "), (r"%", " percent"), (r"\bp99\b", "p 99"),
        (r"[{}\[\]|#*_`]", " "), (r"\s+", " ")]
def speak(t):
    t = clean(t)
    for a, b in SUBS: t = re.sub(a, b, t)
    return t.strip()
