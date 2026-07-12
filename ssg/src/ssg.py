import sys

from ssg.src.config import CONTENT, DEST_DIR, STATIC_DIR, TEMPLATE
from ssg.src.copy_static import generate_public_directory
from ssg.src.generators import generate_pages_recursively


def ssg():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    generate_public_directory(STATIC_DIR, DEST_DIR)
    generate_pages_recursively(CONTENT, TEMPLATE, DEST_DIR, basepath)
