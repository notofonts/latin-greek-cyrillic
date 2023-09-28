## FontBakery report

fontbakery version: 0.9.2

<details><summary><b>[16] NotoSans[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking with ots-sanitize. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ots">com.google.fonts/check/ots</a>)</summary><div>


* 🔥 **FAIL** ots-sanitize returned an error code (1). Output follows:

ERROR: GPOS: Bad mark anchor offset 0 for mark table 63
ERROR: GPOS: Failed to parse mark array
ERROR: GPOS: Failed to parse subtable 0
ERROR: GPOS: Failed to parse lookup 35
ERROR: GPOS: Failed to parse lookup list table
ERROR: GPOS: Failed to parse table
Failed to sanitize file!
 [code: ots-sanitize-error]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- ayvowelsigndeva

	- binducandradeva

	- candralongevowelsigndeva

	- oevowelsigndeva

	- uevowelsigndeva

	- uni0901

	- uni0902

	- uni093C

	- uni0941

	- uni0942

	- uni0943

	- uni0944

	- uni0945

	- uni0946

	- uni0947

	- uni0948

	- uni094D

	- uni0951

	- uni0952

	- uni0953

	- uni0954

	- uni0962

	- uni0963

	- uuevowelsigndeva [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02B0 MODIFIER LETTER SMALL H: not included in any glyphset definition
 * U+02B1 MODIFIER LETTER SMALL H WITH HOOK: not included in any glyphset definition
 * U+02B2 MODIFIER LETTER SMALL J: not included in any glyphset definition
 * U+02B3 MODIFIER LETTER SMALL R: not included in any glyphset definition
 * U+02B4 MODIFIER LETTER SMALL TURNED R: not included in any glyphset definition
 * U+02B5 MODIFIER LETTER SMALL TURNED R WITH HOOK: not included in any glyphset definition
 * U+02B6 MODIFIER LETTER SMALL CAPITAL INVERTED R: not included in any glyphset definition
 * U+02B7 MODIFIER LETTER SMALL W: not included in any glyphset definition
 * U+02B8 MODIFIER LETTER SMALL Y: not included in any glyphset definition
 * U+02B9 MODIFIER LETTER PRIME: not included in any glyphset definition
 * U+02BA MODIFIER LETTER DOUBLE PRIME: not included in any glyphset definition
 * U+02BD MODIFIER LETTER REVERSED COMMA: not included in any glyphset definition
 * U+02BE MODIFIER LETTER RIGHT HALF RING: not included in any glyphset definition
 * U+02BF MODIFIER LETTER LEFT HALF RING: not included in any glyphset definition
 * U+02C0 MODIFIER LETTER GLOTTAL STOP: not included in any glyphset definition
 * U+02C1 MODIFIER LETTER REVERSED GLOTTAL STOP: not included in any glyphset definition
 * U+02C2 MODIFIER LETTER LEFT ARROWHEAD: not included in any glyphset definition
 * U+02C3 MODIFIER LETTER RIGHT ARROWHEAD: not included in any glyphset definition
 * U+02C4 MODIFIER LETTER UP ARROWHEAD: not included in any glyphset definition
 * U+02C5 MODIFIER LETTER DOWN ARROWHEAD: not included in any glyphset definition
 * U+02C7 CARON: try adding one of: canadian-aboriginal, tifinagh, yi
 * U+02C8 MODIFIER LETTER VERTICAL LINE: not included in any glyphset definition
 * U+02C9 MODIFIER LETTER MACRON: not included in any glyphset definition
 * U+02CA MODIFIER LETTER ACUTE ACCENT: not included in any glyphset definition
 * U+02CB MODIFIER LETTER GRAVE ACCENT: not included in any glyphset definition
 * U+02CC MODIFIER LETTER LOW VERTICAL LINE: not included in any glyphset definition
 * U+02CD MODIFIER LETTER LOW MACRON: try adding lisu
 * U+02CE MODIFIER LETTER LOW GRAVE ACCENT: not included in any glyphset definition
 * U+02CF MODIFIER LETTER LOW ACUTE ACCENT: not included in any glyphset definition
 * U+02D0 MODIFIER LETTER TRIANGULAR COLON: not included in any glyphset definition
 * U+02D1 MODIFIER LETTER HALF TRIANGULAR COLON: not included in any glyphset definition
 * U+02D2 MODIFIER LETTER CENTRED RIGHT HALF RING: not included in any glyphset definition
 * U+02D3 MODIFIER LETTER CENTRED LEFT HALF RING: not included in any glyphset definition
 * U+02D4 MODIFIER LETTER UP TACK: not included in any glyphset definition
 * U+02D5 MODIFIER LETTER DOWN TACK: not included in any glyphset definition
 * U+02D6 MODIFIER LETTER PLUS SIGN: not included in any glyphset definition
 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02DE MODIFIER LETTER RHOTIC HOOK: not included in any glyphset definition
 * U+02DF MODIFIER LETTER CROSS ACCENT: not included in any glyphset definition
 * U+02E0 MODIFIER LETTER SMALL GAMMA: not included in any glyphset definition
 * U+02E1 MODIFIER LETTER SMALL L: not included in any glyphset definition
 * U+02E2 MODIFIER LETTER SMALL S: not included in any glyphset definition
 * U+02E3 MODIFIER LETTER SMALL X: not included in any glyphset definition
 * U+02E4 MODIFIER LETTER SMALL REVERSED GLOTTAL STOP: not included in any glyphset definition
 * U+02E5 MODIFIER LETTER EXTRA-HIGH TONE BAR: not included in any glyphset definition
 * U+02E6 MODIFIER LETTER HIGH TONE BAR: not included in any glyphset definition
 * U+02E7 MODIFIER LETTER MID TONE BAR: not included in any glyphset definition
 * U+02E8 MODIFIER LETTER LOW TONE BAR: not included in any glyphset definition
 * U+02E9 MODIFIER LETTER EXTRA-LOW TONE BAR: not included in any glyphset definition
 * U+02EA MODIFIER LETTER YIN DEPARTING TONE MARK: not included in any glyphset definition
 * U+02EB MODIFIER LETTER YANG DEPARTING TONE MARK: not included in any glyphset definition
 * U+02EC MODIFIER LETTER VOICING: not included in any glyphset definition
 * U+02ED MODIFIER LETTER UNASPIRATED: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+02EF MODIFIER LETTER LOW DOWN ARROWHEAD: not included in any glyphset definition
 * U+02F0 MODIFIER LETTER LOW UP ARROWHEAD: not included in any glyphset definition
 * U+02F1 MODIFIER LETTER LOW LEFT ARROWHEAD: not included in any glyphset definition
 * U+02F2 MODIFIER LETTER LOW RIGHT ARROWHEAD: not included in any glyphset definition
 * U+02F3 MODIFIER LETTER LOW RING: not included in any glyphset definition
 * U+02F4 MODIFIER LETTER MIDDLE GRAVE ACCENT: not included in any glyphset definition
 * U+02F5 MODIFIER LETTER MIDDLE DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+02F6 MODIFIER LETTER MIDDLE DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02F7 MODIFIER LETTER LOW TILDE: not included in any glyphset definition
 * U+02F8 MODIFIER LETTER RAISED COLON: not included in any glyphset definition
 * U+02F9 MODIFIER LETTER BEGIN HIGH TONE: not included in any glyphset definition
 * U+02FA MODIFIER LETTER END HIGH TONE: not included in any glyphset definition
 * U+02FB MODIFIER LETTER BEGIN LOW TONE: not included in any glyphset definition
 * U+02FC MODIFIER LETTER END LOW TONE: not included in any glyphset definition
 * U+02FD MODIFIER LETTER SHELF: not included in any glyphset definition
 * U+02FE MODIFIER LETTER OPEN SHELF: not included in any glyphset definition
 * U+02FF MODIFIER LETTER LOW LEFT ARROW: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee
 * U+0305 COMBINING OVERLINE: try adding one of: coptic, gothic, glagolitic, elbasan, math
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: coptic, malayalam, tai-le, old-permic, math, canadian-aboriginal, tifinagh, syriac
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: cherokee, tai-le
 * U+030D COMBINING VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+0310 COMBINING CANDRABINDU: not included in any glyphset definition
 * U+0311 COMBINING INVERTED BREVE: try adding coptic
 * U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition
 * U+0313 COMBINING COMMA ABOVE: try adding old-permic
 * U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition
 * U+0315 COMBINING COMMA ABOVE RIGHT: not included in any glyphset definition
 * U+0316 COMBINING GRAVE ACCENT BELOW: not included in any glyphset definition
 * U+0317 COMBINING ACUTE ACCENT BELOW: not included in any glyphset definition
 * U+0318 COMBINING LEFT TACK BELOW: not included in any glyphset definition
 * U+0319 COMBINING RIGHT TACK BELOW: not included in any glyphset definition
 * U+031A COMBINING LEFT ANGLE ABOVE: not included in any glyphset definition
 * U+031B COMBINING HORN: not included in any glyphset definition
 * U+031C COMBINING LEFT HALF RING BELOW: not included in any glyphset definition
 * U+031D COMBINING UP TACK BELOW: not included in any glyphset definition
 * U+031E COMBINING DOWN TACK BELOW: not included in any glyphset definition
 * U+031F COMBINING PLUS SIGN BELOW: not included in any glyphset definition
 * U+0320 COMBINING MINUS SIGN BELOW: try adding syriac
 * U+0321 COMBINING PALATALIZED HOOK BELOW: not included in any glyphset definition
 * U+0322 COMBINING RETROFLEX HOOK BELOW: not included in any glyphset definition
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition
 * U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition
 * U+032C COMBINING CARON BELOW: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee
 * U+0331 COMBINING MACRON BELOW: try adding one of: gothic, tifinagh, cherokee, syriac, caucasian-albanian
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0333 COMBINING DOUBLE LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition
 * U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0339 COMBINING RIGHT HALF RING BELOW: not included in any glyphset definition
 * U+033A COMBINING INVERTED BRIDGE BELOW: not included in any glyphset definition
 * U+033B COMBINING SQUARE BELOW: not included in any glyphset definition
 * U+033C COMBINING SEAGULL BELOW: not included in any glyphset definition
 * U+033D COMBINING X ABOVE: not included in any glyphset definition
 * U+033E COMBINING VERTICAL TILDE: not included in any glyphset definition
 * U+033F COMBINING DOUBLE OVERLINE: try adding coptic
 * U+0340 COMBINING GRAVE TONE MARK: not included in any glyphset definition
 * U+0341 COMBINING ACUTE TONE MARK: not included in any glyphset definition
 * U+0342 COMBINING GREEK PERISPOMENI: not included in any glyphset definition
 * U+0343 COMBINING GREEK KORONIS: not included in any glyphset definition
 * U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition
 * U+0345 COMBINING GREEK YPOGEGRAMMENI: not included in any glyphset definition
 * U+0346 COMBINING BRIDGE ABOVE: not included in any glyphset definition
 * U+0347 COMBINING EQUALS SIGN BELOW: not included in any glyphset definition
 * U+0348 COMBINING DOUBLE VERTICAL LINE BELOW: not included in any glyphset definition
 * U+0349 COMBINING LEFT ANGLE BELOW: not included in any glyphset definition
 * U+034A COMBINING NOT TILDE ABOVE: not included in any glyphset definition
 * U+034B COMBINING HOMOTHETIC ABOVE: not included in any glyphset definition
 * U+034C COMBINING ALMOST EQUAL TO ABOVE: not included in any glyphset definition
 * U+034D COMBINING LEFT RIGHT ARROW BELOW: not included in any glyphset definition
 * U+034E COMBINING UPWARDS ARROW BELOW: not included in any glyphset definition
 * U+034F COMBINING GRAPHEME JOINER: not included in any glyphset definition
 * U+0350 COMBINING RIGHT ARROWHEAD ABOVE: not included in any glyphset definition
 * U+0351 COMBINING LEFT HALF RING ABOVE: not included in any glyphset definition
 * U+0352 COMBINING FERMATA: not included in any glyphset definition
 * U+0353 COMBINING X BELOW: not included in any glyphset definition
 * U+0354 COMBINING LEFT ARROWHEAD BELOW: not included in any glyphset definition
 * U+0355 COMBINING RIGHT ARROWHEAD BELOW: not included in any glyphset definition
 * U+0356 COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD BELOW: not included in any glyphset definition
 * U+0357 COMBINING RIGHT HALF RING ABOVE: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+0359 COMBINING ASTERISK BELOW: not included in any glyphset definition
 * U+035A COMBINING DOUBLE RING BELOW: not included in any glyphset definition
 * U+035B COMBINING ZIGZAG ABOVE: not included in any glyphset definition
 * U+035C COMBINING DOUBLE BREVE BELOW: not included in any glyphset definition
 * U+035D COMBINING DOUBLE BREVE: not included in any glyphset definition
 * U+035E COMBINING DOUBLE MACRON: try adding coptic
 * U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition
 * U+0360 COMBINING DOUBLE TILDE: not included in any glyphset definition
 * U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
 * U+0362 COMBINING DOUBLE RIGHTWARDS ARROW BELOW: not included in any glyphset definition
 * U+0363 COMBINING LATIN SMALL LETTER A: not included in any glyphset definition
 * U+0364 COMBINING LATIN SMALL LETTER E: not included in any glyphset definition
 * U+0365 COMBINING LATIN SMALL LETTER I: not included in any glyphset definition
 * U+0366 COMBINING LATIN SMALL LETTER O: not included in any glyphset definition
 * U+0367 COMBINING LATIN SMALL LETTER U: not included in any glyphset definition
 * U+0368 COMBINING LATIN SMALL LETTER C: not included in any glyphset definition
 * U+0369 COMBINING LATIN SMALL LETTER D: not included in any glyphset definition
 * U+036A COMBINING LATIN SMALL LETTER H: not included in any glyphset definition
 * U+036B COMBINING LATIN SMALL LETTER M: not included in any glyphset definition
 * U+036C COMBINING LATIN SMALL LETTER R: not included in any glyphset definition
 * U+036D COMBINING LATIN SMALL LETTER T: not included in any glyphset definition
 * U+036E COMBINING LATIN SMALL LETTER V: not included in any glyphset definition
 * U+036F COMBINING LATIN SMALL LETTER X: not included in any glyphset definition
 * U+10FB GEORGIAN PARAGRAPH SEPARATOR: try adding georgian
 * U+1AB0 COMBINING DOUBLED CIRCUMFLEX ACCENT: not included in any glyphset definition
 * U+1AB1 COMBINING DIAERESIS-RING: not included in any glyphset definition
 * U+1AB2 COMBINING INFINITY: not included in any glyphset definition
 * U+1AB3 COMBINING DOWNWARDS ARROW: not included in any glyphset definition
 * U+1AB4 COMBINING TRIPLE DOT: not included in any glyphset definition
 * U+1AB5 COMBINING X-X BELOW: not included in any glyphset definition
 * U+1AB6 COMBINING WIGGLY LINE BELOW: not included in any glyphset definition
 * U+1AB7 COMBINING OPEN MARK BELOW: not included in any glyphset definition
 * U+1AB8 COMBINING DOUBLE OPEN MARK BELOW: not included in any glyphset definition
 * U+1AB9 COMBINING LIGHT CENTRALIZATION STROKE BELOW: not included in any glyphset definition
 * U+1ABA COMBINING STRONG CENTRALIZATION STROKE BELOW: not included in any glyphset definition
 * U+1ABB COMBINING PARENTHESES ABOVE: not included in any glyphset definition
 * U+1ABC COMBINING DOUBLE PARENTHESES ABOVE: not included in any glyphset definition
 * U+1ABD COMBINING PARENTHESES BELOW: not included in any glyphset definition
 * U+1ABE COMBINING PARENTHESES OVERLAY: not included in any glyphset definition
 * U+1ABF COMBINING LATIN SMALL LETTER W BELOW: not included in any glyphset definition
 * U+1AC0 COMBINING LATIN SMALL LETTER TURNED W BELOW: not included in any glyphset definition
 * U+1AC5 COMBINING SQUARE BRACKETS ABOVE: not included in any glyphset definition
 * U+1AC7 COMBINING INVERTED DOUBLE ARCH ABOVE: not included in any glyphset definition
 * U+1AC8 COMBINING PLUS SIGN ABOVE: not included in any glyphset definition
 * U+1AC9 COMBINING DOUBLE PLUS SIGN ABOVE: not included in any glyphset definition
 * U+1ACA COMBINING DOUBLE PLUS SIGN BELOW: not included in any glyphset definition
 * U+1ACB COMBINING TRIPLE ACUTE ACCENT: not included in any glyphset definition
 * U+1ACC COMBINING LATIN SMALL LETTER INSULAR G: not included in any glyphset definition
 * U+1ACD COMBINING LATIN SMALL LETTER INSULAR R: not included in any glyphset definition
 * U+1ACE COMBINING LATIN SMALL LETTER INSULAR T: not included in any glyphset definition
 * U+1D00 LATIN LETTER SMALL CAPITAL A: not included in any glyphset definition
 * U+1D01 LATIN LETTER SMALL CAPITAL AE: not included in any glyphset definition
 * U+1D02 LATIN SMALL LETTER TURNED AE: not included in any glyphset definition
 * U+1D03 LATIN LETTER SMALL CAPITAL BARRED B: not included in any glyphset definition
 * U+1D04 LATIN LETTER SMALL CAPITAL C: not included in any glyphset definition
 * U+1D05 LATIN LETTER SMALL CAPITAL D: not included in any glyphset definition
 * U+1D06 LATIN LETTER SMALL CAPITAL ETH: not included in any glyphset definition
 * U+1D07 LATIN LETTER SMALL CAPITAL E: not included in any glyphset definition
 * U+1D08 LATIN SMALL LETTER TURNED OPEN E: not included in any glyphset definition
 * U+1D09 LATIN SMALL LETTER TURNED I: not included in any glyphset definition
 * U+1D0A LATIN LETTER SMALL CAPITAL J: not included in any glyphset definition
 * U+1D0B LATIN LETTER SMALL CAPITAL K: not included in any glyphset definition
 * U+1D0C LATIN LETTER SMALL CAPITAL L WITH STROKE: not included in any glyphset definition
 * U+1D0D LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition
 * U+1D0E LATIN LETTER SMALL CAPITAL REVERSED N: not included in any glyphset definition
 * U+1D0F LATIN LETTER SMALL CAPITAL O: not included in any glyphset definition
 * U+1D10 LATIN LETTER SMALL CAPITAL OPEN O: not included in any glyphset definition
 * U+1D11 LATIN SMALL LETTER SIDEWAYS O: not included in any glyphset definition
 * U+1D12 LATIN SMALL LETTER SIDEWAYS OPEN O: not included in any glyphset definition
 * U+1D13 LATIN SMALL LETTER SIDEWAYS O WITH STROKE: not included in any glyphset definition
 * U+1D14 LATIN SMALL LETTER TURNED OE: not included in any glyphset definition
 * U+1D15 LATIN LETTER SMALL CAPITAL OU: not included in any glyphset definition
 * U+1D16 LATIN SMALL LETTER TOP HALF O: not included in any glyphset definition
 * U+1D17 LATIN SMALL LETTER BOTTOM HALF O: not included in any glyphset definition
 * U+1D18 LATIN LETTER SMALL CAPITAL P: not included in any glyphset definition
 * U+1D19 LATIN LETTER SMALL CAPITAL REVERSED R: not included in any glyphset definition
 * U+1D1A LATIN LETTER SMALL CAPITAL TURNED R: not included in any glyphset definition
 * U+1D1B LATIN LETTER SMALL CAPITAL T: not included in any glyphset definition
 * U+1D1C LATIN LETTER SMALL CAPITAL U: not included in any glyphset definition
 * U+1D1D LATIN SMALL LETTER SIDEWAYS U: not included in any glyphset definition
 * U+1D1E LATIN SMALL LETTER SIDEWAYS DIAERESIZED U: not included in any glyphset definition
 * U+1D1F LATIN SMALL LETTER SIDEWAYS TURNED M: not included in any glyphset definition
 * U+1D20 LATIN LETTER SMALL CAPITAL V: not included in any glyphset definition
 * U+1D21 LATIN LETTER SMALL CAPITAL W: not included in any glyphset definition
 * U+1D22 LATIN LETTER SMALL CAPITAL Z: not included in any glyphset definition
 * U+1D23 LATIN LETTER SMALL CAPITAL EZH: not included in any glyphset definition
 * U+1D24 LATIN LETTER VOICED LARYNGEAL SPIRANT: not included in any glyphset definition
 * U+1D25 LATIN LETTER AIN: not included in any glyphset definition
 * U+1D26 GREEK LETTER SMALL CAPITAL GAMMA: not included in any glyphset definition
 * U+1D27 GREEK LETTER SMALL CAPITAL LAMDA: not included in any glyphset definition
 * U+1D28 GREEK LETTER SMALL CAPITAL PI: not included in any glyphset definition
 * U+1D29 GREEK LETTER SMALL CAPITAL RHO: not included in any glyphset definition
 * U+1D2A GREEK LETTER SMALL CAPITAL PSI: not included in any glyphset definition
 * U+1D2B CYRILLIC LETTER SMALL CAPITAL EL: not included in any glyphset definition
 * U+1D2C MODIFIER LETTER CAPITAL A: not included in any glyphset definition
 * U+1D2D MODIFIER LETTER CAPITAL AE: not included in any glyphset definition
 * U+1D2E MODIFIER LETTER CAPITAL B: not included in any glyphset definition
 * U+1D2F MODIFIER LETTER CAPITAL BARRED B: not included in any glyphset definition
 * U+1D30 MODIFIER LETTER CAPITAL D: not included in any glyphset definition
 * U+1D31 MODIFIER LETTER CAPITAL E: not included in any glyphset definition
 * U+1D32 MODIFIER LETTER CAPITAL REVERSED E: not included in any glyphset definition
 * U+1D33 MODIFIER LETTER CAPITAL G: not included in any glyphset definition
 * U+1D34 MODIFIER LETTER CAPITAL H: not included in any glyphset definition
 * U+1D35 MODIFIER LETTER CAPITAL I: not included in any glyphset definition
 * U+1D36 MODIFIER LETTER CAPITAL J: not included in any glyphset definition
 * U+1D37 MODIFIER LETTER CAPITAL K: not included in any glyphset definition
 * U+1D38 MODIFIER LETTER CAPITAL L: not included in any glyphset definition
 * U+1D39 MODIFIER LETTER CAPITAL M: not included in any glyphset definition
 * U+1D3A MODIFIER LETTER CAPITAL N: not included in any glyphset definition
 * U+1D3B MODIFIER LETTER CAPITAL REVERSED N: not included in any glyphset definition
 * U+1D3C MODIFIER LETTER CAPITAL O: not included in any glyphset definition
 * U+1D3D MODIFIER LETTER CAPITAL OU: not included in any glyphset definition
 * U+1D3E MODIFIER LETTER CAPITAL P: not included in any glyphset definition
 * U+1D3F MODIFIER LETTER CAPITAL R: not included in any glyphset definition
 * U+1D40 MODIFIER LETTER CAPITAL T: not included in any glyphset definition
 * U+1D41 MODIFIER LETTER CAPITAL U: not included in any glyphset definition
 * U+1D42 MODIFIER LETTER CAPITAL W: not included in any glyphset definition
 * U+1D43 MODIFIER LETTER SMALL A: not included in any glyphset definition
 * U+1D44 MODIFIER LETTER SMALL TURNED A: not included in any glyphset definition
 * U+1D45 MODIFIER LETTER SMALL ALPHA: not included in any glyphset definition
 * U+1D46 MODIFIER LETTER SMALL TURNED AE: not included in any glyphset definition
 * U+1D47 MODIFIER LETTER SMALL B: not included in any glyphset definition
 * U+1D48 MODIFIER LETTER SMALL D: not included in any glyphset definition
 * U+1D49 MODIFIER LETTER SMALL E: not included in any glyphset definition
 * U+1D4A MODIFIER LETTER SMALL SCHWA: not included in any glyphset definition
 * U+1D4B MODIFIER LETTER SMALL OPEN E: not included in any glyphset definition
 * U+1D4C MODIFIER LETTER SMALL TURNED OPEN E: not included in any glyphset definition
 * U+1D4D MODIFIER LETTER SMALL G: not included in any glyphset definition
 * U+1D4E MODIFIER LETTER SMALL TURNED I: not included in any glyphset definition
 * U+1D4F MODIFIER LETTER SMALL K: not included in any glyphset definition
 * U+1D50 MODIFIER LETTER SMALL M: not included in any glyphset definition
 * U+1D51 MODIFIER LETTER SMALL ENG: not included in any glyphset definition
 * U+1D52 MODIFIER LETTER SMALL O: not included in any glyphset definition
 * U+1D53 MODIFIER LETTER SMALL OPEN O: not included in any glyphset definition
 * U+1D54 MODIFIER LETTER SMALL TOP HALF O: not included in any glyphset definition
 * U+1D55 MODIFIER LETTER SMALL BOTTOM HALF O: not included in any glyphset definition
 * U+1D56 MODIFIER LETTER SMALL P: not included in any glyphset definition
 * U+1D57 MODIFIER LETTER SMALL T: not included in any glyphset definition
 * U+1D58 MODIFIER LETTER SMALL U: not included in any glyphset definition
 * U+1D59 MODIFIER LETTER SMALL SIDEWAYS U: not included in any glyphset definition
 * U+1D5A MODIFIER LETTER SMALL TURNED M: not included in any glyphset definition
 * U+1D5B MODIFIER LETTER SMALL V: not included in any glyphset definition
 * U+1D5C MODIFIER LETTER SMALL AIN: not included in any glyphset definition
 * U+1D5D MODIFIER LETTER SMALL BETA: not included in any glyphset definition
 * U+1D5E MODIFIER LETTER SMALL GREEK GAMMA: not included in any glyphset definition
 * U+1D5F MODIFIER LETTER SMALL DELTA: not included in any glyphset definition
 * U+1D60 MODIFIER LETTER SMALL GREEK PHI: not included in any glyphset definition
 * U+1D61 MODIFIER LETTER SMALL CHI: not included in any glyphset definition
 * U+1D62 LATIN SUBSCRIPT SMALL LETTER I: not included in any glyphset definition
 * U+1D63 LATIN SUBSCRIPT SMALL LETTER R: not included in any glyphset definition
 * U+1D64 LATIN SUBSCRIPT SMALL LETTER U: not included in any glyphset definition
 * U+1D65 LATIN SUBSCRIPT SMALL LETTER V: not included in any glyphset definition
 * U+1D66 GREEK SUBSCRIPT SMALL LETTER BETA: not included in any glyphset definition
 * U+1D67 GREEK SUBSCRIPT SMALL LETTER GAMMA: not included in any glyphset definition
 * U+1D68 GREEK SUBSCRIPT SMALL LETTER RHO: not included in any glyphset definition
 * U+1D69 GREEK SUBSCRIPT SMALL LETTER PHI: not included in any glyphset definition
 * U+1D6A GREEK SUBSCRIPT SMALL LETTER CHI: not included in any glyphset definition
 * U+1D6B LATIN SMALL LETTER UE: not included in any glyphset definition
 * U+1D6C LATIN SMALL LETTER B WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6D LATIN SMALL LETTER D WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6E LATIN SMALL LETTER F WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6F LATIN SMALL LETTER M WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D70 LATIN SMALL LETTER N WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D71 LATIN SMALL LETTER P WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D72 LATIN SMALL LETTER R WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D73 LATIN SMALL LETTER R WITH FISHHOOK AND MIDDLE TILDE: not included in any glyphset definition
 * U+1D74 LATIN SMALL LETTER S WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D75 LATIN SMALL LETTER T WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D76 LATIN SMALL LETTER Z WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D77 LATIN SMALL LETTER TURNED G: not included in any glyphset definition
 * U+1D78 MODIFIER LETTER CYRILLIC EN: not included in any glyphset definition
 * U+1D79 LATIN SMALL LETTER INSULAR G: not included in any glyphset definition
 * U+1D7A LATIN SMALL LETTER TH WITH STRIKETHROUGH: not included in any glyphset definition
 * U+1D7B LATIN SMALL CAPITAL LETTER I WITH STROKE: not included in any glyphset definition
 * U+1D7C LATIN SMALL LETTER IOTA WITH STROKE: not included in any glyphset definition
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1D7E LATIN SMALL CAPITAL LETTER U WITH STROKE: not included in any glyphset definition
 * U+1D7F LATIN SMALL LETTER UPSILON WITH STROKE: not included in any glyphset definition
 * U+1D80 LATIN SMALL LETTER B WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D81 LATIN SMALL LETTER D WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D82 LATIN SMALL LETTER F WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D83 LATIN SMALL LETTER G WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D84 LATIN SMALL LETTER K WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D85 LATIN SMALL LETTER L WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D86 LATIN SMALL LETTER M WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D87 LATIN SMALL LETTER N WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D88 LATIN SMALL LETTER P WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D89 LATIN SMALL LETTER R WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8A LATIN SMALL LETTER S WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8B LATIN SMALL LETTER ESH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8C LATIN SMALL LETTER V WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8D LATIN SMALL LETTER X WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8E LATIN SMALL LETTER Z WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8F LATIN SMALL LETTER A WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D90 LATIN SMALL LETTER ALPHA WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D91 LATIN SMALL LETTER D WITH HOOK AND TAIL: not included in any glyphset definition
 * U+1D92 LATIN SMALL LETTER E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D93 LATIN SMALL LETTER OPEN E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D94 LATIN SMALL LETTER REVERSED OPEN E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D95 LATIN SMALL LETTER SCHWA WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D96 LATIN SMALL LETTER I WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D97 LATIN SMALL LETTER OPEN O WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D98 LATIN SMALL LETTER ESH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D99 LATIN SMALL LETTER U WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D9A LATIN SMALL LETTER EZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D9B MODIFIER LETTER SMALL TURNED ALPHA: not included in any glyphset definition
 * U+1D9C MODIFIER LETTER SMALL C: not included in any glyphset definition
 * U+1D9D MODIFIER LETTER SMALL C WITH CURL: not included in any glyphset definition
 * U+1D9E MODIFIER LETTER SMALL ETH: not included in any glyphset definition
 * U+1D9F MODIFIER LETTER SMALL REVERSED OPEN E: not included in any glyphset definition
 * U+1DA0 MODIFIER LETTER SMALL F: not included in any glyphset definition
 * U+1DA1 MODIFIER LETTER SMALL DOTLESS J WITH STROKE: not included in any glyphset definition
 * U+1DA2 MODIFIER LETTER SMALL SCRIPT G: not included in any glyphset definition
 * U+1DA3 MODIFIER LETTER SMALL TURNED H: not included in any glyphset definition
 * U+1DA4 MODIFIER LETTER SMALL I WITH STROKE: not included in any glyphset definition
 * U+1DA5 MODIFIER LETTER SMALL IOTA: not included in any glyphset definition
 * U+1DA6 MODIFIER LETTER SMALL CAPITAL I: not included in any glyphset definition
 * U+1DA7 MODIFIER LETTER SMALL CAPITAL I WITH STROKE: not included in any glyphset definition
 * U+1DA8 MODIFIER LETTER SMALL J WITH CROSSED-TAIL: not included in any glyphset definition
 * U+1DA9 MODIFIER LETTER SMALL L WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DAA MODIFIER LETTER SMALL L WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DAB MODIFIER LETTER SMALL CAPITAL L: not included in any glyphset definition
 * U+1DAC MODIFIER LETTER SMALL M WITH HOOK: not included in any glyphset definition
 * U+1DAD MODIFIER LETTER SMALL TURNED M WITH LONG LEG: not included in any glyphset definition
 * U+1DAE MODIFIER LETTER SMALL N WITH LEFT HOOK: not included in any glyphset definition
 * U+1DAF MODIFIER LETTER SMALL N WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DB0 MODIFIER LETTER SMALL CAPITAL N: not included in any glyphset definition
 * U+1DB1 MODIFIER LETTER SMALL BARRED O: not included in any glyphset definition
 * U+1DB2 MODIFIER LETTER SMALL PHI: not included in any glyphset definition
 * U+1DB3 MODIFIER LETTER SMALL S WITH HOOK: not included in any glyphset definition
 * U+1DB4 MODIFIER LETTER SMALL ESH: not included in any glyphset definition
 * U+1DB5 MODIFIER LETTER SMALL T WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DB6 MODIFIER LETTER SMALL U BAR: not included in any glyphset definition
 * U+1DB7 MODIFIER LETTER SMALL UPSILON: not included in any glyphset definition
 * U+1DB8 MODIFIER LETTER SMALL CAPITAL U: not included in any glyphset definition
 * U+1DB9 MODIFIER LETTER SMALL V WITH HOOK: not included in any glyphset definition
 * U+1DBA MODIFIER LETTER SMALL TURNED V: not included in any glyphset definition
 * U+1DBB MODIFIER LETTER SMALL Z: not included in any glyphset definition
 * U+1DBC MODIFIER LETTER SMALL Z WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DBD MODIFIER LETTER SMALL Z WITH CURL: not included in any glyphset definition
 * U+1DBE MODIFIER LETTER SMALL EZH: not included in any glyphset definition
 * U+1DBF MODIFIER LETTER SMALL THETA: not included in any glyphset definition
 * U+1DC0 COMBINING DOTTED GRAVE ACCENT: not included in any glyphset definition
 * U+1DC1 COMBINING DOTTED ACUTE ACCENT: not included in any glyphset definition
 * U+1DC2 COMBINING SNAKE BELOW: not included in any glyphset definition
 * U+1DC3 COMBINING SUSPENSION MARK: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DC8 COMBINING GRAVE-ACUTE-GRAVE: not included in any glyphset definition
 * U+1DC9 COMBINING ACUTE-GRAVE-ACUTE: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+1DCB COMBINING BREVE-MACRON: not included in any glyphset definition
 * U+1DCC COMBINING MACRON-BREVE: not included in any glyphset definition
 * U+1DCD COMBINING DOUBLE CIRCUMFLEX ABOVE: try adding coptic
 * U+1DCE COMBINING OGONEK ABOVE: not included in any glyphset definition
 * U+1DCF COMBINING ZIGZAG BELOW: not included in any glyphset definition
 * U+1DD0 COMBINING IS BELOW: not included in any glyphset definition
 * U+1DD1 COMBINING UR ABOVE: not included in any glyphset definition
 * U+1DD2 COMBINING US ABOVE: not included in any glyphset definition
 * U+1DD3 COMBINING LATIN SMALL LETTER FLATTENED OPEN A ABOVE: not included in any glyphset definition
 * U+1DD4 COMBINING LATIN SMALL LETTER AE: not included in any glyphset definition
 * U+1DD5 COMBINING LATIN SMALL LETTER AO: not included in any glyphset definition
 * U+1DD6 COMBINING LATIN SMALL LETTER AV: not included in any glyphset definition
 * U+1DD7 COMBINING LATIN SMALL LETTER C CEDILLA: not included in any glyphset definition
 * U+1DD8 COMBINING LATIN SMALL LETTER INSULAR D: not included in any glyphset definition
 * U+1DD9 COMBINING LATIN SMALL LETTER ETH: not included in any glyphset definition
 * U+1DDA COMBINING LATIN SMALL LETTER G: not included in any glyphset definition
 * U+1DDB COMBINING LATIN LETTER SMALL CAPITAL G: not included in any glyphset definition
 * U+1DDC COMBINING LATIN SMALL LETTER K: not included in any glyphset definition
 * U+1DDD COMBINING LATIN SMALL LETTER L: not included in any glyphset definition
 * U+1DDE COMBINING LATIN LETTER SMALL CAPITAL L: not included in any glyphset definition
 * U+1DDF COMBINING LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition
 * U+1DE0 COMBINING LATIN SMALL LETTER N: not included in any glyphset definition
 * U+1DE1 COMBINING LATIN LETTER SMALL CAPITAL N: not included in any glyphset definition
 * U+1DE2 COMBINING LATIN LETTER SMALL CAPITAL R: not included in any glyphset definition
 * U+1DE3 COMBINING LATIN SMALL LETTER R ROTUNDA: not included in any glyphset definition
 * U+1DE4 COMBINING LATIN SMALL LETTER S: not included in any glyphset definition
 * U+1DE5 COMBINING LATIN SMALL LETTER LONG S: not included in any glyphset definition
 * U+1DE6 COMBINING LATIN SMALL LETTER Z: not included in any glyphset definition
 * U+1DE7 COMBINING LATIN SMALL LETTER ALPHA: not included in any glyphset definition
 * U+1DE8 COMBINING LATIN SMALL LETTER B: not included in any glyphset definition
 * U+1DE9 COMBINING LATIN SMALL LETTER BETA: not included in any glyphset definition
 * U+1DEA COMBINING LATIN SMALL LETTER SCHWA: not included in any glyphset definition
 * U+1DEB COMBINING LATIN SMALL LETTER F: not included in any glyphset definition
 * U+1DEC COMBINING LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition
 * U+1DED COMBINING LATIN SMALL LETTER O WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition
 * U+1DEE COMBINING LATIN SMALL LETTER P: not included in any glyphset definition
 * U+1DEF COMBINING LATIN SMALL LETTER ESH: not included in any glyphset definition
 * U+1DF0 COMBINING LATIN SMALL LETTER U WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition
 * U+1DF1 COMBINING LATIN SMALL LETTER W: not included in any glyphset definition
 * U+1DF2 COMBINING LATIN SMALL LETTER A WITH DIAERESIS: not included in any glyphset definition
 * U+1DF3 COMBINING LATIN SMALL LETTER O WITH DIAERESIS: not included in any glyphset definition
 * U+1DF4 COMBINING LATIN SMALL LETTER U WITH DIAERESIS: not included in any glyphset definition
 * U+1DF5 COMBINING UP TACK ABOVE: not included in any glyphset definition
 * U+1DF6 COMBINING KAVYKA ABOVE RIGHT: not included in any glyphset definition
 * U+1DF7 COMBINING KAVYKA ABOVE LEFT: not included in any glyphset definition
 * U+1DF8 COMBINING DOT ABOVE LEFT: not included in any glyphset definition
 * U+1DF9 COMBINING WIDE INVERTED BRIDGE BELOW: not included in any glyphset definition
 * U+1DFB COMBINING DELETION MARK: try adding newa
 * U+1DFC COMBINING DOUBLE INVERTED BREVE BELOW: not included in any glyphset definition
 * U+1DFD COMBINING ALMOST EQUAL TO BELOW: not included in any glyphset definition
 * U+1DFE COMBINING LEFT ARROWHEAD ABOVE: not included in any glyphset definition
 * U+1DFF COMBINING RIGHT ARROWHEAD AND DOWN ARROWHEAD BELOW: not included in any glyphset definition
 * U+2000 EN QUAD: not included in any glyphset definition
 * U+2001 EM QUAD: not included in any glyphset definition
 * U+2003 EM SPACE: try adding nushu
 * U+2004 THREE-PER-EM SPACE: not included in any glyphset definition
 * U+2005 FOUR-PER-EM SPACE: not included in any glyphset definition
 * U+2006 SIX-PER-EM SPACE: not included in any glyphset definition
 * U+2007 FIGURE SPACE: not included in any glyphset definition
 * U+2008 PUNCTUATION SPACE: not included in any glyphset definition
 * U+200A HAIR SPACE: not included in any glyphset definition
 * U+200E LEFT-TO-RIGHT MARK: try adding one of: phags-pa, thaana, syriac, nko
 * U+200F RIGHT-TO-LEFT MARK: try adding one of: phags-pa, thaana, syriac, nko
 * U+2010 HYPHEN: try adding one of: coptic, cham, syloti-nagri, lisu, kayah-li, sundanese, kharoshthi, kaithi, yi, sora-sompeng
 * U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi
 * U+2012 FIGURE DASH: not included in any glyphset definition
 * U+2015 HORIZONTAL BAR: try adding adlam
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2017 DOUBLE LOW LINE: not included in any glyphset definition
 * U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam
 * U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2023 TRIANGULAR BULLET: not included in any glyphset definition
 * U+2024 ONE DOT LEADER: try adding armenian
 * U+2025 TWO DOT LEADER: try adding phags-pa
 * U+2027 HYPHENATION POINT: not included in any glyphset definition
 * U+2028 LINE SEPARATOR: not included in any glyphset definition
 * U+2029 PARAGRAPH SEPARATOR: not included in any glyphset definition
 * U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition
 * U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition
 * U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition
 * U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition
 * U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh
 * U+202F NARROW NO-BREAK SPACE: try adding one of: mongolian, yi
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition
 * U+2034 TRIPLE PRIME: try adding math
 * U+2035 REVERSED PRIME: try adding math
 * U+2036 REVERSED DOUBLE PRIME: try adding math
 * U+2037 REVERSED TRIPLE PRIME: try adding math
 * U+2038 CARET: not included in any glyphset definition
 * U+203B REFERENCE MARK: not included in any glyphset definition
 * U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition
 * U+203D INTERROBANG: not included in any glyphset definition
 * U+203E OVERLINE: not included in any glyphset definition
 * U+203F UNDERTIE: not included in any glyphset definition
 * U+2040 CHARACTER TIE: not included in any glyphset definition
 * U+2041 CARET INSERTION POINT: not included in any glyphset definition
 * U+2042 ASTERISM: not included in any glyphset definition
 * U+2043 HYPHEN BULLET: not included in any glyphset definition
 * U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2047 DOUBLE QUESTION MARK: not included in any glyphset definition
 * U+2048 QUESTION EXCLAMATION MARK: try adding mongolian
 * U+2049 EXCLAMATION QUESTION MARK: try adding mongolian
 * U+204A TIRONIAN SIGN ET: not included in any glyphset definition
 * U+204B REVERSED PILCROW SIGN: not included in any glyphset definition
 * U+204C BLACK LEFTWARDS BULLET: not included in any glyphset definition
 * U+204D BLACK RIGHTWARDS BULLET: not included in any glyphset definition
 * U+204E LOW ASTERISK: not included in any glyphset definition
 * U+204F REVERSED SEMICOLON: try adding adlam
 * U+2050 CLOSE UP: not included in any glyphset definition
 * U+2051 TWO ASTERISKS ALIGNED VERTICALLY: not included in any glyphset definition
 * U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition
 * U+2053 SWUNG DASH: try adding coptic
 * U+2054 INVERTED UNDERTIE: not included in any glyphset definition
 * U+2055 FLOWER PUNCTUATION MARK: try adding syloti-nagri
 * U+2056 THREE DOT PUNCTUATION: try adding coptic
 * U+2057 QUADRUPLE PRIME: try adding math
 * U+2058 FOUR DOT PUNCTUATION: try adding coptic
 * U+2059 FIVE DOT PUNCTUATION: try adding coptic
 * U+205A TWO DOT PUNCTUATION: try adding one of: old-hungarian, old-turkic
 * U+205B FOUR DOT MARK: not included in any glyphset definition
 * U+205C DOTTED CROSS: not included in any glyphset definition
 * U+205D TRICOLON: try adding one of: meroitic, old-hungarian
 * U+205E VERTICAL FOUR DOTS: try adding old-hungarian
 * U+205F MEDIUM MATHEMATICAL SPACE: not included in any glyphset definition
 * U+2060 WORD JOINER: not included in any glyphset definition
 * U+2061 FUNCTION APPLICATION: not included in any glyphset definition
 * U+2062 INVISIBLE TIMES: not included in any glyphset definition
 * U+2063 INVISIBLE SEPARATOR: not included in any glyphset definition
 * U+2064 INVISIBLE PLUS: not included in any glyphset definition
 * U+2066 LEFT-TO-RIGHT ISOLATE: not included in any glyphset definition
 * U+2067 RIGHT-TO-LEFT ISOLATE: not included in any glyphset definition
 * U+2068 FIRST STRONG ISOLATE: not included in any glyphset definition
 * U+2069 POP DIRECTIONAL ISOLATE: not included in any glyphset definition
 * U+206A INHIBIT SYMMETRIC SWAPPING: not included in any glyphset definition
 * U+206B ACTIVATE SYMMETRIC SWAPPING: not included in any glyphset definition
 * U+206C INHIBIT ARABIC FORM SHAPING: not included in any glyphset definition
 * U+206D ACTIVATE ARABIC FORM SHAPING: not included in any glyphset definition
 * U+206E NATIONAL DIGIT SHAPES: not included in any glyphset definition
 * U+206F NOMINAL DIGIT SHAPES: not included in any glyphset definition
 * U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition
 * U+2071 SUPERSCRIPT LATIN SMALL LETTER I: not included in any glyphset definition
 * U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition
 * U+2076 SUPERSCRIPT SIX: not included in any glyphset definition
 * U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition
 * U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition
 * U+2079 SUPERSCRIPT NINE: not included in any glyphset definition
 * U+207A SUPERSCRIPT PLUS SIGN: not included in any glyphset definition
 * U+207B SUPERSCRIPT MINUS: not included in any glyphset definition
 * U+207C SUPERSCRIPT EQUALS SIGN: not included in any glyphset definition
 * U+207D SUPERSCRIPT LEFT PARENTHESIS: not included in any glyphset definition
 * U+207E SUPERSCRIPT RIGHT PARENTHESIS: not included in any glyphset definition
 * U+207F SUPERSCRIPT LATIN SMALL LETTER N: not included in any glyphset definition
 * U+2080 SUBSCRIPT ZERO: not included in any glyphset definition
 * U+2081 SUBSCRIPT ONE: not included in any glyphset definition
 * U+2082 SUBSCRIPT TWO: not included in any glyphset definition
 * U+2083 SUBSCRIPT THREE: not included in any glyphset definition
 * U+2084 SUBSCRIPT FOUR: not included in any glyphset definition
 * U+2085 SUBSCRIPT FIVE: not included in any glyphset definition
 * U+2086 SUBSCRIPT SIX: not included in any glyphset definition
 * U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition
 * U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition
 * U+2089 SUBSCRIPT NINE: not included in any glyphset definition
 * U+208A SUBSCRIPT PLUS SIGN: not included in any glyphset definition
 * U+208B SUBSCRIPT MINUS: not included in any glyphset definition
 * U+208C SUBSCRIPT EQUALS SIGN: not included in any glyphset definition
 * U+208D SUBSCRIPT LEFT PARENTHESIS: not included in any glyphset definition
 * U+208E SUBSCRIPT RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2090 LATIN SUBSCRIPT SMALL LETTER A: not included in any glyphset definition
 * U+2091 LATIN SUBSCRIPT SMALL LETTER E: not included in any glyphset definition
 * U+2092 LATIN SUBSCRIPT SMALL LETTER O: not included in any glyphset definition
 * U+2093 LATIN SUBSCRIPT SMALL LETTER X: not included in any glyphset definition
 * U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: not included in any glyphset definition
 * U+2095 LATIN SUBSCRIPT SMALL LETTER H: not included in any glyphset definition
 * U+2096 LATIN SUBSCRIPT SMALL LETTER K: not included in any glyphset definition
 * U+2097 LATIN SUBSCRIPT SMALL LETTER L: not included in any glyphset definition
 * U+2098 LATIN SUBSCRIPT SMALL LETTER M: not included in any glyphset definition
 * U+2099 LATIN SUBSCRIPT SMALL LETTER N: not included in any glyphset definition
 * U+209A LATIN SUBSCRIPT SMALL LETTER P: not included in any glyphset definition
 * U+209B LATIN SUBSCRIPT SMALL LETTER S: not included in any glyphset definition
 * U+209C LATIN SUBSCRIPT SMALL LETTER T: not included in any glyphset definition
 * U+20F0 COMBINING ASTERISK ABOVE: try adding grantha
 * U+2100 ACCOUNT OF: not included in any glyphset definition
 * U+2101 ADDRESSED TO THE SUBJECT: not included in any glyphset definition
 * U+2102 DOUBLE-STRUCK CAPITAL C: try adding math
 * U+2103 DEGREE CELSIUS: not included in any glyphset definition
 * U+2104 CENTRE LINE SYMBOL: not included in any glyphset definition
 * U+2105 CARE OF: not included in any glyphset definition
 * U+2106 CADA UNA: not included in any glyphset definition
 * U+2107 EULER CONSTANT: not included in any glyphset definition
 * U+2108 SCRUPLE: not included in any glyphset definition
 * U+2109 DEGREE FAHRENHEIT: not included in any glyphset definition
 * U+210A SCRIPT SMALL G: try adding math
 * U+210B SCRIPT CAPITAL H: try adding math
 * U+210C BLACK-LETTER CAPITAL H: try adding math
 * U+210D DOUBLE-STRUCK CAPITAL H: try adding math
 * U+210E PLANCK CONSTANT: try adding math
 * U+210F PLANCK CONSTANT OVER TWO PI: not included in any glyphset definition
 * U+2110 SCRIPT CAPITAL I: try adding math
 * U+2111 BLACK-LETTER CAPITAL I: try adding math
 * U+2112 SCRIPT CAPITAL L: try adding math
 * U+2114 L B BAR SYMBOL: not included in any glyphset definition
 * U+2115 DOUBLE-STRUCK CAPITAL N: try adding math
 * U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition
 * U+2118 SCRIPT CAPITAL P: not included in any glyphset definition
 * U+2119 DOUBLE-STRUCK CAPITAL P: try adding math
 * U+211A DOUBLE-STRUCK CAPITAL Q: try adding math
 * U+211B SCRIPT CAPITAL R: try adding math
 * U+211C BLACK-LETTER CAPITAL R: try adding math
 * U+211D DOUBLE-STRUCK CAPITAL R: try adding math
 * U+211E PRESCRIPTION TAKE: not included in any glyphset definition
 * U+211F RESPONSE: not included in any glyphset definition
 * U+2120 SERVICE MARK: not included in any glyphset definition
 * U+2121 TELEPHONE SIGN: not included in any glyphset definition
 * U+2123 VERSICLE: not included in any glyphset definition
 * U+2124 DOUBLE-STRUCK CAPITAL Z: try adding math
 * U+2125 OUNCE SIGN: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+2127 INVERTED OHM SIGN: not included in any glyphset definition
 * U+2128 BLACK-LETTER CAPITAL Z: try adding math
 * U+2129 TURNED GREEK SMALL LETTER IOTA: not included in any glyphset definition
 * U+212A KELVIN SIGN: not included in any glyphset definition
 * U+212B ANGSTROM SIGN: not included in any glyphset definition
 * U+212C SCRIPT CAPITAL B: try adding math
 * U+212D BLACK-LETTER CAPITAL C: try adding math
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+212F SCRIPT SMALL E: try adding math
 * U+2130 SCRIPT CAPITAL E: try adding math
 * U+2131 SCRIPT CAPITAL F: try adding math
 * U+2132 TURNED CAPITAL F: not included in any glyphset definition
 * U+2133 SCRIPT CAPITAL M: try adding math
 * U+2134 SCRIPT SMALL O: try adding math
 * U+2135 ALEF SYMBOL: try adding math
 * U+2136 BET SYMBOL: try adding math
 * U+2137 GIMEL SYMBOL: try adding math
 * U+2138 DALET SYMBOL: try adding math
 * U+2139 INFORMATION SOURCE: not included in any glyphset definition
 * U+213A ROTATED CAPITAL Q: not included in any glyphset definition
 * U+213B FACSIMILE SIGN: not included in any glyphset definition
 * U+213C DOUBLE-STRUCK SMALL PI: try adding math
 * U+213D DOUBLE-STRUCK SMALL GAMMA: try adding math
 * U+213E DOUBLE-STRUCK CAPITAL GAMMA: try adding math
 * U+213F DOUBLE-STRUCK CAPITAL PI: try adding math
 * U+2140 DOUBLE-STRUCK N-ARY SUMMATION: try adding math
 * U+2141 TURNED SANS-SERIF CAPITAL G: not included in any glyphset definition
 * U+2142 TURNED SANS-SERIF CAPITAL L: not included in any glyphset definition
 * U+2143 REVERSED SANS-SERIF CAPITAL L: not included in any glyphset definition
 * U+2144 TURNED SANS-SERIF CAPITAL Y: not included in any glyphset definition
 * U+2145 DOUBLE-STRUCK ITALIC CAPITAL D: try adding math
 * U+2146 DOUBLE-STRUCK ITALIC SMALL D: try adding math
 * U+2147 DOUBLE-STRUCK ITALIC SMALL E: try adding math
 * U+2148 DOUBLE-STRUCK ITALIC SMALL I: try adding math
 * U+2149 DOUBLE-STRUCK ITALIC SMALL J: try adding math
 * U+214A PROPERTY LINE: not included in any glyphset definition
 * U+214B TURNED AMPERSAND: not included in any glyphset definition
 * U+214C PER SIGN: not included in any glyphset definition
 * U+214D AKTIESELSKAB: not included in any glyphset definition
 * U+214E TURNED SMALL F: not included in any glyphset definition
 * U+214F SYMBOL FOR SAMARITAN SOURCE: not included in any glyphset definition
 * U+2150 VULGAR FRACTION ONE SEVENTH: not included in any glyphset definition
 * U+2151 VULGAR FRACTION ONE NINTH: not included in any glyphset definition
 * U+2152 VULGAR FRACTION ONE TENTH: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2155 VULGAR FRACTION ONE FIFTH: not included in any glyphset definition
 * U+2156 VULGAR FRACTION TWO FIFTHS: not included in any glyphset definition
 * U+2157 VULGAR FRACTION THREE FIFTHS: not included in any glyphset definition
 * U+2158 VULGAR FRACTION FOUR FIFTHS: not included in any glyphset definition
 * U+2159 VULGAR FRACTION ONE SIXTH: not included in any glyphset definition
 * U+215A VULGAR FRACTION FIVE SIXTHS: not included in any glyphset definition
 * U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition
 * U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition
 * U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition
 * U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition
 * U+215F FRACTION NUMERATOR ONE: not included in any glyphset definition
 * U+2183 ROMAN NUMERAL REVERSED ONE HUNDRED: try adding symbols
 * U+2184 LATIN SMALL LETTER REVERSED C: not included in any glyphset definition
 * U+2189 VULGAR FRACTION ZERO THIRDS: not included in any glyphset definition
 * U+2E00 RIGHT ANGLE SUBSTITUTION MARKER: not included in any glyphset definition
 * U+2E01 RIGHT ANGLE DOTTED SUBSTITUTION MARKER: not included in any glyphset definition
 * U+2E02 LEFT SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E03 RIGHT SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E04 LEFT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E05 RIGHT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E06 RAISED INTERPOLATION MARKER: not included in any glyphset definition
 * U+2E07 RAISED DOTTED INTERPOLATION MARKER: not included in any glyphset definition
 * U+2E08 DOTTED TRANSPOSITION MARKER: not included in any glyphset definition
 * U+2E09 LEFT TRANSPOSITION BRACKET: not included in any glyphset definition
 * U+2E0A RIGHT TRANSPOSITION BRACKET: not included in any glyphset definition
 * U+2E0B RAISED SQUARE: not included in any glyphset definition
 * U+2E0C LEFT RAISED OMISSION BRACKET: not included in any glyphset definition
 * U+2E0D RIGHT RAISED OMISSION BRACKET: not included in any glyphset definition
 * U+2E0E EDITORIAL CORONIS: not included in any glyphset definition
 * U+2E0F PARAGRAPHOS: not included in any glyphset definition
 * U+2E10 FORKED PARAGRAPHOS: not included in any glyphset definition
 * U+2E11 REVERSED FORKED PARAGRAPHOS: not included in any glyphset definition
 * U+2E12 HYPODIASTOLE: not included in any glyphset definition
 * U+2E13 DOTTED OBELOS: not included in any glyphset definition
 * U+2E14 DOWNWARDS ANCORA: not included in any glyphset definition
 * U+2E15 UPWARDS ANCORA: not included in any glyphset definition
 * U+2E16 DOTTED RIGHT-POINTING ANGLE: not included in any glyphset definition
 * U+2E17 DOUBLE OBLIQUE HYPHEN: try adding coptic
 * U+2E18 INVERTED INTERROBANG: not included in any glyphset definition
 * U+2E19 PALM BRANCH: not included in any glyphset definition
 * U+2E1A HYPHEN WITH DIAERESIS: not included in any glyphset definition
 * U+2E1B TILDE WITH RING ABOVE: not included in any glyphset definition
 * U+2E1C LEFT LOW PARAPHRASE BRACKET: try adding nko
 * U+2E1D RIGHT LOW PARAPHRASE BRACKET: try adding nko
 * U+2E1E TILDE WITH DOT ABOVE: not included in any glyphset definition
 * U+2E1F TILDE WITH DOT BELOW: not included in any glyphset definition
 * U+2E20 LEFT VERTICAL BAR WITH QUILL: not included in any glyphset definition
 * U+2E21 RIGHT VERTICAL BAR WITH QUILL: not included in any glyphset definition
 * U+2E22 TOP LEFT HALF BRACKET: not included in any glyphset definition
 * U+2E23 TOP RIGHT HALF BRACKET: not included in any glyphset definition
 * U+2E24 BOTTOM LEFT HALF BRACKET: not included in any glyphset definition
 * U+2E25 BOTTOM RIGHT HALF BRACKET: not included in any glyphset definition
 * U+2E26 LEFT SIDEWAYS U BRACKET: not included in any glyphset definition
 * U+2E27 RIGHT SIDEWAYS U BRACKET: not included in any glyphset definition
 * U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam
 * U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam
 * U+2E2A TWO DOTS OVER ONE DOT PUNCTUATION: not included in any glyphset definition
 * U+2E2B ONE DOT OVER TWO DOTS PUNCTUATION: not included in any glyphset definition
 * U+2E2C SQUARED FOUR DOT PUNCTUATION: not included in any glyphset definition
 * U+2E2D FIVE DOT MARK: not included in any glyphset definition
 * U+2E2E REVERSED QUESTION MARK: not included in any glyphset definition
 * U+2E2F VERTICAL TILDE: not included in any glyphset definition
 * U+2E30 RING POINT: try adding avestan
 * U+2E31 WORD SEPARATOR MIDDLE DOT: try adding one of: avestan, old-hungarian, samaritan
 * U+2E32 TURNED COMMA: not included in any glyphset definition
 * U+2E33 RAISED DOT: try adding coptic
 * U+2E34 RAISED COMMA: try adding coptic
 * U+2E35 TURNED SEMICOLON: not included in any glyphset definition
 * U+2E36 DAGGER WITH LEFT GUARD: not included in any glyphset definition
 * U+2E37 DAGGER WITH RIGHT GUARD: not included in any glyphset definition
 * U+2E38 TURNED DAGGER: not included in any glyphset definition
 * U+2E39 TOP HALF SECTION SIGN: not included in any glyphset definition
 * U+2E3A TWO-EM DASH: not included in any glyphset definition
 * U+2E3B THREE-EM DASH: not included in any glyphset definition
 * U+2E3C STENOGRAPHIC FULL STOP: not included in any glyphset definition
 * U+2E3D VERTICAL SIX DOTS: not included in any glyphset definition
 * U+2E3E WIGGLY VERTICAL LINE: not included in any glyphset definition
 * U+2E3F CAPITULUM: not included in any glyphset definition
 * U+2E40 DOUBLE HYPHEN: not included in any glyphset definition
 * U+2E41 REVERSED COMMA: try adding adlam
 * U+2E42 DOUBLE LOW-REVERSED-9 QUOTATION MARK: not included in any glyphset definition
 * U+2E43 DASH WITH LEFT UPTURN: not included in any glyphset definition
 * U+2E44 DOUBLE SUSPENSION MARK: not included in any glyphset definition
 * U+2E45 INVERTED LOW KAVYKA: not included in any glyphset definition
 * U+2E46 INVERTED LOW KAVYKA WITH KAVYKA ABOVE: not included in any glyphset definition
 * U+2E47 LOW KAVYKA: not included in any glyphset definition
 * U+2E48 LOW KAVYKA WITH DOT: not included in any glyphset definition
 * U+2E49 DOUBLE STACKED COMMA: not included in any glyphset definition
 * U+2E4A DOTTED SOLIDUS: not included in any glyphset definition
 * U+2E4B TRIPLE DAGGER: not included in any glyphset definition
 * U+2E4C MEDIEVAL COMMA: not included in any glyphset definition
 * U+2E4D PARAGRAPHUS MARK: not included in any glyphset definition
 * U+2E4E PUNCTUS ELEVATUS MARK: not included in any glyphset definition
 * U+2E4F CORNISH VERSE DIVIDER: not included in any glyphset definition
 * U+2E50 CROSS PATTY WITH RIGHT CROSSBAR: not included in any glyphset definition
 * U+2E51 CROSS PATTY WITH LEFT CROSSBAR: not included in any glyphset definition
 * U+2E52 TIRONIAN SIGN CAPITAL ET: not included in any glyphset definition
 * U+2E53 MEDIEVAL EXCLAMATION MARK: not included in any glyphset definition
 * U+2E54 MEDIEVAL QUESTION MARK: not included in any glyphset definition
 * U+2E55 LEFT SQUARE BRACKET WITH STROKE: not included in any glyphset definition
 * U+2E56 RIGHT SQUARE BRACKET WITH STROKE: not included in any glyphset definition
 * U+2E57 LEFT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition
 * U+2E58 RIGHT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition
 * U+2E59 TOP HALF LEFT PARENTHESIS: not included in any glyphset definition
 * U+2E5A TOP HALF RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2E5B BOTTOM HALF LEFT PARENTHESIS: not included in any glyphset definition
 * U+2E5C BOTTOM HALF RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2E5D OBLIQUE HYPHEN: not included in any glyphset definition
 * U+A700 MODIFIER LETTER CHINESE TONE YIN PING: not included in any glyphset definition
 * U+A701 MODIFIER LETTER CHINESE TONE YANG PING: not included in any glyphset definition
 * U+A702 MODIFIER LETTER CHINESE TONE YIN SHANG: not included in any glyphset definition
 * U+A703 MODIFIER LETTER CHINESE TONE YANG SHANG: not included in any glyphset definition
 * U+A704 MODIFIER LETTER CHINESE TONE YIN QU: not included in any glyphset definition
 * U+A705 MODIFIER LETTER CHINESE TONE YANG QU: not included in any glyphset definition
 * U+A706 MODIFIER LETTER CHINESE TONE YIN RU: not included in any glyphset definition
 * U+A707 MODIFIER LETTER CHINESE TONE YANG RU: not included in any glyphset definition
 * U+A708 MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR: not included in any glyphset definition
 * U+A709 MODIFIER LETTER HIGH DOTTED TONE BAR: not included in any glyphset definition
 * U+A70A MODIFIER LETTER MID DOTTED TONE BAR: not included in any glyphset definition
 * U+A70B MODIFIER LETTER LOW DOTTED TONE BAR: not included in any glyphset definition
 * U+A70C MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR: not included in any glyphset definition
 * U+A70D MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A70E MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A70F MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A710 MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A711 MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A712 MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A713 MODIFIER LETTER HIGH LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A714 MODIFIER LETTER MID LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A715 MODIFIER LETTER LOW LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A716 MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A717 MODIFIER LETTER DOT VERTICAL BAR: not included in any glyphset definition
 * U+A718 MODIFIER LETTER DOT SLASH: not included in any glyphset definition
 * U+A719 MODIFIER LETTER DOT HORIZONTAL BAR: not included in any glyphset definition
 * U+A71A MODIFIER LETTER LOWER RIGHT CORNER ANGLE: not included in any glyphset definition
 * U+A71B MODIFIER LETTER RAISED UP ARROW: not included in any glyphset definition
 * U+A71C MODIFIER LETTER RAISED DOWN ARROW: not included in any glyphset definition
 * U+A71D MODIFIER LETTER RAISED EXCLAMATION MARK: not included in any glyphset definition
 * U+A71E MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK: not included in any glyphset definition
 * U+A71F MODIFIER LETTER LOW INVERTED EXCLAMATION MARK: not included in any glyphset definition
 * U+A92E KAYAH LI SIGN CWI: try adding kayah-li
 * U+AB30 LATIN SMALL LETTER BARRED ALPHA: not included in any glyphset definition
 * U+AB31 LATIN SMALL LETTER A REVERSED-SCHWA: not included in any glyphset definition
 * U+AB32 LATIN SMALL LETTER BLACKLETTER E: not included in any glyphset definition
 * U+AB33 LATIN SMALL LETTER BARRED E: not included in any glyphset definition
 * U+AB34 LATIN SMALL LETTER E WITH FLOURISH: not included in any glyphset definition
 * U+AB35 LATIN SMALL LETTER LENIS F: not included in any glyphset definition
 * U+AB36 LATIN SMALL LETTER SCRIPT G WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB37 LATIN SMALL LETTER L WITH INVERTED LAZY S: not included in any glyphset definition
 * U+AB38 LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition
 * U+AB39 LATIN SMALL LETTER L WITH MIDDLE RING: not included in any glyphset definition
 * U+AB3A LATIN SMALL LETTER M WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3B LATIN SMALL LETTER N WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3C LATIN SMALL LETTER ENG WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3D LATIN SMALL LETTER BLACKLETTER O: not included in any glyphset definition
 * U+AB3E LATIN SMALL LETTER BLACKLETTER O WITH STROKE: not included in any glyphset definition
 * U+AB3F LATIN SMALL LETTER OPEN O WITH STROKE: not included in any glyphset definition
 * U+AB40 LATIN SMALL LETTER INVERTED OE: not included in any glyphset definition
 * U+AB41 LATIN SMALL LETTER TURNED OE WITH STROKE: not included in any glyphset definition
 * U+AB42 LATIN SMALL LETTER TURNED OE WITH HORIZONTAL STROKE: not included in any glyphset definition
 * U+AB43 LATIN SMALL LETTER TURNED O OPEN-O: not included in any glyphset definition
 * U+AB44 LATIN SMALL LETTER TURNED O OPEN-O WITH STROKE: not included in any glyphset definition
 * U+AB45 LATIN SMALL LETTER STIRRUP R: not included in any glyphset definition
 * U+AB46 LATIN LETTER SMALL CAPITAL R WITH RIGHT LEG: not included in any glyphset definition
 * U+AB47 LATIN SMALL LETTER R WITHOUT HANDLE: not included in any glyphset definition
 * U+AB48 LATIN SMALL LETTER DOUBLE R: not included in any glyphset definition
 * U+AB49 LATIN SMALL LETTER R WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB4A LATIN SMALL LETTER DOUBLE R WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB4B LATIN SMALL LETTER SCRIPT R: not included in any glyphset definition
 * U+AB4C LATIN SMALL LETTER SCRIPT R WITH RING: not included in any glyphset definition
 * U+AB4D LATIN SMALL LETTER BASELINE ESH: not included in any glyphset definition
 * U+AB4E LATIN SMALL LETTER U WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB4F LATIN SMALL LETTER U BAR WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB50 LATIN SMALL LETTER UI: not included in any glyphset definition
 * U+AB51 LATIN SMALL LETTER TURNED UI: not included in any glyphset definition
 * U+AB52 LATIN SMALL LETTER U WITH LEFT HOOK: not included in any glyphset definition
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+AB54 LATIN SMALL LETTER CHI WITH LOW RIGHT RING: not included in any glyphset definition
 * U+AB55 LATIN SMALL LETTER CHI WITH LOW LEFT SERIF: not included in any glyphset definition
 * U+AB56 LATIN SMALL LETTER X WITH LOW RIGHT RING: not included in any glyphset definition
 * U+AB57 LATIN SMALL LETTER X WITH LONG LEFT LEG: not included in any glyphset definition
 * U+AB58 LATIN SMALL LETTER X WITH LONG LEFT LEG AND LOW RIGHT RING: not included in any glyphset definition
 * U+AB59 LATIN SMALL LETTER X WITH LONG LEFT LEG WITH SERIF: not included in any glyphset definition
 * U+AB5A LATIN SMALL LETTER Y WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB5B MODIFIER BREVE WITH INVERTED BREVE: not included in any glyphset definition
 * U+AB5C MODIFIER LETTER SMALL HENG: not included in any glyphset definition
 * U+AB5D MODIFIER LETTER SMALL L WITH INVERTED LAZY S: not included in any glyphset definition
 * U+AB5E MODIFIER LETTER SMALL L WITH MIDDLE TILDE: not included in any glyphset definition
 * U+AB5F MODIFIER LETTER SMALL U WITH LEFT HOOK: not included in any glyphset definition
 * U+AB60 LATIN SMALL LETTER SAKHA YAT: not included in any glyphset definition
 * U+AB61 LATIN SMALL LETTER IOTIFIED E: not included in any glyphset definition
 * U+AB62 LATIN SMALL LETTER OPEN OE: not included in any glyphset definition
 * U+AB63 LATIN SMALL LETTER UO: not included in any glyphset definition
 * U+AB64 LATIN SMALL LETTER INVERTED ALPHA: not included in any glyphset definition
 * U+AB65 GREEK LETTER SMALL CAPITAL OMEGA: not included in any glyphset definition
 * U+AB66 LATIN SMALL LETTER DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+AB67 LATIN SMALL LETTER TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+AB68 LATIN SMALL LETTER TURNED R WITH MIDDLE TILDE: not included in any glyphset definition
 * U+AB69 MODIFIER LETTER SMALL TURNED W: not included in any glyphset definition
 * U+AB6A MODIFIER LETTER LEFT TACK: not included in any glyphset definition
 * U+AB6B MODIFIER LETTER RIGHT TACK: not included in any glyphset definition
 * U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition
 * U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition
 * U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition
 * U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition
 * U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition
 * U+FB05 LATIN SMALL LIGATURE LONG S T: not included in any glyphset definition
 * U+FB06 LATIN SMALL LIGATURE ST: not included in any glyphset definition
 * U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi
 * U+FE20 COMBINING LIGATURE LEFT HALF: try adding caucasian-albanian
 * U+FE21 COMBINING LIGATURE RIGHT HALF: try adding caucasian-albanian
 * U+FE22 COMBINING DOUBLE TILDE LEFT HALF: try adding caucasian-albanian
 * U+FE23 COMBINING DOUBLE TILDE RIGHT HALF: try adding caucasian-albanian
 * U+FE24 COMBINING MACRON LEFT HALF: try adding one of: coptic, caucasian-albanian
 * U+FE25 COMBINING MACRON RIGHT HALF: try adding one of: coptic, caucasian-albanian
 * U+FE26 COMBINING CONJOINING MACRON: try adding one of: coptic, caucasian-albanian
 * U+FE27 COMBINING LIGATURE LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE28 COMBINING LIGATURE RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE29 COMBINING TILDE LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE2A COMBINING TILDE RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE2B COMBINING MACRON LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE2C COMBINING MACRON RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE2D COMBINING CONJOINING MACRON BELOW: try adding caucasian-albanian
 * U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition
 * U+10780 MODIFIER LETTER SMALL CAPITAL AA: not included in any glyphset definition
 * U+10781 MODIFIER LETTER SUPERSCRIPT TRIANGULAR COLON: not included in any glyphset definition
 * U+10782 MODIFIER LETTER SUPERSCRIPT HALF TRIANGULAR COLON: not included in any glyphset definition
 * U+10783 MODIFIER LETTER SMALL AE: not included in any glyphset definition
 * U+10784 MODIFIER LETTER SMALL CAPITAL B: not included in any glyphset definition
 * U+10785 MODIFIER LETTER SMALL B WITH HOOK: not included in any glyphset definition
 * U+10787 MODIFIER LETTER SMALL DZ DIGRAPH: not included in any glyphset definition
 * U+10788 MODIFIER LETTER SMALL DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+10789 MODIFIER LETTER SMALL DZ DIGRAPH WITH CURL: not included in any glyphset definition
 * U+1078A MODIFIER LETTER SMALL DEZH DIGRAPH: not included in any glyphset definition
 * U+1078B MODIFIER LETTER SMALL D WITH TAIL: not included in any glyphset definition
 * U+1078C MODIFIER LETTER SMALL D WITH HOOK: not included in any glyphset definition
 * U+1078D MODIFIER LETTER SMALL D WITH HOOK AND TAIL: not included in any glyphset definition
 * U+1078E MODIFIER LETTER SMALL REVERSED E: not included in any glyphset definition
 * U+1078F MODIFIER LETTER SMALL CLOSED REVERSED OPEN E: not included in any glyphset definition
 * U+10790 MODIFIER LETTER SMALL FENG DIGRAPH: not included in any glyphset definition
 * U+10791 MODIFIER LETTER SMALL RAMS HORN: not included in any glyphset definition
 * U+10792 MODIFIER LETTER SMALL CAPITAL G: not included in any glyphset definition
 * U+10793 MODIFIER LETTER SMALL G WITH HOOK: not included in any glyphset definition
 * U+10794 MODIFIER LETTER SMALL CAPITAL G WITH HOOK: not included in any glyphset definition
 * U+10795 MODIFIER LETTER SMALL H WITH STROKE: not included in any glyphset definition
 * U+10796 MODIFIER LETTER SMALL CAPITAL H: not included in any glyphset definition
 * U+10797 MODIFIER LETTER SMALL HENG WITH HOOK: not included in any glyphset definition
 * U+10798 MODIFIER LETTER SMALL DOTLESS J WITH STROKE AND HOOK: not included in any glyphset definition
 * U+10799 MODIFIER LETTER SMALL LS DIGRAPH: not included in any glyphset definition
 * U+1079A MODIFIER LETTER SMALL LZ DIGRAPH: not included in any glyphset definition
 * U+1079B MODIFIER LETTER SMALL L WITH BELT: not included in any glyphset definition
 * U+1079C MODIFIER LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition
 * U+1079D MODIFIER LETTER SMALL L WITH RETROFLEX HOOK AND BELT: not included in any glyphset definition
 * U+1079E MODIFIER LETTER SMALL LEZH: not included in any glyphset definition
 * U+1079F MODIFIER LETTER SMALL LEZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107A0 MODIFIER LETTER SMALL TURNED Y: not included in any glyphset definition
 * U+107A1 MODIFIER LETTER SMALL TURNED Y WITH BELT: not included in any glyphset definition
 * U+107A2 MODIFIER LETTER SMALL O WITH STROKE: not included in any glyphset definition
 * U+107A3 MODIFIER LETTER SMALL CAPITAL OE: not included in any glyphset definition
 * U+107A4 MODIFIER LETTER SMALL CLOSED OMEGA: not included in any glyphset definition
 * U+107A5 MODIFIER LETTER SMALL Q: not included in any glyphset definition
 * U+107A6 MODIFIER LETTER SMALL TURNED R WITH LONG LEG: not included in any glyphset definition
 * U+107A7 MODIFIER LETTER SMALL TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition
 * U+107A8 MODIFIER LETTER SMALL R WITH TAIL: not included in any glyphset definition
 * U+107A9 MODIFIER LETTER SMALL R WITH FISHHOOK: not included in any glyphset definition
 * U+107AA MODIFIER LETTER SMALL CAPITAL R: not included in any glyphset definition
 * U+107AB MODIFIER LETTER SMALL TC DIGRAPH WITH CURL: not included in any glyphset definition
 * U+107AC MODIFIER LETTER SMALL TS DIGRAPH: not included in any glyphset definition
 * U+107AD MODIFIER LETTER SMALL TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107AE MODIFIER LETTER SMALL TESH DIGRAPH: not included in any glyphset definition
 * U+107AF MODIFIER LETTER SMALL T WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107B0 MODIFIER LETTER SMALL V WITH RIGHT HOOK: not included in any glyphset definition
 * U+107B2 MODIFIER LETTER SMALL CAPITAL Y: not included in any glyphset definition
 * U+107B3 MODIFIER LETTER GLOTTAL STOP WITH STROKE: not included in any glyphset definition
 * U+107B4 MODIFIER LETTER REVERSED GLOTTAL STOP WITH STROKE: not included in any glyphset definition
 * U+107B5 MODIFIER LETTER BILABIAL CLICK: not included in any glyphset definition
 * U+107B6 MODIFIER LETTER DENTAL CLICK: not included in any glyphset definition
 * U+107B7 MODIFIER LETTER LATERAL CLICK: not included in any glyphset definition
 * U+107B8 MODIFIER LETTER ALVEOLAR CLICK: not included in any glyphset definition
 * U+107B9 MODIFIER LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107BA MODIFIER LETTER SMALL S WITH CURL: not included in any glyphset definition
 * U+1DF00 LATIN SMALL LETTER FENG DIGRAPH WITH TRILL: not included in any glyphset definition
 * U+1DF01 LATIN SMALL LETTER REVERSED SCRIPT G: not included in any glyphset definition
 * U+1DF02 LATIN LETTER SMALL CAPITAL TURNED G: not included in any glyphset definition
 * U+1DF03 LATIN SMALL LETTER REVERSED K: not included in any glyphset definition
 * U+1DF04 LATIN LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition
 * U+1DF05 LATIN SMALL LETTER LEZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF06 LATIN SMALL LETTER TURNED Y WITH BELT: not included in any glyphset definition
 * U+1DF07 LATIN SMALL LETTER REVERSED ENG: not included in any glyphset definition
 * U+1DF08 LATIN SMALL LETTER TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF09 LATIN SMALL LETTER T WITH HOOK AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF0A LATIN LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF0B LATIN SMALL LETTER ESH WITH DOUBLE BAR: not included in any glyphset definition
 * U+1DF0C LATIN SMALL LETTER ESH WITH DOUBLE BAR AND CURL: not included in any glyphset definition
 * U+1DF0D LATIN SMALL LETTER TURNED T WITH CURL: not included in any glyphset definition
 * U+1DF0E LATIN LETTER INVERTED GLOTTAL STOP WITH CURL: not included in any glyphset definition
 * U+1DF0F LATIN LETTER STRETCHED C WITH CURL: not included in any glyphset definition
 * U+1DF10 LATIN LETTER SMALL CAPITAL TURNED K: not included in any glyphset definition
 * U+1DF11 LATIN SMALL LETTER L WITH FISHHOOK: not included in any glyphset definition
 * U+1DF12 LATIN SMALL LETTER DEZH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF13 LATIN SMALL LETTER L WITH BELT AND PALATAL HOOK: not included in any glyphset definition
 * U+1DF14 LATIN SMALL LETTER ENG WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF15 LATIN SMALL LETTER TURNED R WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF16 LATIN SMALL LETTER R WITH FISHHOOK AND PALATAL HOOK: not included in any glyphset definition
 * U+1DF17 LATIN SMALL LETTER TESH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF18 LATIN SMALL LETTER EZH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF19 LATIN SMALL LETTER DEZH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1A LATIN SMALL LETTER I WITH STROKE AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1B LATIN SMALL LETTER O WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1C LATIN SMALL LETTER TESH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1D LATIN SMALL LETTER C WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1E LATIN SMALL LETTER S WITH CURL: not included in any glyphset definition

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic`, `cyrillic-ext`, `devanagari`, `greek`, `greek-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.4Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Desoftcy
	* Elsoftcy
	* Iotaserifed
	* Ocrossedcy
	* Smiddlestroke
	* Ukmonographcy
	* Ustroke
	* Wanglicana
	* aanuktadeva
	* acandraanusvaradeva
	* acandradeva
	* acandranuktaanusvaradeva
	* acandranuktadeva
	* anuktadeva
	* ashortanusvaradeva
	* ashortdeva
	* ashortnuktaanusvaradeva
	* ashortnuktadeva
	* auanusvaradeva
	* aunuktaanusvaradeva
	* aunuktadeva
	* awanusvaradeva
	* awdeva
	* babardeva
	* badhadeva
	* banuktaradeva
	* banuktaraprehalfdeva
	* baradeva
	* baraprehalfdeva
	* canuktaradeva
	* canuktaraprehalfdeva
	* caradeva
	* caraprehalfdeva
	* chaaltdeva
	* chanuktaaltdeva
	* chayadeva
	* dabadeva
	* dadayadeva
	* dadhayadeva
	* daghadeva
	* danuktaradeva
	* danuktarvocalicdeva
	* danuktaudeva
	* danuktauudeva
	* daradeva
	* dararvocalicdeva
	* daraudeva
	* darauudeva
	* darvocalicdeva
	* daudeva
	* dauudeva
	* davayadeva
	* dayadeva
	* ddhaddhadeva
	* ddhayadeva
	* desoftcy
	* dhanuktaradeva
	* dhanuktaraprehalfdeva
	* dharadeva
	* dharaprehalfdeva
	* ecandravowelrephcandrabindudeva
	* elsoftcy
	* emsoftcy
	* ghanuktadeva
	* ghanuktaprehalfdeva
	* ghanuktaradeva
	* ghanuktaraprehalfdeva
	* ghaprehalfdeva
	* gharadeva
	* gharaprehalfdeva
	* haladeva
	* hannadeva
	* haraudeva
	* harauuUIdeva
	* harauudeva
	* heavyyaradeva
	* heavyyaraprehalfdeva
	* iianusvaradeva
	* iinuktaanusvaradeva
	* iinuktadeva
	* iivowelcandrabindu1deva
	* iivowelcandrabindudeva
	* iivowelsignreph2deva
	* iivowelsignreph3deva
	* iivowelsignrephanusvara2deva
	* iivowelsignrephanusvara3deva
	* iivowelsignrephcandrabindu2deva
	* iivowelsignrephcandrabindu3deva
	* inuktadeva
	* ivowelsignreph01deva
	* ivowelsignreph02deva
	* ivowelsignreph03deva
	* ivowelsignreph04deva
	* ivowelsignrephanusvara01deva
	* ivowelsignrephanusvara02deva
	* ivowelsignrephanusvara03deva
	* ivowelsignrephanusvara04deva
	* ivowelsignrephanusvara05deva
	* ivowelsignrephcandrabindu01deva
	* ivowelsignrephcandrabindu02deva
	* ivowelsignrephcandrabindu03deva
	* ivowelsignrephcandrabindu04deva
	* ivowelsignrephcandrabindu05deva
	* ivowelsignrephcandrabindu06deva
	* ivowelsignrephcandrabindu07deva
	* ivowelsignrephcandrabindu08deva
	* ivowelsignrephcandrabindu09deva
	* ivowelsignrephcandrabindu10deva
	* jaddadeva
	* jajadeva
	* janyadeva
	* janyaradeva
	* jhanuktadeva
	* jhanuktaprehalfdeva
	* jhanuktaradeva
	* jhanuktaraprehalfdeva
	* jhaprehalfdeva
	* jharadeva
	* jharaprehalfdeva
	* kanuktaradeva
	* kanuktaraprehalfdeva
	* karadeva
	* karaprehalfdeva
	* kashadeva
	* kassadeva
	* kassaprehalfdeva
	* kassaradeva
	* kassaraprehalfdeva
	* khanuktaradeva
	* kharadeva
	* khashadeva
	* laddadeva
	* laddaradeva
	* lanuktaradeva
	* laradeva
	* llaaltdeva
	* llanuktaradeva
	* llaradeva
	* lllaaltdeva
	* llvocalicnuktadeva
	* lvocalicnuktadeva
	* mabhadeva
	* maparadeva
	* marwariddaddadeva
	* marwariddaddhadeva
	* marwariddaradeva
	* marwariddayadeva
	* naddadeva
	* naddaradeva
	* nadharadeva
	* natharadeva
	* ngayadeva
	* nyajadeva
	* nyanuktadeva
	* nyanuktaradeva
	* nyaradeva
	* oanusvaradeva
	* ocandraanusvaradeva
	* ocandranuktaanusvaradeva
	* ocandranuktadeva
	* ocandravowelrephcandrabindudeva
	* oeanusvaradeva
	* oedeva
	* oeopen
	* onuktaanusvaradeva
	* onuktadeva
	* ooeanusvaradeva
	* ooedeva
	* oshortanusvaradeva
	* oshortnuktaanusvaradeva
	* oshortnuktadeva
	* panadeva
	* panuktaradeva
	* panuktaraprehalfdeva
	* paradeva
	* paragraphus
	* paraprehalfdeva
	* phanuktaradeva
	* phanuktaraprehalfdeva
	* pharadeva
	* pharaprehalfdeva
	* ranuktauudeva
	* rauudeva
	* rrvocalicnuktadeva
	* sanuktadeva
	* sanuktaradeva
	* sapadeva
	* sapaprehalfdeva
	* saparadeva
	* saphadeva
	* saradeva
	* sathadeva
	* sathaprehalfdeva
	* shadevaMAR
	* shanuktadevaMAR
	* shanuktaprehalfdevaMAR
	* shaprehalfdevaMAR
	* smiddlestroke
	* solidusdotted
	* ssanuktaradeva
	* ssaradeva
	* ssattayadeva
	* ssatthadeva
	* ssattharadeva
	* ssatthayadeva
	* stackedcommadbl
	* thanuktaradeva
	* tharadeva
	* tthayadeva
	* uedeva
	* uni0224
	* uni023A
	* uni023B
	* uni023C
	* uni023E
	* uni0244
	* uni0246
	* uni024E
	* uni024F
	* uni0289
	* uni0372
	* uni0406
	* uni0407
	* uni0409
	* uni040C
	* uni040E
	* uni0416
	* uni0419
	* uni041A
	* uni0436
	* uni0444
	* uni049C
	* uni049D
	* uni049E
	* uni04C1
	* uni04C2
	* uni04D0
	* uni04D1
	* uni04D6
	* uni04D7
	* uni04DC
	* uni04DD
	* uni051E
	* uni051F
	* uni052A
	* uni052B
	* uni1D70
	* uni1D7A
	* uni1D7D
	* uni1D7E
	* uni1D7F
	* uni1EFB
	* uni20A5
	* uni20B2
	* uni20B6
	* uni20B7
	* uni20BD
	* uni20BE
	* uni20BF
	* uni211F
	* uni2123
	* uni2C66
	* uni2C7A
	* uni2E3F
	* uniA642
	* uniA648
	* uniA649
	* uniA66E
	* uniA680
	* uniA681
	* uniA684
	* uniA685
	* uniA692
	* uniA733
	* uniA734
	* uniA735
	* uniA737
	* uniA73A
	* uniA740
	* uniA744
	* uniA745
	* uniA74A
	* uniA74B
	* uniA75E
	* uniA773
	* uniA776
	* uniA7A1
	* uniA7A3
	* uniA7A4
	* uniA7A5
	* uniA7A8
	* uniA7A9
	* uniAB30
	* uniAB39
	* uniAB3E
	* uniAB41
	* uniAB44
	* uniAB4F
	* uniAB5A
	* uniAB65
	* unuktadeva
	* uo
	* uuedeva
	* uunuktadeva
	* vanuktaradeva
	* vanuktaraprehalfdeva
	* varadeva
	* varaprehalfdeva
	* wanglicana
	* yanuktaradeva and yaradeva
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


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03C5030803060301

	- uni1FD8.salt

	- uni1FD9.salt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 572 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 322:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 uni031A (U+031A), uni1ACC (U+1ACC), uni1ACD (U+1ACD) and uni1ACE (U+1ACE) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><br></div></details><details><summary><b>[17] NotoSans-Italic[wdth,wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking with ots-sanitize. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ots">com.google.fonts/check/ots</a>)</summary><div>


* 🔥 **FAIL** ots-sanitize returned an error code (1). Output follows:

ERROR: GPOS: Bad mark anchor offset 0 for mark table 34
ERROR: GPOS: Failed to parse mark array
ERROR: GPOS: Failed to parse subtable 0
ERROR: GPOS: Failed to parse lookup 35
ERROR: GPOS: Failed to parse lookup list table
ERROR: GPOS: Failed to parse table
Failed to sanitize file!
 [code: ots-sanitize-error]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* 🔥 **FAIL** The following glyphs could not be attached to the dotted circle glyph:

	- ayvowelsigndeva

	- binducandradeva

	- candralongevowelsigndeva

	- oevowelsigndeva

	- uevowelsigndeva

	- uni0901

	- uni0902

	- uni093C

	- uni0941

	- uni0942

	- uni0943

	- uni0944

	- uni0945

	- uni0946

	- uni0947

	- uni0948

	- uni094D

	- uni0951

	- uni0952

	- uni0953

	- uni0954

	- uni0962

	- uni0963

	- uuevowelsigndeva [code: unattached-dotted-circle-marks]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02B0 MODIFIER LETTER SMALL H: not included in any glyphset definition
 * U+02B1 MODIFIER LETTER SMALL H WITH HOOK: not included in any glyphset definition
 * U+02B2 MODIFIER LETTER SMALL J: not included in any glyphset definition
 * U+02B3 MODIFIER LETTER SMALL R: not included in any glyphset definition
 * U+02B4 MODIFIER LETTER SMALL TURNED R: not included in any glyphset definition
 * U+02B5 MODIFIER LETTER SMALL TURNED R WITH HOOK: not included in any glyphset definition
 * U+02B6 MODIFIER LETTER SMALL CAPITAL INVERTED R: not included in any glyphset definition
 * U+02B7 MODIFIER LETTER SMALL W: not included in any glyphset definition
 * U+02B8 MODIFIER LETTER SMALL Y: not included in any glyphset definition
 * U+02B9 MODIFIER LETTER PRIME: not included in any glyphset definition
 * U+02BA MODIFIER LETTER DOUBLE PRIME: not included in any glyphset definition
 * U+02BD MODIFIER LETTER REVERSED COMMA: not included in any glyphset definition
 * U+02BE MODIFIER LETTER RIGHT HALF RING: not included in any glyphset definition
 * U+02BF MODIFIER LETTER LEFT HALF RING: not included in any glyphset definition
 * U+02C0 MODIFIER LETTER GLOTTAL STOP: not included in any glyphset definition
 * U+02C1 MODIFIER LETTER REVERSED GLOTTAL STOP: not included in any glyphset definition
 * U+02C2 MODIFIER LETTER LEFT ARROWHEAD: not included in any glyphset definition
 * U+02C3 MODIFIER LETTER RIGHT ARROWHEAD: not included in any glyphset definition
 * U+02C4 MODIFIER LETTER UP ARROWHEAD: not included in any glyphset definition
 * U+02C5 MODIFIER LETTER DOWN ARROWHEAD: not included in any glyphset definition
 * U+02C7 CARON: try adding one of: canadian-aboriginal, tifinagh, yi
 * U+02C8 MODIFIER LETTER VERTICAL LINE: not included in any glyphset definition
 * U+02C9 MODIFIER LETTER MACRON: not included in any glyphset definition
 * U+02CA MODIFIER LETTER ACUTE ACCENT: not included in any glyphset definition
 * U+02CB MODIFIER LETTER GRAVE ACCENT: not included in any glyphset definition
 * U+02CC MODIFIER LETTER LOW VERTICAL LINE: not included in any glyphset definition
 * U+02CD MODIFIER LETTER LOW MACRON: try adding lisu
 * U+02CE MODIFIER LETTER LOW GRAVE ACCENT: not included in any glyphset definition
 * U+02CF MODIFIER LETTER LOW ACUTE ACCENT: not included in any glyphset definition
 * U+02D0 MODIFIER LETTER TRIANGULAR COLON: not included in any glyphset definition
 * U+02D1 MODIFIER LETTER HALF TRIANGULAR COLON: not included in any glyphset definition
 * U+02D2 MODIFIER LETTER CENTRED RIGHT HALF RING: not included in any glyphset definition
 * U+02D3 MODIFIER LETTER CENTRED LEFT HALF RING: not included in any glyphset definition
 * U+02D4 MODIFIER LETTER UP TACK: not included in any glyphset definition
 * U+02D5 MODIFIER LETTER DOWN TACK: not included in any glyphset definition
 * U+02D6 MODIFIER LETTER PLUS SIGN: not included in any glyphset definition
 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02DE MODIFIER LETTER RHOTIC HOOK: not included in any glyphset definition
 * U+02DF MODIFIER LETTER CROSS ACCENT: not included in any glyphset definition
 * U+02E0 MODIFIER LETTER SMALL GAMMA: not included in any glyphset definition
 * U+02E1 MODIFIER LETTER SMALL L: not included in any glyphset definition
 * U+02E2 MODIFIER LETTER SMALL S: not included in any glyphset definition
 * U+02E3 MODIFIER LETTER SMALL X: not included in any glyphset definition
 * U+02E4 MODIFIER LETTER SMALL REVERSED GLOTTAL STOP: not included in any glyphset definition
 * U+02E5 MODIFIER LETTER EXTRA-HIGH TONE BAR: not included in any glyphset definition
 * U+02E6 MODIFIER LETTER HIGH TONE BAR: not included in any glyphset definition
 * U+02E7 MODIFIER LETTER MID TONE BAR: not included in any glyphset definition
 * U+02E8 MODIFIER LETTER LOW TONE BAR: not included in any glyphset definition
 * U+02E9 MODIFIER LETTER EXTRA-LOW TONE BAR: not included in any glyphset definition
 * U+02EA MODIFIER LETTER YIN DEPARTING TONE MARK: not included in any glyphset definition
 * U+02EB MODIFIER LETTER YANG DEPARTING TONE MARK: not included in any glyphset definition
 * U+02EC MODIFIER LETTER VOICING: not included in any glyphset definition
 * U+02ED MODIFIER LETTER UNASPIRATED: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+02EF MODIFIER LETTER LOW DOWN ARROWHEAD: not included in any glyphset definition
 * U+02F0 MODIFIER LETTER LOW UP ARROWHEAD: not included in any glyphset definition
 * U+02F1 MODIFIER LETTER LOW LEFT ARROWHEAD: not included in any glyphset definition
 * U+02F2 MODIFIER LETTER LOW RIGHT ARROWHEAD: not included in any glyphset definition
 * U+02F3 MODIFIER LETTER LOW RING: not included in any glyphset definition
 * U+02F4 MODIFIER LETTER MIDDLE GRAVE ACCENT: not included in any glyphset definition
 * U+02F5 MODIFIER LETTER MIDDLE DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+02F6 MODIFIER LETTER MIDDLE DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02F7 MODIFIER LETTER LOW TILDE: not included in any glyphset definition
 * U+02F8 MODIFIER LETTER RAISED COLON: not included in any glyphset definition
 * U+02F9 MODIFIER LETTER BEGIN HIGH TONE: not included in any glyphset definition
 * U+02FA MODIFIER LETTER END HIGH TONE: not included in any glyphset definition
 * U+02FB MODIFIER LETTER BEGIN LOW TONE: not included in any glyphset definition
 * U+02FC MODIFIER LETTER END LOW TONE: not included in any glyphset definition
 * U+02FD MODIFIER LETTER SHELF: not included in any glyphset definition
 * U+02FE MODIFIER LETTER OPEN SHELF: not included in any glyphset definition
 * U+02FF MODIFIER LETTER LOW LEFT ARROW: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee
 * U+0305 COMBINING OVERLINE: try adding one of: coptic, gothic, glagolitic, elbasan, math
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: coptic, malayalam, tai-le, old-permic, math, canadian-aboriginal, tifinagh, syriac
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: cherokee, tai-le
 * U+030D COMBINING VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+0310 COMBINING CANDRABINDU: not included in any glyphset definition
 * U+0311 COMBINING INVERTED BREVE: try adding coptic
 * U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition
 * U+0313 COMBINING COMMA ABOVE: try adding old-permic
 * U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition
 * U+0315 COMBINING COMMA ABOVE RIGHT: not included in any glyphset definition
 * U+0316 COMBINING GRAVE ACCENT BELOW: not included in any glyphset definition
 * U+0317 COMBINING ACUTE ACCENT BELOW: not included in any glyphset definition
 * U+0318 COMBINING LEFT TACK BELOW: not included in any glyphset definition
 * U+0319 COMBINING RIGHT TACK BELOW: not included in any glyphset definition
 * U+031A COMBINING LEFT ANGLE ABOVE: not included in any glyphset definition
 * U+031B COMBINING HORN: not included in any glyphset definition
 * U+031C COMBINING LEFT HALF RING BELOW: not included in any glyphset definition
 * U+031D COMBINING UP TACK BELOW: not included in any glyphset definition
 * U+031E COMBINING DOWN TACK BELOW: not included in any glyphset definition
 * U+031F COMBINING PLUS SIGN BELOW: not included in any glyphset definition
 * U+0320 COMBINING MINUS SIGN BELOW: try adding syriac
 * U+0321 COMBINING PALATALIZED HOOK BELOW: not included in any glyphset definition
 * U+0322 COMBINING RETROFLEX HOOK BELOW: not included in any glyphset definition
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition
 * U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition
 * U+032C COMBINING CARON BELOW: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee
 * U+0331 COMBINING MACRON BELOW: try adding one of: gothic, tifinagh, cherokee, syriac, caucasian-albanian
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0333 COMBINING DOUBLE LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition
 * U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0339 COMBINING RIGHT HALF RING BELOW: not included in any glyphset definition
 * U+033A COMBINING INVERTED BRIDGE BELOW: not included in any glyphset definition
 * U+033B COMBINING SQUARE BELOW: not included in any glyphset definition
 * U+033C COMBINING SEAGULL BELOW: not included in any glyphset definition
 * U+033D COMBINING X ABOVE: not included in any glyphset definition
 * U+033E COMBINING VERTICAL TILDE: not included in any glyphset definition
 * U+033F COMBINING DOUBLE OVERLINE: try adding coptic
 * U+0340 COMBINING GRAVE TONE MARK: not included in any glyphset definition
 * U+0341 COMBINING ACUTE TONE MARK: not included in any glyphset definition
 * U+0342 COMBINING GREEK PERISPOMENI: not included in any glyphset definition
 * U+0343 COMBINING GREEK KORONIS: not included in any glyphset definition
 * U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition
 * U+0345 COMBINING GREEK YPOGEGRAMMENI: not included in any glyphset definition
 * U+0346 COMBINING BRIDGE ABOVE: not included in any glyphset definition
 * U+0347 COMBINING EQUALS SIGN BELOW: not included in any glyphset definition
 * U+0348 COMBINING DOUBLE VERTICAL LINE BELOW: not included in any glyphset definition
 * U+0349 COMBINING LEFT ANGLE BELOW: not included in any glyphset definition
 * U+034A COMBINING NOT TILDE ABOVE: not included in any glyphset definition
 * U+034B COMBINING HOMOTHETIC ABOVE: not included in any glyphset definition
 * U+034C COMBINING ALMOST EQUAL TO ABOVE: not included in any glyphset definition
 * U+034D COMBINING LEFT RIGHT ARROW BELOW: not included in any glyphset definition
 * U+034E COMBINING UPWARDS ARROW BELOW: not included in any glyphset definition
 * U+034F COMBINING GRAPHEME JOINER: not included in any glyphset definition
 * U+0350 COMBINING RIGHT ARROWHEAD ABOVE: not included in any glyphset definition
 * U+0351 COMBINING LEFT HALF RING ABOVE: not included in any glyphset definition
 * U+0352 COMBINING FERMATA: not included in any glyphset definition
 * U+0353 COMBINING X BELOW: not included in any glyphset definition
 * U+0354 COMBINING LEFT ARROWHEAD BELOW: not included in any glyphset definition
 * U+0355 COMBINING RIGHT ARROWHEAD BELOW: not included in any glyphset definition
 * U+0356 COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD BELOW: not included in any glyphset definition
 * U+0357 COMBINING RIGHT HALF RING ABOVE: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+0359 COMBINING ASTERISK BELOW: not included in any glyphset definition
 * U+035A COMBINING DOUBLE RING BELOW: not included in any glyphset definition
 * U+035B COMBINING ZIGZAG ABOVE: not included in any glyphset definition
 * U+035C COMBINING DOUBLE BREVE BELOW: not included in any glyphset definition
 * U+035D COMBINING DOUBLE BREVE: not included in any glyphset definition
 * U+035E COMBINING DOUBLE MACRON: try adding coptic
 * U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition
 * U+0360 COMBINING DOUBLE TILDE: not included in any glyphset definition
 * U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
 * U+0362 COMBINING DOUBLE RIGHTWARDS ARROW BELOW: not included in any glyphset definition
 * U+0363 COMBINING LATIN SMALL LETTER A: not included in any glyphset definition
 * U+0364 COMBINING LATIN SMALL LETTER E: not included in any glyphset definition
 * U+0365 COMBINING LATIN SMALL LETTER I: not included in any glyphset definition
 * U+0366 COMBINING LATIN SMALL LETTER O: not included in any glyphset definition
 * U+0367 COMBINING LATIN SMALL LETTER U: not included in any glyphset definition
 * U+0368 COMBINING LATIN SMALL LETTER C: not included in any glyphset definition
 * U+0369 COMBINING LATIN SMALL LETTER D: not included in any glyphset definition
 * U+036A COMBINING LATIN SMALL LETTER H: not included in any glyphset definition
 * U+036B COMBINING LATIN SMALL LETTER M: not included in any glyphset definition
 * U+036C COMBINING LATIN SMALL LETTER R: not included in any glyphset definition
 * U+036D COMBINING LATIN SMALL LETTER T: not included in any glyphset definition
 * U+036E COMBINING LATIN SMALL LETTER V: not included in any glyphset definition
 * U+036F COMBINING LATIN SMALL LETTER X: not included in any glyphset definition
 * U+1AB0 COMBINING DOUBLED CIRCUMFLEX ACCENT: not included in any glyphset definition
 * U+1AB1 COMBINING DIAERESIS-RING: not included in any glyphset definition
 * U+1AB2 COMBINING INFINITY: not included in any glyphset definition
 * U+1AB3 COMBINING DOWNWARDS ARROW: not included in any glyphset definition
 * U+1AB4 COMBINING TRIPLE DOT: not included in any glyphset definition
 * U+1AB5 COMBINING X-X BELOW: not included in any glyphset definition
 * U+1AB6 COMBINING WIGGLY LINE BELOW: not included in any glyphset definition
 * U+1AB7 COMBINING OPEN MARK BELOW: not included in any glyphset definition
 * U+1AB8 COMBINING DOUBLE OPEN MARK BELOW: not included in any glyphset definition
 * U+1AB9 COMBINING LIGHT CENTRALIZATION STROKE BELOW: not included in any glyphset definition
 * U+1ABA COMBINING STRONG CENTRALIZATION STROKE BELOW: not included in any glyphset definition
 * U+1ABB COMBINING PARENTHESES ABOVE: not included in any glyphset definition
 * U+1ABC COMBINING DOUBLE PARENTHESES ABOVE: not included in any glyphset definition
 * U+1ABD COMBINING PARENTHESES BELOW: not included in any glyphset definition
 * U+1ABE COMBINING PARENTHESES OVERLAY: not included in any glyphset definition
 * U+1ABF COMBINING LATIN SMALL LETTER W BELOW: not included in any glyphset definition
 * U+1AC0 COMBINING LATIN SMALL LETTER TURNED W BELOW: not included in any glyphset definition
 * U+1AC5 COMBINING SQUARE BRACKETS ABOVE: not included in any glyphset definition
 * U+1AC7 COMBINING INVERTED DOUBLE ARCH ABOVE: not included in any glyphset definition
 * U+1AC8 COMBINING PLUS SIGN ABOVE: not included in any glyphset definition
 * U+1AC9 COMBINING DOUBLE PLUS SIGN ABOVE: not included in any glyphset definition
 * U+1ACA COMBINING DOUBLE PLUS SIGN BELOW: not included in any glyphset definition
 * U+1ACB COMBINING TRIPLE ACUTE ACCENT: not included in any glyphset definition
 * U+1ACC COMBINING LATIN SMALL LETTER INSULAR G: not included in any glyphset definition
 * U+1ACD COMBINING LATIN SMALL LETTER INSULAR R: not included in any glyphset definition
 * U+1ACE COMBINING LATIN SMALL LETTER INSULAR T: not included in any glyphset definition
 * U+1D00 LATIN LETTER SMALL CAPITAL A: not included in any glyphset definition
 * U+1D01 LATIN LETTER SMALL CAPITAL AE: not included in any glyphset definition
 * U+1D02 LATIN SMALL LETTER TURNED AE: not included in any glyphset definition
 * U+1D03 LATIN LETTER SMALL CAPITAL BARRED B: not included in any glyphset definition
 * U+1D04 LATIN LETTER SMALL CAPITAL C: not included in any glyphset definition
 * U+1D05 LATIN LETTER SMALL CAPITAL D: not included in any glyphset definition
 * U+1D06 LATIN LETTER SMALL CAPITAL ETH: not included in any glyphset definition
 * U+1D07 LATIN LETTER SMALL CAPITAL E: not included in any glyphset definition
 * U+1D08 LATIN SMALL LETTER TURNED OPEN E: not included in any glyphset definition
 * U+1D09 LATIN SMALL LETTER TURNED I: not included in any glyphset definition
 * U+1D0A LATIN LETTER SMALL CAPITAL J: not included in any glyphset definition
 * U+1D0B LATIN LETTER SMALL CAPITAL K: not included in any glyphset definition
 * U+1D0C LATIN LETTER SMALL CAPITAL L WITH STROKE: not included in any glyphset definition
 * U+1D0D LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition
 * U+1D0E LATIN LETTER SMALL CAPITAL REVERSED N: not included in any glyphset definition
 * U+1D0F LATIN LETTER SMALL CAPITAL O: not included in any glyphset definition
 * U+1D10 LATIN LETTER SMALL CAPITAL OPEN O: not included in any glyphset definition
 * U+1D11 LATIN SMALL LETTER SIDEWAYS O: not included in any glyphset definition
 * U+1D12 LATIN SMALL LETTER SIDEWAYS OPEN O: not included in any glyphset definition
 * U+1D13 LATIN SMALL LETTER SIDEWAYS O WITH STROKE: not included in any glyphset definition
 * U+1D14 LATIN SMALL LETTER TURNED OE: not included in any glyphset definition
 * U+1D15 LATIN LETTER SMALL CAPITAL OU: not included in any glyphset definition
 * U+1D16 LATIN SMALL LETTER TOP HALF O: not included in any glyphset definition
 * U+1D17 LATIN SMALL LETTER BOTTOM HALF O: not included in any glyphset definition
 * U+1D18 LATIN LETTER SMALL CAPITAL P: not included in any glyphset definition
 * U+1D19 LATIN LETTER SMALL CAPITAL REVERSED R: not included in any glyphset definition
 * U+1D1A LATIN LETTER SMALL CAPITAL TURNED R: not included in any glyphset definition
 * U+1D1B LATIN LETTER SMALL CAPITAL T: not included in any glyphset definition
 * U+1D1C LATIN LETTER SMALL CAPITAL U: not included in any glyphset definition
 * U+1D1D LATIN SMALL LETTER SIDEWAYS U: not included in any glyphset definition
 * U+1D1E LATIN SMALL LETTER SIDEWAYS DIAERESIZED U: not included in any glyphset definition
 * U+1D1F LATIN SMALL LETTER SIDEWAYS TURNED M: not included in any glyphset definition
 * U+1D20 LATIN LETTER SMALL CAPITAL V: not included in any glyphset definition
 * U+1D21 LATIN LETTER SMALL CAPITAL W: not included in any glyphset definition
 * U+1D22 LATIN LETTER SMALL CAPITAL Z: not included in any glyphset definition
 * U+1D23 LATIN LETTER SMALL CAPITAL EZH: not included in any glyphset definition
 * U+1D24 LATIN LETTER VOICED LARYNGEAL SPIRANT: not included in any glyphset definition
 * U+1D25 LATIN LETTER AIN: not included in any glyphset definition
 * U+1D26 GREEK LETTER SMALL CAPITAL GAMMA: not included in any glyphset definition
 * U+1D27 GREEK LETTER SMALL CAPITAL LAMDA: not included in any glyphset definition
 * U+1D28 GREEK LETTER SMALL CAPITAL PI: not included in any glyphset definition
 * U+1D29 GREEK LETTER SMALL CAPITAL RHO: not included in any glyphset definition
 * U+1D2A GREEK LETTER SMALL CAPITAL PSI: not included in any glyphset definition
 * U+1D2B CYRILLIC LETTER SMALL CAPITAL EL: not included in any glyphset definition
 * U+1D2C MODIFIER LETTER CAPITAL A: not included in any glyphset definition
 * U+1D2D MODIFIER LETTER CAPITAL AE: not included in any glyphset definition
 * U+1D2E MODIFIER LETTER CAPITAL B: not included in any glyphset definition
 * U+1D2F MODIFIER LETTER CAPITAL BARRED B: not included in any glyphset definition
 * U+1D30 MODIFIER LETTER CAPITAL D: not included in any glyphset definition
 * U+1D31 MODIFIER LETTER CAPITAL E: not included in any glyphset definition
 * U+1D32 MODIFIER LETTER CAPITAL REVERSED E: not included in any glyphset definition
 * U+1D33 MODIFIER LETTER CAPITAL G: not included in any glyphset definition
 * U+1D34 MODIFIER LETTER CAPITAL H: not included in any glyphset definition
 * U+1D35 MODIFIER LETTER CAPITAL I: not included in any glyphset definition
 * U+1D36 MODIFIER LETTER CAPITAL J: not included in any glyphset definition
 * U+1D37 MODIFIER LETTER CAPITAL K: not included in any glyphset definition
 * U+1D38 MODIFIER LETTER CAPITAL L: not included in any glyphset definition
 * U+1D39 MODIFIER LETTER CAPITAL M: not included in any glyphset definition
 * U+1D3A MODIFIER LETTER CAPITAL N: not included in any glyphset definition
 * U+1D3B MODIFIER LETTER CAPITAL REVERSED N: not included in any glyphset definition
 * U+1D3C MODIFIER LETTER CAPITAL O: not included in any glyphset definition
 * U+1D3D MODIFIER LETTER CAPITAL OU: not included in any glyphset definition
 * U+1D3E MODIFIER LETTER CAPITAL P: not included in any glyphset definition
 * U+1D3F MODIFIER LETTER CAPITAL R: not included in any glyphset definition
 * U+1D40 MODIFIER LETTER CAPITAL T: not included in any glyphset definition
 * U+1D41 MODIFIER LETTER CAPITAL U: not included in any glyphset definition
 * U+1D42 MODIFIER LETTER CAPITAL W: not included in any glyphset definition
 * U+1D43 MODIFIER LETTER SMALL A: not included in any glyphset definition
 * U+1D44 MODIFIER LETTER SMALL TURNED A: not included in any glyphset definition
 * U+1D45 MODIFIER LETTER SMALL ALPHA: not included in any glyphset definition
 * U+1D46 MODIFIER LETTER SMALL TURNED AE: not included in any glyphset definition
 * U+1D47 MODIFIER LETTER SMALL B: not included in any glyphset definition
 * U+1D48 MODIFIER LETTER SMALL D: not included in any glyphset definition
 * U+1D49 MODIFIER LETTER SMALL E: not included in any glyphset definition
 * U+1D4A MODIFIER LETTER SMALL SCHWA: not included in any glyphset definition
 * U+1D4B MODIFIER LETTER SMALL OPEN E: not included in any glyphset definition
 * U+1D4C MODIFIER LETTER SMALL TURNED OPEN E: not included in any glyphset definition
 * U+1D4D MODIFIER LETTER SMALL G: not included in any glyphset definition
 * U+1D4E MODIFIER LETTER SMALL TURNED I: not included in any glyphset definition
 * U+1D4F MODIFIER LETTER SMALL K: not included in any glyphset definition
 * U+1D50 MODIFIER LETTER SMALL M: not included in any glyphset definition
 * U+1D51 MODIFIER LETTER SMALL ENG: not included in any glyphset definition
 * U+1D52 MODIFIER LETTER SMALL O: not included in any glyphset definition
 * U+1D53 MODIFIER LETTER SMALL OPEN O: not included in any glyphset definition
 * U+1D54 MODIFIER LETTER SMALL TOP HALF O: not included in any glyphset definition
 * U+1D55 MODIFIER LETTER SMALL BOTTOM HALF O: not included in any glyphset definition
 * U+1D56 MODIFIER LETTER SMALL P: not included in any glyphset definition
 * U+1D57 MODIFIER LETTER SMALL T: not included in any glyphset definition
 * U+1D58 MODIFIER LETTER SMALL U: not included in any glyphset definition
 * U+1D59 MODIFIER LETTER SMALL SIDEWAYS U: not included in any glyphset definition
 * U+1D5A MODIFIER LETTER SMALL TURNED M: not included in any glyphset definition
 * U+1D5B MODIFIER LETTER SMALL V: not included in any glyphset definition
 * U+1D5C MODIFIER LETTER SMALL AIN: not included in any glyphset definition
 * U+1D5D MODIFIER LETTER SMALL BETA: not included in any glyphset definition
 * U+1D5E MODIFIER LETTER SMALL GREEK GAMMA: not included in any glyphset definition
 * U+1D5F MODIFIER LETTER SMALL DELTA: not included in any glyphset definition
 * U+1D60 MODIFIER LETTER SMALL GREEK PHI: not included in any glyphset definition
 * U+1D61 MODIFIER LETTER SMALL CHI: not included in any glyphset definition
 * U+1D62 LATIN SUBSCRIPT SMALL LETTER I: not included in any glyphset definition
 * U+1D63 LATIN SUBSCRIPT SMALL LETTER R: not included in any glyphset definition
 * U+1D64 LATIN SUBSCRIPT SMALL LETTER U: not included in any glyphset definition
 * U+1D65 LATIN SUBSCRIPT SMALL LETTER V: not included in any glyphset definition
 * U+1D66 GREEK SUBSCRIPT SMALL LETTER BETA: not included in any glyphset definition
 * U+1D67 GREEK SUBSCRIPT SMALL LETTER GAMMA: not included in any glyphset definition
 * U+1D68 GREEK SUBSCRIPT SMALL LETTER RHO: not included in any glyphset definition
 * U+1D69 GREEK SUBSCRIPT SMALL LETTER PHI: not included in any glyphset definition
 * U+1D6A GREEK SUBSCRIPT SMALL LETTER CHI: not included in any glyphset definition
 * U+1D6B LATIN SMALL LETTER UE: not included in any glyphset definition
 * U+1D6C LATIN SMALL LETTER B WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6D LATIN SMALL LETTER D WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6E LATIN SMALL LETTER F WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D6F LATIN SMALL LETTER M WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D70 LATIN SMALL LETTER N WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D71 LATIN SMALL LETTER P WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D72 LATIN SMALL LETTER R WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D73 LATIN SMALL LETTER R WITH FISHHOOK AND MIDDLE TILDE: not included in any glyphset definition
 * U+1D74 LATIN SMALL LETTER S WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D75 LATIN SMALL LETTER T WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D76 LATIN SMALL LETTER Z WITH MIDDLE TILDE: not included in any glyphset definition
 * U+1D77 LATIN SMALL LETTER TURNED G: not included in any glyphset definition
 * U+1D78 MODIFIER LETTER CYRILLIC EN: not included in any glyphset definition
 * U+1D79 LATIN SMALL LETTER INSULAR G: not included in any glyphset definition
 * U+1D7A LATIN SMALL LETTER TH WITH STRIKETHROUGH: not included in any glyphset definition
 * U+1D7B LATIN SMALL CAPITAL LETTER I WITH STROKE: not included in any glyphset definition
 * U+1D7C LATIN SMALL LETTER IOTA WITH STROKE: not included in any glyphset definition
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1D7E LATIN SMALL CAPITAL LETTER U WITH STROKE: not included in any glyphset definition
 * U+1D7F LATIN SMALL LETTER UPSILON WITH STROKE: not included in any glyphset definition
 * U+1D80 LATIN SMALL LETTER B WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D81 LATIN SMALL LETTER D WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D82 LATIN SMALL LETTER F WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D83 LATIN SMALL LETTER G WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D84 LATIN SMALL LETTER K WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D85 LATIN SMALL LETTER L WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D86 LATIN SMALL LETTER M WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D87 LATIN SMALL LETTER N WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D88 LATIN SMALL LETTER P WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D89 LATIN SMALL LETTER R WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8A LATIN SMALL LETTER S WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8B LATIN SMALL LETTER ESH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8C LATIN SMALL LETTER V WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8D LATIN SMALL LETTER X WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8E LATIN SMALL LETTER Z WITH PALATAL HOOK: not included in any glyphset definition
 * U+1D8F LATIN SMALL LETTER A WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D90 LATIN SMALL LETTER ALPHA WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D91 LATIN SMALL LETTER D WITH HOOK AND TAIL: not included in any glyphset definition
 * U+1D92 LATIN SMALL LETTER E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D93 LATIN SMALL LETTER OPEN E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D94 LATIN SMALL LETTER REVERSED OPEN E WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D95 LATIN SMALL LETTER SCHWA WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D96 LATIN SMALL LETTER I WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D97 LATIN SMALL LETTER OPEN O WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D98 LATIN SMALL LETTER ESH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D99 LATIN SMALL LETTER U WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D9A LATIN SMALL LETTER EZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1D9B MODIFIER LETTER SMALL TURNED ALPHA: not included in any glyphset definition
 * U+1D9C MODIFIER LETTER SMALL C: not included in any glyphset definition
 * U+1D9D MODIFIER LETTER SMALL C WITH CURL: not included in any glyphset definition
 * U+1D9E MODIFIER LETTER SMALL ETH: not included in any glyphset definition
 * U+1D9F MODIFIER LETTER SMALL REVERSED OPEN E: not included in any glyphset definition
 * U+1DA0 MODIFIER LETTER SMALL F: not included in any glyphset definition
 * U+1DA1 MODIFIER LETTER SMALL DOTLESS J WITH STROKE: not included in any glyphset definition
 * U+1DA2 MODIFIER LETTER SMALL SCRIPT G: not included in any glyphset definition
 * U+1DA3 MODIFIER LETTER SMALL TURNED H: not included in any glyphset definition
 * U+1DA4 MODIFIER LETTER SMALL I WITH STROKE: not included in any glyphset definition
 * U+1DA5 MODIFIER LETTER SMALL IOTA: not included in any glyphset definition
 * U+1DA6 MODIFIER LETTER SMALL CAPITAL I: not included in any glyphset definition
 * U+1DA7 MODIFIER LETTER SMALL CAPITAL I WITH STROKE: not included in any glyphset definition
 * U+1DA8 MODIFIER LETTER SMALL J WITH CROSSED-TAIL: not included in any glyphset definition
 * U+1DA9 MODIFIER LETTER SMALL L WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DAA MODIFIER LETTER SMALL L WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DAB MODIFIER LETTER SMALL CAPITAL L: not included in any glyphset definition
 * U+1DAC MODIFIER LETTER SMALL M WITH HOOK: not included in any glyphset definition
 * U+1DAD MODIFIER LETTER SMALL TURNED M WITH LONG LEG: not included in any glyphset definition
 * U+1DAE MODIFIER LETTER SMALL N WITH LEFT HOOK: not included in any glyphset definition
 * U+1DAF MODIFIER LETTER SMALL N WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DB0 MODIFIER LETTER SMALL CAPITAL N: not included in any glyphset definition
 * U+1DB1 MODIFIER LETTER SMALL BARRED O: not included in any glyphset definition
 * U+1DB2 MODIFIER LETTER SMALL PHI: not included in any glyphset definition
 * U+1DB3 MODIFIER LETTER SMALL S WITH HOOK: not included in any glyphset definition
 * U+1DB4 MODIFIER LETTER SMALL ESH: not included in any glyphset definition
 * U+1DB5 MODIFIER LETTER SMALL T WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DB6 MODIFIER LETTER SMALL U BAR: not included in any glyphset definition
 * U+1DB7 MODIFIER LETTER SMALL UPSILON: not included in any glyphset definition
 * U+1DB8 MODIFIER LETTER SMALL CAPITAL U: not included in any glyphset definition
 * U+1DB9 MODIFIER LETTER SMALL V WITH HOOK: not included in any glyphset definition
 * U+1DBA MODIFIER LETTER SMALL TURNED V: not included in any glyphset definition
 * U+1DBB MODIFIER LETTER SMALL Z: not included in any glyphset definition
 * U+1DBC MODIFIER LETTER SMALL Z WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DBD MODIFIER LETTER SMALL Z WITH CURL: not included in any glyphset definition
 * U+1DBE MODIFIER LETTER SMALL EZH: not included in any glyphset definition
 * U+1DBF MODIFIER LETTER SMALL THETA: not included in any glyphset definition
 * U+1DC0 COMBINING DOTTED GRAVE ACCENT: not included in any glyphset definition
 * U+1DC1 COMBINING DOTTED ACUTE ACCENT: not included in any glyphset definition
 * U+1DC2 COMBINING SNAKE BELOW: not included in any glyphset definition
 * U+1DC3 COMBINING SUSPENSION MARK: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DC8 COMBINING GRAVE-ACUTE-GRAVE: not included in any glyphset definition
 * U+1DC9 COMBINING ACUTE-GRAVE-ACUTE: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+1DCB COMBINING BREVE-MACRON: not included in any glyphset definition
 * U+1DCC COMBINING MACRON-BREVE: not included in any glyphset definition
 * U+1DCD COMBINING DOUBLE CIRCUMFLEX ABOVE: try adding coptic
 * U+1DCE COMBINING OGONEK ABOVE: not included in any glyphset definition
 * U+1DCF COMBINING ZIGZAG BELOW: not included in any glyphset definition
 * U+1DD0 COMBINING IS BELOW: not included in any glyphset definition
 * U+1DD1 COMBINING UR ABOVE: not included in any glyphset definition
 * U+1DD2 COMBINING US ABOVE: not included in any glyphset definition
 * U+1DD3 COMBINING LATIN SMALL LETTER FLATTENED OPEN A ABOVE: not included in any glyphset definition
 * U+1DD4 COMBINING LATIN SMALL LETTER AE: not included in any glyphset definition
 * U+1DD5 COMBINING LATIN SMALL LETTER AO: not included in any glyphset definition
 * U+1DD6 COMBINING LATIN SMALL LETTER AV: not included in any glyphset definition
 * U+1DD7 COMBINING LATIN SMALL LETTER C CEDILLA: not included in any glyphset definition
 * U+1DD8 COMBINING LATIN SMALL LETTER INSULAR D: not included in any glyphset definition
 * U+1DD9 COMBINING LATIN SMALL LETTER ETH: not included in any glyphset definition
 * U+1DDA COMBINING LATIN SMALL LETTER G: not included in any glyphset definition
 * U+1DDB COMBINING LATIN LETTER SMALL CAPITAL G: not included in any glyphset definition
 * U+1DDC COMBINING LATIN SMALL LETTER K: not included in any glyphset definition
 * U+1DDD COMBINING LATIN SMALL LETTER L: not included in any glyphset definition
 * U+1DDE COMBINING LATIN LETTER SMALL CAPITAL L: not included in any glyphset definition
 * U+1DDF COMBINING LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition
 * U+1DE0 COMBINING LATIN SMALL LETTER N: not included in any glyphset definition
 * U+1DE1 COMBINING LATIN LETTER SMALL CAPITAL N: not included in any glyphset definition
 * U+1DE2 COMBINING LATIN LETTER SMALL CAPITAL R: not included in any glyphset definition
 * U+1DE3 COMBINING LATIN SMALL LETTER R ROTUNDA: not included in any glyphset definition
 * U+1DE4 COMBINING LATIN SMALL LETTER S: not included in any glyphset definition
 * U+1DE5 COMBINING LATIN SMALL LETTER LONG S: not included in any glyphset definition
 * U+1DE6 COMBINING LATIN SMALL LETTER Z: not included in any glyphset definition
 * U+1DE7 COMBINING LATIN SMALL LETTER ALPHA: not included in any glyphset definition
 * U+1DE8 COMBINING LATIN SMALL LETTER B: not included in any glyphset definition
 * U+1DE9 COMBINING LATIN SMALL LETTER BETA: not included in any glyphset definition
 * U+1DEA COMBINING LATIN SMALL LETTER SCHWA: not included in any glyphset definition
 * U+1DEB COMBINING LATIN SMALL LETTER F: not included in any glyphset definition
 * U+1DEC COMBINING LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition
 * U+1DED COMBINING LATIN SMALL LETTER O WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition
 * U+1DEE COMBINING LATIN SMALL LETTER P: not included in any glyphset definition
 * U+1DEF COMBINING LATIN SMALL LETTER ESH: not included in any glyphset definition
 * U+1DF0 COMBINING LATIN SMALL LETTER U WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition
 * U+1DF1 COMBINING LATIN SMALL LETTER W: not included in any glyphset definition
 * U+1DF2 COMBINING LATIN SMALL LETTER A WITH DIAERESIS: not included in any glyphset definition
 * U+1DF3 COMBINING LATIN SMALL LETTER O WITH DIAERESIS: not included in any glyphset definition
 * U+1DF4 COMBINING LATIN SMALL LETTER U WITH DIAERESIS: not included in any glyphset definition
 * U+1DF5 COMBINING UP TACK ABOVE: not included in any glyphset definition
 * U+1DF6 COMBINING KAVYKA ABOVE RIGHT: not included in any glyphset definition
 * U+1DF7 COMBINING KAVYKA ABOVE LEFT: not included in any glyphset definition
 * U+1DF8 COMBINING DOT ABOVE LEFT: not included in any glyphset definition
 * U+1DF9 COMBINING WIDE INVERTED BRIDGE BELOW: not included in any glyphset definition
 * U+1DFB COMBINING DELETION MARK: try adding newa
 * U+1DFC COMBINING DOUBLE INVERTED BREVE BELOW: not included in any glyphset definition
 * U+1DFD COMBINING ALMOST EQUAL TO BELOW: not included in any glyphset definition
 * U+1DFE COMBINING LEFT ARROWHEAD ABOVE: not included in any glyphset definition
 * U+1DFF COMBINING RIGHT ARROWHEAD AND DOWN ARROWHEAD BELOW: not included in any glyphset definition
 * U+2000 EN QUAD: not included in any glyphset definition
 * U+2001 EM QUAD: not included in any glyphset definition
 * U+2003 EM SPACE: try adding nushu
 * U+2004 THREE-PER-EM SPACE: not included in any glyphset definition
 * U+2005 FOUR-PER-EM SPACE: not included in any glyphset definition
 * U+2006 SIX-PER-EM SPACE: not included in any glyphset definition
 * U+2007 FIGURE SPACE: not included in any glyphset definition
 * U+2008 PUNCTUATION SPACE: not included in any glyphset definition
 * U+200A HAIR SPACE: not included in any glyphset definition
 * U+200E LEFT-TO-RIGHT MARK: try adding one of: phags-pa, thaana, syriac, nko
 * U+200F RIGHT-TO-LEFT MARK: try adding one of: phags-pa, thaana, syriac, nko
 * U+2010 HYPHEN: try adding one of: coptic, cham, syloti-nagri, lisu, kayah-li, sundanese, kharoshthi, kaithi, yi, sora-sompeng
 * U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi
 * U+2012 FIGURE DASH: not included in any glyphset definition
 * U+2015 HORIZONTAL BAR: try adding adlam
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2017 DOUBLE LOW LINE: not included in any glyphset definition
 * U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam
 * U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2023 TRIANGULAR BULLET: not included in any glyphset definition
 * U+2024 ONE DOT LEADER: try adding armenian
 * U+2025 TWO DOT LEADER: try adding phags-pa
 * U+2027 HYPHENATION POINT: not included in any glyphset definition
 * U+2028 LINE SEPARATOR: not included in any glyphset definition
 * U+2029 PARAGRAPH SEPARATOR: not included in any glyphset definition
 * U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition
 * U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition
 * U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition
 * U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition
 * U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh
 * U+202F NARROW NO-BREAK SPACE: try adding one of: mongolian, yi
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition
 * U+2034 TRIPLE PRIME: try adding math
 * U+2035 REVERSED PRIME: try adding math
 * U+2036 REVERSED DOUBLE PRIME: try adding math
 * U+2037 REVERSED TRIPLE PRIME: try adding math
 * U+2038 CARET: not included in any glyphset definition
 * U+203B REFERENCE MARK: not included in any glyphset definition
 * U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition
 * U+203D INTERROBANG: not included in any glyphset definition
 * U+203E OVERLINE: not included in any glyphset definition
 * U+203F UNDERTIE: not included in any glyphset definition
 * U+2040 CHARACTER TIE: not included in any glyphset definition
 * U+2041 CARET INSERTION POINT: not included in any glyphset definition
 * U+2042 ASTERISM: not included in any glyphset definition
 * U+2043 HYPHEN BULLET: not included in any glyphset definition
 * U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition
 * U+2047 DOUBLE QUESTION MARK: not included in any glyphset definition
 * U+2048 QUESTION EXCLAMATION MARK: try adding mongolian
 * U+2049 EXCLAMATION QUESTION MARK: try adding mongolian
 * U+204A TIRONIAN SIGN ET: not included in any glyphset definition
 * U+204B REVERSED PILCROW SIGN: not included in any glyphset definition
 * U+204C BLACK LEFTWARDS BULLET: not included in any glyphset definition
 * U+204D BLACK RIGHTWARDS BULLET: not included in any glyphset definition
 * U+204E LOW ASTERISK: not included in any glyphset definition
 * U+204F REVERSED SEMICOLON: try adding adlam
 * U+2050 CLOSE UP: not included in any glyphset definition
 * U+2051 TWO ASTERISKS ALIGNED VERTICALLY: not included in any glyphset definition
 * U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition
 * U+2053 SWUNG DASH: try adding coptic
 * U+2054 INVERTED UNDERTIE: not included in any glyphset definition
 * U+2055 FLOWER PUNCTUATION MARK: try adding syloti-nagri
 * U+2056 THREE DOT PUNCTUATION: try adding coptic
 * U+2057 QUADRUPLE PRIME: try adding math
 * U+2058 FOUR DOT PUNCTUATION: try adding coptic
 * U+2059 FIVE DOT PUNCTUATION: try adding coptic
 * U+205A TWO DOT PUNCTUATION: try adding one of: old-hungarian, old-turkic
 * U+205B FOUR DOT MARK: not included in any glyphset definition
 * U+205C DOTTED CROSS: not included in any glyphset definition
 * U+205D TRICOLON: try adding one of: meroitic, old-hungarian
 * U+205E VERTICAL FOUR DOTS: try adding old-hungarian
 * U+205F MEDIUM MATHEMATICAL SPACE: not included in any glyphset definition
 * U+2060 WORD JOINER: not included in any glyphset definition
 * U+2061 FUNCTION APPLICATION: not included in any glyphset definition
 * U+2062 INVISIBLE TIMES: not included in any glyphset definition
 * U+2063 INVISIBLE SEPARATOR: not included in any glyphset definition
 * U+2064 INVISIBLE PLUS: not included in any glyphset definition
 * U+2066 LEFT-TO-RIGHT ISOLATE: not included in any glyphset definition
 * U+2067 RIGHT-TO-LEFT ISOLATE: not included in any glyphset definition
 * U+2068 FIRST STRONG ISOLATE: not included in any glyphset definition
 * U+2069 POP DIRECTIONAL ISOLATE: not included in any glyphset definition
 * U+206A INHIBIT SYMMETRIC SWAPPING: not included in any glyphset definition
 * U+206B ACTIVATE SYMMETRIC SWAPPING: not included in any glyphset definition
 * U+206C INHIBIT ARABIC FORM SHAPING: not included in any glyphset definition
 * U+206D ACTIVATE ARABIC FORM SHAPING: not included in any glyphset definition
 * U+206E NATIONAL DIGIT SHAPES: not included in any glyphset definition
 * U+206F NOMINAL DIGIT SHAPES: not included in any glyphset definition
 * U+2070 SUPERSCRIPT ZERO: not included in any glyphset definition
 * U+2071 SUPERSCRIPT LATIN SMALL LETTER I: not included in any glyphset definition
 * U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition
 * U+2076 SUPERSCRIPT SIX: not included in any glyphset definition
 * U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition
 * U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition
 * U+2079 SUPERSCRIPT NINE: not included in any glyphset definition
 * U+207A SUPERSCRIPT PLUS SIGN: not included in any glyphset definition
 * U+207B SUPERSCRIPT MINUS: not included in any glyphset definition
 * U+207C SUPERSCRIPT EQUALS SIGN: not included in any glyphset definition
 * U+207D SUPERSCRIPT LEFT PARENTHESIS: not included in any glyphset definition
 * U+207E SUPERSCRIPT RIGHT PARENTHESIS: not included in any glyphset definition
 * U+207F SUPERSCRIPT LATIN SMALL LETTER N: not included in any glyphset definition
 * U+2080 SUBSCRIPT ZERO: not included in any glyphset definition
 * U+2081 SUBSCRIPT ONE: not included in any glyphset definition
 * U+2082 SUBSCRIPT TWO: not included in any glyphset definition
 * U+2083 SUBSCRIPT THREE: not included in any glyphset definition
 * U+2084 SUBSCRIPT FOUR: not included in any glyphset definition
 * U+2085 SUBSCRIPT FIVE: not included in any glyphset definition
 * U+2086 SUBSCRIPT SIX: not included in any glyphset definition
 * U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition
 * U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition
 * U+2089 SUBSCRIPT NINE: not included in any glyphset definition
 * U+208A SUBSCRIPT PLUS SIGN: not included in any glyphset definition
 * U+208B SUBSCRIPT MINUS: not included in any glyphset definition
 * U+208C SUBSCRIPT EQUALS SIGN: not included in any glyphset definition
 * U+208D SUBSCRIPT LEFT PARENTHESIS: not included in any glyphset definition
 * U+208E SUBSCRIPT RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2090 LATIN SUBSCRIPT SMALL LETTER A: not included in any glyphset definition
 * U+2091 LATIN SUBSCRIPT SMALL LETTER E: not included in any glyphset definition
 * U+2092 LATIN SUBSCRIPT SMALL LETTER O: not included in any glyphset definition
 * U+2093 LATIN SUBSCRIPT SMALL LETTER X: not included in any glyphset definition
 * U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: not included in any glyphset definition
 * U+2095 LATIN SUBSCRIPT SMALL LETTER H: not included in any glyphset definition
 * U+2096 LATIN SUBSCRIPT SMALL LETTER K: not included in any glyphset definition
 * U+2097 LATIN SUBSCRIPT SMALL LETTER L: not included in any glyphset definition
 * U+2098 LATIN SUBSCRIPT SMALL LETTER M: not included in any glyphset definition
 * U+2099 LATIN SUBSCRIPT SMALL LETTER N: not included in any glyphset definition
 * U+209A LATIN SUBSCRIPT SMALL LETTER P: not included in any glyphset definition
 * U+209B LATIN SUBSCRIPT SMALL LETTER S: not included in any glyphset definition
 * U+209C LATIN SUBSCRIPT SMALL LETTER T: not included in any glyphset definition
 * U+20F0 COMBINING ASTERISK ABOVE: try adding grantha
 * U+2100 ACCOUNT OF: not included in any glyphset definition
 * U+2101 ADDRESSED TO THE SUBJECT: not included in any glyphset definition
 * U+2102 DOUBLE-STRUCK CAPITAL C: try adding math
 * U+2103 DEGREE CELSIUS: not included in any glyphset definition
 * U+2104 CENTRE LINE SYMBOL: not included in any glyphset definition
 * U+2105 CARE OF: not included in any glyphset definition
 * U+2106 CADA UNA: not included in any glyphset definition
 * U+2107 EULER CONSTANT: not included in any glyphset definition
 * U+2108 SCRUPLE: not included in any glyphset definition
 * U+2109 DEGREE FAHRENHEIT: not included in any glyphset definition
 * U+210A SCRIPT SMALL G: try adding math
 * U+210B SCRIPT CAPITAL H: try adding math
 * U+210C BLACK-LETTER CAPITAL H: try adding math
 * U+210D DOUBLE-STRUCK CAPITAL H: try adding math
 * U+210E PLANCK CONSTANT: try adding math
 * U+210F PLANCK CONSTANT OVER TWO PI: not included in any glyphset definition
 * U+2110 SCRIPT CAPITAL I: try adding math
 * U+2111 BLACK-LETTER CAPITAL I: try adding math
 * U+2112 SCRIPT CAPITAL L: try adding math
 * U+2114 L B BAR SYMBOL: not included in any glyphset definition
 * U+2115 DOUBLE-STRUCK CAPITAL N: try adding math
 * U+2117 SOUND RECORDING COPYRIGHT: not included in any glyphset definition
 * U+2118 SCRIPT CAPITAL P: not included in any glyphset definition
 * U+2119 DOUBLE-STRUCK CAPITAL P: try adding math
 * U+211A DOUBLE-STRUCK CAPITAL Q: try adding math
 * U+211B SCRIPT CAPITAL R: try adding math
 * U+211C BLACK-LETTER CAPITAL R: try adding math
 * U+211D DOUBLE-STRUCK CAPITAL R: try adding math
 * U+211E PRESCRIPTION TAKE: not included in any glyphset definition
 * U+211F RESPONSE: not included in any glyphset definition
 * U+2120 SERVICE MARK: not included in any glyphset definition
 * U+2121 TELEPHONE SIGN: not included in any glyphset definition
 * U+2123 VERSICLE: not included in any glyphset definition
 * U+2124 DOUBLE-STRUCK CAPITAL Z: try adding math
 * U+2125 OUNCE SIGN: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+2127 INVERTED OHM SIGN: not included in any glyphset definition
 * U+2128 BLACK-LETTER CAPITAL Z: try adding math
 * U+2129 TURNED GREEK SMALL LETTER IOTA: not included in any glyphset definition
 * U+212A KELVIN SIGN: not included in any glyphset definition
 * U+212B ANGSTROM SIGN: not included in any glyphset definition
 * U+212C SCRIPT CAPITAL B: try adding math
 * U+212D BLACK-LETTER CAPITAL C: try adding math
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+212F SCRIPT SMALL E: try adding math
 * U+2130 SCRIPT CAPITAL E: try adding math
 * U+2131 SCRIPT CAPITAL F: try adding math
 * U+2132 TURNED CAPITAL F: not included in any glyphset definition
 * U+2133 SCRIPT CAPITAL M: try adding math
 * U+2134 SCRIPT SMALL O: try adding math
 * U+2135 ALEF SYMBOL: try adding math
 * U+2136 BET SYMBOL: try adding math
 * U+2137 GIMEL SYMBOL: try adding math
 * U+2138 DALET SYMBOL: try adding math
 * U+2139 INFORMATION SOURCE: not included in any glyphset definition
 * U+213A ROTATED CAPITAL Q: not included in any glyphset definition
 * U+213B FACSIMILE SIGN: not included in any glyphset definition
 * U+213C DOUBLE-STRUCK SMALL PI: try adding math
 * U+213D DOUBLE-STRUCK SMALL GAMMA: try adding math
 * U+213E DOUBLE-STRUCK CAPITAL GAMMA: try adding math
 * U+213F DOUBLE-STRUCK CAPITAL PI: try adding math
 * U+2140 DOUBLE-STRUCK N-ARY SUMMATION: try adding math
 * U+2141 TURNED SANS-SERIF CAPITAL G: not included in any glyphset definition
 * U+2142 TURNED SANS-SERIF CAPITAL L: not included in any glyphset definition
 * U+2143 REVERSED SANS-SERIF CAPITAL L: not included in any glyphset definition
 * U+2144 TURNED SANS-SERIF CAPITAL Y: not included in any glyphset definition
 * U+2145 DOUBLE-STRUCK ITALIC CAPITAL D: try adding math
 * U+2146 DOUBLE-STRUCK ITALIC SMALL D: try adding math
 * U+2147 DOUBLE-STRUCK ITALIC SMALL E: try adding math
 * U+2148 DOUBLE-STRUCK ITALIC SMALL I: try adding math
 * U+2149 DOUBLE-STRUCK ITALIC SMALL J: try adding math
 * U+214A PROPERTY LINE: not included in any glyphset definition
 * U+214B TURNED AMPERSAND: not included in any glyphset definition
 * U+214C PER SIGN: not included in any glyphset definition
 * U+214D AKTIESELSKAB: not included in any glyphset definition
 * U+214E TURNED SMALL F: not included in any glyphset definition
 * U+214F SYMBOL FOR SAMARITAN SOURCE: not included in any glyphset definition
 * U+2150 VULGAR FRACTION ONE SEVENTH: not included in any glyphset definition
 * U+2151 VULGAR FRACTION ONE NINTH: not included in any glyphset definition
 * U+2152 VULGAR FRACTION ONE TENTH: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2155 VULGAR FRACTION ONE FIFTH: not included in any glyphset definition
 * U+2156 VULGAR FRACTION TWO FIFTHS: not included in any glyphset definition
 * U+2157 VULGAR FRACTION THREE FIFTHS: not included in any glyphset definition
 * U+2158 VULGAR FRACTION FOUR FIFTHS: not included in any glyphset definition
 * U+2159 VULGAR FRACTION ONE SIXTH: not included in any glyphset definition
 * U+215A VULGAR FRACTION FIVE SIXTHS: not included in any glyphset definition
 * U+215B VULGAR FRACTION ONE EIGHTH: not included in any glyphset definition
 * U+215C VULGAR FRACTION THREE EIGHTHS: not included in any glyphset definition
 * U+215D VULGAR FRACTION FIVE EIGHTHS: not included in any glyphset definition
 * U+215E VULGAR FRACTION SEVEN EIGHTHS: not included in any glyphset definition
 * U+215F FRACTION NUMERATOR ONE: not included in any glyphset definition
 * U+2184 LATIN SMALL LETTER REVERSED C: not included in any glyphset definition
 * U+2189 VULGAR FRACTION ZERO THIRDS: not included in any glyphset definition
 * U+2E00 RIGHT ANGLE SUBSTITUTION MARKER: not included in any glyphset definition
 * U+2E01 RIGHT ANGLE DOTTED SUBSTITUTION MARKER: not included in any glyphset definition
 * U+2E02 LEFT SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E03 RIGHT SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E04 LEFT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E05 RIGHT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition
 * U+2E06 RAISED INTERPOLATION MARKER: not included in any glyphset definition
 * U+2E07 RAISED DOTTED INTERPOLATION MARKER: not included in any glyphset definition
 * U+2E08 DOTTED TRANSPOSITION MARKER: not included in any glyphset definition
 * U+2E09 LEFT TRANSPOSITION BRACKET: not included in any glyphset definition
 * U+2E0A RIGHT TRANSPOSITION BRACKET: not included in any glyphset definition
 * U+2E0B RAISED SQUARE: not included in any glyphset definition
 * U+2E0C LEFT RAISED OMISSION BRACKET: not included in any glyphset definition
 * U+2E0D RIGHT RAISED OMISSION BRACKET: not included in any glyphset definition
 * U+2E0E EDITORIAL CORONIS: not included in any glyphset definition
 * U+2E0F PARAGRAPHOS: not included in any glyphset definition
 * U+2E10 FORKED PARAGRAPHOS: not included in any glyphset definition
 * U+2E11 REVERSED FORKED PARAGRAPHOS: not included in any glyphset definition
 * U+2E12 HYPODIASTOLE: not included in any glyphset definition
 * U+2E13 DOTTED OBELOS: not included in any glyphset definition
 * U+2E14 DOWNWARDS ANCORA: not included in any glyphset definition
 * U+2E15 UPWARDS ANCORA: not included in any glyphset definition
 * U+2E16 DOTTED RIGHT-POINTING ANGLE: not included in any glyphset definition
 * U+2E17 DOUBLE OBLIQUE HYPHEN: try adding coptic
 * U+2E18 INVERTED INTERROBANG: not included in any glyphset definition
 * U+2E19 PALM BRANCH: not included in any glyphset definition
 * U+2E1A HYPHEN WITH DIAERESIS: not included in any glyphset definition
 * U+2E1B TILDE WITH RING ABOVE: not included in any glyphset definition
 * U+2E1C LEFT LOW PARAPHRASE BRACKET: try adding nko
 * U+2E1D RIGHT LOW PARAPHRASE BRACKET: try adding nko
 * U+2E1E TILDE WITH DOT ABOVE: not included in any glyphset definition
 * U+2E1F TILDE WITH DOT BELOW: not included in any glyphset definition
 * U+2E20 LEFT VERTICAL BAR WITH QUILL: not included in any glyphset definition
 * U+2E21 RIGHT VERTICAL BAR WITH QUILL: not included in any glyphset definition
 * U+2E22 TOP LEFT HALF BRACKET: not included in any glyphset definition
 * U+2E23 TOP RIGHT HALF BRACKET: not included in any glyphset definition
 * U+2E24 BOTTOM LEFT HALF BRACKET: not included in any glyphset definition
 * U+2E25 BOTTOM RIGHT HALF BRACKET: not included in any glyphset definition
 * U+2E26 LEFT SIDEWAYS U BRACKET: not included in any glyphset definition
 * U+2E27 RIGHT SIDEWAYS U BRACKET: not included in any glyphset definition
 * U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam
 * U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam
 * U+2E2A TWO DOTS OVER ONE DOT PUNCTUATION: not included in any glyphset definition
 * U+2E2B ONE DOT OVER TWO DOTS PUNCTUATION: not included in any glyphset definition
 * U+2E2C SQUARED FOUR DOT PUNCTUATION: not included in any glyphset definition
 * U+2E2D FIVE DOT MARK: not included in any glyphset definition
 * U+2E2E REVERSED QUESTION MARK: not included in any glyphset definition
 * U+2E2F VERTICAL TILDE: not included in any glyphset definition
 * U+2E30 RING POINT: try adding avestan
 * U+2E31 WORD SEPARATOR MIDDLE DOT: try adding one of: avestan, old-hungarian, samaritan
 * U+2E32 TURNED COMMA: not included in any glyphset definition
 * U+2E33 RAISED DOT: try adding coptic
 * U+2E34 RAISED COMMA: try adding coptic
 * U+2E35 TURNED SEMICOLON: not included in any glyphset definition
 * U+2E36 DAGGER WITH LEFT GUARD: not included in any glyphset definition
 * U+2E37 DAGGER WITH RIGHT GUARD: not included in any glyphset definition
 * U+2E38 TURNED DAGGER: not included in any glyphset definition
 * U+2E39 TOP HALF SECTION SIGN: not included in any glyphset definition
 * U+2E3A TWO-EM DASH: not included in any glyphset definition
 * U+2E3B THREE-EM DASH: not included in any glyphset definition
 * U+2E3C STENOGRAPHIC FULL STOP: not included in any glyphset definition
 * U+2E3D VERTICAL SIX DOTS: not included in any glyphset definition
 * U+2E3E WIGGLY VERTICAL LINE: not included in any glyphset definition
 * U+2E3F CAPITULUM: not included in any glyphset definition
 * U+2E40 DOUBLE HYPHEN: not included in any glyphset definition
 * U+2E41 REVERSED COMMA: try adding adlam
 * U+2E42 DOUBLE LOW-REVERSED-9 QUOTATION MARK: not included in any glyphset definition
 * U+2E43 DASH WITH LEFT UPTURN: not included in any glyphset definition
 * U+2E44 DOUBLE SUSPENSION MARK: not included in any glyphset definition
 * U+2E45 INVERTED LOW KAVYKA: not included in any glyphset definition
 * U+2E46 INVERTED LOW KAVYKA WITH KAVYKA ABOVE: not included in any glyphset definition
 * U+2E47 LOW KAVYKA: not included in any glyphset definition
 * U+2E48 LOW KAVYKA WITH DOT: not included in any glyphset definition
 * U+2E49 DOUBLE STACKED COMMA: not included in any glyphset definition
 * U+2E4A DOTTED SOLIDUS: not included in any glyphset definition
 * U+2E4B TRIPLE DAGGER: not included in any glyphset definition
 * U+2E4C MEDIEVAL COMMA: not included in any glyphset definition
 * U+2E4D PARAGRAPHUS MARK: not included in any glyphset definition
 * U+2E4E PUNCTUS ELEVATUS MARK: not included in any glyphset definition
 * U+2E4F CORNISH VERSE DIVIDER: not included in any glyphset definition
 * U+2E50 CROSS PATTY WITH RIGHT CROSSBAR: not included in any glyphset definition
 * U+2E51 CROSS PATTY WITH LEFT CROSSBAR: not included in any glyphset definition
 * U+2E52 TIRONIAN SIGN CAPITAL ET: not included in any glyphset definition
 * U+2E53 MEDIEVAL EXCLAMATION MARK: not included in any glyphset definition
 * U+2E54 MEDIEVAL QUESTION MARK: not included in any glyphset definition
 * U+2E55 LEFT SQUARE BRACKET WITH STROKE: not included in any glyphset definition
 * U+2E56 RIGHT SQUARE BRACKET WITH STROKE: not included in any glyphset definition
 * U+2E57 LEFT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition
 * U+2E58 RIGHT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition
 * U+2E59 TOP HALF LEFT PARENTHESIS: not included in any glyphset definition
 * U+2E5A TOP HALF RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2E5B BOTTOM HALF LEFT PARENTHESIS: not included in any glyphset definition
 * U+2E5C BOTTOM HALF RIGHT PARENTHESIS: not included in any glyphset definition
 * U+2E5D OBLIQUE HYPHEN: not included in any glyphset definition
 * U+A700 MODIFIER LETTER CHINESE TONE YIN PING: not included in any glyphset definition
 * U+A701 MODIFIER LETTER CHINESE TONE YANG PING: not included in any glyphset definition
 * U+A702 MODIFIER LETTER CHINESE TONE YIN SHANG: not included in any glyphset definition
 * U+A703 MODIFIER LETTER CHINESE TONE YANG SHANG: not included in any glyphset definition
 * U+A704 MODIFIER LETTER CHINESE TONE YIN QU: not included in any glyphset definition
 * U+A705 MODIFIER LETTER CHINESE TONE YANG QU: not included in any glyphset definition
 * U+A706 MODIFIER LETTER CHINESE TONE YIN RU: not included in any glyphset definition
 * U+A707 MODIFIER LETTER CHINESE TONE YANG RU: not included in any glyphset definition
 * U+A708 MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR: not included in any glyphset definition
 * U+A709 MODIFIER LETTER HIGH DOTTED TONE BAR: not included in any glyphset definition
 * U+A70A MODIFIER LETTER MID DOTTED TONE BAR: not included in any glyphset definition
 * U+A70B MODIFIER LETTER LOW DOTTED TONE BAR: not included in any glyphset definition
 * U+A70C MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR: not included in any glyphset definition
 * U+A70D MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A70E MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A70F MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A710 MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A711 MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A712 MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A713 MODIFIER LETTER HIGH LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A714 MODIFIER LETTER MID LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A715 MODIFIER LETTER LOW LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A716 MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR: not included in any glyphset definition
 * U+A717 MODIFIER LETTER DOT VERTICAL BAR: not included in any glyphset definition
 * U+A718 MODIFIER LETTER DOT SLASH: not included in any glyphset definition
 * U+A719 MODIFIER LETTER DOT HORIZONTAL BAR: not included in any glyphset definition
 * U+A71A MODIFIER LETTER LOWER RIGHT CORNER ANGLE: not included in any glyphset definition
 * U+A71B MODIFIER LETTER RAISED UP ARROW: not included in any glyphset definition
 * U+A71C MODIFIER LETTER RAISED DOWN ARROW: not included in any glyphset definition
 * U+A71D MODIFIER LETTER RAISED EXCLAMATION MARK: not included in any glyphset definition
 * U+A71E MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK: not included in any glyphset definition
 * U+A71F MODIFIER LETTER LOW INVERTED EXCLAMATION MARK: not included in any glyphset definition
 * U+A92E KAYAH LI SIGN CWI: try adding kayah-li
 * U+AB30 LATIN SMALL LETTER BARRED ALPHA: not included in any glyphset definition
 * U+AB31 LATIN SMALL LETTER A REVERSED-SCHWA: not included in any glyphset definition
 * U+AB32 LATIN SMALL LETTER BLACKLETTER E: not included in any glyphset definition
 * U+AB33 LATIN SMALL LETTER BARRED E: not included in any glyphset definition
 * U+AB34 LATIN SMALL LETTER E WITH FLOURISH: not included in any glyphset definition
 * U+AB35 LATIN SMALL LETTER LENIS F: not included in any glyphset definition
 * U+AB36 LATIN SMALL LETTER SCRIPT G WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB37 LATIN SMALL LETTER L WITH INVERTED LAZY S: not included in any glyphset definition
 * U+AB38 LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition
 * U+AB39 LATIN SMALL LETTER L WITH MIDDLE RING: not included in any glyphset definition
 * U+AB3A LATIN SMALL LETTER M WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3B LATIN SMALL LETTER N WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3C LATIN SMALL LETTER ENG WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB3D LATIN SMALL LETTER BLACKLETTER O: not included in any glyphset definition
 * U+AB3E LATIN SMALL LETTER BLACKLETTER O WITH STROKE: not included in any glyphset definition
 * U+AB3F LATIN SMALL LETTER OPEN O WITH STROKE: not included in any glyphset definition
 * U+AB40 LATIN SMALL LETTER INVERTED OE: not included in any glyphset definition
 * U+AB41 LATIN SMALL LETTER TURNED OE WITH STROKE: not included in any glyphset definition
 * U+AB42 LATIN SMALL LETTER TURNED OE WITH HORIZONTAL STROKE: not included in any glyphset definition
 * U+AB43 LATIN SMALL LETTER TURNED O OPEN-O: not included in any glyphset definition
 * U+AB44 LATIN SMALL LETTER TURNED O OPEN-O WITH STROKE: not included in any glyphset definition
 * U+AB45 LATIN SMALL LETTER STIRRUP R: not included in any glyphset definition
 * U+AB46 LATIN LETTER SMALL CAPITAL R WITH RIGHT LEG: not included in any glyphset definition
 * U+AB47 LATIN SMALL LETTER R WITHOUT HANDLE: not included in any glyphset definition
 * U+AB48 LATIN SMALL LETTER DOUBLE R: not included in any glyphset definition
 * U+AB49 LATIN SMALL LETTER R WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB4A LATIN SMALL LETTER DOUBLE R WITH CROSSED-TAIL: not included in any glyphset definition
 * U+AB4B LATIN SMALL LETTER SCRIPT R: not included in any glyphset definition
 * U+AB4C LATIN SMALL LETTER SCRIPT R WITH RING: not included in any glyphset definition
 * U+AB4D LATIN SMALL LETTER BASELINE ESH: not included in any glyphset definition
 * U+AB4E LATIN SMALL LETTER U WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB4F LATIN SMALL LETTER U BAR WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB50 LATIN SMALL LETTER UI: not included in any glyphset definition
 * U+AB51 LATIN SMALL LETTER TURNED UI: not included in any glyphset definition
 * U+AB52 LATIN SMALL LETTER U WITH LEFT HOOK: not included in any glyphset definition
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+AB54 LATIN SMALL LETTER CHI WITH LOW RIGHT RING: not included in any glyphset definition
 * U+AB55 LATIN SMALL LETTER CHI WITH LOW LEFT SERIF: not included in any glyphset definition
 * U+AB56 LATIN SMALL LETTER X WITH LOW RIGHT RING: not included in any glyphset definition
 * U+AB57 LATIN SMALL LETTER X WITH LONG LEFT LEG: not included in any glyphset definition
 * U+AB58 LATIN SMALL LETTER X WITH LONG LEFT LEG AND LOW RIGHT RING: not included in any glyphset definition
 * U+AB59 LATIN SMALL LETTER X WITH LONG LEFT LEG WITH SERIF: not included in any glyphset definition
 * U+AB5A LATIN SMALL LETTER Y WITH SHORT RIGHT LEG: not included in any glyphset definition
 * U+AB5B MODIFIER BREVE WITH INVERTED BREVE: not included in any glyphset definition
 * U+AB5C MODIFIER LETTER SMALL HENG: not included in any glyphset definition
 * U+AB5D MODIFIER LETTER SMALL L WITH INVERTED LAZY S: not included in any glyphset definition
 * U+AB5E MODIFIER LETTER SMALL L WITH MIDDLE TILDE: not included in any glyphset definition
 * U+AB5F MODIFIER LETTER SMALL U WITH LEFT HOOK: not included in any glyphset definition
 * U+AB60 LATIN SMALL LETTER SAKHA YAT: not included in any glyphset definition
 * U+AB61 LATIN SMALL LETTER IOTIFIED E: not included in any glyphset definition
 * U+AB62 LATIN SMALL LETTER OPEN OE: not included in any glyphset definition
 * U+AB63 LATIN SMALL LETTER UO: not included in any glyphset definition
 * U+AB64 LATIN SMALL LETTER INVERTED ALPHA: not included in any glyphset definition
 * U+AB65 GREEK LETTER SMALL CAPITAL OMEGA: not included in any glyphset definition
 * U+AB66 LATIN SMALL LETTER DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+AB67 LATIN SMALL LETTER TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+AB68 LATIN SMALL LETTER TURNED R WITH MIDDLE TILDE: not included in any glyphset definition
 * U+AB69 MODIFIER LETTER SMALL TURNED W: not included in any glyphset definition
 * U+AB6A MODIFIER LETTER LEFT TACK: not included in any glyphset definition
 * U+AB6B MODIFIER LETTER RIGHT TACK: not included in any glyphset definition
 * U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition
 * U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition
 * U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition
 * U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition
 * U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition
 * U+FB05 LATIN SMALL LIGATURE LONG S T: not included in any glyphset definition
 * U+FB06 LATIN SMALL LIGATURE ST: not included in any glyphset definition
 * U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, phags-pa, yi
 * U+FE20 COMBINING LIGATURE LEFT HALF: try adding caucasian-albanian
 * U+FE21 COMBINING LIGATURE RIGHT HALF: try adding caucasian-albanian
 * U+FE22 COMBINING DOUBLE TILDE LEFT HALF: try adding caucasian-albanian
 * U+FE23 COMBINING DOUBLE TILDE RIGHT HALF: try adding caucasian-albanian
 * U+FE24 COMBINING MACRON LEFT HALF: try adding one of: coptic, caucasian-albanian
 * U+FE25 COMBINING MACRON RIGHT HALF: try adding one of: coptic, caucasian-albanian
 * U+FE26 COMBINING CONJOINING MACRON: try adding one of: coptic, caucasian-albanian
 * U+FE27 COMBINING LIGATURE LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE28 COMBINING LIGATURE RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE29 COMBINING TILDE LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE2A COMBINING TILDE RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE2B COMBINING MACRON LEFT HALF BELOW: try adding caucasian-albanian
 * U+FE2C COMBINING MACRON RIGHT HALF BELOW: try adding caucasian-albanian
 * U+FE2D COMBINING CONJOINING MACRON BELOW: try adding caucasian-albanian
 * U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition
 * U+10780 MODIFIER LETTER SMALL CAPITAL AA: not included in any glyphset definition
 * U+10781 MODIFIER LETTER SUPERSCRIPT TRIANGULAR COLON: not included in any glyphset definition
 * U+10782 MODIFIER LETTER SUPERSCRIPT HALF TRIANGULAR COLON: not included in any glyphset definition
 * U+10783 MODIFIER LETTER SMALL AE: not included in any glyphset definition
 * U+10784 MODIFIER LETTER SMALL CAPITAL B: not included in any glyphset definition
 * U+10785 MODIFIER LETTER SMALL B WITH HOOK: not included in any glyphset definition
 * U+10787 MODIFIER LETTER SMALL DZ DIGRAPH: not included in any glyphset definition
 * U+10788 MODIFIER LETTER SMALL DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+10789 MODIFIER LETTER SMALL DZ DIGRAPH WITH CURL: not included in any glyphset definition
 * U+1078A MODIFIER LETTER SMALL DEZH DIGRAPH: not included in any glyphset definition
 * U+1078B MODIFIER LETTER SMALL D WITH TAIL: not included in any glyphset definition
 * U+1078C MODIFIER LETTER SMALL D WITH HOOK: not included in any glyphset definition
 * U+1078D MODIFIER LETTER SMALL D WITH HOOK AND TAIL: not included in any glyphset definition
 * U+1078E MODIFIER LETTER SMALL REVERSED E: not included in any glyphset definition
 * U+1078F MODIFIER LETTER SMALL CLOSED REVERSED OPEN E: not included in any glyphset definition
 * U+10790 MODIFIER LETTER SMALL FENG DIGRAPH: not included in any glyphset definition
 * U+10791 MODIFIER LETTER SMALL RAMS HORN: not included in any glyphset definition
 * U+10792 MODIFIER LETTER SMALL CAPITAL G: not included in any glyphset definition
 * U+10793 MODIFIER LETTER SMALL G WITH HOOK: not included in any glyphset definition
 * U+10794 MODIFIER LETTER SMALL CAPITAL G WITH HOOK: not included in any glyphset definition
 * U+10795 MODIFIER LETTER SMALL H WITH STROKE: not included in any glyphset definition
 * U+10796 MODIFIER LETTER SMALL CAPITAL H: not included in any glyphset definition
 * U+10797 MODIFIER LETTER SMALL HENG WITH HOOK: not included in any glyphset definition
 * U+10798 MODIFIER LETTER SMALL DOTLESS J WITH STROKE AND HOOK: not included in any glyphset definition
 * U+10799 MODIFIER LETTER SMALL LS DIGRAPH: not included in any glyphset definition
 * U+1079A MODIFIER LETTER SMALL LZ DIGRAPH: not included in any glyphset definition
 * U+1079B MODIFIER LETTER SMALL L WITH BELT: not included in any glyphset definition
 * U+1079C MODIFIER LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition
 * U+1079D MODIFIER LETTER SMALL L WITH RETROFLEX HOOK AND BELT: not included in any glyphset definition
 * U+1079E MODIFIER LETTER SMALL LEZH: not included in any glyphset definition
 * U+1079F MODIFIER LETTER SMALL LEZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107A0 MODIFIER LETTER SMALL TURNED Y: not included in any glyphset definition
 * U+107A1 MODIFIER LETTER SMALL TURNED Y WITH BELT: not included in any glyphset definition
 * U+107A2 MODIFIER LETTER SMALL O WITH STROKE: not included in any glyphset definition
 * U+107A3 MODIFIER LETTER SMALL CAPITAL OE: not included in any glyphset definition
 * U+107A4 MODIFIER LETTER SMALL CLOSED OMEGA: not included in any glyphset definition
 * U+107A5 MODIFIER LETTER SMALL Q: not included in any glyphset definition
 * U+107A6 MODIFIER LETTER SMALL TURNED R WITH LONG LEG: not included in any glyphset definition
 * U+107A7 MODIFIER LETTER SMALL TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition
 * U+107A8 MODIFIER LETTER SMALL R WITH TAIL: not included in any glyphset definition
 * U+107A9 MODIFIER LETTER SMALL R WITH FISHHOOK: not included in any glyphset definition
 * U+107AA MODIFIER LETTER SMALL CAPITAL R: not included in any glyphset definition
 * U+107AB MODIFIER LETTER SMALL TC DIGRAPH WITH CURL: not included in any glyphset definition
 * U+107AC MODIFIER LETTER SMALL TS DIGRAPH: not included in any glyphset definition
 * U+107AD MODIFIER LETTER SMALL TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107AE MODIFIER LETTER SMALL TESH DIGRAPH: not included in any glyphset definition
 * U+107AF MODIFIER LETTER SMALL T WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107B0 MODIFIER LETTER SMALL V WITH RIGHT HOOK: not included in any glyphset definition
 * U+107B2 MODIFIER LETTER SMALL CAPITAL Y: not included in any glyphset definition
 * U+107B3 MODIFIER LETTER GLOTTAL STOP WITH STROKE: not included in any glyphset definition
 * U+107B4 MODIFIER LETTER REVERSED GLOTTAL STOP WITH STROKE: not included in any glyphset definition
 * U+107B5 MODIFIER LETTER BILABIAL CLICK: not included in any glyphset definition
 * U+107B6 MODIFIER LETTER DENTAL CLICK: not included in any glyphset definition
 * U+107B7 MODIFIER LETTER LATERAL CLICK: not included in any glyphset definition
 * U+107B8 MODIFIER LETTER ALVEOLAR CLICK: not included in any glyphset definition
 * U+107B9 MODIFIER LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+107BA MODIFIER LETTER SMALL S WITH CURL: not included in any glyphset definition
 * U+11AB0 CANADIAN SYLLABICS NATTILIK HI: try adding canadian-aboriginal
 * U+11AB1 CANADIAN SYLLABICS NATTILIK HII: try adding canadian-aboriginal
 * U+1DF00 LATIN SMALL LETTER FENG DIGRAPH WITH TRILL: not included in any glyphset definition
 * U+1DF01 LATIN SMALL LETTER REVERSED SCRIPT G: not included in any glyphset definition
 * U+1DF02 LATIN LETTER SMALL CAPITAL TURNED G: not included in any glyphset definition
 * U+1DF03 LATIN SMALL LETTER REVERSED K: not included in any glyphset definition
 * U+1DF04 LATIN LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition
 * U+1DF05 LATIN SMALL LETTER LEZH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF06 LATIN SMALL LETTER TURNED Y WITH BELT: not included in any glyphset definition
 * U+1DF07 LATIN SMALL LETTER REVERSED ENG: not included in any glyphset definition
 * U+1DF08 LATIN SMALL LETTER TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF09 LATIN SMALL LETTER T WITH HOOK AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF0A LATIN LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF0B LATIN SMALL LETTER ESH WITH DOUBLE BAR: not included in any glyphset definition
 * U+1DF0C LATIN SMALL LETTER ESH WITH DOUBLE BAR AND CURL: not included in any glyphset definition
 * U+1DF0D LATIN SMALL LETTER TURNED T WITH CURL: not included in any glyphset definition
 * U+1DF0E LATIN LETTER INVERTED GLOTTAL STOP WITH CURL: not included in any glyphset definition
 * U+1DF0F LATIN LETTER STRETCHED C WITH CURL: not included in any glyphset definition
 * U+1DF10 LATIN LETTER SMALL CAPITAL TURNED K: not included in any glyphset definition
 * U+1DF11 LATIN SMALL LETTER L WITH FISHHOOK: not included in any glyphset definition
 * U+1DF12 LATIN SMALL LETTER DEZH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF13 LATIN SMALL LETTER L WITH BELT AND PALATAL HOOK: not included in any glyphset definition
 * U+1DF14 LATIN SMALL LETTER ENG WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF15 LATIN SMALL LETTER TURNED R WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF16 LATIN SMALL LETTER R WITH FISHHOOK AND PALATAL HOOK: not included in any glyphset definition
 * U+1DF17 LATIN SMALL LETTER TESH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF18 LATIN SMALL LETTER EZH WITH PALATAL HOOK: not included in any glyphset definition
 * U+1DF19 LATIN SMALL LETTER DEZH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1A LATIN SMALL LETTER I WITH STROKE AND RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1B LATIN SMALL LETTER O WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1C LATIN SMALL LETTER TESH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1D LATIN SMALL LETTER C WITH RETROFLEX HOOK: not included in any glyphset definition
 * U+1DF1E LATIN SMALL LETTER S WITH CURL: not included in any glyphset definition

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic`, `cyrillic-ext`, `devanagari`, `greek`, `greek-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure files are not too large. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/file_size">com.google.fonts/check/file_size</a>)</summary><div>


* ⚠ **WARN** Font file is 2.6Mb; ideally it should be less than 1.0Mb [code: large-font]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Desoftcy
	* Iotaserifed
	* Ocrossedcy
	* Smiddlestroke
	* Ukmonographcy
	* Ustroke
	* Wanglicana
	* Yatiotifiedcy
	* Yusiotifiedclosedlittlecy
	* elsoftcy
	* emsoftcy
	* hbar.sc
	* lslash.sc
	* oslash.sc
	* oslashacute.sc
	* smiddlestroke
	* solidusdotted
	* stackedcommadbl
	* uni023A
	* uni023B
	* uni023C
	* uni023E
	* uni0246
	* uni024F
	* uni0289
	* uni0372
	* uni0406
	* uni0407
	* uni0416
	* uni043C
	* uni043F
	* uni0444
	* uni0459
	* uni049C
	* uni049D
	* uni04C1
	* uni04DC
	* uni052A
	* uni052B
	* uni052F
	* uni1D6F
	* uni1D70
	* uni1D7A
	* uni1D7D
	* uni1D7E
	* uni1D7F
	* uni1EFB
	* uni20A5
	* uni20AD
	* uni20B7
	* uni20BE
	* uni20BF
	* uni2114
	* uni211F
	* uni2123
	* uni2C65
	* uni2C66
	* uni2C7A
	* uni2E3F
	* uniA642
	* uniA648
	* uniA649
	* uniA66E
	* uniA680
	* uniA684
	* uniA685
	* uniA734
	* uniA73A
	* uniA744
	* uniA745
	* uniA74A
	* uniA74B
	* uniA75E
	* uniA771
	* uniA773
	* uniA774
	* uniA776
	* uniA792
	* uniA7A1
	* uniA7A2
	* uniA7A3
	* uniA7A4
	* uniA7A5
	* uniA7A6
	* uniA7A8
	* uniA7A9
	* uniAB30
	* uniAB38
	* uniAB39
	* uniAB3E
	* uniAB3F
	* uniAB41
	* uniAB44
	* uniAB4F
	* uniAB5A
	* uo
	* wanglicana
	* yatiotifiedcy
	* yerubackyercy and zero.slash
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


* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
kavykawithkavykaaboveinvertedlow [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- iogonek.loclNAV

	- psilioxia_macronmod

	- psilivaria_macronmod

	- tonos.case

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- uni03B9030403130301

	- uni03B9030403140300

	- uni03B9030403140301

	- uni03B9030603130300

	- uni03B9030603130301

	- uni03B9030603140300

	- uni03B9030603140301

	- uni03B9030803040300

	- uni03B9030803040301

	- uni03B9030803060300

	- uni03B9030803060301

	- uni03C5030403130300

	- uni03C5030403130301

	- uni03C5030403140300

	- uni03C5030403140301

	- uni03C5030603130300

	- uni03C5030603130301

	- uni03C5030603140300

	- uni03C5030603140301

	- uni03C5030803040300

	- uni03C5030803040301

	- uni03C5030803060300

	- uni03C5030803060301

	- uni1FBD.case

	- uni1FBF.case

	- uni1FC0.case

	- uni1FC1.case

	- uni1FCD.case

	- uni1FCD0306

	- uni1FCE.case

	- uni1FCE0306

	- uni1FCF.case

	- uni1FDD.case

	- uni1FDD0306

	- uni1FDE.case

	- uni1FDE0306

	- uni1FDF.case

	- uni1FED.case

	- uni1FEE.case

	- uni1FEF.case

	- uni1FFD.case

	- uni1FFE.case

	- uniA733.pcap
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>


* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fd50>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fcd90>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fcf50>

	- Contour 1 start point differs in glyph 'uni213A' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fd1d0>

	- Contour 1 start point differs in glyph 'omegaroundcy' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fd1d0>

	- Contour 1 start point differs in glyph 'zero' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fd1d0>

	- Contour 0 start point differs in glyph 'uni1DBF' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fcc90>

	- Contour 0 start point differs in glyph 'theta' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fcc90>

	- Contour 2 start point differs in glyph 'zero.slash' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee9328fa90> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x7fee938fd1d0> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 572 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 313:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>


* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 uni0903 (U+0903) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+0903 [code: non-mark-chars]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 6 | 27 | 183 | 17 | 248 | 0 |
| 0% | 1% | 6% | 38% | 4% | 52% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
