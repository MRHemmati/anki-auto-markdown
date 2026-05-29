import sys
import os
from anki import version as anki_version

# Modern Anki uses YY.MM.Patch versioning (e.g. "25.09.4")
# Older Anki used "2.1.x" format
# Parse the major version number to detect Anki era
_version_parts = anki_version.split(".")
_major = int(_version_parts[0])

# Anki 2.1+ or any modern version (23+, 24+, 25+, etc.) — all Python 3
anki21 = _major >= 2
sys_encoding = sys.getfilesystemencoding()

# Always use str paths in Python 3 (no .decode() needed)
addon_path = os.path.dirname(__file__)
