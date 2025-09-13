import os
import subprocess


def main():
    docs_dir = os.path.join(os.path.dirname(__file__), "../docs")
    build_dir = os.path.join(docs_dir, "_build/html")
    subprocess.run(["sphinx-build", "-b", "html", docs_dir, build_dir])
    print(f"Documentation built at {build_dir}")


if __name__ == "__main__":
    main()
