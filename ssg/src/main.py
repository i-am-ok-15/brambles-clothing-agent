import sys

from config import CONTENT, DEST_DIR, STATIC_DIR, TEMPLATE
from copy_static import generate_public_directory
from generators import generate_pages_recursively


def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    generate_public_directory(STATIC_DIR, DEST_DIR)
    generate_pages_recursively(CONTENT, TEMPLATE, DEST_DIR, basepath)


main()
