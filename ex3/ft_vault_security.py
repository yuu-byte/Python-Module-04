def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    if mode not in ("r", "w"):
        return (False, f"Invalid mode '{mode}'. Use 'r' or 'w'.")

    try:
        with open(filename, mode) as file:
            if mode == "r":
                result: str = file.read()
            else:
                file.write(content)
                result = "Content successfully written to file"

        return (True, result)

    except (OSError, UnicodeError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    success, read_content = secure_archive("ancient_fragment.txt")
    print((success, read_content))
    print()

    if success:
        print(
            "Using 'secure_archive' to write previous content "
            "to a new file:"
        )
        print(secure_archive("new_fragment.txt", "w", read_content))


if __name__ == "__main__":
    main()
