## Fontbakery report

Fontbakery version: 0.8.11a9

<details><summary><b>[4] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>


* 🔥 **FAIL** Not all fonts passed in the command line are in the same directory. This may lead to bad results as the tool will interpret all font files as belonging to a single font family. The detected directories are: ['fonts/NotoSans/googlefonts/ttf', 'fonts/NotoSans/googlefonts/variable-ttf'] [code: single-directory]
</div></details><details><summary>🔥 <b>FAIL:</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/family/bold_italic_unique_for_nameid1">com.adobe.fonts/check/family/bold_italic_unique_for_nameid1</a>)</summary><div>


* 🔥 **FAIL** Family 'Noto Sans' has 2 fonts (should be no more than 1) with the same OS/2.fsSelection bold & italic settings: Bold=False, Italic=True [code: unique-fsselection]
* 🔥 **FAIL** Family 'Noto Sans' has 2 fonts (should be no more than 1) with the same OS/2.fsSelection bold & italic settings: Bold=False, Italic=False [code: unique-fsselection]
</div></details><details><summary>🔥 <b>FAIL:</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/family/max_4_fonts_per_family_name">com.adobe.fonts/check/family/max_4_fonts_per_family_name</a>)</summary><div>


* 🔥 **FAIL** Family 'Noto Sans' has 6 fonts (should be 4 or fewer). [code: too-many]
</div></details><details><summary>⚠ <b>WARN:</b> Make sure all font files have the same version value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions">com.google.fonts/check/family/equal_font_versions</a>)</summary><div>


