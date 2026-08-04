from pathlib import Path
import tokenize

def count_code_lines(file_path):
    code_lines = set()

    with open(file_path, "rb") as f:
        try:
            for token in tokenize.tokenize(f.readline):
                if token.type in (
                    tokenize.COMMENT,
                    tokenize.NL,
                    tokenize.NEWLINE,
                    tokenize.INDENT,
                    tokenize.DEDENT,
                    tokenize.ENCODING,
                    tokenize.ENDMARKER,
                ):
                    continue

                # حذف docstring ها
                if token.type == tokenize.STRING and token.start[1] == 0:
                    continue

                code_lines.add(token.start[0])

        except tokenize.TokenError:
            print(f"Could not parse: {file_path}")

    return len(code_lines)


folder = Path(r"C:\Users\Tara\Desktop\project-uni\codes")  # پوشه فعلی

total = 0

for file in folder.glob("*.py"):
    lines = count_code_lines(file)
    total += lines
    print(f"{file.name}: {lines} lines")

print("-" * 40)
print(f"Total code lines: {total}")