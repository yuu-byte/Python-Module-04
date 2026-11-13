import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    try:
        content: str = file.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{filename}': {e}")
        return
    finally:
        file.close()

    print("---\n")
    print(content)
    print("---")
    print(f"File '{filename}' closed.")
    print()

    new_content: str = content.replace("\n", "#\n")
    if content and not content.endswith("\n"):
        new_content += "#"

    print("Transform data:")
    print("---\n")
    print(new_content)
    print("---")

    output_filename: str = input("Enter new file name (or empty): ")
    if output_filename:
        print(f"Saving data to '{output_filename}'")

        try:
            output_file: typing.IO[str] = open(output_filename, "w")
        except OSError as e:
            print(f"Error opening file '{output_filename}': {e}")
            return

        try:
            output_file.write(new_content)
        except (OSError, UnicodeEncodeError) as e:
            print(f"Error writing file '{output_filename}': {e}")
            return
        finally:
            output_file.close()

        print(f"Data saved in file '{output_filename}'.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
