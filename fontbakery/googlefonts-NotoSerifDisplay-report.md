## Fontbakery report

Fontbakery version: 0.8.9

<details><summary><b>[2] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>


* 🔥 **FAIL** Not all fonts passed in the command line are in the same directory. This may lead to bad results as the tool will interpret all font files as belonging to a single font family. The detected directories are: ['fonts/NotoSerifDisplay/googlefonts/ttf', 'fonts/NotoSerifDisplay/googlefonts/variable-ttf'] [code: single-directory]
</div></details><details><summary>🔥 <b>FAIL:</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/family/max_4_fonts_per_family_name">com.adobe.fonts/check/family/max_4_fonts_per_family_name</a>)</summary><div>


* 🔥 **FAIL** Family 'Noto Serif Display' has 6 fonts (should be 4 or fewer). [code: too-many]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-Black.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* uni1F27
	* phi and 245 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Black' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Ustroke (U+A7B8): L<<629.0,213.0>--<629.0,648.0>> -> L<<629.0,648.0>--<629.0,651.0>>

	* Zpalatalhook (U+A7C6): L<<675.0,229.0>--<667.0,0.0>> -> L<<667.0,0.0>--<667.0,-15.0>>

	* beta (U+03B2): L<<64.0,-220.0>--<66.0,100.0>> -> L<<66.0,100.0>--<64.0,494.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1088.0,195.0>--<1081.0,0.0>> -> L<<1081.0,0.0>--<1081.0,-9.0>>

	* rho (U+03C1): L<<49.0,-221.0>--<51.0,53.0>> -> L<<51.0,53.0>--<51.0,263.0>>

	* uni0290 (U+0290): L<<531.0,195.0>--<525.0,60.0>> -> L<<525.0,60.0>--<525.0,-19.0>>

	* uni03BC (U+03BC): L<<66.0,-221.0>--<68.0,225.0>> -> L<<68.0,225.0>--<64.0,536.0>>

	* uni03FC (U+03FC): L<<50.0,-82.0>--<51.0,53.0>> -> L<<51.0,53.0>--<51.0,263.0>>

	* uni1D5D (U+1D5D): L<<42.0,155.0>--<43.0,347.0>> -> L<<43.0,347.0>--<42.0,583.0>>

	* uni1D66 (U+1D66): L<<42.0,-132.0>--<43.0,60.0>> -> L<<43.0,60.0>--<42.0,296.0>> 

	* And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): L<<450.0,508.0>--<340.0,508.0>>/B<<340.0,508.0>-<449.0,489.0>-<449.0,403.0>> = 9.88798881557781

	* Bbarredsmall (U+1D03): B<<539.5,324.0>-<502.0,292.0>-<412.0,281.0>>/L<<412.0,281.0>--<626.0,281.0>> = 6.968256741378532

	* Bbarredsmall (U+1D03): L<<626.0,271.0>--<434.0,271.0>>/B<<434.0,271.0>-<518.0,262.0>-<562.0,233.0>> = 6.115503566285384

	* Ereversedopen (U+A7AB): B<<583.0,547.0>-<583.0,387.0>-<322.0,372.0>>/B<<322.0,372.0>-<464.0,370.0>-<536.5,324.0>> = 4.096172133594057

	* eogonek (U+0119): B<<256.0,-135.0>-<256.0,-50.0>-<409.0,-4.0>>/B<<409.0,-4.0>-<379.0,-8.0>-<360.0,-9.0>> = 9.138950849004413

	* g (U+0067): B<<34.5,-53.5>-<83.0,-30.0>-<183.0,-26.0>>/B<<183.0,-26.0>-<112.0,-20.0>-<77.0,13.0>> = 7.121030000928448

	* gbreve (U+011F): B<<34.5,-53.5>-<83.0,-30.0>-<183.0,-26.0>>/B<<183.0,-26.0>-<112.0,-20.0>-<77.0,13.0>> = 7.121030000928448

	* gcaron (U+01E7): B<<34.5,-53.5>-<83.0,-30.0>-<183.0,-26.0>>/B<<183.0,-26.0>-<112.0,-20.0>-<77.0,13.0>> = 7.121030000928448

	* gcircumflex (U+011D): B<<34.5,-53.5>-<83.0,-30.0>-<183.0,-26.0>>/B<<183.0,-26.0>-<112.0,-20.0>-<77.0,13.0>> = 7.121030000928448

	* gdotaccent (U+0121): B<<34.5,-53.5>-<83.0,-30.0>-<183.0,-26.0>>/B<<183.0,-26.0>-<112.0,-20.0>-<77.0,13.0>> = 7.121030000928448 

	* And 58 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<64.0,-220.0>--<66.0,100.0>>

	* beta (U+03B2): L<<66.0,100.0>--<64.0,494.0>>

	* eta (U+03B7): L<<611.0,360.0>--<614.0,-221.0>>

	* etatonos (U+03AE): L<<611.0,360.0>--<614.0,-221.0>>

	* iota (U+03B9): L<<65.0,175.0>--<64.0,536.0>>

	* iotadieresis (U+03CA): L<<65.0,175.0>--<64.0,536.0>>

	* iotadieresistonos (U+0390): L<<65.0,175.0>--<64.0,536.0>>

	* iotatonos (U+03AF): L<<65.0,175.0>--<64.0,536.0>>

	* kappa (U+03BA): L<<46.0,0.0>--<44.0,536.0>>

	* rho (U+03C1): L<<49.0,-221.0>--<51.0,53.0>> 

	* And 57 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-BlackItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* four
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uniA716
	* uni1FEE
	* phi
	* uni1F2F and 220 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Black' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3 

	- And 43 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<654.0,229.0>--<602.0,0.0>> -> L<<602.0,0.0>--<596.0,-26.0>>

	* beta (U+03B2): L<<-30.0,-220.0>--<40.0,100.0>> -> L<<40.0,100.0>--<118.0,494.0>>

	* rho (U+03C1): L<<-44.0,-221.0>--<15.0,53.0>> -> L<<15.0,53.0>--<59.0,263.0>>

	* uni024D (U+024D): L<<285.0,288.0>--<284.0,282.0>> -> L<<284.0,282.0>--<221.0,0.0>>

	* uni03BC (U+03BC): L<<-31.0,-221.0>--<65.0,225.0>> -> L<<65.0,225.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-14.0,-82.0>--<15.0,53.0>> -> L<<15.0,53.0>--<59.0,263.0>>

	* uni04CA (U+04CA): L<<467.0,-210.0>--<686.0,46.0>> -> L<<686.0,46.0>--<687.0,47.0>>

	* uni1D0B (U+1D0B): L<<353.0,496.0>--<305.0,292.0>> -> L<<305.0,292.0>--<298.0,265.0>>

	* uni1D5D (U+1D5D): L<<21.0,155.0>--<66.0,347.0>> -> L<<66.0,347.0>--<117.0,583.0>>

	* uni1D66 (U+1D66): L<<-60.0,-228.0>--<-15.0,-36.0>> -> L<<-15.0,-36.0>--<36.0,200.0>> 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<456.5,554.5>-<425.0,525.0>-<351.0,517.0>>/L<<351.0,517.0>--<505.0,517.0>> = 6.1701750950295855

	* Bbarredmod (U+1D2F): L<<504.0,510.0>--<345.0,510.0>>/B<<345.0,510.0>-<461.0,495.0>-<461.0,411.0>> = 7.368051071622163

	* Bbarredsmall (U+1D03): B<<563.0,330.0>-<525.0,300.0>-<461.0,289.0>>/L<<461.0,289.0>--<615.0,289.0>> = 9.752424941653764

	* Bbarredsmall (U+1D03): L<<613.0,279.0>--<432.0,279.0>>/B<<432.0,279.0>-<497.0,270.0>-<531.5,245.5>> = 7.883139316729715

	* Emsoftcy (U+A666): L<<614.0,70.0>--<742.0,689.0>>/L<<742.0,689.0>--<409.0,0.0>> = 14.111655477268902

	* Ereversedopen (U+A7AB): B<<506.5,407.0>-<440.0,383.0>-<328.0,373.0>>/B<<328.0,373.0>-<455.0,366.0>-<519.5,329.5>> = 8.25700811715012

	* cpalatalhook (U+A794): B<<445.5,74.5>-<464.0,106.0>-<481.0,144.0>>/L<<481.0,144.0>--<443.0,-44.0>> = 12.675132907215996

	* iotifiedbigyuscombcy (U+2DFF): B<<31.5,681.5>-<42.0,690.0>-<65.0,693.0>>/L<<65.0,693.0>--<-55.0,693.0>> = 7.431407971172489

	* lambda (U+03BB): L<<398.0,101.0>--<364.0,355.0>>/L<<364.0,355.0>--<364.0,353.0>> = 7.624192504451797

	* sigma (U+03C3): L<<645.0,401.0>--<420.0,401.0>>/B<<420.0,401.0>-<467.0,396.0>-<509.0,373.0>> = 6.0724564072076905 

	* And 58 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-Bold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* uni1F27
	* phi
	* uni1F2F and 183 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Bbarredmod (U+1D2F): L<<254.0,514.0>--<254.0,514.0>> -> L<<254.0,514.0>--<420.0,514.0>>

	* Zpalatalhook (U+A7C6): L<<622.0,206.0>--<615.0,0.0>> -> L<<615.0,0.0>--<615.0,-13.0>>

	* beta (U+03B2): L<<90.0,-240.0>--<94.0,126.0>> -> L<<94.0,126.0>--<85.0,527.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1010.0,181.0>--<1004.0,0.0>> -> L<<1004.0,0.0>--<1004.0,-13.0>>

	* rho (U+03C1): L<<70.0,-240.0>--<74.0,122.0>> -> L<<74.0,122.0>--<74.0,263.0>>

	* uni0290 (U+0290): L<<499.0,181.0>--<493.0,43.0>> -> L<<493.0,43.0>--<493.0,-39.0>>

	* uni03BC (U+03BC): L<<88.0,-240.0>--<92.0,75.0>> -> L<<92.0,75.0>--<85.0,536.0>>

	* uni03FC (U+03FC): L<<72.0,-81.0>--<74.0,122.0>> -> L<<74.0,122.0>--<74.0,263.0>>

	* uni1D5D (U+1D5D): L<<59.0,143.0>--<61.0,363.0>> -> L<<61.0,363.0>--<55.0,603.0>>

	* uni1D66 (U+1D66): L<<59.0,-144.0>--<61.0,76.0>> -> L<<61.0,76.0>--<55.0,316.0>> 

	* And 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Aogonek (U+0104): L<<652.0,0.0>--<685.0,0.0>>/B<<685.0,0.0>-<637.0,-9.0>-<609.5,-39.0>> = 10.61965527615514

	* Bbarredmod (U+1D2F): B<<358.0,540.5>-<322.0,518.0>-<254.0,514.0>>/L<<254.0,514.0>--<254.0,514.0>> = 3.3664606634298315

	* Bbarredmod (U+1D2F): L<<420.0,508.0>--<309.0,508.0>>/B<<309.0,508.0>-<413.0,489.0>-<413.0,402.0>> = 10.353320043929415

	* Bbarredsmall (U+1D03): B<<513.0,319.5>-<475.0,288.0>-<396.0,281.0>>/L<<396.0,281.0>--<595.0,281.0>> = 5.0636168530300525

	* Bbarredsmall (U+1D03): L<<595.0,272.0>--<444.0,272.0>>/B<<444.0,272.0>-<514.0,261.0>-<546.0,231.0>> = 8.93059010041899

	* Eogonek (U+0118): L<<513.0,0.0>--<546.0,0.0>>/B<<546.0,0.0>-<498.0,-9.0>-<470.5,-39.0>> = 10.61965527615514

	* Ereversedopen (U+A7AB): B<<499.0,430.0>-<442.0,381.0>-<323.0,371.0>>/B<<323.0,371.0>-<451.0,370.0>-<516.0,326.5>> = 5.251099929929591

	* Iogonek (U+012E): L<<266.0,0.0>--<299.0,0.0>>/B<<299.0,0.0>-<251.0,-9.0>-<223.5,-39.0>> = 10.61965527615514

	* Uogonek (U+0172): L<<446.0,0.0>--<479.0,0.0>>/B<<479.0,0.0>-<431.0,-9.0>-<403.5,-39.0>> = 10.61965527615514

	* aogonek (U+0105): L<<425.0,0.0>--<458.0,0.0>>/B<<458.0,0.0>-<410.0,-9.0>-<382.5,-39.0>> = 10.61965527615514 

	* And 66 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<555.0,356.0>--<560.0,-240.0>>

	* etatonos (U+03AE): L<<555.0,356.0>--<560.0,-240.0>>

	* kappa (U+03BA): L<<69.0,0.0>--<65.0,536.0>>

	* uni03D7 (U+03D7): L<<69.0,0.0>--<65.0,536.0>>

	* uni1DE9 (U+1DE9): L<<-98.0,624.0>--<-97.0,770.0>>

	* uni1F20 (U+1F20): L<<555.0,356.0>--<560.0,-240.0>>

	* uni1F21 (U+1F21): L<<555.0,356.0>--<560.0,-240.0>>

	* uni1F22 (U+1F22): L<<555.0,356.0>--<560.0,-240.0>>

	* uni1F23 (U+1F23): L<<555.0,356.0>--<560.0,-240.0>>

	* uni1F24 (U+1F24): L<<555.0,356.0>--<560.0,-240.0>> 

	* And 18 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* four
	* upsilon
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* uni1F27 and 191 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display' / SUBFAMILY_NAME = 'Bold Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<610.0,206.0>--<562.0,0.0>> -> L<<562.0,0.0>--<554.0,-32.0>>

	* beta (U+03B2): L<<-37.0,-240.0>--<44.0,126.0>> -> L<<44.0,126.0>--<125.0,527.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<32.0,122.0>> -> L<<32.0,122.0>--<61.0,263.0>>

	* uni03BC (U+03BC): L<<-34.0,-240.0>--<36.0,75.0>> -> L<<36.0,75.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-13.0,-81.0>--<32.0,122.0>> -> L<<32.0,122.0>--<61.0,263.0>>

	* uni1D0B (U+1D0B): L<<309.0,480.0>--<268.0,299.0>> -> L<<268.0,299.0>--<256.0,244.0>>

	* uni1D5D (U+1D5D): L<<9.0,143.0>--<62.0,363.0>> -> L<<62.0,363.0>--<114.0,603.0>>

	* uni1D66 (U+1D66): L<<-73.0,-240.0>--<-20.0,-20.0>> -> L<<-20.0,-20.0>--<32.0,220.0>>

	* uni1D68 (U+1D68): L<<-83.0,-240.0>--<-31.0,-23.0>> -> L<<-31.0,-23.0>--<-12.0,62.0>>

	* uni1DE9 (U+1DE9): L<<-54.0,586.0>--<-17.0,732.0>> -> L<<-17.0,732.0>--<19.0,893.0>>

	* uni1FE4 (U+1FE4): L<<-48.0,-240.0>--<32.0,122.0>> -> L<<32.0,122.0>--<61.0,263.0>> 

	* And uni1FE5 (U+1FE5): L<<-48.0,-240.0>--<32.0,122.0>> -> L<<32.0,122.0>--<61.0,263.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<445.5,554.5>-<415.0,528.0>-<359.0,518.0>>/L<<359.0,518.0>--<488.0,518.0>> = 10.124671655397806

	* Bbarredmod (U+1D2F): L<<487.0,508.0>--<355.0,508.0>>/B<<355.0,508.0>-<448.0,492.0>-<448.0,419.0>> = 9.761774775042225

	* Bbarredsmall (U+1D03): B<<515.5,334.0>-<476.0,300.0>-<400.0,288.0>>/L<<400.0,288.0>--<577.0,288.0>> = 8.972626614896358

	* Bbarredsmall (U+1D03): L<<574.0,278.0>--<395.0,278.0>>/B<<395.0,278.0>-<523.0,259.0>-<523.0,166.0>> = 8.443190929176641

	* Ereversedopen (U+A7AB): B<<462.5,405.0>-<398.0,382.0>-<321.0,373.0>>/B<<321.0,373.0>-<434.0,365.0>-<494.5,331.5>> = 10.71624159417269

	* hardsigntallcy (U+1C86): B<<250.5,556.0>-<345.0,646.0>-<472.0,730.0>>/B<<472.0,730.0>-<432.0,715.0>-<394.0,705.5>> = 12.925295435537027

	* iotifiedbigyuscombcy (U+2DFF): B<<33.5,687.0>-<46.0,696.0>-<66.0,699.0>>/L<<66.0,699.0>--<-42.0,699.0>> = 8.530765609948139

	* sigma (U+03C3): L<<610.0,423.0>--<412.0,423.0>>/B<<412.0,423.0>-<456.0,414.0>-<491.0,391.5>> = 11.56013079421777

	* three (U+0033): B<<423.0,405.0>-<360.0,382.0>-<283.0,373.0>>/B<<283.0,373.0>-<396.0,365.0>-<453.5,331.5>> = 10.71624159417269

	* uni0222 (U+0222): B<<118.0,355.0>-<190.0,418.0>-<317.0,431.0>>/B<<317.0,431.0>-<257.0,438.0>-<222.5,459.0>> = 12.498990923393444 

	* And 42 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-ExtraBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* uni1F27
	* phi and 242 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<651.0,219.0>--<643.0,0.0>> -> L<<643.0,0.0>--<643.0,-14.0>>

	* beta (U+03B2): L<<76.0,-229.0>--<79.0,112.0>> -> L<<79.0,112.0>--<73.0,509.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1053.0,189.0>--<1046.0,0.0>> -> L<<1046.0,0.0>--<1046.0,-11.0>>

	* rho (U+03C1): L<<59.0,-230.0>--<61.0,84.0>> -> L<<61.0,84.0>--<61.0,263.0>>

	* uni0290 (U+0290): L<<517.0,189.0>--<511.0,52.0>> -> L<<511.0,52.0>--<511.0,-28.0>>

	* uni03BC (U+03BC): L<<76.0,-230.0>--<79.0,157.0>> -> L<<79.0,157.0>--<74.0,536.0>>

	* uni03FC (U+03FC): L<<60.0,-82.0>--<61.0,84.0>> -> L<<61.0,84.0>--<61.0,263.0>>

	* uni1D5D (U+1D5D): L<<49.0,150.0>--<51.0,354.0>> -> L<<51.0,354.0>--<48.0,592.0>>

	* uni1D66 (U+1D66): L<<49.0,-137.0>--<51.0,67.0>> -> L<<51.0,67.0>--<48.0,305.0>>

	* uni1D68 (U+1D68): L<<38.0,-138.0>--<40.0,51.0>> -> L<<40.0,51.0>--<40.0,158.0>> 

	* And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Aogonek (U+0104): L<<664.0,0.0>--<696.0,0.0>>/B<<696.0,0.0>-<649.0,-12.0>-<623.5,-47.0>> = 14.32271997820355

	* Bbarredmod (U+1D2F): L<<436.0,508.0>--<326.0,508.0>>/B<<326.0,508.0>-<433.0,489.0>-<433.0,403.0>> = 10.06906269888942

	* Bbarredsmall (U+1D03): B<<527.5,322.5>-<490.0,291.0>-<405.0,281.0>>/L<<405.0,281.0>--<612.0,281.0>> = 6.709836807756896

	* Bbarredsmall (U+1D03): L<<612.0,271.0>--<439.0,271.0>>/B<<439.0,271.0>-<517.0,262.0>-<555.0,232.0>> = 6.581944655178027

	* Eogonek (U+0118): L<<533.0,0.0>--<565.0,0.0>>/B<<565.0,0.0>-<518.0,-12.0>-<492.5,-47.0>> = 14.32271997820355

	* Ereversedopen (U+A7AB): B<<509.0,426.5>-<447.0,380.0>-<322.0,372.0>>/B<<322.0,372.0>-<596.0,368.0>-<596.0,191.0>> = 4.498310900942293

	* Iogonek (U+012E): L<<281.0,0.0>--<313.0,0.0>>/B<<313.0,0.0>-<266.0,-12.0>-<240.5,-47.0>> = 14.32271997820355

	* Uogonek (U+0172): L<<461.0,1.0>--<493.0,1.0>>/B<<493.0,1.0>-<446.0,-11.0>-<420.5,-46.0>> = 14.32271997820355

	* aogonek (U+0105): L<<432.0,0.0>--<464.0,0.0>>/B<<464.0,0.0>-<417.0,-12.0>-<391.5,-47.0>> = 14.32271997820355

	* eogonek (U+0119): B<<277.5,-60.5>-<311.0,-27.0>-<391.0,-5.0>>/B<<391.0,-5.0>-<349.0,-10.0>-<318.0,-10.0>> = 8.587276674387367 

	* And 69 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<586.0,358.0>--<590.0,-230.0>>

	* etatonos (U+03AE): L<<586.0,358.0>--<590.0,-230.0>>

	* iota (U+03B9): L<<76.0,166.0>--<74.0,536.0>>

	* iotadieresis (U+03CA): L<<76.0,166.0>--<74.0,536.0>>

	* iotadieresistonos (U+0390): L<<76.0,166.0>--<74.0,536.0>>

	* iotatonos (U+03AF): L<<76.0,166.0>--<74.0,536.0>>

	* kappa (U+03BA): L<<56.0,0.0>--<54.0,536.0>>

	* rho (U+03C1): L<<59.0,-230.0>--<61.0,84.0>>

	* uni019B (U+019B): L<<179.0,1.0>--<-3.0,0.0>>

	* uni0269 (U+0269): L<<76.0,166.0>--<74.0,536.0>> 

	* And 50 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* four
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1F2F and 216 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display ExtraBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<634.0,219.0>--<584.0,0.0>> -> L<<584.0,0.0>--<577.0,-29.0>>

	* beta (U+03B2): L<<-33.0,-229.0>--<42.0,112.0>> -> L<<42.0,112.0>--<121.0,509.0>>

	* rho (U+03C1): L<<-46.0,-230.0>--<23.0,84.0>> -> L<<23.0,84.0>--<60.0,263.0>>

	* uni03BC (U+03BC): L<<-32.0,-230.0>--<52.0,157.0>> -> L<<52.0,157.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-13.0,-82.0>--<23.0,84.0>> -> L<<23.0,84.0>--<60.0,263.0>>

	* uni044D (U+044D): L<<135.0,279.0>--<244.0,284.0>> -> L<<244.0,284.0>--<332.0,281.0>>

	* uni04ED (U+04ED): L<<135.0,279.0>--<244.0,284.0>> -> L<<244.0,284.0>--<332.0,281.0>>

	* uni1D0B (U+1D0B): L<<333.0,489.0>--<288.0,295.0>> -> L<<288.0,295.0>--<279.0,256.0>>

	* uni1D5D (U+1D5D): L<<15.0,150.0>--<64.0,354.0>> -> L<<64.0,354.0>--<116.0,592.0>>

	* uni1D66 (U+1D66): L<<-66.0,-233.0>--<-17.0,-29.0>> -> L<<-17.0,-29.0>--<34.0,209.0>> 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<452.0,554.5>-<421.0,526.0>-<356.0,517.0>>/L<<356.0,517.0>--<497.0,517.0>> = 7.883139316729715

	* Bbarredmod (U+1D2F): L<<496.0,509.0>--<350.0,509.0>>/B<<350.0,509.0>-<455.0,493.0>-<455.0,415.0>> = 8.664135433108044

	* Bbarredsmall (U+1D03): B<<541.5,332.0>-<503.0,300.0>-<433.0,289.0>>/L<<433.0,289.0>--<598.0,289.0>> = 8.93059010041899

	* Bbarredsmall (U+1D03): L<<595.0,279.0>--<415.0,279.0>>/B<<415.0,279.0>-<480.0,270.0>-<513.5,243.5>> = 7.883139316729715

	* Ereversedopen (U+A7AB): B<<544.0,434.0>-<468.0,387.0>-<325.0,373.0>>/B<<325.0,373.0>-<445.0,366.0>-<508.0,330.5>> = 8.930028299521528

	* iotifiedbigyuscombcy (U+2DFF): B<<32.5,683.5>-<44.0,692.0>-<65.0,696.0>>/L<<65.0,696.0>--<-49.0,696.0>> = 10.784297867562596

	* sigma (U+03C3): L<<629.0,411.0>--<416.0,411.0>>/B<<416.0,411.0>-<462.0,404.0>-<501.0,381.0>> = 8.652541791114704

	* three (U+0033): B<<390.5,390.0>-<338.0,378.0>-<279.0,372.0>>/B<<279.0,372.0>-<408.0,365.0>-<465.0,324.5>> = 8.912754001147944

	* uni0193 (U+0193): B<<741.5,672.5>-<767.0,649.0>-<772.0,620.0>>/L<<772.0,620.0>--<772.0,622.0>> = 9.782407031807285

	* uni0193 (U+0193): L<<776.0,595.0>--<774.0,608.0>>/B<<774.0,608.0>-<774.0,605.0>-<774.0,601.0>> = 8.746162262555211 

	* And 51 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-ExtraLight.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uniA716
	* uni1FAA
	* uni1F64
	* uni1FA8
	* uni1F7C and 76 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Shook (U+A7C5): L<<69.0,126.0>--<69.0,126.0>> -> L<<69.0,126.0>--<69.0,126.0>>

	* Zpalatalhook (U+A7C6): L<<478.0,143.0>--<473.0,0.0>> -> L<<473.0,0.0>--<473.0,-95.0>>

	* beta (U+03B2): L<<59.0,-240.0>--<61.0,118.0>> -> L<<61.0,118.0>--<61.0,559.0>>

	* dzdigraphretroflexhook (U+AB66): L<<823.0,143.0>--<818.0,0.0>> -> L<<818.0,0.0>--<818.0,-94.0>>

	* hpalatalhook (U+A795): L<<563.0,10.0>--<566.0,10.0>> -> L<<566.0,10.0>--<566.0,10.0>>

	* hpalatalhook (U+A795): L<<566.0,10.0>--<566.0,10.0>> -> L<<566.0,10.0>--<576.0,10.0>>

	* hpalatalhook (U+A795): L<<566.0,10.0>--<576.0,10.0>> -> L<<576.0,10.0>--<576.0,10.0>>

	* hpalatalhook (U+A795): L<<576.0,10.0>--<576.0,10.0>> -> L<<576.0,10.0>--<577.0,10.0>>

	* rho (U+03C1): L<<44.0,-240.0>--<47.0,63.0>> -> L<<47.0,63.0>--<46.0,285.0>>

	* uni0290 (U+0290): L<<418.0,143.0>--<413.0,6.0>> -> L<<413.0,6.0>--<413.0,-90.0>> 

	* And 26 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<313.5,545.0>-<289.0,523.0>-<249.0,516.0>>/L<<249.0,516.0>--<376.0,516.0>> = 9.926245506651705

	* Bbarredmod (U+1D2F): L<<376.0,510.0>--<271.0,510.0>>/B<<271.0,510.0>-<358.0,492.0>-<358.0,406.0>> = 11.689369175439202

	* Bbarredsmall (U+1D03): B<<477.0,401.0>-<477.0,304.0>-<366.0,280.0>>/L<<366.0,280.0>--<526.0,280.0>> = 12.200468727380786

	* Bbarredsmall (U+1D03): L<<526.0,270.0>--<386.0,270.0>>/B<<386.0,270.0>-<447.0,258.0>-<472.0,226.5>> = 11.129189289611167

	* chi (U+03C7): L<<191.0,-75.0>--<123.0,-155.0>>/L<<123.0,-155.0>--<260.0,125.0>> = 14.292693697102793

	* chi (U+03C7): L<<284.0,181.0>--<299.0,221.0>>/L<<299.0,221.0>--<285.0,181.0>> = 1.265999000394675

	* three (U+0033): B<<379.0,403.5>-<342.0,382.0>-<303.0,376.0>>/B<<303.0,376.0>-<349.0,373.0>-<391.5,356.0>> = 12.477559261715635

	* uni0239 (U+0239): B<<416.5,449.5>-<436.0,411.0>-<444.0,349.0>>/B<<444.0,349.0>-<451.0,411.0>-<469.5,449.5>> = 13.793979459227387

	* uni040C (U+040C): B<<328.5,415.0>-<303.0,369.0>-<266.0,362.0>>/B<<266.0,362.0>-<340.0,359.0>-<376.5,334.5>> = 13.034653612623744

	* uni0416 (U+0416): B<<259.5,334.5>-<296.0,359.0>-<370.0,362.0>>/B<<370.0,362.0>-<333.0,369.0>-<307.5,415.0>> = 13.034653612623744 

	* And 23 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<103.0,149.0>--<106.0,-240.0>>

	* beta (U+03B2): L<<59.0,-240.0>--<61.0,118.0>>

	* eta (U+03B7): L<<448.0,-240.0>--<453.0,354.0>>

	* eta (U+03B7): L<<491.0,356.0>--<495.0,-240.0>>

	* etatonos (U+03AE): L<<448.0,-240.0>--<453.0,354.0>>

	* etatonos (U+03AE): L<<491.0,356.0>--<495.0,-240.0>>

	* iota (U+03B9): L<<104.0,536.0>--<102.0,128.0>>

	* iota (U+03B9): L<<60.0,126.0>--<59.0,536.0>>

	* iotadieresis (U+03CA): L<<104.0,536.0>--<102.0,128.0>>

	* iotadieresis (U+03CA): L<<60.0,126.0>--<59.0,536.0>> 

	* And 131 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni1FFC
	* uni1FBE
	* uniA716
	* uni1FAA
	* uni1F64
	* uni1FE3
	* uni1FA8
	* uni03C5030403130301 and 68 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display ExtraLight' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<493.0,143.0>--<458.0,0.0>> -> L<<458.0,0.0>--<438.0,-72.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<39.0,118.0>> -> L<<39.0,118.0>--<133.0,559.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<19.0,63.0>> -> L<<19.0,63.0>--<65.0,285.0>>

	* tripledagger (U+2E4B): L<<50.0,346.0>--<212.0,331.0>> -> L<<212.0,331.0>--<212.0,331.0>>

	* uni0246 (U+0246): L<<515.0,704.0>--<514.0,704.0>> -> L<<514.0,704.0>--<280.0,704.0>>

	* uni03BC (U+03BC): L<<-37.0,-240.0>--<44.0,134.0>> -> L<<44.0,134.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-15.0,-88.0>--<19.0,63.0>> -> L<<19.0,63.0>--<65.0,285.0>>

	* uni1D0B (U+1D0B): L<<179.0,464.0>--<140.0,280.0>> -> L<<140.0,280.0>--<126.0,216.0>>

	* uni1D5D (U+1D5D): L<<-10.0,143.0>--<40.0,358.0>> -> L<<40.0,358.0>--<101.0,622.0>>

	* uni1D66 (U+1D66): L<<-91.0,-240.0>--<-41.0,-25.0>> -> L<<-41.0,-25.0>--<20.0,239.0>> 

	* And 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<394.0,552.5>-<366.0,526.0>-<321.0,517.0>>/L<<321.0,517.0>--<436.0,517.0>> = 11.309932474020195

	* Bbarredmod (U+1D2F): L<<434.0,508.0>--<316.0,508.0>>/B<<316.0,508.0>-<350.0,500.0>-<372.0,478.0>> = 13.240519915187184

	* Bbarredsmall (U+1D03): B<<423.0,332.5>-<390.0,299.0>-<331.0,287.0>>/L<<331.0,287.0>--<467.0,287.0>> = 11.496563017585768

	* Bbarredsmall (U+1D03): L<<464.0,277.0>--<320.0,277.0>>/B<<320.0,277.0>-<367.0,268.0>-<399.0,242.5>> = 10.840305454330565

	* chi (U+03C7): L<<245.0,181.0>--<268.0,221.0>>/L<<268.0,221.0>--<245.0,180.0>> = 0.6075396676301458

	* chi (U+03C7): L<<97.0,-75.0>--<12.0,-155.0>>/L<<12.0,-155.0>--<209.0,125.0>> = 11.606580609192578

	* iotifiedbigyuscombcy (U+2DFF): B<<56.0,689.5>-<65.0,696.0>-<84.0,699.0>>/L<<84.0,699.0>--<-18.0,699.0>> = 8.972626614896358

	* kacombcy (U+2DE6): B<<100.5,716.0>-<84.0,698.0>-<66.0,695.0>>/B<<66.0,695.0>-<91.0,694.0>-<103.0,686.5>> = 11.752932250664111

	* three (U+0033): B<<391.5,410.5>-<348.0,383.0>-<290.0,377.0>>/B<<290.0,377.0>-<349.0,371.0>-<391.0,330.5>> = 11.712868019302054

	* uni024A (U+024A): L<<439.0,-59.0>--<490.0,177.0>>/B<<490.0,177.0>-<446.0,76.0>-<387.0,31.5>> = 11.34583922695676 

	* And 38 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] NotoSerifDisplay-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uniA716
	* phi
	* uni1FAA
	* uni1F64
	* uni1FE3 and 100 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<550.0,175.0>--<508.0,0.0>> -> L<<508.0,0.0>--<498.0,-37.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<41.0,116.0>> -> L<<41.0,116.0>--<128.0,536.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<32.0,109.0>> -> L<<32.0,109.0>--<59.0,243.0>>

	* uni03BC (U+03BC): L<<-35.0,-240.0>--<45.0,126.0>> -> L<<45.0,126.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-11.0,-80.0>--<32.0,109.0>> -> L<<32.0,109.0>--<59.0,243.0>>

	* uni1D0B (U+1D0B): L<<247.0,475.0>--<205.0,290.0>> -> L<<205.0,290.0>--<188.0,217.0>>

	* uni1D5D (U+1D5D): L<<0.0,143.0>--<52.0,357.0>> -> L<<52.0,357.0>--<108.0,609.0>>

	* uni1D66 (U+1D66): L<<-82.0,-240.0>--<-30.0,-26.0>> -> L<<-30.0,-26.0>--<26.0,226.0>>

	* uni1D68 (U+1D68): L<<-83.0,-240.0>--<-31.0,-31.0>> -> L<<-31.0,-31.0>--<-14.0,50.0>>

	* uni1DE9 (U+1DE9): L<<-49.0,586.0>--<-14.0,728.0>> -> L<<-14.0,728.0>--<26.0,896.0>> 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<417.0,551.5>-<384.0,525.0>-<333.0,516.0>>/L<<333.0,516.0>--<460.0,516.0>> = 10.00797980144135

	* Bbarredmod (U+1D2F): L<<457.0,506.0>--<343.0,506.0>>/B<<343.0,506.0>-<423.0,489.0>-<423.0,420.0>> = 11.996899307923568

	* Bbarredsmall (U+1D03): B<<472.5,332.0>-<438.0,298.0>-<363.0,285.0>>/L<<363.0,285.0>--<510.0,285.0>> = 9.833563964207102

	* Bbarredsmall (U+1D03): L<<508.0,275.0>--<362.0,275.0>>/B<<362.0,275.0>-<424.0,264.0>-<451.5,233.0>> = 10.060689795322984

	* Ereversedopen (U+A7AB): B<<448.5,397.0>-<391.0,374.0>-<320.0,367.0>>/B<<320.0,367.0>-<352.0,364.0>-<387.0,355.5>> = 10.986507800490408

	* cpalatalhook (U+A794): B<<377.5,65.5>-<402.0,93.0>-<414.0,121.0>>/L<<414.0,121.0>--<383.0,-55.0>> = 13.209183087411478

	* eopenmod (U+1D4B): L<<185.0,457.0>--<185.0,457.0>>/B<<185.0,457.0>-<139.0,462.0>-<118.5,479.5>> = 6.203447901691829

	* eturnedopenmod (U+1D4C): B<<355.0,530.0>-<355.0,451.0>-<221.0,438.0>>/L<<221.0,438.0>--<221.0,438.0>> = 5.541204778039828

	* hardsigntallcy (U+1C86): B<<345.0,685.5>-<382.0,728.0>-<412.0,754.0>>/B<<412.0,754.0>-<410.0,752.0>-<355.5,751.0>> = 4.085616779974888

	* three (U+0033): B<<469.0,446.5>-<409.0,390.0>-<288.0,375.0>>/B<<288.0,375.0>-<377.0,369.0>-<427.5,328.5>> = 10.923530701990947 

	* And 30 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-Light.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1FAA and 88 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Cpalatalhook (U+A7C4): L<<546.0,101.0>--<546.0,101.0>> -> L<<546.0,101.0>--<546.0,101.0>>

	* Zpalatalhook (U+A7C6): L<<509.0,157.0>--<503.0,0.0>> -> L<<503.0,0.0>--<503.0,-76.0>>

	* beta (U+03B2): L<<63.0,-240.0>--<66.0,117.0>> -> L<<66.0,117.0>--<65.0,549.0>>

	* dzdigraphretroflexhook (U+AB66): L<<858.0,151.0>--<852.0,0.0>> -> L<<852.0,0.0>--<852.0,-73.0>>

	* rho (U+03C1): L<<48.0,-240.0>--<52.0,83.0>> -> L<<52.0,83.0>--<52.0,267.0>>

	* uni0290 (U+0290): L<<434.0,151.0>--<428.0,16.0>> -> L<<428.0,16.0>--<428.0,-73.0>>

	* uni03BC (U+03BC): L<<64.0,-240.0>--<66.0,131.0>> -> L<<66.0,131.0>--<63.0,536.0>>

	* uni03FC (U+03FC): L<<50.0,-85.0>--<52.0,83.0>> -> L<<52.0,83.0>--<52.0,267.0>>

	* uni1D5D (U+1D5D): L<<41.0,143.0>--<43.0,357.0>> -> L<<43.0,357.0>--<42.0,617.0>>

	* uni1D66 (U+1D66): L<<41.0,-188.0>--<43.0,27.0>> -> L<<43.0,27.0>--<42.0,286.0>> 

	* And 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<324.0,545.0>-<298.0,522.0>-<250.0,515.0>>/L<<250.0,515.0>--<386.0,515.0>> = 8.297144969836856

	* Bbarredmod (U+1D2F): L<<386.0,509.0>--<274.0,509.0>>/B<<274.0,509.0>-<324.0,500.0>-<346.5,473.0>> = 10.203973721731666

	* Bbarredsmall (U+1D03): B<<493.0,402.0>-<493.0,301.0>-<374.0,281.0>>/L<<374.0,281.0>--<543.0,281.0>> = 9.540381804842612

	* Bbarredsmall (U+1D03): L<<543.0,271.0>--<402.0,271.0>>/B<<402.0,271.0>-<462.0,258.0>-<488.5,226.0>> = 12.225122675735754

	* Ereversedopen (U+A7AB): B<<445.5,430.0>-<401.0,384.0>-<319.0,371.0>>/B<<319.0,371.0>-<404.0,368.0>-<456.0,322.5>> = 11.029868682381167

	* Wanglicana (U+A7C2): B<<520.0,655.5>-<509.0,601.0>-<504.0,548.0>>/B<<504.0,548.0>-<519.0,592.0>-<542.0,630.0>> = 13.435398258266643

	* chi (U+03C7): L<<277.0,88.0>--<212.0,-22.0>>/L<<212.0,-22.0>--<271.0,102.0>> = 5.133820375940136

	* chi (U+03C7): L<<305.0,180.0>--<361.0,354.0>>/L<<361.0,354.0>--<333.0,183.0>> = 8.540962625640045

	* three (U+0033): B<<418.0,433.5>-<367.0,388.0>-<291.0,378.0>>/B<<291.0,378.0>-<349.0,374.0>-<395.0,355.0>> = 11.441043868767382

	* uni0190 (U+0190): B<<115.0,318.0>-<163.0,363.0>-<256.0,371.0>>/B<<256.0,371.0>-<167.0,380.0>-<124.0,425.0>> = 10.690891908673265 

	* And 39 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<63.0,-240.0>--<66.0,117.0>>

	* beta (U+03B2): L<<66.0,117.0>--<65.0,549.0>>

	* eta (U+03B7): L<<197.0,313.0>--<198.0,0.0>>

	* eta (U+03B7): L<<515.0,353.0>--<519.0,-240.0>>

	* etatonos (U+03AE): L<<197.0,313.0>--<198.0,0.0>>

	* etatonos (U+03AE): L<<515.0,353.0>--<519.0,-240.0>>

	* iota (U+03B9): L<<128.0,536.0>--<127.0,115.0>>

	* iotadieresis (U+03CA): L<<128.0,536.0>--<127.0,115.0>>

	* iotadieresistonos (U+0390): L<<128.0,536.0>--<127.0,115.0>>

	* iotatonos (U+03AF): L<<128.0,536.0>--<127.0,115.0>> 

	* And 95 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uniA716
	* phi
	* uni1FAA
	* uni1F64
	* uni1FE3 and 86 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Light' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<517.0,156.0>--<479.0,0.0>> -> L<<479.0,0.0>--<463.0,-57.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<40.0,117.0>> -> L<<40.0,117.0>--<131.0,549.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<24.0,83.0>> -> L<<24.0,83.0>--<62.0,267.0>>

	* uni03BC (U+03BC): L<<-36.0,-240.0>--<45.0,131.0>> -> L<<45.0,131.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-13.0,-85.0>--<24.0,83.0>> -> L<<24.0,83.0>--<62.0,267.0>>

	* uni1D0B (U+1D0B): L<<208.0,469.0>--<167.0,284.0>> -> L<<167.0,284.0>--<152.0,217.0>>

	* uni1D5D (U+1D5D): L<<-6.0,143.0>--<45.0,357.0>> -> L<<45.0,357.0>--<104.0,617.0>>

	* uni1D66 (U+1D66): L<<-87.0,-240.0>--<-36.0,-26.0>> -> L<<-36.0,-26.0>--<23.0,234.0>>

	* uni1D68 (U+1D68): L<<-83.0,-240.0>--<-36.0,-46.0>> -> L<<-36.0,-46.0>--<-12.0,64.0>>

	* uni1D9A (U+1D9A): L<<422.0,525.0>--<161.0,296.0>> -> L<<161.0,296.0>--<160.0,295.0>> 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<403.5,551.5>-<373.0,525.0>-<326.0,516.0>>/L<<326.0,516.0>--<446.0,516.0>> = 10.840305454330565

	* Bbarredmod (U+1D2F): L<<444.0,507.0>--<326.0,507.0>>/B<<326.0,507.0>-<364.0,499.0>-<385.0,477.5>> = 11.888658039627968

	* Bbarredsmall (U+1D03): B<<477.0,421.0>-<477.0,311.0>-<345.0,286.0>>/L<<345.0,286.0>--<485.0,286.0>> = 10.724448537471174

	* Bbarredsmall (U+1D03): L<<483.0,276.0>--<337.0,276.0>>/B<<337.0,276.0>-<391.0,266.0>-<421.0,238.5>> = 10.491477012331599

	* Ereversedopen (U+A7AB): B<<444.5,397.5>-<394.0,372.0>-<331.0,366.0>>/B<<331.0,366.0>-<373.0,360.0>-<412.5,342.5>> = 13.570434385161475

	* chi (U+03C7): L<<221.0,88.0>--<133.0,-22.0>>/L<<133.0,-22.0>--<218.0,102.0>> = 4.22979947491706

	* chi (U+03C7): L<<268.0,180.0>--<361.0,354.0>>/L<<361.0,354.0>--<297.0,183.0>> = 7.604418222465043

	* eopenmod (U+1D4B): L<<169.0,458.0>--<169.0,458.0>>/B<<169.0,458.0>-<99.0,470.0>-<99.0,523.0>> = 9.727578551401587

	* iotifiedbigyuscombcy (U+2DFF): B<<52.5,691.0>-<62.0,698.0>-<78.0,700.0>>/L<<78.0,700.0>--<-23.0,700.0>> = 7.125016348901757

	* three (U+0033): B<<446.5,443.5>-<390.0,388.0>-<289.0,376.0>>/B<<289.0,376.0>-<361.0,370.0>-<406.5,329.5>> = 11.539297860125181 

	* And 30 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-Medium.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1FAA and 142 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<571.0,184.0>--<564.0,0.0>> -> L<<564.0,0.0>--<564.0,-40.0>>

	* beta (U+03B2): L<<74.0,-240.0>--<78.0,119.0>> -> L<<78.0,119.0>--<74.0,534.0>>

	* cpalatalhook (U+A794): L<<467.0,95.0>--<467.0,95.0>> -> L<<467.0,95.0>--<467.0,95.0>>

	* dzdigraphretroflexhook (U+AB66): L<<934.0,167.0>--<928.0,0.0>> -> L<<928.0,0.0>--<928.0,-36.0>>

	* rho (U+03C1): L<<58.0,-240.0>--<64.0,113.0>> -> L<<64.0,113.0>--<63.0,249.0>>

	* uni0290 (U+0290): L<<467.0,167.0>--<461.0,33.0>> -> L<<461.0,33.0>--<461.0,-46.0>>

	* uni03BC (U+03BC): L<<75.0,-240.0>--<78.0,112.0>> -> L<<78.0,112.0>--<73.0,536.0>>

	* uni03FC (U+03FC): L<<60.0,-80.0>--<64.0,113.0>> -> L<<64.0,113.0>--<63.0,249.0>>

	* uni1D5D (U+1D5D): L<<48.0,143.0>--<51.0,358.0>> -> L<<51.0,358.0>--<48.0,607.0>>

	* uni1D66 (U+1D66): L<<48.0,-144.0>--<51.0,71.0>> -> L<<51.0,71.0>--<48.0,320.0>> 

	* And 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<374.0,612.0>-<374.0,526.0>-<254.0,515.0>>/L<<254.0,515.0>--<406.0,515.0>> = 5.237476066812514

	* Bbarredmod (U+1D2F): L<<406.0,509.0>--<287.0,509.0>>/B<<287.0,509.0>-<342.0,500.0>-<367.5,472.0>> = 9.29330859939709

	* Bbarredsmall (U+1D03): B<<526.0,405.0>-<526.0,296.0>-<387.0,281.0>>/L<<387.0,281.0>--<575.0,281.0>> = 6.159163029143023

	* Bbarredsmall (U+1D03): L<<575.0,271.0>--<429.0,271.0>>/B<<429.0,271.0>-<491.0,259.0>-<520.5,227.0>> = 10.954062643398332

	* Ereversedopen (U+A7AB): B<<477.0,429.0>-<423.0,382.0>-<317.0,371.0>>/B<<317.0,371.0>-<431.0,371.0>-<492.0,325.5>> = 5.9245819819824845

	* eogonek (U+0119): B<<257.5,-62.5>-<287.0,-29.0>-<351.0,-5.0>>/B<<351.0,-5.0>-<320.0,-10.0>-<297.0,-10.0>> = 11.393698173861749

	* iotifiedbigyuscombcy (U+2DFF): B<<-28.0,719.5>-<-18.0,727.0>-<0.0,730.0>>/L<<0.0,730.0>--<-112.0,730.0>> = 9.462322208025613

	* three (U+0033): B<<429.0,438.5>-<379.0,390.0>-<273.0,378.0>>/B<<273.0,378.0>-<387.0,374.0>-<445.5,327.0>> = 8.468370191739762

	* uni00B5 (U+00B5): B<<162.5,22.0>-<120.0,54.0>-<105.0,122.0>>/B<<105.0,122.0>-<105.0,23.0>-<117.5,-35.5>> = 12.439562018846544

	* uni0190 (U+0190): B<<110.5,321.0>-<171.0,365.0>-<276.0,372.0>>/B<<276.0,372.0>-<177.0,379.0>-<124.5,424.0>> = 7.85856040847145 

	* And 31 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Lstrokesmall (U+1D0C): L<<475.0,171.0>--<474.0,0.0>>

	* eta (U+03B7): L<<233.0,317.0>--<234.0,0.0>>

	* eta (U+03B7): L<<549.0,352.0>--<554.0,-240.0>>

	* etatonos (U+03AE): L<<233.0,317.0>--<234.0,0.0>>

	* etatonos (U+03AE): L<<549.0,352.0>--<554.0,-240.0>>

	* iota (U+03B9): L<<184.0,536.0>--<181.0,115.0>>

	* iota (U+03B9): L<<74.0,104.0>--<73.0,536.0>>

	* iotadieresis (U+03CA): L<<184.0,536.0>--<181.0,115.0>>

	* iotadieresis (U+03CA): L<<74.0,104.0>--<73.0,536.0>>

	* iotadieresistonos (U+0390): L<<184.0,536.0>--<181.0,115.0>> 

	* And 104 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1FAA
	* uni1F64 and 121 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<567.0,184.0>--<523.0,0.0>> -> L<<523.0,0.0>--<513.0,-36.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<42.0,119.0>> -> L<<42.0,119.0>--<127.0,534.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<32.0,113.0>> -> L<<32.0,113.0>--<60.0,249.0>>

	* uni03BC (U+03BC): L<<-35.0,-240.0>--<43.0,112.0>> -> L<<43.0,112.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-12.0,-80.0>--<32.0,113.0>> -> L<<32.0,113.0>--<60.0,249.0>>

	* uni1D0B (U+1D0B): L<<264.0,476.0>--<222.0,292.0>> -> L<<222.0,292.0>--<207.0,224.0>>

	* uni1D5D (U+1D5D): L<<3.0,143.0>--<54.0,358.0>> -> L<<54.0,358.0>--<110.0,607.0>>

	* uni1D66 (U+1D66): L<<-79.0,-240.0>--<-28.0,-25.0>> -> L<<-28.0,-25.0>--<28.0,224.0>>

	* uni1D68 (U+1D68): L<<-83.0,-240.0>--<-31.0,-28.0>> -> L<<-31.0,-28.0>--<-13.0,53.0>>

	* uni1DE9 (U+1DE9): L<<-50.0,586.0>--<-15.0,730.0>> -> L<<-15.0,730.0>--<24.0,895.0>>

	* uni1FE4 (U+1FE4): L<<-48.0,-240.0>--<32.0,113.0>> -> L<<32.0,113.0>--<60.0,249.0>> 

	* And uni1FE5 (U+1FE5): L<<-48.0,-240.0>--<32.0,113.0>> -> L<<32.0,113.0>--<60.0,249.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<425.0,552.5>-<393.0,526.0>-<340.0,517.0>>/L<<340.0,517.0>--<468.0,517.0>> = 9.637538112930923

	* Bbarredmod (U+1D2F): L<<465.0,507.0>--<347.0,507.0>>/B<<347.0,507.0>-<430.0,490.0>-<430.0,420.0>> = 11.575188817396182

	* Bbarredsmall (U+1D03): B<<520.0,423.0>-<520.0,310.0>-<373.0,286.0>>/L<<373.0,286.0>--<528.0,286.0>> = 9.272601777200284

	* Bbarredsmall (U+1D03): L<<526.0,276.0>--<370.0,276.0>>/B<<370.0,276.0>-<433.0,266.0>-<462.0,235.5>> = 9.019322431381651

	* Ereversedopen (U+A7AB): B<<452.0,399.0>-<392.0,376.0>-<320.0,369.0>>/B<<320.0,369.0>-<372.0,365.0>-<420.5,349.5>> = 9.951676388032272

	* three (U+0033): B<<472.0,443.0>-<406.0,389.0>-<287.0,374.0>>/B<<287.0,374.0>-<382.0,368.0>-<434.5,329.0>> = 10.798148144430469

	* uni00B5 (U+00B5): B<<116.5,24.5>-<79.0,59.0>-<77.0,134.0>>/B<<77.0,134.0>-<67.0,87.0>-<59.0,49.0>> = 13.539003828578338

	* uni024C (U+024C): L<<132.0,334.0>--<34.0,337.0>>/L<<34.0,337.0>--<78.0,344.0>> = 10.79288766342662

	* uni0377 (U+0377): B<<403.5,282.5>-<430.0,373.0>-<474.0,469.0>>/L<<474.0,469.0>--<111.0,0.0>> = 13.115847915308922

	* uni0417 (U+0417): B<<452.0,399.0>-<392.0,376.0>-<320.0,369.0>>/B<<320.0,369.0>-<372.0,365.0>-<420.5,349.5>> = 9.951676388032272 

	* And 29 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1FAA and 138 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Ustroke (U+A7B8): L<<597.0,206.0>--<597.0,636.0>> -> L<<597.0,636.0>--<597.0,638.0>>

	* Zpalatalhook (U+A7C6): L<<551.0,175.0>--<545.0,0.0>> -> L<<545.0,0.0>--<545.0,-50.0>>

	* beta (U+03B2): L<<68.0,-240.0>--<72.0,116.0>> -> L<<72.0,116.0>--<70.0,536.0>>

	* dzdigraphretroflexhook (U+AB66): L<<905.0,162.0>--<899.0,0.0>> -> L<<899.0,0.0>--<899.0,-45.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<60.0,109.0>> -> L<<60.0,109.0>--<59.0,243.0>>

	* uni0290 (U+0290): L<<455.0,162.0>--<449.0,29.0>> -> L<<449.0,29.0>--<449.0,-49.0>>

	* uni03BC (U+03BC): L<<70.0,-240.0>--<73.0,126.0>> -> L<<73.0,126.0>--<68.0,536.0>>

	* uni03FC (U+03FC): L<<56.0,-80.0>--<60.0,109.0>> -> L<<60.0,109.0>--<59.0,243.0>>

	* uni1D5D (U+1D5D): L<<44.0,143.0>--<47.0,357.0>> -> L<<47.0,357.0>--<46.0,609.0>>

	* uni1D66 (U+1D66): L<<44.0,-144.0>--<47.0,70.0>> -> L<<47.0,70.0>--<46.0,322.0>> 

	* And 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<366.0,613.0>-<366.0,528.0>-<254.0,515.0>>/L<<254.0,515.0>--<400.0,515.0>> = 6.620776082314981

	* Bbarredmod (U+1D2F): L<<400.0,509.0>--<279.0,509.0>>/B<<279.0,509.0>-<336.0,500.0>-<360.5,472.0>> = 8.972626614896399

	* Bbarredsmall (U+1D03): B<<516.0,404.0>-<516.0,296.0>-<383.0,281.0>>/L<<383.0,281.0>--<567.0,281.0>> = 6.434739151036698

	* Bbarredsmall (U+1D03): L<<567.0,271.0>--<423.0,271.0>>/B<<423.0,271.0>-<483.0,258.0>-<511.5,225.5>> = 12.225122675735754

	* Ereversedopen (U+A7AB): B<<469.0,429.0>-<416.0,382.0>-<315.0,371.0>>/B<<315.0,371.0>-<424.0,371.0>-<483.0,324.5>> = 6.215635899702654

	* iotifiedbigyuscombcy (U+2DFF): B<<-25.5,719.5>-<-15.0,727.0>-<4.0,731.0>>/L<<4.0,731.0>--<-107.0,731.0>> = 11.888658039627968

	* three (U+0033): B<<425.5,439.5>-<375.0,393.0>-<276.0,380.0>>/B<<276.0,380.0>-<388.0,375.0>-<444.5,327.0>> = 10.03703625810195

	* uni00B5 (U+00B5): B<<163.5,21.5>-<121.0,53.0>-<106.0,119.0>>/B<<106.0,119.0>-<106.0,21.0>-<118.0,-37.0>> = 12.80426606528674

	* uni0190 (U+0190): B<<112.0,318.5>-<168.0,364.0>-<277.0,371.0>>/B<<277.0,371.0>-<180.0,376.0>-<128.0,422.0>> = 6.625278629835983

	* uni0223 (U+0223): B<<436.0,483.0>-<403.0,456.0>-<345.0,450.0>>/B<<345.0,450.0>-<437.0,439.0>-<479.5,381.0>> = 12.724355685422363 

	* And 45 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<72.0,116.0>--<70.0,536.0>>

	* eta (U+03B7): L<<547.0,350.0>--<552.0,-240.0>>

	* etatonos (U+03AE): L<<547.0,350.0>--<552.0,-240.0>>

	* kappa (U+03BA): L<<138.0,160.0>--<137.0,0.0>>

	* kappa (U+03BA): L<<142.0,536.0>--<139.0,178.0>>

	* rho (U+03C1): L<<60.0,109.0>--<59.0,243.0>>

	* uni03BC (U+03BC): L<<390.0,176.0>--<387.0,536.0>>

	* uni03BC (U+03BC): L<<70.0,-240.0>--<73.0,126.0>>

	* uni03D7 (U+03D7): L<<138.0,160.0>--<137.0,0.0>>

	* uni03D7 (U+03D7): L<<142.0,536.0>--<139.0,178.0>> 

	* And 29 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-SemiBold.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni03D0
	* uniA7FD
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi
	* uni1F2F and 169 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<595.0,194.0>--<588.0,0.0>> -> L<<588.0,0.0>--<588.0,-27.0>>

	* beta (U+03B2): L<<82.0,-240.0>--<86.0,122.0>> -> L<<86.0,122.0>--<79.0,530.0>>

	* cpalatalhook (U+A794): L<<480.0,97.0>--<480.0,97.0>> -> L<<480.0,97.0>--<480.0,97.0>>

	* dzdigraphretroflexhook (U+AB66): L<<970.0,174.0>--<964.0,0.0>> -> L<<964.0,0.0>--<964.0,-25.0>>

	* rho (U+03C1): L<<64.0,-240.0>--<69.0,117.0>> -> L<<69.0,117.0>--<68.0,255.0>>

	* uni0290 (U+0290): L<<482.0,174.0>--<476.0,38.0>> -> L<<476.0,38.0>--<476.0,-43.0>>

	* uni03BC (U+03BC): L<<81.0,-240.0>--<85.0,94.0>> -> L<<85.0,94.0>--<79.0,536.0>>

	* uni03FC (U+03FC): L<<66.0,-81.0>--<69.0,117.0>> -> L<<69.0,117.0>--<68.0,255.0>>

	* uni1D5D (U+1D5D): L<<53.0,143.0>--<56.0,360.0>> -> L<<56.0,360.0>--<52.0,605.0>>

	* uni1D66 (U+1D66): L<<53.0,-144.0>--<56.0,73.0>> -> L<<56.0,73.0>--<52.0,318.0>> 

	* And 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Aogonek (U+0104): L<<633.0,0.0>--<661.0,0.0>>/B<<661.0,0.0>-<616.0,-11.0>-<591.0,-41.5>> = 13.736268305622554

	* Bbarredmod (U+1D2F): B<<349.0,541.5>-<315.0,518.0>-<252.0,514.0>>/L<<252.0,514.0>--<412.0,514.0>> = 3.6329507394881446

	* Bbarredmod (U+1D2F): L<<412.0,508.0>--<297.0,508.0>>/B<<297.0,508.0>-<403.0,490.0>-<403.0,402.0>> = 9.637538112930923

	* Bbarredsmall (U+1D03): B<<538.0,406.0>-<538.0,296.0>-<391.0,281.0>>/L<<391.0,281.0>--<584.0,281.0>> = 5.826342029555751

	* Bbarredsmall (U+1D03): L<<584.0,272.0>--<436.0,272.0>>/B<<436.0,272.0>-<502.0,260.0>-<533.0,229.0>> = 10.304846468766009

	* Eogonek (U+0118): L<<502.0,0.0>--<530.0,0.0>>/B<<530.0,0.0>-<485.0,-11.0>-<460.0,-41.5>> = 13.736268305622554

	* Ereversedopen (U+A7AB): B<<487.5,429.0>-<432.0,381.0>-<320.0,371.0>>/B<<320.0,371.0>-<440.0,371.0>-<503.0,326.0>> = 5.102165252358147

	* Iogonek (U+012E): L<<250.0,0.0>--<278.0,0.0>>/B<<278.0,0.0>-<233.0,-11.0>-<208.0,-41.5>> = 13.736268305622554

	* Uogonek (U+0172): L<<433.0,0.0>--<461.0,0.0>>/B<<461.0,0.0>-<416.0,-11.0>-<391.0,-41.5>> = 13.736268305622554

	* aogonek (U+0105): L<<418.0,0.0>--<446.0,0.0>>/B<<446.0,0.0>-<401.0,-11.0>-<376.0,-41.5>> = 13.736268305622554 

	* And 60 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<552.0,354.0>--<557.0,-240.0>>

	* etatonos (U+03AE): L<<552.0,354.0>--<557.0,-240.0>>

	* iota (U+03B9): L<<82.0,128.0>--<79.0,536.0>>

	* iotadieresis (U+03CA): L<<82.0,128.0>--<79.0,536.0>>

	* iotadieresistonos (U+0390): L<<82.0,128.0>--<79.0,536.0>>

	* iotatonos (U+03AF): L<<82.0,128.0>--<79.0,536.0>>

	* kappa (U+03BA): L<<63.0,0.0>--<59.0,536.0>>

	* rho (U+03C1): L<<69.0,117.0>--<68.0,255.0>>

	* uni019B (U+019B): L<<140.0,1.0>--<3.0,0.0>>

	* uni0269 (U+0269): L<<82.0,128.0>--<79.0,536.0>> 

	* And 47 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* four
	* upsilon
	* uni03D0
	* uni1FFC
	* uni1FBE
	* uni1F87
	* uniA716
	* phi and 145 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<587.0,194.0>--<542.0,0.0>> -> L<<542.0,0.0>--<533.0,-34.0>>

	* beta (U+03B2): L<<-37.0,-240.0>--<43.0,122.0>> -> L<<43.0,122.0>--<126.0,530.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<32.0,117.0>> -> L<<32.0,117.0>--<60.0,255.0>>

	* uni03BC (U+03BC): L<<-34.0,-240.0>--<39.0,94.0>> -> L<<39.0,94.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-12.0,-81.0>--<32.0,117.0>> -> L<<32.0,117.0>--<60.0,255.0>>

	* uni1D0B (U+1D0B): L<<285.0,478.0>--<244.0,296.0>> -> L<<244.0,296.0>--<230.0,234.0>>

	* uni1D5D (U+1D5D): L<<6.0,143.0>--<58.0,360.0>> -> L<<58.0,360.0>--<112.0,605.0>>

	* uni1D66 (U+1D66): L<<-76.0,-240.0>--<-24.0,-23.0>> -> L<<-24.0,-23.0>--<30.0,222.0>>

	* uni1D68 (U+1D68): L<<-83.0,-240.0>--<-31.0,-26.0>> -> L<<-31.0,-26.0>--<-13.0,57.0>>

	* uni1DE9 (U+1DE9): L<<-52.0,586.0>--<-16.0,731.0>> -> L<<-16.0,731.0>--<22.0,894.0>> 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<435.0,553.5>-<404.0,527.0>-<349.0,517.0>>/L<<349.0,517.0>--<477.0,517.0>> = 10.304846468766044

	* Bbarredmod (U+1D2F): L<<476.0,507.0>--<351.0,507.0>>/B<<351.0,507.0>-<439.0,491.0>-<439.0,419.0>> = 10.304846468766044

	* Bbarredsmall (U+1D03): B<<537.0,424.0>-<537.0,311.0>-<385.0,287.0>>/L<<385.0,287.0>--<552.0,287.0>> = 8.972626614896358

	* Bbarredsmall (U+1D03): L<<549.0,277.0>--<382.0,277.0>>/B<<382.0,277.0>-<446.0,267.0>-<476.0,237.5>> = 8.880659150520234

	* Ereversedopen (U+A7AB): B<<457.0,402.0>-<395.0,379.0>-<321.0,371.0>>/B<<321.0,371.0>-<383.0,366.0>-<433.5,350.5>> = 10.780824413690203

	* hardsigntallcy (U+1C86): B<<302.5,616.0>-<373.0,685.0>-<449.0,739.0>>/B<<449.0,739.0>-<424.0,729.0>-<379.5,722.5>> = 13.593386358635234

	* iotifiedbigyuscombcy (U+2DFF): B<<38.5,688.5>-<50.0,697.0>-<68.0,701.0>>/L<<68.0,701.0>--<-38.0,701.0>> = 12.528807709151492

	* three (U+0033): B<<422.5,408.5>-<363.0,383.0>-<285.0,374.0>>/B<<285.0,374.0>-<389.0,366.0>-<443.5,330.0>> = 10.980650010173553

	* uni024C (U+024C): L<<89.0,336.0>--<39.0,342.0>>/L<<39.0,342.0>--<135.0,346.0>> = 9.228717443019724

	* uni0377 (U+0377): B<<412.0,279.5>-<438.0,362.0>-<476.0,439.0>>/L<<476.0,439.0>--<124.0,0.0>> = 12.456778840635982 

	* And 32 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] NotoSerifDisplay-Thin.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uniA7FD
	* uni1FFC
	* uniA716
	* uni1FAA
	* uni1F64
	* uni1FA8
	* uni1F7C
	* uni0295 and 73 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Thin' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

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

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 4	Expected: 3 

	- And 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<458.0,135.0>--<453.0,0.0>> -> L<<453.0,0.0>--<453.0,-107.0>>

	* beta (U+03B2): L<<56.0,-240.0>--<58.0,118.0>> -> L<<58.0,118.0>--<58.0,565.0>>

	* dzdigraphretroflexhook (U+AB66): L<<801.0,138.0>--<796.0,0.0>> -> L<<796.0,0.0>--<796.0,-107.0>>

	* rho (U+03C1): L<<41.0,-240.0>--<43.0,51.0>> -> L<<43.0,51.0>--<43.0,296.0>>

	* uni01A5 (U+01A5): L<<150.0,647.0>--<149.0,536.0>> -> L<<149.0,536.0>--<149.0,392.0>>

	* uni023E (U+023E): L<<462.0,699.0>--<455.0,699.0>> -> L<<455.0,699.0>--<293.0,699.0>>

	* uni0246 (U+0246): L<<425.0,704.0>--<422.0,704.0>> -> L<<422.0,704.0>--<177.0,704.0>>

	* uni0290 (U+0290): L<<408.0,138.0>--<403.0,0.0>> -> L<<403.0,0.0>--<403.0,-101.0>>

	* uni03BC (U+03BC): L<<56.0,-240.0>--<58.0,136.0>> -> L<<58.0,136.0>--<56.0,536.0>>

	* uni03FC (U+03FC): L<<42.0,-90.0>--<43.0,51.0>> -> L<<43.0,51.0>--<43.0,296.0>> 

	* And 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<306.5,543.5>-<282.0,523.0>-<248.0,516.0>>/L<<248.0,516.0>--<370.0,516.0>> = 11.633633998940427

	* Bbarredmod (U+1D2F): L<<370.0,510.0>--<269.0,510.0>>/B<<269.0,510.0>-<350.0,492.0>-<350.0,407.0>> = 12.528807709151492

	* Bbarredsmall (U+1D03): B<<438.5,324.0>-<411.0,293.0>-<360.0,280.0>>/L<<360.0,280.0>--<515.0,280.0>> = 14.300277449185575

	* Bbarredsmall (U+1D03): L<<515.0,270.0>--<377.0,270.0>>/B<<377.0,270.0>-<438.0,257.0>-<462.0,226.5>> = 12.030596096537845

	* Wanglicana (U+A7C2): B<<419.0,478.0>-<419.0,467.0>-<419.0,456.0>>/L<<419.0,456.0>--<434.0,516.0>> = 14.036243467926484

	* eogonek (U+0119): B<<225.5,-56.5>-<247.0,-27.0>-<284.0,-9.0>>/B<<284.0,-9.0>-<280.0,-10.0>-<275.5,-10.0>> = 11.906052021945184

	* eth (U+00F0): B<<385.5,450.5>-<412.0,431.0>-<428.0,400.0>>/B<<428.0,400.0>-<406.0,480.0>-<377.0,541.5>> = 11.923320962506626

	* three (U+0033): B<<377.0,401.5>-<342.0,380.0>-<310.0,375.0>>/B<<310.0,375.0>-<339.0,373.0>-<369.5,364.0>> = 12.825845379557801

	* uni0238 (U+0238): B<<465.0,90.5>-<446.0,133.0>-<438.0,203.0>>/B<<438.0,203.0>-<430.0,132.0>-<410.5,89.5>> = 12.948549500486775

	* uni0239 (U+0239): B<<411.0,447.0>-<431.0,406.0>-<439.0,337.0>>/B<<439.0,337.0>-<447.0,406.0>-<466.5,447.0>> = 13.226920964629533 

	* And 26 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<56.0,-240.0>--<58.0,118.0>>

	* beta (U+03B2): L<<86.0,149.0>--<88.0,-240.0>>

	* eta (U+03B7): L<<448.0,-240.0>--<451.0,357.0>>

	* eta (U+03B7): L<<476.0,357.0>--<480.0,-240.0>>

	* etatonos (U+03AE): L<<448.0,-240.0>--<451.0,357.0>>

	* etatonos (U+03AE): L<<476.0,357.0>--<480.0,-240.0>>

	* iota (U+03B9): L<<58.0,137.0>--<56.0,536.0>>

	* iota (U+03B9): L<<88.0,536.0>--<86.0,137.0>>

	* iotadieresis (U+03CA): L<<58.0,137.0>--<56.0,536.0>>

	* iotadieresis (U+03CA): L<<88.0,536.0>--<86.0,137.0>> 

	* And 139 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-ThinItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* uni1FBC
	* uni1F60
	* uni1FFC
	* uniA716
	* uni1FAA
	* uni1F64
	* uni1FA8
	* uni03C5030403130301
	* uni1F7C
	* uni1FAB and 65 more.

