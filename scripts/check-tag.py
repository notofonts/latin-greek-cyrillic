import os
import sys
from fontv.libfv import FontVersion
from fontTools.ttLib import TTFont
from glob import glob
import yaml


tag = sys.argv[1]
try:
	family, version = tag.split("-v", 2)
except Exception as e:
	print(f"::notice file=scripts/checktag.py::Tag '{tag}' had unknown format")
	print("::set-output name=result::skip")
	sys.exit(0)

if not os.path.exists("fonts/" + family):
	print(f"::error file=scripts/checktag.py::Family '{family}' did not exist")
	sys.exit(1)

a_font = glob(f"fonts/{family}/*/*/*Regular.ttf") + glob(f"fonts/{family}/*/*/*VF.ttf")
if not a_font:
	print(f"::error file=scripts/checktag.py::No regular fonts found for family '{family}'")
	sys.exit(1)


ttf_version = FontVersion(a_font[0]).version
real_family_names = [ TTFont(x)["name"].getDebugName(1) for x in a_font ]

# Identify the config file which created this
found_config = None
for config in glob("sources/*yaml"):
	this_config = yaml.load(open(config), Loader=yaml.FullLoader)
	if "familyName" in this_config and this_config["familyName"] in real_family_names:
		found_config = config
		break
if not found_config:
	print(f"::error file=scripts/checktag.py::Could not identify config file for {family} (found a font of family {real_family_names})")
	sys.exit(1)

if "Version "+version != ttf_version:
	print(f"::error file=scripts/checktag.py::Trying to create release for version {version}, found font version {ttf_version}")
	sys.exit(1)

print("::set-output name=result::pass")
print(f"::set-output name=family::{family}")
print(f"::set-output name=config_file::{found_config}")
sys.exit(0)
