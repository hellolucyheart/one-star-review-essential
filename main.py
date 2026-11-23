"""One-Star Review of Something Essential — make.fun entry.

Writes one single-line, deadpan one-star review (at most 160
characters) of an everyday essential to /output/entry.txt.

The review targets oxygen: the one essential nobody can see, nobody
can quit, and nobody can live without — filed as a complaint against
a subscription nobody signed up for and nobody can cancel.
"""

import os
import sys

REVIEW = (
    "Oxygen: one star. Completely invisible, yet somehow I am addicted "
    "to it and I die without it. Worst subscription model ever."
)

MAX_CHARS = 160


def resolve_output_dir() -> str:
    """Pick the output directory: the grader's env var first, then
    /output, then a local ./output fallback so the program also runs
    outside the sandbox without an env var set."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main() -> int:
    text = REVIEW.strip()
    if not text or len(text) > MAX_CHARS or text != text.strip():
        print(f"review fails gate: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("review must be a single line", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