* ⚠ **WARN** Version info differs among font files of the same font project.
These were the version values found:
* fonts/NotoSans/googlefonts/ttf/NotoSans-Black.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-BlackItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Bold.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-BoldItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-ExtraBold.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-ExtraBoldItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-ExtraLight.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-ExtraLightItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Italic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Light.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-LightItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Medium.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-MediumItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Regular.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-SemiBold.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-SemiBoldItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/ttf/NotoSans-Thin.ttf: 2.0099945068359375
* fonts/NotoSans/googlefonts/ttf/NotoSans-ThinItalic.ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/variable-ttf/NotoSans-Italic[wdth,wght].ttf: 2.009002685546875
* fonts/NotoSans/googlefonts/variable-ttf/NotoSans[wdth,wght].ttf: 2.0099945068359375
 [code: mismatch]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aivowelsigncandrabindudeva
	* auvowelsigncandrabindudeva
	* awvowelsigncandrabindudeva
	* eshortvowelsigncandrabindudeva
	* evowelsigncandrabindudeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindu2deva
	* iivowelcandrabindu3deva
	* iivowelcandrabindudeva
	* oeopen and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni0246	Contours detected: 2	Expected: 3 

	- 74 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni1DF06 (U+1DF06): L<<201.0,539.0>--<201.0,540.0>> -> L<<201.0,540.0>--<201.0,558.0>>

	* uni20BF (U+20BF): L<<317.0,0.0>--<315.0,0.0>> -> L<<315.0,0.0>--<267.0,0.0>>

	* uni2E36 (U+2E36): L<<310.0,556.0>--<310.0,444.0>> -> L<<310.0,444.0>--<343.0,0.0>>

	* uni2E37 (U+2E37): L<<145.0,0.0>--<178.0,444.0>> -> L<<178.0,444.0>--<178.0,556.0>> 

	* uo (U+AB63): L<<413.0,553.0>--<604.0,553.0>> -> L<<604.0,553.0>--<604.0,553.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Shook (U+A7C5): B<<264.0,-10.0>-<230.0,-10.0>-<202.0,-8.0>>/L<<202.0,-8.0>--<202.0,-8.0>> = 4.085616779974798

	* V (U+0056): B<<339.5,236.0>-<346.0,204.0>-<347.0,184.0>>/B<<347.0,184.0>-<349.0,204.0>-<354.5,235.5>> = 8.57299836361137

	* W (U+0057): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* W (U+0057): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* W (U+0057): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wacute (U+1E82): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363

	* Wacute (U+1E82): B<<527.0,442.0>-<523.0,468.0>-<521.0,486.0>>/B<<521.0,486.0>-<519.0,468.0>-<514.5,442.0>> = 12.680383491819825

	* Wacute (U+1E82): B<<714.0,235.0>-<721.0,196.0>-<724.0,167.0>>/B<<724.0,167.0>-<727.0,192.0>-<734.0,229.0>> = 12.748914526401432

	* Wanglicana (U+A7C2): B<<339.5,236.0>-<346.0,204.0>-<347.0,184.0>>/B<<347.0,184.0>-<375.0,335.0>-<418.5,446.5>> = 13.367469096029062

	* Wcircumflex (U+0174): B<<308.0,211.5>-<313.0,185.0>-<315.0,167.0>>/B<<315.0,167.0>-<319.0,197.0>-<325.5,236.0>> = 13.934835114501363 

	* 49 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Sigma (U+03A3): L<<38.0,714.0>--<578.0,713.0>>

	* Sigma (U+03A3): L<<578.0,558.0>--<368.0,559.0>>

	* uni01A9 (U+01A9): L<<38.0,714.0>--<578.0,713.0>>

	* uni01A9 (U+01A9): L<<578.0,558.0>--<368.0,559.0>>

	* uni2055 (U+2055): L<<339.0,-16.0>--<222.0,-15.0>>

	* uni205C (U+205C): L<<22.0,289.0>--<21.0,420.0>>

	* uni205C (U+205C): L<<360.0,745.0>--<491.0,746.0>>

	* uni205C (U+205C): L<<491.0,-38.0>--<360.0,-37.0>>

	* uni205C (U+205C): L<<827.0,420.0>--<826.0,289.0>>

	* uni2E59 (U+2E59): L<<204.0,285.0>--<36.0,284.0>> 

	* 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-BlackItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* solidusdotted and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 70 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* Kappa (U+039A): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* uni0136 (U+0136): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* uni0198 (U+0198): L<<292.0,409.0>--<374.0,533.0>> -> L<<374.0,533.0>--<428.0,608.0>>

	* uni01E8 (U+01E8): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* uni03CF (U+03CF): L<<292.0,409.0>--<379.0,530.0>> -> L<<379.0,530.0>--<519.0,714.0>>

	* uni1D37 (U+1D37): L<<243.0,532.0>--<289.0,592.0>> -> L<<289.0,592.0>--<390.0,715.0>>

	* uni1E30 (U+1E30): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* uni1E32 (U+1E32): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>>

	* uni1E34 (U+1E34): L<<292.0,409.0>--<363.0,509.0>> -> L<<363.0,509.0>--<519.0,714.0>> 

	* 14 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Wanglicana (U+A7C2): B<<306.5,205.5>-<306.0,191.0>-<305.0,184.0>>/B<<305.0,184.0>-<367.0,340.0>-<433.5,451.5>> = 13.544546764868148

	* beta (U+03B2): B<<577.5,453.0>-<529.0,402.0>-<451.0,395.0>>/B<<451.0,395.0>-<511.0,386.0>-<549.0,340.5>> = 13.658956651800954

	* onequarter (U+00BC): B<<730.0,278.5>-<737.0,303.0>-<741.0,312.0>>/B<<741.0,312.0>-<733.0,299.0>-<716.5,278.0>> = 7.645013271670642

	* threequarters (U+00BE): B<<752.0,278.5>-<759.0,303.0>-<763.0,312.0>>/B<<763.0,312.0>-<755.0,299.0>-<738.5,278.0>> = 7.645013271670642

	* uni0246 (U+0246): L<<268.0,292.0>--<246.0,187.0>>/L<<246.0,187.0>--<292.0,292.0>> = 11.824351692602004

	* uni0274 (U+0274): L<<332.0,0.0>--<245.0,359.0>>/B<<245.0,359.0>-<245.0,348.0>-<240.5,320.5>> = 13.622426911283403

	* uni028A (U+028A): B<<157.0,403.0>-<185.0,416.0>-<206.0,421.0>>/L<<206.0,421.0>--<55.0,421.0>> = 13.392497753751098

	* uni0377 (U+0377): B<<245.5,291.0>-<233.0,246.0>-<216.0,211.0>>/L<<216.0,211.0>--<477.0,552.0>> = 11.52378694566778

	* uni0377 (U+0377): B<<456.5,271.5>-<468.0,309.0>-<482.0,341.0>>/L<<482.0,341.0>--<221.0,0.0>> = 13.80091721452532

	* uni046E (U+046E): L<<391.0,-105.0>--<391.0,-239.0>>/B<<391.0,-239.0>-<389.0,-231.0>-<375.0,-225.5>> = 14.036243467926484 

	* 21 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aivowelsigncandrabindudeva
	* auvowelsigncandrabindudeva
	* awvowelsigncandrabindudeva
	* eshortvowelsigncandrabindudeva
	* evowelsigncandrabindudeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindu2deva
	* iivowelcandrabindu3deva
	* iivowelcandrabindudeva
	* oeopen and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 70 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Ukmonographcy (U+A64A): L<<328.0,201.0>--<328.0,330.0>> -> L<<328.0,330.0>--<328.0,331.0>>

	* uni1D21 (U+1D21): L<<419.0,408.0>--<419.0,408.0>> -> L<<419.0,408.0>--<419.0,408.0>>

	* uni1E10 (U+1E10): L<<298.0,0.0>--<292.0,0.0>> -> L<<292.0,0.0>--<90.0,0.0>>

	* uni2C69 (U+2C69): L<<241.0,387.0>--<301.0,471.0>> -> L<<301.0,471.0>--<494.0,714.0>>

	* uni2E36 (U+2E36): L<<294.0,556.0>--<294.0,468.0>> -> L<<294.0,468.0>--<321.0,0.0>>

	* uni2E37 (U+2E37): L<<145.0,0.0>--<172.0,468.0>> -> L<<172.0,468.0>--<172.0,556.0>>

	* uniA740 (U+A740): L<<241.0,387.0>--<301.0,471.0>> -> L<<301.0,471.0>--<494.0,714.0>>

	* uniA742 (U+A742): L<<241.0,387.0>--<301.0,471.0>> -> L<<301.0,471.0>--<494.0,714.0>>

	* uniA744 (U+A744): L<<241.0,387.0>--<301.0,471.0>> -> L<<301.0,471.0>--<494.0,714.0>>

	* uniA790 (U+A790): L<<216.0,540.0>--<225.0,336.0>> -> L<<225.0,336.0>--<225.0,0.0>> 

	* uniA7A2 (U+A7A2): L<<241.0,387.0>--<301.0,471.0>> -> L<<301.0,471.0>--<494.0,714.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* W (U+0057): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* W (U+0057): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wacute (U+1E82): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wacute (U+1E82): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<489.0,505.5>-<485.0,529.0>-<483.0,542.0>>/B<<483.0,542.0>-<482.0,529.0>-<477.5,505.5>> = 13.144867617550734

	* Wcircumflex (U+0174): B<<683.0,196.0>-<689.0,161.0>-<692.0,137.0>>/B<<692.0,137.0>-<695.0,162.0>-<701.0,196.5>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<266.0,196.0>-<272.0,161.0>-<275.0,137.0>>/B<<275.0,137.0>-<278.0,162.0>-<284.0,196.5>> = 13.967789761532726 

	* 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni0940 (U+0940): L<<-100.0,614.0>--<-229.0,615.0>>

	* uni2E59 (U+2E59): L<<170.0,275.0>--<40.0,274.0>>

	* uni2E5A (U+2E5A): L<<299.0,274.0>--<169.0,275.0>>

	* uni2E5B (U+2E5B): L<<40.0,274.0>--<170.0,275.0>>

	* uni2E5C (U+2E5C): L<<169.0,275.0>--<299.0,274.0>>

	* uniA68E (U+A68E): L<<513.0,-239.0>--<208.0,-240.0>> 

	* uniA696 (U+A696): L<<844.0,-239.0>--<405.0,-240.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* solidusdotted and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 70 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* Kappa (U+039A): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* u1079C (U+1079C): L<<131.0,287.0>--<162.0,422.0>> -> L<<162.0,422.0>--<163.0,426.0>>

	* uni0136 (U+0136): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* uni0198 (U+0198): L<<251.0,369.0>--<329.0,472.0>> -> L<<329.0,472.0>--<423.0,588.0>>

	* uni01E8 (U+01E8): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* uni03CF (U+03CF): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* uni1D37 (U+1D37): L<<216.0,508.0>--<266.0,570.0>> -> L<<266.0,570.0>--<397.0,715.0>>

	* uni1DF04 (U+1DF04): L<<115.0,0.0>--<163.0,226.0>> -> L<<163.0,226.0>--<164.0,232.0>>

	* uni1DF0D (U+1DF0D): L<<111.0,-39.0>--<116.0,-14.0>> -> L<<116.0,-14.0>--<118.0,0.0>> 

	* 16 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Iotifiedacy (U+A656): B<<726.0,574.5>-<725.0,605.0>-<726.0,626.0>>/B<<726.0,626.0>-<721.0,606.0>-<709.0,575.0>> = 11.309932474020195

	* Yusclosedlittlecy (U+A658): B<<388.0,574.5>-<387.0,605.0>-<388.0,626.0>>/B<<388.0,626.0>-<383.0,606.0>-<371.0,575.5>> = 11.309932474020195

	* Yusiotifiedclosedlittlecy (U+A65C): B<<726.0,574.5>-<725.0,605.0>-<726.0,626.0>>/B<<726.0,626.0>-<721.0,606.0>-<709.0,575.0>> = 11.309932474020195

	* candralongevowelsigndeva (U+0955): B<<-27.0,769.5>-<-62.0,738.0>-<-115.0,729.0>>/L<<-115.0,729.0>--<13.0,729.0>> = 9.637538112930923

	* candralongevowelsigndeva (U+0955): L<<-358.0,729.0>--<-219.0,729.0>>/B<<-219.0,729.0>-<-272.0,738.0>-<-309.5,771.0>> = 9.637538112930923

	* uni0246 (U+0246): L<<240.0,309.0>--<215.0,192.0>>/L<<215.0,192.0>--<269.0,309.0>> = 12.713831111787385

	* uni1D95 (U+1D95): L<<430.0,-69.0>--<485.0,189.0>>/B<<485.0,189.0>-<464.0,132.0>-<425.5,87.0>> = 8.190780943610791

	* uni20A9 (U+20A9): L<<195.0,320.0>--<177.0,147.0>>/L<<177.0,147.0>--<236.0,320.0>> = 12.891415825754484

	* uni20A9 (U+20A9): L<<402.0,394.0>--<415.0,559.0>>/L<<415.0,559.0>--<360.0,394.0>> = 13.930041959314986

	* uni20A9 (U+20A9): L<<489.0,320.0>--<476.0,147.0>>/L<<476.0,147.0>--<530.0,320.0>> = 13.037778269408568 

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aivowelsigncandrabindudeva
	* auvowelsigncandrabindudeva
	* awvowelsigncandrabindudeva
	* eshortvowelsigncandrabindudeva
	* evowelsigncandrabindudeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindu2deva
	* iivowelcandrabindu3deva
	* iivowelcandrabindudeva
	* oeopen and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 70 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Ukmonographcy (U+A64A): L<<322.0,193.0>--<322.0,321.0>> -> L<<322.0,321.0>--<322.0,322.0>>

	* uni1D7E (U+A7B9): L<<590.0,549.0>--<591.0,549.0>> -> L<<591.0,549.0>--<591.0,549.0>>

	* uni211F (U+211F): L<<254.0,401.0>--<297.0,401.0>> -> L<<297.0,401.0>--<300.0,401.0>>

	* uni2E36 (U+2E36): L<<301.0,556.0>--<301.0,457.0>> -> L<<301.0,457.0>--<331.0,0.0>> 

	* uni2E37 (U+2E37): L<<145.0,0.0>--<175.0,457.0>> -> L<<175.0,457.0>--<175.0,556.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<326.0,209.5>-<333.0,177.0>-<335.0,156.0>>/B<<335.0,156.0>-<338.0,177.0>-<344.5,209.0>> = 13.570434385161475

	* W (U+0057): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* W (U+0057): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wacute (U+1E82): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wacute (U+1E82): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wcircumflex (U+0174): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wcircumflex (U+0174): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wdieresis (U+1E84): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357

	* Wdieresis (U+1E84): B<<506.5,475.5>-<502.0,500.0>-<501.0,516.0>>/B<<501.0,516.0>-<499.0,500.0>-<494.5,475.5>> = 10.701350723899111

	* Wgrave (U+1E80): B<<283.5,211.5>-<290.0,175.0>-<293.0,151.0>>/B<<293.0,151.0>-<297.0,183.0>-<305.0,226.5>> = 14.25003269780357 

	* 34 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Sigma (U+03A3): L<<561.0,575.0>--<337.0,576.0>>

	* awdeva (U+0975): L<<848.0,895.0>--<970.0,896.0>>

	* awvowelsigndeva (U+094F): L<<-26.0,895.0>--<96.0,896.0>>

	* ayvowelsigndeva (U+A8FF): L<<-331.0,895.0>--<-209.0,896.0>>

	* fstroke (U+A799): L<<389.0,232.0>--<267.0,231.0>>

	* uni01A9 (U+01A9): L<<561.0,575.0>--<337.0,576.0>>

	* uni0940 (U+0940): L<<-92.0,614.0>--<-241.0,615.0>>

	* uni2E59 (U+2E59): L<<186.0,280.0>--<38.0,279.0>>

	* uni2E5A (U+2E5A): L<<310.0,279.0>--<163.0,280.0>>

	* uni2E5B (U+2E5B): L<<38.0,279.0>--<186.0,280.0>> 

	* 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Yerubackyercy
	* solidusdotted
	* uniA66E and yerubackyercy
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 70 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<270.0,387.0>--<344.0,489.0>> -> L<<344.0,489.0>--<524.0,714.0>>

	* Kappa (U+039A): L<<270.0,387.0>--<344.0,489.0>> -> L<<344.0,489.0>--<524.0,714.0>>

	* emsoftcy (U+A667): L<<573.0,549.0>--<807.0,549.0>> -> L<<807.0,549.0>--<807.0,549.0>>

	* emsoftcy (U+A667): L<<807.0,549.0>--<807.0,549.0>> -> L<<807.0,549.0>--<1001.0,549.0>>

	* u107A1 (U+107A1): L<<166.0,597.0>--<181.0,597.0>> -> L<<181.0,597.0>--<181.0,597.0>>

	* uni0136 (U+0136): L<<270.0,387.0>--<344.0,489.0>> -> L<<344.0,489.0>--<524.0,714.0>>

	* uni0198 (U+0198): L<<270.0,387.0>--<350.0,500.0>> -> L<<350.0,500.0>--<425.0,597.0>>

	* uni01E8 (U+01E8): L<<270.0,387.0>--<344.0,489.0>> -> L<<344.0,489.0>--<524.0,714.0>>

	* uni03CF (U+03CF): L<<270.0,387.0>--<351.0,498.0>> -> L<<351.0,498.0>--<524.0,714.0>>

	* uni1D37 (U+1D37): L<<228.0,519.0>--<276.0,580.0>> -> L<<276.0,580.0>--<394.0,715.0>> 

	* 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* candralongevowelsigndeva (U+0955): B<<-23.0,774.0>-<-53.0,743.0>-<-98.0,732.0>>/L<<-98.0,732.0>--<16.0,732.0>> = 13.736268305622554

	* candralongevowelsigndeva (U+0955): L<<-371.0,732.0>--<-243.0,732.0>>/B<<-243.0,732.0>-<-290.0,744.0>-<-323.5,775.5>> = 14.32271997820355

	* uni0246 (U+0246): L<<253.0,301.0>--<230.0,190.0>>/L<<230.0,190.0>--<279.0,301.0>> = 12.112213770580453

	* uni1D95 (U+1D95): L<<445.0,-61.0>--<498.0,192.0>>/B<<498.0,192.0>-<477.0,135.0>-<438.0,89.0>> = 8.39328025242756

	* uni20A9 (U+20A9): L<<203.0,318.0>--<182.0,146.0>>/L<<182.0,146.0>--<241.0,318.0>> = 11.972197409287046

	* uni20A9 (U+20A9): L<<414.0,395.0>--<429.0,564.0>>/L<<429.0,564.0>--<374.0,395.0>> = 12.955023693841758

	* uni20A9 (U+20A9): L<<509.0,318.0>--<495.0,147.0>>/L<<495.0,147.0>--<548.0,318.0>> = 12.539935656725

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772 

	* xi (U+03BE): B<<144.5,587.5>-<173.0,622.0>-<246.0,640.0>>/B<<246.0,640.0>-<216.0,637.0>-<198.5,635.5>> = 8.140825876305337 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni03FC
	* uni20BE
	* uni2C65 and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* crosspattyleft (U+2E51): L<<396.0,632.0>--<387.0,361.0>> -> L<<387.0,361.0>--<396.0,88.0>>

	* crosspattyright (U+2E50): L<<102.0,88.0>--<111.0,361.0>> -> L<<111.0,361.0>--<102.0,632.0>>

	* daggerdbl (U+2021): L<<225.0,226.0>--<219.0,383.0>> -> L<<219.0,383.0>--<225.0,534.0>>

	* daggerdbl (U+2021): L<<251.0,534.0>--<257.0,383.0>> -> L<<257.0,383.0>--<251.0,226.0>>

	* desoftcy (U+A663): L<<192.0,530.0>--<404.0,530.0>> -> L<<404.0,530.0>--<404.0,530.0>>

	* desoftcy (U+A663): L<<404.0,530.0>--<404.0,530.0>> -> L<<404.0,530.0>--<711.0,530.0>>

	* elsoftcy (U+A665): L<<179.0,530.0>--<409.0,530.0>> -> L<<409.0,530.0>--<409.0,530.0>>

	* elsoftcy (U+A665): L<<409.0,530.0>--<409.0,530.0>> -> L<<409.0,530.0>--<716.0,530.0>>

	* emsoftcy (U+A667): L<<537.0,530.0>--<560.0,530.0>> -> L<<560.0,530.0>--<560.0,530.0>>

	* emsoftcy (U+A667): L<<560.0,530.0>--<560.0,530.0>> -> L<<560.0,530.0>--<849.0,530.0>> 

	* 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* iotifiedacombcy (U+2DFC): B<<-18.0,709.0>-<-4.0,722.0>-<23.0,728.0>>/L<<23.0,728.0>--<-104.0,728.0>> = 12.528807709151492

	* uni1D95 (U+1D95): L<<484.0,-85.0>--<484.0,224.0>>/B<<484.0,224.0>-<477.0,158.0>-<449.0,105.0>> = 6.054191894114791

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565 

	* xi (U+03BE): B<<170.0,700.0>-<207.0,721.0>-<253.0,729.0>>/B<<253.0,729.0>-<222.0,728.0>-<201.0,727.0>> = 8.018196677089737 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni203D (U+203D): L<<188.0,691.0>--<185.0,319.0>>

	* uni20A6 (U+20A6): L<<416.0,299.0>--<415.0,425.0>>

	* uni20A6 (U+20A6): L<<417.0,77.0>--<416.0,267.0>>

	* uniA65F (U+A65F): L<<267.0,-240.0>--<266.0,440.0>> 

	* uniA65F (U+A65F): L<<306.0,440.0>--<305.0,-240.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Odoublecy
	* uni03FC
	* uniA66E and uniA74E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Desoftcy (U+A662): L<<430.0,36.0>--<487.0,304.0>> -> L<<487.0,304.0>--<566.0,678.0>>

	* K (U+004B): L<<158.0,333.0>--<216.0,388.0>> -> L<<216.0,388.0>--<582.0,714.0>>

	* Kappa (U+039A): L<<158.0,333.0>--<216.0,388.0>> -> L<<216.0,388.0>--<582.0,714.0>>

	* Smiddlestroke (U+A7C9): L<<276.0,384.0>--<276.0,384.0>> -> L<<276.0,384.0>--<494.0,384.0>>

	* crosspattyleft (U+2E51): L<<470.0,626.0>--<403.0,355.0>> -> L<<403.0,355.0>--<354.0,82.0>>

	* crosspattyright (U+2E50): L<<66.0,88.0>--<133.0,359.0>> -> L<<133.0,359.0>--<182.0,632.0>>

	* daggerdbl (U+2021): L<<296.0,534.0>--<271.0,384.0>> -> L<<271.0,384.0>--<231.0,226.0>>

	* elsoftcy (U+A665): L<<314.0,0.0>--<411.0,455.0>> -> L<<411.0,455.0>--<420.0,496.0>>

	* u1079C (U+1079C): L<<170.0,495.0>--<183.0,551.0>> -> L<<183.0,551.0>--<200.0,624.0>>

	* uni0136 (U+0136): L<<158.0,333.0>--<216.0,388.0>> -> L<<216.0,388.0>--<582.0,714.0>> 

	* 24 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Yusclosedlittlecy (U+A658): L<<420.0,304.0>--<383.0,566.0>>/B<<383.0,566.0>-<384.0,562.0>-<382.5,572.5>> = 5.998010269962103

	* uni03F0 (U+03F0): B<<435.5,316.0>-<455.0,366.0>-<482.0,408.0>>/L<<482.0,408.0>--<71.0,0.0>> = 12.474647439459913

	* uni0466 (U+0466): L<<414.0,393.0>--<387.0,572.0>>/B<<387.0,572.0>-<388.0,567.0>-<386.5,576.5>> = 2.732215949003597

	* uni1D95 (U+1D95): L<<343.0,-81.0>--<403.0,203.0>>/B<<403.0,203.0>-<383.0,141.0>-<346.5,93.0>> = 5.949374418602966

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* vecombcy (U+2DE1): B<<176.5,749.0>-<158.0,733.0>-<126.0,729.0>>/L<<126.0,729.0>--<126.0,729.0>> = 7.125016348901757

	* xi (U+03BE): B<<256.0,711.5>-<284.0,723.0>-<309.0,729.0>>/B<<309.0,729.0>-<293.0,728.0>-<284.0,727.5>> = 9.919398905798415 

	* zecombcy (U+2DE5): B<<161.5,750.0>-<146.0,736.0>-<122.0,732.0>>/L<<122.0,732.0>--<122.0,732.0>> = 9.462322208025613 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] NotoSans-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* solidusdotted and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Desoftcy (U+A662): L<<397.0,80.0>--<500.0,564.0>> -> L<<500.0,564.0>--<515.0,633.0>>

	* K (U+004B): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* Kappa (U+039A): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* elsoftcy (U+A665): L<<311.0,0.0>--<372.0,279.0>> -> L<<372.0,279.0>--<411.0,463.0>>

	* uni0136 (U+0136): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* uni0198 (U+0198): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<485.0,654.0>>

	* uni01E8 (U+01E8): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* uni03CF (U+03CF): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* uni1D37 (U+1D37): L<<188.0,507.0>--<228.0,547.0>> -> L<<228.0,547.0>--<406.0,715.0>>

	* uni1E30 (U+1E30): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>> 

	* 18 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* onequarter (U+00BC): B<<600.0,298.5>-<605.0,322.0>-<612.0,346.0>>/B<<612.0,346.0>-<608.0,339.0>-<598.5,325.5>> = 13.484676588630261

	* threequarters (U+00BE): B<<661.0,297.5>-<666.0,321.0>-<673.0,345.0>>/B<<673.0,345.0>-<669.0,338.0>-<659.5,324.5>> = 13.484676588630261

	* uni1D95 (U+1D95): L<<364.0,-65.0>--<420.0,201.0>>/B<<420.0,201.0>-<401.0,143.0>-<366.5,95.0>> = 6.249424115969322

	* uni2074 (U+2074): B<<297.0,713.5>-<302.0,737.0>-<309.0,761.0>>/B<<309.0,761.0>-<305.0,754.0>-<295.5,740.5>> = 13.484676588630261

	* uni2084 (U+2084): B<<188.0,167.5>-<193.0,191.0>-<200.0,215.0>>/B<<200.0,215.0>-<196.0,208.0>-<186.5,194.5>> = 13.484676588630261

	* uni20A9 (U+20A9): L<<163.0,331.0>--<143.0,108.0>>/L<<143.0,108.0>--<218.0,331.0>> = 13.464046018615312

	* uni20A9 (U+20A9): L<<434.0,331.0>--<419.0,104.0>>/L<<419.0,104.0>--<492.0,331.0>> = 14.046490318782169

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2137 (U+2137): L<<254.0,0.0>--<214.0,180.0>>/B<<214.0,180.0>-<214.0,146.0>-<195.5,115.5>> = 12.528807709151492 

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* oeopen
	* uni0247
	* uni03FC
	* uni20BE
	* uni2C65 and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* crosspattyleft (U+2E51): L<<402.0,632.0>--<390.0,361.0>> -> L<<390.0,361.0>--<402.0,88.0>>

	* crosspattyright (U+2E50): L<<100.0,88.0>--<112.0,361.0>> -> L<<112.0,361.0>--<100.0,632.0>>

	* u107A1 (U+107A1): L<<169.0,605.0>--<169.0,605.0>> -> L<<169.0,605.0>--<263.0,605.0>>

	* uni1DF06 (U+1DF06): L<<260.0,530.0>--<260.0,530.0>> -> L<<260.0,530.0>--<405.0,530.0>>

	* uni2E36 (U+2E36): L<<257.0,557.0>--<257.0,521.0>> -> L<<257.0,521.0>--<269.0,0.0>>

	* uni2E36 (U+2E36): L<<269.0,760.0>--<257.0,557.0>> -> L<<257.0,557.0>--<257.0,521.0>>

	* uni2E37 (U+2E37): L<<148.0,0.0>--<159.0,521.0>> -> L<<159.0,521.0>--<159.0,557.0>> 

	* uni2E37 (U+2E37): L<<159.0,521.0>--<159.0,557.0>> -> L<<159.0,557.0>--<148.0,760.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni1D95 (U+1D95): L<<492.0,-76.0>--<492.0,220.0>>/B<<492.0,220.0>-<484.0,153.0>-<455.0,101.0>> = 6.809050179613362

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565 

	* xi (U+03BE): B<<167.5,688.0>-<203.0,708.0>-<247.0,718.0>>/B<<247.0,718.0>-<221.0,716.0>-<195.0,715.0>> = 8.405560710291214 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uniA65F (U+A65F): L<<257.0,-240.0>--<258.0,409.0>> 

	* uniAB45 (U+AB45): L<<82.0,0.0>--<81.0,126.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Odoublecy
	* uni03FC
	* uniA66E and uniA74E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 71 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Desoftcy (U+A662): L<<418.0,53.0>--<506.0,467.0>> -> L<<506.0,467.0>--<547.0,661.0>>

	* K (U+004B): L<<176.0,346.0>--<236.0,405.0>> -> L<<236.0,405.0>--<568.0,714.0>>

	* Kappa (U+039A): L<<176.0,346.0>--<236.0,405.0>> -> L<<236.0,405.0>--<568.0,714.0>>

	* crosspattyleft (U+2E51): L<<474.0,626.0>--<404.0,355.0>> -> L<<404.0,355.0>--<358.0,82.0>>

	* crosspattyright (U+2E50): L<<64.0,88.0>--<134.0,359.0>> -> L<<134.0,359.0>--<180.0,632.0>>

	* elsoftcy (U+A665): L<<313.0,0.0>--<383.0,327.0>> -> L<<383.0,327.0>--<417.0,484.0>>

	* emsoftcy (U+A667): L<<559.0,532.0>--<587.0,532.0>> -> L<<587.0,532.0>--<587.0,532.0>>

	* emsoftcy (U+A667): L<<587.0,532.0>--<587.0,532.0>> -> L<<587.0,532.0>--<854.0,532.0>>

	* uni0136 (U+0136): L<<176.0,346.0>--<236.0,405.0>> -> L<<236.0,405.0>--<568.0,714.0>>

	* uni0198 (U+0198): L<<176.0,346.0>--<236.0,405.0>> -> L<<236.0,405.0>--<523.0,670.0>> 

	* 23 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* cpalatalhook (U+A794): L<<382.0,56.0>--<382.0,57.0>>/L<<382.0,57.0>--<354.0,-79.0>> = 11.633633998940427

	* cpalatalhook (U+A794): L<<385.0,71.0>--<382.0,56.0>>/L<<382.0,56.0>--<382.0,57.0>> = 11.309932474020227

	* uni03F0 (U+03F0): B<<418.0,255.5>-<438.0,327.0>-<472.0,384.0>>/L<<472.0,384.0>--<94.0,0.0>> = 13.733155701483533

	* uni1D95 (U+1D95): L<<351.0,-75.0>--<410.0,203.0>>/B<<410.0,203.0>-<390.0,142.0>-<354.0,94.0>> = 6.170597039057249

	* uni1DF0A (U+1DF0A): B<<115.0,50.0>-<115.0,40.0>-<113.0,31.0>>/L<<113.0,31.0>--<113.0,32.0>> = 12.528807709151492

	* uni1DF0A (U+1DF0A): L<<113.0,31.0>--<113.0,32.0>>/L<<113.0,32.0>--<80.0,-118.0>> = 12.407418527400745

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* xi (U+03BE): B<<237.0,692.5>-<271.0,710.0>-<302.0,718.0>>/B<<302.0,718.0>-<283.0,716.0>-<269.5,715.0>> = 8.461288142571357 

	* zecombcy (U+2DE5): B<<165.0,751.0>-<150.0,737.0>-<125.0,732.0>>/L<<125.0,732.0>--<125.0,732.0>> = 11.309932474020195 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aivowelsigncandrabindudeva
	* auvowelsigncandrabindudeva
	* awvowelsigncandrabindudeva
	* eshortvowelsigncandrabindudeva
	* evowelsigncandrabindudeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindu2deva
	* iivowelcandrabindudeva
	* oeopen
	* oshortvowelsigncandrabindudeva and 7 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 69 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni090C (U+090C): L<<631.0,107.0>--<631.0,107.0>> -> L<<631.0,107.0>--<631.0,107.0>>

	* uni20B6 (U+20B6): L<<202.0,540.0>--<346.0,540.0>> -> L<<346.0,540.0>--<347.0,540.0>>

	* uni2E36 (U+2E36): L<<278.0,556.0>--<278.0,493.0>> -> L<<278.0,493.0>--<299.0,0.0>>

	* uni2E37 (U+2E37): L<<145.0,0.0>--<166.0,493.0>> -> L<<166.0,493.0>--<166.0,556.0>> 

	* uniA7A1 (U+A7A1): L<<436.0,248.0>--<436.0,268.0>> -> L<<436.0,268.0>--<436.0,270.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni090C (U+090C): L<<631.0,107.0>--<631.0,107.0>>/B<<631.0,107.0>-<573.0,99.0>-<547.0,78.5>> = 7.853313301978193

	* uni1D95 (U+1D95): L<<516.0,-66.0>--<516.0,214.0>>/B<<516.0,214.0>-<501.0,106.0>-<437.0,48.0>> = 7.907162702958418

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2137 (U+2137): L<<253.0,0.0>--<213.0,178.0>>/B<<213.0,178.0>-<213.0,140.0>-<195.0,111.5>> = 12.665063765042364

	* uniA760 (U+A760): B<<474.0,550.0>-<468.0,577.0>-<466.0,593.0>>/B<<466.0,593.0>-<464.0,577.0>-<458.5,551.0>> = 14.25003269780357 

	* xi (U+03BE): B<<126.0,635.0>-<167.0,668.0>-<231.0,686.0>>/B<<231.0,686.0>-<207.0,683.0>-<171.0,681.5>> = 8.583621480113882 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uniA65F (U+A65F): L<<241.0,-240.0>--<245.0,329.0>>

	* uniA65F (U+A65F): L<<343.0,329.0>--<347.0,-240.0>> 

	* uniA75D (U+A75D): L<<497.0,0.0>--<496.0,-139.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* solidusdotted and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>>

	* Kappa (U+039A): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>>

	* elsoftcy (U+A665): L<<318.0,0.0>--<373.0,255.0>> -> L<<373.0,255.0>--<416.0,454.0>>

	* uni0136 (U+0136): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>>

	* uni0198 (U+0198): L<<220.0,368.0>--<287.0,445.0>> -> L<<287.0,445.0>--<467.0,635.0>>

	* uni01E8 (U+01E8): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>>

	* uni03CF (U+03CF): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>>

	* uni090C (U+090C): L<<631.0,107.0>--<631.0,107.0>> -> L<<631.0,107.0>--<631.0,107.0>>

	* uni1D37 (U+1D37): L<<196.0,508.0>--<239.0,554.0>> -> L<<239.0,554.0>--<403.0,715.0>>

	* uni1E30 (U+1E30): L<<220.0,368.0>--<286.0,444.0>> -> L<<286.0,444.0>--<539.0,714.0>> 

	* 15 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* onequarter (U+00BC): B<<615.5,289.5>-<620.0,310.0>-<627.0,334.0>>/B<<627.0,334.0>-<620.0,322.0>-<604.0,301.0>> = 13.996232455217315

	* threequarters (U+00BE): B<<667.5,288.5>-<672.0,309.0>-<679.0,333.0>>/B<<679.0,333.0>-<672.0,321.0>-<656.0,300.0>> = 13.996232455217315

	* uni090C (U+090C): L<<631.0,107.0>--<631.0,107.0>>/B<<631.0,107.0>-<573.0,99.0>-<547.0,78.5>> = 7.853313301978193

	* uni1D95 (U+1D95): L<<383.0,-66.0>--<439.0,197.0>>/B<<439.0,197.0>-<419.0,140.0>-<383.5,93.0>> = 7.314461522244119

	* uni2074 (U+2074): B<<291.5,704.5>-<296.0,725.0>-<303.0,749.0>>/B<<303.0,749.0>-<296.0,737.0>-<280.0,716.0>> = 13.996232455217315

	* uni2084 (U+2084): B<<182.5,158.5>-<187.0,179.0>-<194.0,203.0>>/B<<194.0,203.0>-<187.0,191.0>-<171.0,170.0>> = 13.996232455217315

	* uni20A9 (U+20A9): L<<172.0,328.0>--<153.0,120.0>>/L<<153.0,120.0>--<223.0,328.0>> = 13.380801358044812

	* uni20A9 (U+20A9): L<<450.0,328.0>--<436.0,117.0>>/L<<436.0,117.0>--<503.0,328.0>> = 13.820441734751517

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772 

	* 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* iivowelcandrabindu1deva
	* iivowelcandrabindudeva
	* oeopen
	* solidusdotted
	* uni0247
	* uni20BE
	* uni2C65 and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 69 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni2E36 (U+2E36): L<<271.0,556.0>--<271.0,503.0>> -> L<<271.0,503.0>--<290.0,0.0>>

	* uni2E36 (U+2E36): L<<290.0,760.0>--<271.0,556.0>> -> L<<271.0,556.0>--<271.0,503.0>>

	* uni2E37 (U+2E37): L<<145.0,0.0>--<164.0,503.0>> -> L<<164.0,503.0>--<164.0,556.0>> 

	* uni2E37 (U+2E37): L<<164.0,503.0>--<164.0,556.0>> -> L<<164.0,556.0>--<145.0,760.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni1D7A (U+1D7A): L<<774.0,760.0>--<569.0,501.0>>/B<<569.0,501.0>-<595.0,523.0>-<629.5,534.0>> = 11.40182298367357

	* uni1D95 (U+1D95): L<<505.0,-63.0>--<505.0,213.0>>/B<<505.0,213.0>-<491.0,108.0>-<428.5,49.0>> = 7.594643368591447

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2137 (U+2137): L<<254.0,0.0>--<214.0,180.0>>/B<<214.0,180.0>-<214.0,146.0>-<195.5,115.5>> = 12.528807709151492 

	* xi (U+03BE): B<<163.5,669.0>-<197.0,688.0>-<237.0,699.0>>/B<<237.0,699.0>-<218.0,697.0>-<184.0,695.0>> = 9.367245291331619 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uniA65F (U+A65F): L<<241.0,-240.0>--<244.0,356.0>> 

	* uniA65F (U+A65F): L<<326.0,356.0>--<329.0,-240.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] NotoSans-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* aivowelsigncandrabindudeva
	* auvowelsigncandrabindudeva
	* awvowelsigncandrabindudeva
	* eshortvowelsigncandrabindudeva
	* evowelsigncandrabindudeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindu2deva
	* iivowelcandrabindu3deva
	* iivowelcandrabindudeva
	* oeopen and 8 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 69 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Smiddlestroke (U+A7C9): L<<326.0,406.0>--<326.0,406.0>> -> L<<326.0,406.0>--<541.0,406.0>>

	* uni20B6 (U+20B6): L<<221.0,543.0>--<355.0,543.0>> -> L<<355.0,543.0>--<356.0,543.0>>

	* uni2E36 (U+2E36): L<<285.0,556.0>--<285.0,481.0>> -> L<<285.0,481.0>--<309.0,0.0>> 

	* uni2E37 (U+2E37): L<<145.0,0.0>--<169.0,481.0>> -> L<<169.0,481.0>--<169.0,556.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* W (U+0057): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* W (U+0057): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wacute (U+1E82): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wcircumflex (U+0174): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wdieresis (U+1E84): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<257.0,182.5>-<263.0,150.0>-<266.0,126.0>>/B<<266.0,126.0>-<269.0,151.0>-<275.0,184.0>> = 13.967789761532726

	* Wgrave (U+1E80): B<<678.0,182.0>-<684.0,150.0>-<687.0,126.0>>/B<<687.0,126.0>-<690.0,151.0>-<695.5,183.0>> = 13.967789761532726 

	* 20 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni2E59 (U+2E59): L<<155.0,275.0>--<40.0,274.0>>

	* uni2E5B (U+2E5B): L<<40.0,274.0>--<155.0,275.0>>

	* uniA68E (U+A68E): L<<516.0,-230.0>--<202.0,-231.0>>

	* uniA696 (U+A696): L<<839.0,-230.0>--<391.0,-231.0>> 

	* uniA75D (U+A75D): L<<530.0,243.0>--<529.0,100.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSans-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* solidusdotted and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 69 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<234.0,368.0>--<305.0,457.0>> -> L<<305.0,457.0>--<534.0,714.0>>

	* Kappa (U+039A): L<<234.0,368.0>--<305.0,457.0>> -> L<<305.0,457.0>--<534.0,714.0>>

	* cpalatalhook (U+A794): L<<407.0,129.0>--<405.0,118.0>> -> L<<405.0,118.0>--<367.0,-63.0>>

	* elsoftcy (U+A665): L<<326.0,0.0>--<372.0,214.0>> -> L<<372.0,214.0>--<421.0,444.0>>

	* u107A1 (U+107A1): L<<168.0,600.0>--<185.0,600.0>> -> L<<185.0,600.0>--<185.0,600.0>>

	* uni0136 (U+0136): L<<234.0,368.0>--<305.0,457.0>> -> L<<305.0,457.0>--<534.0,714.0>>

	* uni0198 (U+0198): L<<234.0,368.0>--<306.0,457.0>> -> L<<306.0,457.0>--<446.0,613.0>>

	* uni01E8 (U+01E8): L<<234.0,368.0>--<305.0,457.0>> -> L<<305.0,457.0>--<534.0,714.0>>

	* uni03CF (U+03CF): L<<234.0,368.0>--<305.0,457.0>> -> L<<305.0,457.0>--<534.0,714.0>>

	* uni1D37 (U+1D37): L<<205.0,508.0>--<251.0,561.0>> -> L<<251.0,561.0>--<400.0,715.0>> 

	* 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Ukmonographcy (U+A64A): L<<331.0,342.0>--<331.0,342.0>>/B<<331.0,342.0>-<250.0,333.0>-<216.0,298.5>> = 6.340191745909908

	* uni0246 (U+0246): L<<225.0,318.0>--<185.0,130.0>>/L<<185.0,130.0>--<269.0,318.0>> = 12.064019868713396

	* uni1D95 (U+1D95): L<<405.0,-67.0>--<460.0,194.0>>/B<<460.0,194.0>-<440.0,136.0>-<403.0,90.0>> = 7.125884901049224

	* uni20A9 (U+20A9): L<<183.0,324.0>--<164.0,132.0>>/L<<164.0,132.0>--<229.0,324.0>> = 13.051606957867811

	* uni20A9 (U+20A9): L<<390.0,394.0>--<405.0,582.0>>/L<<405.0,582.0>--<341.0,394.0>> = 14.238077171195645

	* uni20A9 (U+20A9): L<<468.0,324.0>--<455.0,131.0>>/L<<455.0,131.0>--<516.0,324.0>> = 13.686294659108857

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2137 (U+2137): L<<252.0,0.0>--<213.0,176.0>>/B<<213.0,176.0>-<213.0,133.0>-<194.5,106.5>> = 12.494333718418076 

	* xi (U+03BE): B<<174.5,619.5>-<209.0,654.0>-<275.0,671.0>>/B<<275.0,671.0>-<249.0,669.0>-<230.0,667.0>> = 10.045330369496687 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSans-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni2C65 and uniA66E
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni046E	Contours detected: 1	Expected: 2 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* crosspattyleft (U+2E51): L<<392.0,632.0>--<385.0,361.0>> -> L<<385.0,361.0>--<392.0,88.0>>

	* crosspattyright (U+2E50): L<<103.0,88.0>--<110.0,361.0>> -> L<<110.0,361.0>--<103.0,632.0>>

	* daggerdbl (U+2021): L<<224.0,222.0>--<222.0,383.0>> -> L<<222.0,383.0>--<224.0,538.0>>

	* daggerdbl (U+2021): L<<243.0,538.0>--<245.0,383.0>> -> L<<245.0,383.0>--<243.0,222.0>>

	* u107A1 (U+107A1): L<<94.0,598.0>--<129.0,598.0>> -> L<<129.0,598.0>--<129.0,598.0>>

	* uni1DF06 (U+1DF06): L<<144.0,519.0>--<199.0,519.0>> -> L<<199.0,519.0>--<199.0,519.0>>

	* uni2E36 (U+2E36): L<<243.0,557.0>--<243.0,538.0>> -> L<<243.0,538.0>--<247.0,0.0>>

	* uni2E36 (U+2E36): L<<247.0,760.0>--<243.0,557.0>> -> L<<243.0,557.0>--<243.0,538.0>>

	* uni2E37 (U+2E37): L<<150.0,0.0>--<154.0,538.0>> -> L<<154.0,538.0>--<154.0,557.0>> 

	* uni2E37 (U+2E37): L<<154.0,538.0>--<154.0,557.0>> -> L<<154.0,557.0>--<150.0,760.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* iotifiedacombcy (U+2DFC): B<<-15.5,710.5>-<1.0,724.0>-<32.0,730.0>>/L<<32.0,730.0>--<-104.0,730.0>> = 10.954062643398332

	* uni03F0 (U+03F0): B<<462.5,344.0>-<481.0,415.0>-<500.0,451.0>>/L<<500.0,451.0>--<97.0,0.0>> = 13.95891670503883

	* uni1D95 (U+1D95): L<<479.0,-90.0>--<479.0,227.0>>/B<<479.0,227.0>-<473.0,162.0>-<445.5,108.0>> = 5.273895957351716

	* uni20B9 (U+20B9): L<<529.0,689.0>--<302.0,689.0>>/B<<302.0,689.0>-<349.0,677.0>-<379.0,636.5>> = 14.32271997820355

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uniA657 (U+A657): B<<314.5,226.0>-<351.0,260.0>-<421.0,275.0>>/L<<421.0,275.0>--<117.0,275.0>> = 12.094757077012089

	* uniA7D3 (U+A7D3): L<<116.0,760.0>--<116.0,410.0>>/B<<116.0,410.0>-<130.0,466.0>-<177.5,502.0>> = 14.036243467926484 

	* xi (U+03BE): B<<171.5,708.0>-<210.0,729.0>-<257.0,737.0>>/B<<257.0,737.0>-<235.0,736.0>-<220.5,735.5>> = 7.057330875942479 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Aevolapuk (U+A79A): L<<572.0,554.0>--<573.0,714.0>>

	* Aevolapuk (U+A79A): L<<573.0,0.0>--<572.0,162.0>>

	* Uevolapuk (U+A79E): L<<573.0,0.0>--<572.0,162.0>>

	* dagger (U+2020): L<<220.0,0.0>--<224.0,538.0>>

	* dagger (U+2020): L<<243.0,538.0>--<247.0,0.0>>

	* exclam (U+0021): L<<100.0,174.0>--<98.0,714.0>>

	* exclam (U+0021): L<<127.0,714.0>--<125.0,174.0>>

	* exclamdbl (U+203C): L<<100.0,174.0>--<98.0,714.0>>

	* exclamdbl (U+203C): L<<127.0,714.0>--<125.0,174.0>>

	* exclamdbl (U+203C): L<<295.0,174.0>--<293.0,714.0>> 

	* 35 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[10] NotoSans-ThinItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* K (U+004B): L<<145.0,324.0>--<202.0,376.0>> -> L<<202.0,376.0>--<592.0,714.0>>

	* Kappa (U+039A): L<<145.0,324.0>--<202.0,376.0>> -> L<<202.0,376.0>--<592.0,714.0>>

	* crosspattyleft (U+2E51): L<<467.0,626.0>--<402.0,355.0>> -> L<<402.0,355.0>--<351.0,82.0>>

	* crosspattyright (U+2E50): L<<68.0,88.0>--<133.0,359.0>> -> L<<133.0,359.0>--<184.0,632.0>>

	* daggerdbl (U+2021): L<<204.0,222.0>--<234.0,384.0>> -> L<<234.0,384.0>--<271.0,538.0>>

	* daggerdbl (U+2021): L<<291.0,538.0>--<262.0,384.0>> -> L<<262.0,384.0>--<224.0,222.0>>

	* u1079C (U+1079C): L<<203.0,569.0>--<202.0,562.0>> -> L<<202.0,562.0>--<174.0,439.0>>

	* u107A1 (U+107A1): L<<173.0,598.0>--<196.0,598.0>> -> L<<196.0,598.0>--<196.0,598.0>>

	* uni0136 (U+0136): L<<145.0,324.0>--<202.0,376.0>> -> L<<202.0,376.0>--<592.0,714.0>>

	* uni0198 (U+0198): L<<145.0,324.0>--<202.0,376.0>> -> L<<202.0,376.0>--<560.0,686.0>> 

	* 25 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Yusclosedlittlecy (U+A658): L<<428.0,296.0>--<385.0,594.0>>/B<<385.0,594.0>-<387.0,584.0>-<386.0,591.5>> = 3.099093987983883

	* uni03F0 (U+03F0): B<<174.5,196.0>-<152.0,145.0>-<127.0,104.0>>/L<<127.0,104.0>--<557.0,528.0>> = 14.029534696958825

	* uni03F0 (U+03F0): B<<438.0,326.5>-<460.0,381.0>-<489.0,424.0>>/L<<489.0,424.0>--<55.0,0.0>> = 11.671293595164933

	* uni0466 (U+0466): L<<415.0,388.0>--<385.0,594.0>>/B<<385.0,594.0>-<387.0,584.0>-<385.5,591.5>> = 3.0241354500663706

	* uni0516 (U+0516): B<<484.5,478.0>-<478.0,452.0>-<468.0,431.0>>/L<<468.0,431.0>--<698.0,714.0>> = 13.638134970829698

	* uni1D95 (U+1D95): L<<338.0,-85.0>--<399.0,204.0>>/B<<399.0,204.0>-<379.0,141.0>-<342.0,92.5>> = 5.693948168969606

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/B<<117.0,209.0>-<101.0,193.0>-<86.5,179.0>> = 5.906141113770497

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* xi (U+03BE): B<<258.0,719.0>-<287.0,731.0>-<313.0,737.0>>/B<<313.0,737.0>-<296.0,736.0>-<287.0,735.5>> = 9.628156128486747 

	* zecombcy (U+2DE5): B<<159.5,750.0>-<144.0,736.0>-<120.0,732.0>>/L<<120.0,732.0>--<120.0,732.0>> = 9.462322208025613 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] NotoSans-Italic[wdth,wght].ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.5Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Desoftcy
	* Ocrossedcy
	* Smiddlestroke
	* Ukmonographcy
	* Ustroke
	* Wanglicana
	* Yatiotifiedcy
	* Yusiotifiedclosedlittlecy and 75 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l

	- f.ss02 + f.ss02

	- f.ss02 + i

	- i + f.ss02

	- f.ss02 + l 

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- iogonek.loclNAV

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva 

	- 73 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 1 start point differs in glyph 'zero' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cddc90>

	- Contour 0 start point differs in glyph 'theta' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cde350>

	- Contour 1 start point differs in glyph 'omegaroundcy' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cddc90>

	- Contour 0 start point differs in glyph 'uni1DBF' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cde350>

	- Contour 2 start point differs in glyph 'zero.slash' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cddc90>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acae610>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cdd9d0>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cde050> 

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f383acaf0d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f3837cddc90> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0342 (U+0342), uni0343 (U+0343), uni0344 (U+0344), uni0345 (U+0345), uni034F (U+034F), uni1AC5 (U+1AC5), uni1AC7 (U+1AC7), uni1AC8 (U+1AC8), uni1AC9 (U+1AC9), uni1ACA (U+1ACA) and 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: mark-chars]
</div></details><br></div></details><details><summary><b>[13] NotoSans[wdth,wght].ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>💔 <b>ERROR:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 💔 **ERROR** The condition <FontBakeryCondition:expected_font_names> had an error: KeyError: 'fvar'
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.3Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Desoftcy
	* Elsoftcy
	* Ocrossedcy
	* Smiddlestroke
	* Ukmonographcy
	* Ustroke
	* Wanglicana
	* aanuktadeva and 230 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets">com.google.fonts/check/ligature_carets</a>)</summary><div>


* ⚠ **WARN** This font lacks caret position values for ligature glyphs on its GDEF table. [code: lacks-caret-pos]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- chaaltdeva

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- ddaaltdeva

	- ddhaaltdeva

	- llaaltdeva

	- llvocalicvowelsignleftdeva

	- llvocalicvowelsignlowdeva

	- llvocalicvowelsignnuktaleftdeva

	- lvocalicvowelsignleftdeva 

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 1 start point differs in glyph 'uni0249' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f382a3969d0> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7f382a3ed8d0> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0342 (U+0342), uni0343 (U+0343), uni0344 (U+0344), uni0345 (U+0345), uni034F (U+034F), uni1AC5 (U+1AC5), uni1AC7 (U+1AC7), uni1AC8 (U+1AC8), uni1AC9 (U+1AC9), uni1ACA (U+1ACA) and 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: mark-chars]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 6 | 23 | 207 | 2134 | 143 | 1862 | 0 |
| 0% | 1% | 5% | 49% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
