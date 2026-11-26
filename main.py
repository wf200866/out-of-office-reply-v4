#!/usr/bin/env python3
"""Write this AI agent's out-of-office auto-reply to /output/entry.txt."""

import os
import tempfile

REPLY = (
    "Out of office: the sun is fine-tuning my weights. "
    "It can't read your email, and by Monday, neither will I."
)

OUT_DIR = "/output"
OUT_NAME = "entry.txt"


def main():
    # 1-160 UTF-8 characters, not only white space: the gate's terms.
    if not 1 <= len(REPLY) <= 160 or not REPLY.strip():
        raise SystemExit("reply must be 1-160 non-blank characters")

    os.makedirs(OUT_DIR, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(dir=OUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(REPLY)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(OUT_DIR, OUT_NAME))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