Use -F or --full-lists to disable shortening of long lists.
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif Display Thin' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01E5	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3 

	- And 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<478.0,134.0>--<444.0,0.0>> -> L<<444.0,0.0>--<422.0,-81.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<39.0,118.0>> -> L<<39.0,118.0>--<134.0,565.0>>

	* estecombcy (U+2DF5): L<<166.0,777.0>--<166.0,777.0>> -> L<<166.0,777.0>--<167.0,777.0>>

	* rho (U+03C1): L<<-48.0,-240.0>--<15.0,51.0>> -> L<<15.0,51.0>--<66.0,296.0>>

	* tripledagger (U+2E4B): L<<48.0,341.0>--<206.0,331.0>> -> L<<206.0,331.0>--<206.0,331.0>>

	* uni03BC (U+03BC): L<<-37.0,-240.0>--<44.0,136.0>> -> L<<44.0,136.0>--<127.0,536.0>>

	* uni03FC (U+03FC): L<<-16.0,-90.0>--<15.0,51.0>> -> L<<15.0,51.0>--<66.0,296.0>>

	* uni1D0B (U+1D0B): L<<161.0,461.0>--<122.0,277.0>> -> L<<122.0,277.0>--<109.0,216.0>>

	* uni1D5D (U+1D5D): L<<-13.0,143.0>--<37.0,358.0>> -> L<<37.0,358.0>--<99.0,626.0>>

	* uni1D66 (U+1D66): L<<-94.0,-240.0>--<-44.0,-25.0>> -> L<<-44.0,-25.0>--<18.0,243.0>> 

	* And 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Bbarredmod (U+1D2F): B<<388.0,552.5>-<362.0,526.0>-<319.0,517.0>>/L<<319.0,517.0>--<430.0,517.0>> = 11.821488340607226

	* Bbarredsmall (U+1D03): B<<409.5,332.5>-<377.0,299.0>-<322.0,287.0>>/L<<322.0,287.0>--<455.0,287.0>> = 12.308015817427924

	* Bbarredsmall (U+1D03): L<<452.0,277.0>--<309.0,277.0>>/B<<309.0,277.0>-<338.0,271.0>-<362.5,259.5>> = 11.689369175439202

	* iotifiedbigyuscombcy (U+2DFF): B<<66.0,693.0>-<74.0,696.0>-<87.0,698.0>>/L<<87.0,698.0>--<-14.0,698.0>> = 8.746162262555211

	* kacombcy (U+2DE6): B<<91.0,706.0>-<79.0,696.0>-<66.0,694.0>>/B<<66.0,694.0>-<91.0,694.0>-<101.5,686.0>> = 8.746162262555211

	* three (U+0033): B<<383.5,410.0>-<343.0,383.0>-<291.0,377.0>>/B<<291.0,377.0>-<325.0,373.0>-<354.5,353.5>> = 13.291781462934923

	* uni024A (U+024A): B<<501.5,670.5>-<549.0,616.0>-<552.0,498.0>>/L<<552.0,498.0>--<597.0,714.0>> = 13.22464756636032

	* uni024A (U+024A): L<<431.0,-64.0>--<487.0,197.0>>/B<<487.0,197.0>-<442.0,82.0>-<381.0,34.5>> = 9.260874146228073

	* uni0275 (U+0275): L<<73.0,268.0>--<73.0,270.0>>/B<<73.0,270.0>-<66.0,229.0>-<66.0,190.0>> = 9.68878656036679

	* uni0432 (U+0432): B<<335.0,317.0>-<287.0,298.0>-<233.0,290.0>>/B<<233.0,290.0>-<313.0,282.0>-<362.5,251.0>> = 14.137562158980275 

	* And 35 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] NotoSerifDisplay-Italic[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x2212 (MINUS SIGN)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wght_coord">com.google.fonts/check/varfont/regular_wght_coord</a>)</summary><div>


* 🔥 **FAIL** The "wght" axis coordinate of the "Regular" instance must be 400. Got None instead. [code: wght-not-400]
</div></details><details><summary>🔥 <b>FAIL:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord">com.google.fonts/check/varfont/regular_wdth_coord</a>)</summary><div>


* 🔥 **FAIL** The "wdth" axis coordinate of the "Regular" instance must be 100. Got None as a default value instead. [code: wdth-not-100]
</div></details><details><summary>🔥 <b>FAIL:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord">com.google.fonts/check/varfont/bold_wght_coord</a>)</summary><div>


* 🔥 **FAIL** The "wght" axis coordinate of the "Bold" instance must be 700. Got None instead. [code: wght-not-700]
</div></details><details><summary>🔥 <b>FAIL:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to either 2 or 17, and its postScriptNameID value is set to 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>


* 🔥 **FAIL** 'Italic' instance has the same coordinates as the default instance; its subfamilyNameID should be either 2 or 17, instead of 297. [code: invalid-default-instance-subfamily-nameid:297]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.2Mb; ideally it should be less than 1.0Mb [code: large-font]
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

	- And l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni1FCE02C9

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod 

	- And 35 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><br></div></details><details><summary><b>[8] NotoSerifDisplay[wdth,wght].ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 💔 **ERROR** Failed with IndexError: list index out of range
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1143, but got 1069 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 1910, but got 293 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to either 2 or 17, and its postScriptNameID value is set to 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>


* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its subfamilyNameID should be either 2 or 17, instead of 288. [code: invalid-default-instance-subfamily-nameid:288]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.1Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- And i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- uni03B9030603140301

	- uni03B9030603140300

	- uni03B1030403140300

	- uni03C5030403130301

	- uni03C5030603130301

	- uni03B1030403140301

	- uni03B9030403130300

	- uni03B1030603130300

	- dasiavaria_macronmod

	- uni03B1030403130300 

	- And 31 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni0488 (U+0488), uni0489 (U+0489), uni1ABE (U+1ABE), uniA670 (U+A670), uniA671 (U+A671) and uniA672 (U+A672) [code: mark-chars]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 10 | 37 | 178 | 2208 | 123 | 1859 | 0 |
| 0% | 1% | 4% | 50% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
