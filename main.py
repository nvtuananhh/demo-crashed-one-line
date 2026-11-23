from pathlib import Path

JOKE = "My coding agent's demo crashed exactly once \u2014 on the one line it let me write."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
