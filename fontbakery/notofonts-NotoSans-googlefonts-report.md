## FontBakery report

fontbakery version: 0.13.2





## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[1] NotoSans-Italic[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)

- uni1ABE (U+1ABE)

- uniA670 (U+A670)

- uniA671 (U+A671)

- uniA672 (U+A672)
</code></pre>
 [code: zero-width-bases]



</div>
</details>
</div>
</details>

<details><summary>[1] NotoSans[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)

- uni1ABE (U+1ABE)

- uniA670 (U+A670)

- uniA671 (U+A671)

- uniA672 (U+A672)
</code></pre>
 [code: zero-width-bases]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[16] NotoSans-Italic[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+2184: LATIN SMALL LETTER REVERSED C</td>
<td align="left">U+2183: ROMAN NUMERAL REVERSED ONE HUNDRED</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 508, but got 395 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Greek_Expert glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɤ̀, Ɤ̂, Ɤ̋, Ɤ̄, Ɤ, Ɤ́, Ɤ̏</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030F to .notdef when shaping the text 'Ɤ̏'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to .notdef when shaping the text 'Ɤ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0304 to .notdef when shaping the text 'Ɤ̄'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to .notdef when shaping the text 'Ɤ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030B to .notdef when shaping the text 'Ɤ̋'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to .notdef when shaping the text 'Ɤ̂'</td>
<td align="left">dnj_Latn (Dan)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA7B7 when shaping the text 'ꞷ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA7B6 when shaping the text 'Ꞷ̃'</td>
<td align="left">kzc_Latn (Bondoukou Kulango)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɤ, Ɤ̂, Ɤ́, Ɤ̀</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to .notdef when shaping the text 'Ɤ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to .notdef when shaping the text 'Ɤ̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to .notdef when shaping the text 'Ɤ̀'</td>
<td align="left">gov_Latn (Goo)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uniA78D when shaping the text 'Ɥ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uniA78D when shaping the text 'Ɥ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uniA78D when shaping the text 'Ɥ̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA78D when shaping the text 'Ɥ̃̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA78D when shaping the text 'Ɥ̃́'</td>
<td align="left">dnj_Latn_LR (Liberian Dan)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Greek_Expert glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ſ' and shaping the text 'ſ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">de_Latn (German)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǥ' and shaping the text 'ǥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȟ' and shaping the text 'ȟ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǩ' and shaping the text 'ǩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǯ' and shaping the text 'ǯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ſ' and shaping the text 'ſ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fr_Latn (French)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lt_Latn (Lithuanian), sad_Latn (Sandawe) and umb_Latn (Umbundu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tr_Latn (Turkish)</td>
</tr>
<tr>
<td align="left">Small caps i should be dotted:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'i' with features: smcp and shaping the text 'i' in language 'tr' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tr_Latn (Turkish)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bm_Latn (Bambara), dyu_Latn (Dyula), bm_Latn (Bambara), bzx_Latn (Bozo, Hainyaxo), dyu_Latn (Dyula), sus_Latn (Susu), man_Latn (Mandingo), kqs_Latn (Kissi, Northern), mwk_Latn (Kita Maninkakan), dtm_Latn (Tomo Kan Dogon), myk_Latn (Mamara Senoufo), emk_Latn (Maninkakan, Eastern), dts_Latn (Dogon, Toro So), bwq_Latn (Southern Bobo Madaré) and boz_Latn (Tiéyaxo Bozo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fat_Latn (Fanti), tw_akuapem_Latn (Akuapem Twi), suq_Latn (Suri, Tirmaga-Chai), dga_Latn (Dagaare, Southern), ekm_Latn (Elip), cbj_Latn (Ede Cabe), saf_Latn (Safaliba), nym_Latn (Nyamwezi), idd_Latn (Ede Idaca), tw_akuapem_Latn (Akuapem Twi), fat_Latn (Fanti), ngb_Latn (Ngbandi, Northern), lok_Latn (Loko), ncu_Latn (Chumburung), mfq_Latn (Moba), agc_Latn (Agatu), bov_Latn (Tuwuli), bci_Latn (Baoulé), maw_Latn (Mampruli), nzi_Latn (Nzima), bba_Latn (Baatonum), utr_Latn (Etulo), etx_Latn (Iten), ica_Latn (Ede Ica), adj_Latn (Adioukrou), ada_Latn (Adangme), nfr_Latn (Nafaanra), lia_Latn (Limba, West-Central), tvu_Latn (Tunen), abr_Latn (Abron), mkl_Latn (Mokole), yas_Latn (Nugunu), sef_Latn (Cebaara Senoufo), ati_Latn (Attié), mym_Latn (Me’en), ijj_Latn (Ede Ije), lem_Latn (Nomaande), bhy_Latn (Bhele), ich_Latn (Etkywan), hag_Latn (Hanga), cko_Latn (Anufo), mfo_Latn (Mbe), nhb_Latn (Beng), mzw_Latn (Deg), cme_Latn (Cerma), xrb_Latn (Karaboro, Eastern), ntr_Latn (Delo), vag_Latn (Vagla), bet_Latn (Bété, Guiberoua), wan_Latn (Wan), kez_Latn (Kukele), mur_Latn (Murle), kri_Latn (Krio), lig_Latn (Ligbi), mmu_Latn (Mmaala), ddn_Latn (Dendi), lu_Latn (Luba-Katanga), yba_Latn (Yala), men_Latn (Mende), gjn_Latn (Gonja), moa_Latn (Mwan) and guk_Latn (Gumuz)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ff_Latn (Fulah), fub_Latn (Fulfulde, Adamawa), daa_Latn (Dangaléat), fuc_Latn (Pulaar), sav_Latn (Saafi-Saafi), tnr_Latn (Ménik), ff_Latn (Fulah), djc_Latn (Dar Daju Daju), fuh_Latn (Fulfulde, Western Niger) and fue_Latn (Fulfulde, Borgu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ha_Latn (Hausa) and ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṅ' and shaping the text 'ṅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɵ' and shaping the text 'ɵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ig_Latn (Igbo) and ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yo_Latn (Yoruba) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ả' and shaping the text 'ả' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ằ' and shaping the text 'ằ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẳ' and shaping the text 'ẳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẵ' and shaping the text 'ẵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ắ' and shaping the text 'ắ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ặ' and shaping the text 'ặ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ầ' and shaping the text 'ầ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẩ' and shaping the text 'ẩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẫ' and shaping the text 'ẫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ấ' and shaping the text 'ấ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ậ' and shaping the text 'ậ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẻ' and shaping the text 'ẻ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ề' and shaping the text 'ề' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ể' and shaping the text 'ể' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ễ' and shaping the text 'ễ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ế' and shaping the text 'ế' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỉ' and shaping the text 'ỉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỏ' and shaping the text 'ỏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ồ' and shaping the text 'ồ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ổ' and shaping the text 'ổ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỗ' and shaping the text 'ỗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ố' and shaping the text 'ố' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ơ' and shaping the text 'ơ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ờ' and shaping the text 'ờ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ở' and shaping the text 'ở' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỡ' and shaping the text 'ỡ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ớ' and shaping the text 'ớ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ợ' and shaping the text 'ợ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ủ' and shaping the text 'ủ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ư' and shaping the text 'ư' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ừ' and shaping the text 'ừ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ử' and shaping the text 'ử' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ữ' and shaping the text 'ữ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ứ' and shaping the text 'ứ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ự' and shaping the text 'ự' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỷ' and shaping the text 'ỷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỵ' and shaping the text 'ỵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vi_Latn (Vietnamese)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">igb_Latn (Ebira) and ekp_Latn (Ekpeye)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kyq_Latn (Kenga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nmg_Latn (Kwasio)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nza_Latn (Tigon Mbembe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ahs_Latn (Ashe), bqv_Latn (Koro Wachi) and ldb_Latn (Duya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʈ' and shaping the text 'ʈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nus_Latn (Nuer)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snf_Latn (Noon) and fuq_Latn (Central-Eastern Niger Fulfulde)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tsw_Latn (Tsishingini) and kdl_Latn (Tsikimba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ồ' and shaping the text 'ồ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mg_Latn (Malagasy)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yam_Latn (Yamba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ybb_Latn (Yemba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aks_Latn (Akeselem) and kdh_Latn (Tem)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʈ' and shaping the text 'ʈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">luo_Latn (Luo) and ach_Latn (Acoli)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gng_Latn (Ngangam)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɂ' and shaping the text 'ɂ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mfd_Latn (Mendankwe-Nkwen)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pcm_Latn (Nigerian Pidgin), bin_Latn (Bini), ish_Latn (Esan) and atg_Latn (Ivbie North-Okpela-Arhe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mas_Latn (Masai), buu_Latn (Budu), niy_Latn (Ngiti), mdj_Latn (Mangbetu), teo_Latn (Teso) and kdj_Latn (Karamojong)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bev_Latn (Bété, Daloa), nko_Latn (Nkonya), nwb_Latn (Nyabwa), ted_Latn (Krumen, Tepo), sig_Latn (Paasaal), yre_Latn (Yaouré), god_Latn (Godié), wob_Latn (Wè Northern), kye_Latn (Krache), ade_Latn (Adele), gud_Latn (Dida, Yocoboué), sil_Latn (Sisaala, Tumulung) and lor_Latn (Téén)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dow_Latn (Doyayo), gmm_Latn (Gbaya-Mbodomo), dua_Latn (Duala), kkj_Latn (Kako) and bkc_Latn (Baka, Cameroon/Gabon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȁ' and shaping the text 'ȁ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǣ' and shaping the text 'ǣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȅ' and shaping the text 'ȅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȉ' and shaping the text 'ȉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȍ' and shaping the text 'ȍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɤ' and shaping the text 'ɤ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȕ' and shaping the text 'ȕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɯ' and shaping the text 'ɯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dnj_Latn (Dan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snw_Latn (Selee), dyi_Latn (Sénoufo, Djimini), anv_Latn (Denya) and tpm_Latn (Tampulma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">hia_Latn (Lamang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xsm_Latn (Kasem)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kus_Latn (Kusaal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǜ' and shaping the text 'ǜ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǘ' and shaping the text 'ǘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǚ' and shaping the text 'ǚ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǖ' and shaping the text 'ǖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bax_Latn (Bamun (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɪ' and shaping the text 'ɪ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞷ' and shaping the text 'ꞷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kzc_Latn (Bondoukou Kulango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">acd_Latn (Gikyode)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">swb_Latn (Maore Comorian, Latin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dag_Latn (Dagbani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tik_Latn (Tikar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dbd_Latn (Dadiya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ank_Latn (Goemai), pip_Latn (Pero), wja_Latn (Waja), wji_Latn (Warji) and tal_Latn (Tal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bbo_Latn (Northern Bobo Madaré) and nku_Latn (Kulango, Bouna)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bfd_Latn (Bafut)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nhu_Latn (Noone)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snk_Latn (Soninke) and kao_Latn (Xaasongaxango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dgi_Latn (Northern Dagara)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kzr_Latn (Karang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bze_Latn (Jenaama Bozo), msc_Latn (Maninka, Sankaran), shz_Latn (Syenara Senoufo), spp_Latn (Sénoufo, Supyire) and yal_Latn (Yalunka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">muy_Latn (Muyang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgo_Latn (Metaʼ) and bum_Latn (Bulu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aha_Latn (Ahanta)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">goa_Latn (Guro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">did_Latn (Didinga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mcp_Latn (Makaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xuo_Latn (Kuo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sok_Latn (Sokoro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tuz_Latn (Turka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">les_Latn (Lese), led_Latn (Lendu), nzk_Latn (Nzakara) and lag_Latn (Langi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yo_Latn_BJ (Yoruba, Benin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ee_Latn (Ewe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mhi_Latn (Ma’di)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xed_Latn (Hdi), dbq_Latn (Daba), gnd_Latn (Zulgo-Gemzek), mqb_Latn (Mbuko), gde_Latn (Gude), hig_Latn (Kamwe) and bwr_Latn (Bura-Pabir)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nuv_Latn (Nuni, Northern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pnz_Latn (Pana, Central African Republic)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sba_Latn (Ngambay)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ln_Latn (Lingala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ksf_Latn (Bafia)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sbd_Latn (Southern Samo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mfn_Latn (Mbembe, Cross River)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fod_Latn (Foodo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bjv_Latn (Bedjond)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">izz_Latn (Izii)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bvb_Latn (Bube), eka_Latn (Ekajuk) and kub_Latn (Kutep)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ffm_Latn (Maasina Fulfulde)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dop_Latn (Lukpa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ktj_Latn (Krumen, Plapo), kyf_Latn (Kouya), any_Latn (Anyin), kvf_Latn (Kabalai) and naw_Latn (Nawuri)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tda_Latn (Tagdal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dur_Latn (Dii)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʕ' and shaping the text 'ʕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tsb_Latn (Tsamai) and gwd_Latn (Gawwada)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mfi_Latn (Wandala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yay_Latn (Agwagwune)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƃ' and shaping the text 'ƃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lom_Latn (Loma, Liberia)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƈ' and shaping the text 'ƈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƥ' and shaping the text 'ƥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṕ' and shaping the text 'ṕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">srr_Latn (Serer)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcn_Latn (Bali)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yaz_Latn (Lokaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sld_Latn (Sissala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgc_Latn (Morokodo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">meq_Latn (Merey) and pbi_Latn (Parkwa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƀ' and shaping the text 'ƀ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẑ' and shaping the text 'ẑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">buc_Latn (Bushi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʘ' and shaping the text 'ʘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ngh_Latn (Nǁng) and nmn_Latn (ǃXoon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">shi_Latn (Tachelhit (Latin)) and tzm_Latn (Central Atlas Tamazight)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ⓐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ⓐ</td>
<td align="left">kib_Latn (Koalib)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɽ' and shaping the text 'ɽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɐ' and shaping the text 'ɐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kib_Latn (Koalib)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dje_Latn (Zarma), twq_Latn (Tasawaq), ses_Latn (Koyraboro Senni) and khq_Latn (Koyra Chiini)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kst_Latn (Winyé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">eto_Latn (Eton, Cameroon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">abi_Latn (Abidji)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ndv_Latn (Ndut)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cla_Latn (Ron), fuv_Latn (Nigerian Fulfulde), asg_Latn (Cishingini), giz_Latn (Southern Giziga), ttr_Latn (Tera), mne_Latn (Naba) and bys_Latn (Burak)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pil_Latn (Yom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mwm_Latn (Sar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɤ' and shaping the text 'ɤ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gov_Latn (Goo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">din_Latn (Dinka), bza_Latn (Bandi) and dip_Latn (Dinka, Northeastern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cky_Latn (Cakfem-Mushere) and sur_Latn (Mwaghavul)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pym_Latn (Pyam)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lgg_Latn (Lugbara)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gby_Latn (Gbari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mge_Latn (Mango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">box_Latn (Buamu) and bwj_Latn (Láá Láá Bwamu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gkn_Latn (Gokana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">she_Latn (Sheko), beh_Latn (Biali) and lns_Latn (Lamnso’)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṳ' and shaping the text 'ṳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fan_Latn (Fang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ⱳ' and shaping the text 'ⱳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pug_Latn (Phuie)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">guw_Latn (Gun) and ayb_Latn (Ayizo Gbe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kia_Latn (Kim)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ajg_Latn (Aja)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jab_Latn (Hyam) and btt_Latn (Bete-Bendi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ndz_Latn (Ndogo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">okr_Latn (Kirike) and ijs_Latn (Ijo, Southeast)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bbj_Latn (Ghomala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">muh_Latn (Mündü), cdr_Latn (Kamuku) and png_Latn (Pangu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tmh_Latn (Tamashek)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">avn_Latn (Avatime)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꟈ' and shaping the text 'ꟈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɽ' and shaping the text 'ɽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mor_Latn (Moro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bkv_Latn (Bekwarra)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƹ' and shaping the text 'ƹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȓ' and shaping the text 'ȓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">rif_Latn (Riffian (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḯ' and shaping the text 'ḯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǘ' and shaping the text 'ǘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bvi_Latn (Belanda Viri, Latin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṿ' and shaping the text 'ṿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bdh_Latn (Baka, DRC/South Sudan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsq_Latn (Bassa (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bzw_Latn (Basa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǫ' and shaping the text 'ǫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gkp_Latn (Kpelle, Guinea)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dzg_Latn (Dazaga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ibb_Latn (Ibibio)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ⱳ' and shaping the text 'ⱳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lob_Latn (Lobi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɍ' and shaping the text 'ɍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kr_Latn (Kanuri), knc_Latn (Kanuri, Central) and kby_Latn (Kanuri, Manga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dya_Latn (Dyan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jbu_Latn (Jukun Takum)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bfo_Latn (Malba Birifor)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ife_Latn (Ifè)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">awc_Latn (Cicipu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɍ' and shaping the text 'ɍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mdt_Latn (Mbere)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dno_Latn (Ndrulo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kbo_Latn (Keliko)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ahl_Latn (Igo), fon_Latn (Fon) and tfi_Latn (Gbe, Tofin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">neb_Latn (Toura)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cae_Latn (Lehar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wib_Latn (Toussian, Southern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">etu_Latn (Ejagham)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gqr_Latn (Gor)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">buw_Latn (gevové)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nnw_Latn (Southern Nuni)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">anc_Latn (Ngas)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gej_Latn (Gen)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kai_Latn (Karekare)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcw_Latn (Bana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">agq_Latn (Aghem) and ken_Latn (Kenyang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsp_Latn (Baga Sitemu) and ksp_Latn (Kabba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kbp_Latn (Kabiyé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">keu_Latn (Akebu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">loq_Latn (Lobala) and mbo_Latn (Mbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bud_Latn (Ntcham)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lol_Latn (Mongo) and krw_Latn (Western Krahn)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tcd_Latn (Tafi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ann_Latn (Obolo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mnf_Latn (Mundani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wci_Latn (Gbe, Waci)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kmy_Latn (Koma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṃ' and shaping the text 'ṃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẉ' and shaping the text 'ẉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ttq_Latn (Tawallammat Tamajaq)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">enn_Latn (Engenni)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gna_Latn (Kaansa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jib_Latn (Jibu) and nup_Latn (Nupe-Nupe-Tako)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yav_Latn (Yangben)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">blo_Latn (Anii)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">byv_Latn (Medumba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ckl_Latn (Kibaku)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bjt_Latn (Balanta-Ganja) and dgh_Latn (Dghwede)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṽ' and shaping the text 'ṽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mua_Latn (Mundang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḓ' and shaping the text 'ḓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṋ' and shaping the text 'ṋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṱ' and shaping the text 'ṱ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">hz_Latn (Herero)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">las_Latn (Lama, Togo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ậ' and shaping the text 'ậ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">avu_Latn (Avokaya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṅ' and shaping the text 'ṅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ikw_Latn (Ikwere)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nnh_Latn (Ngiemboon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mos_Latn (Mossi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vut_Latn (Vute)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ozm_Latn (Koonzime)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mda_Latn (Mada)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḕ' and shaping the text 'ḕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṃ' and shaping the text 'ṃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aeb_Latn (Tunisian Darija)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bkm_Latn (Kom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sxw_Latn (Saxwe Gbe) and xwe_Latn (Gbe, Xwela)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jen_Latn (Dza)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bmq_Latn (Bomu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">knp_Latn (Kwanja)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mql_Latn (Mbelime)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cou_Latn (Wamey)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gaa_Latn (Ga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mev_Latn (Mano)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ewo_Latn (Ewondo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wwa_Latn (Waama)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṫ' and shaping the text 'ṫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṡ' and shaping the text 'ṡ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḋ' and shaping the text 'ḋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȧ' and shaping the text 'ȧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḣ' and shaping the text 'ḣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">har_Latn (Harari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">iby_Latn (Ibani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tan_Latn (Tangale)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḵ' and shaping the text 'ḵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẖ' and shaping the text 'ẖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">udu_Latn (Uduk)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">azo_Latn (Awing)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ᵽ' and shaping the text 'ᵽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bqj_Latn (Bandial)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fmp_Latn (Fe’fe’)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xsm_Latn_BF (Kasem, Burkina Faso)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mbu_Latn (Mbula-Bwazza)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɉ' and shaping the text 'ɉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsc_Latn_GN (Guinean Bassari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yer_Latn (Tarok)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">biv_Latn (Birifor, Southern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pkb_Latn (Pokomo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḓ' and shaping the text 'ḓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḽ' and shaping the text 'ḽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṋ' and shaping the text 'ṋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṅ' and shaping the text 'ṅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṱ' and shaping the text 'ṱ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ve_Latn (Venda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">iqw_Latn (Ikwo), eza_Latn (Ezaa) and ige_Latn (Igede)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xon_Latn (Konkomba), bim_Latn (Bimoba) and mcu_Latn (Mambila, Cameroon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tbz_Latn (Ditammari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fuf_Latn (Pular)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nga_Latn (Ngbaka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yat_Latn (Yambeta)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɵ' and shaping the text 'ɵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɥ' and shaping the text 'ɥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƃ' and shaping the text 'ƃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dnj_Latn_LR (Liberian Dan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lee_Latn (Lyélé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṉ' and shaping the text 'ṉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lnu_Latn (Longuda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">idu_Latn (Idoma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lip_Latn (Sekpele)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bqp_Latn (Bisã)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṅ' and shaping the text 'ṅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ikk_Latn (Ika)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vai_Latn (Vai (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lmp_Latn (Limbum)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nin_Latn (Ninzo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">log_Latn (Logo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tod_Latn (Toma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bqc_Latn (Boko)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsc_Latn (Bassari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">puu_Latn (Punu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ntm_Latn (Nateni)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bss_Latn (Akoose)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kpo_Latn (Ikposo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḇ' and shaping the text 'ḇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mcn_Latn (Masana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wok_Latn (Longto)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">taq_Latn (Tamasheq (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">akp_Latn (Siwu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nfu_Latn (Mfumte)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẋ' and shaping the text 'ẋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mey_Latn (Hassaniyya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lnl_Latn (South Central Banda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kss_Latn (Southern Kisi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ebo_Latn (Teke-Ebo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʝ' and shaping the text 'ʝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ikx_Latn (Ik)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bas_Latn (Basaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bom_Latn (Berom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">soy_Latn (Miyobe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">maf_Latn (Mafa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nyb_Latn (Nyangbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kpe_Latn (Kpelle)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kqp_Latn (Kimré)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">krs_Latn (Gbaya, Sudan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bav_Latn (Vengo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gur_Latn (Frafra)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">abn_Latn (Abua)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gvl_Latn (Gulay)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcy_Latn (Bacama)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tuq_Latn (Tedaga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mzm_Latn (Mumuye)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nmz_Latn (Nawdm)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bex_Latn (Jur Modo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgd_Latn (Moru)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">grb_Latn (Grebo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ọ' and shaping the text 'ọ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẹ' and shaping the text 'ẹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ị' and shaping the text 'ị' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ụ' and shaping the text 'ụ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">efi_Latn (Efik)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṣ' and shaping the text 'ṣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kab_Latn (Kabyle)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jgk_Latn (Gwak)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fvr_Latn (Fur)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bib_Latn (Bissa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȧ' and shaping the text 'ȧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tem_Latn (Timne)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḿ' and shaping the text 'ḿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǹ' and shaping the text 'ǹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jgo_Latn (Ngomba)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-article">googlefonts/description/has_article</a></summary>
    <div>







* 🔥 **FAIL** <p>This is a Noto font but it lacks an ARTICLE.en_us.html file.</p>
 [code: missing-article]



* 🔥 **FAIL** <p>This is a Noto font but it lacks a DESCRIPTION.en_us.html file.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- uni0334

- uni0335

- uni0336

- uni0337

- uni0338

- uni1ABE
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#file-size">file_size</a></summary>
    <div>







* ⚠️ **WARN** <p>Font file is 2.2Mb; ideally it should be less than 1.0Mb</p>
 [code: large-font]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 1 start point differs in glyph 'uni213A' between location wght=400,wdth=100 and location wght=400,wdth=62

- Contour 1 start point differs in glyph 'uni213A' between location wght=400,wdth=62 and location wght=100,wdth=100

- Contour 0 point 26 in glyph 'u10791' has a kink between location wght=900,wdth=100 and location wght=100,wdth=62

- Contour 0 point 28 in glyph 'uniAB38' has a kink between location wght=100,wdth=100 and location wght=704,wdth=100

- Contour 1 point 28 in glyph 'uniAB38' has a kink between location wght=100,wdth=100 and location wght=704,wdth=100
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 572 among a set of 8 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 313:
minus</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _Comp_candraBindudeva.02

- _Comp_nga_Shortdeva

- _Comp_nukta_rakar_matradeva

- _Comp_rakar_matradeva

- dasiaoxia_macronmod

- dasiavaria_macronmod

- iogonek.loclNAV

- psilioxia_macronmod

- psilivaria_macronmod

- tonos.case

- uni030003040308

- uni030003060308

- uni030103040308

- uni030103060308

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

- uni0903.alt

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
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
kavykawithkavykaaboveinvertedlow</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/NotoSans/googlefonts/variable-ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02CD MODIFIER LETTER LOW MACRON: try adding lisu</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, math, coptic</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: math, glagolitic, coptic, gothic, elbasan</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: tifinagh, math, hebrew, old-permic, coptic, syriac, todhri, malayalam, canadian-aboriginal, tai-le, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: math, sunuwar</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+0316 COMBINING GRAVE ACCENT BELOW: not included in any glyphset definition</li>
<li>U+0317 COMBINING ACUTE ACCENT BELOW: not included in any glyphset definition</li>
<li>U+0318 COMBINING LEFT TACK BELOW: not included in any glyphset definition</li>
<li>U+0319 COMBINING RIGHT TACK BELOW: not included in any glyphset definition</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+031C COMBINING LEFT HALF RING BELOW: not included in any glyphset definition</li>
<li>U+031D COMBINING UP TACK BELOW: not included in any glyphset definition</li>
<li>U+031E COMBINING DOWN TACK BELOW: not included in any glyphset definition</li>
<li>U+031F COMBINING PLUS SIGN BELOW: not included in any glyphset definition</li>
<li>U+0320 COMBINING MINUS SIGN BELOW: try adding syriac</li>
<li>U+0321 COMBINING PALATALIZED HOOK BELOW: not included in any glyphset definition</li>
<li>U+0322 COMBINING RETROFLEX HOOK BELOW: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: syriac, sunuwar</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, caucasian-albanian, sunuwar, syriac, cherokee, gothic, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0333 COMBINING DOUBLE LOW LINE: try adding math</li>
<li>U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0339 COMBINING RIGHT HALF RING BELOW: not included in any glyphset definition</li>
<li>U+033A COMBINING INVERTED BRIDGE BELOW: try adding math</li>
<li>U+033B COMBINING SQUARE BELOW: not included in any glyphset definition</li>
<li>U+033C COMBINING SEAGULL BELOW: not included in any glyphset definition</li>
<li>U+033D COMBINING X ABOVE: not included in any glyphset definition</li>
<li>U+033E COMBINING VERTICAL TILDE: not included in any glyphset definition</li>
<li>U+033F COMBINING DOUBLE OVERLINE: try adding coptic</li>
<li>U+0340 COMBINING GRAVE TONE MARK: not included in any glyphset definition</li>
<li>U+0341 COMBINING ACUTE TONE MARK: not included in any glyphset definition</li>
<li>U+0342 COMBINING GREEK PERISPOMENI: not included in any glyphset definition</li>
<li>U+0343 COMBINING GREEK KORONIS: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+0345 COMBINING GREEK YPOGEGRAMMENI: not included in any glyphset definition</li>
<li>U+0346 COMBINING BRIDGE ABOVE: try adding math</li>
<li>U+0347 COMBINING EQUALS SIGN BELOW: not included in any glyphset definition</li>
<li>U+0348 COMBINING DOUBLE VERTICAL LINE BELOW: not included in any glyphset definition</li>
<li>U+0349 COMBINING LEFT ANGLE BELOW: not included in any glyphset definition</li>
<li>U+034A COMBINING NOT TILDE ABOVE: not included in any glyphset definition</li>
<li>U+034B COMBINING HOMOTHETIC ABOVE: not included in any glyphset definition</li>
<li>U+034C COMBINING ALMOST EQUAL TO ABOVE: not included in any glyphset definition</li>
<li>U+034D COMBINING LEFT RIGHT ARROW BELOW: try adding math</li>
<li>U+034E COMBINING UPWARDS ARROW BELOW: not included in any glyphset definition</li>
<li>U+034F COMBINING GRAPHEME JOINER: not included in any glyphset definition</li>
<li>U+0350 COMBINING RIGHT ARROWHEAD ABOVE: not included in any glyphset definition</li>
<li>U+0351 COMBINING LEFT HALF RING ABOVE: not included in any glyphset definition</li>
<li>U+0352 COMBINING FERMATA: not included in any glyphset definition</li>
<li>U+0353 COMBINING X BELOW: not included in any glyphset definition</li>
<li>U+0354 COMBINING LEFT ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0355 COMBINING RIGHT ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0356 COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0357 COMBINING RIGHT HALF RING ABOVE: not included in any glyphset definition</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0359 COMBINING ASTERISK BELOW: not included in any glyphset definition</li>
<li>U+035A COMBINING DOUBLE RING BELOW: not included in any glyphset definition</li>
<li>U+035B COMBINING ZIGZAG ABOVE: not included in any glyphset definition</li>
<li>U+035C COMBINING DOUBLE BREVE BELOW: not included in any glyphset definition</li>
<li>U+035D COMBINING DOUBLE BREVE: not included in any glyphset definition</li>
<li>U+035E COMBINING DOUBLE MACRON: try adding one of: todhri, coptic, caucasian-albanian</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0360 COMBINING DOUBLE TILDE: not included in any glyphset definition</li>
<li>U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic</li>
<li>U+0362 COMBINING DOUBLE RIGHTWARDS ARROW BELOW: not included in any glyphset definition</li>
<li>U+0363 COMBINING LATIN SMALL LETTER A: not included in any glyphset definition</li>
<li>U+0364 COMBINING LATIN SMALL LETTER E: not included in any glyphset definition</li>
<li>U+0365 COMBINING LATIN SMALL LETTER I: not included in any glyphset definition</li>
<li>U+0366 COMBINING LATIN SMALL LETTER O: not included in any glyphset definition</li>
<li>U+0367 COMBINING LATIN SMALL LETTER U: not included in any glyphset definition</li>
<li>U+0368 COMBINING LATIN SMALL LETTER C: not included in any glyphset definition</li>
<li>U+0369 COMBINING LATIN SMALL LETTER D: not included in any glyphset definition</li>
<li>U+036A COMBINING LATIN SMALL LETTER H: not included in any glyphset definition</li>
<li>U+036B COMBINING LATIN SMALL LETTER M: not included in any glyphset definition</li>
<li>U+036C COMBINING LATIN SMALL LETTER R: not included in any glyphset definition</li>
<li>U+036D COMBINING LATIN SMALL LETTER T: not included in any glyphset definition</li>
<li>U+036E COMBINING LATIN SMALL LETTER V: not included in any glyphset definition</li>
<li>U+036F COMBINING LATIN SMALL LETTER X: not included in any glyphset definition</li>
<li>U+1AB0 COMBINING DOUBLED CIRCUMFLEX ACCENT: not included in any glyphset definition</li>
<li>U+1AB1 COMBINING DIAERESIS-RING: not included in any glyphset definition</li>
<li>U+1AB2 COMBINING INFINITY: not included in any glyphset definition</li>
<li>U+1AB3 COMBINING DOWNWARDS ARROW: not included in any glyphset definition</li>
<li>U+1AB4 COMBINING TRIPLE DOT: not included in any glyphset definition</li>
<li>U+1AB5 COMBINING X-X BELOW: not included in any glyphset definition</li>
<li>U+1AB6 COMBINING WIGGLY LINE BELOW: not included in any glyphset definition</li>
<li>U+1AB7 COMBINING OPEN MARK BELOW: not included in any glyphset definition</li>
<li>U+1AB8 COMBINING DOUBLE OPEN MARK BELOW: not included in any glyphset definition</li>
<li>U+1AB9 COMBINING LIGHT CENTRALIZATION STROKE BELOW: not included in any glyphset definition</li>
<li>U+1ABA COMBINING STRONG CENTRALIZATION STROKE BELOW: not included in any glyphset definition</li>
<li>U+1ABB COMBINING PARENTHESES ABOVE: not included in any glyphset definition</li>
<li>U+1ABC COMBINING DOUBLE PARENTHESES ABOVE: not included in any glyphset definition</li>
<li>U+1ABD COMBINING PARENTHESES BELOW: not included in any glyphset definition</li>
<li>U+1ABE COMBINING PARENTHESES OVERLAY: not included in any glyphset definition</li>
<li>U+1ABF COMBINING LATIN SMALL LETTER W BELOW: not included in any glyphset definition</li>
<li>U+1AC0 COMBINING LATIN SMALL LETTER TURNED W BELOW: not included in any glyphset definition</li>
<li>U+1AC5 COMBINING SQUARE BRACKETS ABOVE: not included in any glyphset definition</li>
<li>U+1AC7 COMBINING INVERTED DOUBLE ARCH ABOVE: not included in any glyphset definition</li>
<li>U+1AC8 COMBINING PLUS SIGN ABOVE: not included in any glyphset definition</li>
<li>U+1AC9 COMBINING DOUBLE PLUS SIGN ABOVE: not included in any glyphset definition</li>
<li>U+1ACA COMBINING DOUBLE PLUS SIGN BELOW: not included in any glyphset definition</li>
<li>U+1ACB COMBINING TRIPLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+1ACC COMBINING LATIN SMALL LETTER INSULAR G: not included in any glyphset definition</li>
<li>U+1ACD COMBINING LATIN SMALL LETTER INSULAR R: not included in any glyphset definition</li>
<li>U+1ACE COMBINING LATIN SMALL LETTER INSULAR T: not included in any glyphset definition</li>
<li>U+1DC0 COMBINING DOTTED GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+1DC1 COMBINING DOTTED ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+1DC2 COMBINING SNAKE BELOW: not included in any glyphset definition</li>
<li>U+1DC3 COMBINING SUSPENSION MARK: not included in any glyphset definition</li>
<li>U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition</li>
<li>U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition</li>
<li>U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition</li>
<li>U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition</li>
<li>U+1DC8 COMBINING GRAVE-ACUTE-GRAVE: not included in any glyphset definition</li>
<li>U+1DC9 COMBINING ACUTE-GRAVE-ACUTE: not included in any glyphset definition</li>
<li>U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition</li>
<li>U+1DCB COMBINING BREVE-MACRON: not included in any glyphset definition</li>
<li>U+1DCC COMBINING MACRON-BREVE: not included in any glyphset definition</li>
<li>U+1DCD COMBINING DOUBLE CIRCUMFLEX ABOVE: try adding coptic</li>
<li>U+1DCE COMBINING OGONEK ABOVE: not included in any glyphset definition</li>
<li>U+1DCF COMBINING ZIGZAG BELOW: not included in any glyphset definition</li>
<li>U+1DD0 COMBINING IS BELOW: not included in any glyphset definition</li>
<li>U+1DD1 COMBINING UR ABOVE: not included in any glyphset definition</li>
<li>U+1DD2 COMBINING US ABOVE: not included in any glyphset definition</li>
<li>U+1DD3 COMBINING LATIN SMALL LETTER FLATTENED OPEN A ABOVE: not included in any glyphset definition</li>
<li>U+1DD4 COMBINING LATIN SMALL LETTER AE: not included in any glyphset definition</li>
<li>U+1DD5 COMBINING LATIN SMALL LETTER AO: not included in any glyphset definition</li>
<li>U+1DD6 COMBINING LATIN SMALL LETTER AV: not included in any glyphset definition</li>
<li>U+1DD7 COMBINING LATIN SMALL LETTER C CEDILLA: not included in any glyphset definition</li>
<li>U+1DD8 COMBINING LATIN SMALL LETTER INSULAR D: not included in any glyphset definition</li>
<li>U+1DD9 COMBINING LATIN SMALL LETTER ETH: not included in any glyphset definition</li>
<li>U+1DDA COMBINING LATIN SMALL LETTER G: not included in any glyphset definition</li>
<li>U+1DDB COMBINING LATIN LETTER SMALL CAPITAL G: not included in any glyphset definition</li>
<li>U+1DDC COMBINING LATIN SMALL LETTER K: not included in any glyphset definition</li>
<li>U+1DDD COMBINING LATIN SMALL LETTER L: not included in any glyphset definition</li>
<li>U+1DDE COMBINING LATIN LETTER SMALL CAPITAL L: not included in any glyphset definition</li>
<li>U+1DDF COMBINING LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition</li>
<li>U+1DE0 COMBINING LATIN SMALL LETTER N: not included in any glyphset definition</li>
<li>U+1DE1 COMBINING LATIN LETTER SMALL CAPITAL N: not included in any glyphset definition</li>
<li>U+1DE2 COMBINING LATIN LETTER SMALL CAPITAL R: not included in any glyphset definition</li>
<li>U+1DE3 COMBINING LATIN SMALL LETTER R ROTUNDA: not included in any glyphset definition</li>
<li>U+1DE4 COMBINING LATIN SMALL LETTER S: not included in any glyphset definition</li>
<li>U+1DE5 COMBINING LATIN SMALL LETTER LONG S: not included in any glyphset definition</li>
<li>U+1DE6 COMBINING LATIN SMALL LETTER Z: not included in any glyphset definition</li>
<li>U+1DE7 COMBINING LATIN SMALL LETTER ALPHA: not included in any glyphset definition</li>
<li>U+1DE8 COMBINING LATIN SMALL LETTER B: not included in any glyphset definition</li>
<li>U+1DE9 COMBINING LATIN SMALL LETTER BETA: not included in any glyphset definition</li>
<li>U+1DEA COMBINING LATIN SMALL LETTER SCHWA: not included in any glyphset definition</li>
<li>U+1DEB COMBINING LATIN SMALL LETTER F: not included in any glyphset definition</li>
<li>U+1DEC COMBINING LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+1DED COMBINING LATIN SMALL LETTER O WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition</li>
<li>U+1DEE COMBINING LATIN SMALL LETTER P: not included in any glyphset definition</li>
<li>U+1DEF COMBINING LATIN SMALL LETTER ESH: not included in any glyphset definition</li>
<li>U+1DF0 COMBINING LATIN SMALL LETTER U WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition</li>
<li>U+1DF1 COMBINING LATIN SMALL LETTER W: not included in any glyphset definition</li>
<li>U+1DF2 COMBINING LATIN SMALL LETTER A WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF3 COMBINING LATIN SMALL LETTER O WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF4 COMBINING LATIN SMALL LETTER U WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF5 COMBINING UP TACK ABOVE: not included in any glyphset definition</li>
<li>U+1DF6 COMBINING KAVYKA ABOVE RIGHT: not included in any glyphset definition</li>
<li>U+1DF7 COMBINING KAVYKA ABOVE LEFT: not included in any glyphset definition</li>
<li>U+1DF8 COMBINING DOT ABOVE LEFT: try adding syriac</li>
<li>U+1DF9 COMBINING WIDE INVERTED BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+1DFB COMBINING DELETION MARK: try adding newa</li>
<li>U+1DFC COMBINING DOUBLE INVERTED BREVE BELOW: not included in any glyphset definition</li>
<li>U+1DFD COMBINING ALMOST EQUAL TO BELOW: not included in any glyphset definition</li>
<li>U+1DFE COMBINING LEFT ARROWHEAD ABOVE: not included in any glyphset definition</li>
<li>U+1DFF COMBINING RIGHT ARROWHEAD AND DOWN ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+2000 EN QUAD: try adding symbols2</li>
<li>U+2001 EM QUAD: try adding symbols2</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2004 THREE-PER-EM SPACE: try adding symbols2</li>
<li>U+2005 FOUR-PER-EM SPACE: try adding symbols2</li>
<li>U+2006 SIX-PER-EM SPACE: try adding symbols2</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+200A HAIR SPACE: try adding symbols2</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: thaana, nko, hebrew, syriac, arabic, phags-pa</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: thaana, nko, hebrew, syriac, phags-pa</li>
<li>U+2010 HYPHEN: try adding one of: lisu, yi, sundanese, armenian, hebrew, kayah-li, coptic, cham, kaithi, kharoshthi, arabic, syloti-nagri, sora-sompeng</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2028 LINE SEPARATOR: not included in any glyphset definition</li>
<li>U+2029 PARAGRAPH SEPARATOR: not included in any glyphset definition</li>
<li>U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition</li>
<li>U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition</li>
<li>U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition</li>
<li>U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition</li>
<li>U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: mongolian, yi, phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+2035 REVERSED PRIME: try adding math</li>
<li>U+2036 REVERSED DOUBLE PRIME: try adding math</li>
<li>U+2037 REVERSED TRIPLE PRIME: try adding math</li>
<li>U+2038 CARET: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+203F UNDERTIE: not included in any glyphset definition</li>
<li>U+2040 CHARACTER TIE: try adding math</li>
<li>U+2041 CARET INSERTION POINT: not included in any glyphset definition</li>
<li>U+2042 ASTERISM: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+204A TIRONIAN SIGN ET: not included in any glyphset definition</li>
<li>U+204B REVERSED PILCROW SIGN: not included in any glyphset definition</li>
<li>U+204C BLACK LEFTWARDS BULLET: not included in any glyphset definition</li>
<li>U+204D BLACK RIGHTWARDS BULLET: not included in any glyphset definition</li>
<li>U+204E LOW ASTERISK: not included in any glyphset definition</li>
<li>U+204F REVERSED SEMICOLON: try adding one of: arabic, adlam</li>
<li>U+2050 CLOSE UP: try adding math</li>
<li>U+2051 TWO ASTERISKS ALIGNED VERTICALLY: not included in any glyphset definition</li>
<li>U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition</li>
<li>U+2053 SWUNG DASH: try adding coptic</li>
<li>U+2054 INVERTED UNDERTIE: not included in any glyphset definition</li>
<li>U+2055 FLOWER PUNCTUATION MARK: try adding syloti-nagri</li>
<li>U+2056 THREE DOT PUNCTUATION: try adding coptic</li>
<li>U+2057 QUADRUPLE PRIME: try adding math</li>
<li>U+2058 FOUR DOT PUNCTUATION: try adding coptic</li>
<li>U+2059 FIVE DOT PUNCTUATION: try adding coptic</li>
<li>U+205A TWO DOT PUNCTUATION: try adding one of: old-hungarian, glagolitic, old-turkic, lycian, carian, georgian</li>
<li>U+205B FOUR DOT MARK: not included in any glyphset definition</li>
<li>U+205C DOTTED CROSS: not included in any glyphset definition</li>
<li>U+205D TRICOLON: try adding one of: carian, meroitic, old-hungarian, meroitic-hieroglyphs</li>
<li>U+205E VERTICAL FOUR DOTS: try adding old-hungarian</li>
<li>U+205F MEDIUM MATHEMATICAL SPACE: try adding math</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2061 FUNCTION APPLICATION: not included in any glyphset definition</li>
<li>U+2062 INVISIBLE TIMES: not included in any glyphset definition</li>
<li>U+2063 INVISIBLE SEPARATOR: not included in any glyphset definition</li>
<li>U+2064 INVISIBLE PLUS: not included in any glyphset definition</li>
<li>U+2066 LEFT-TO-RIGHT ISOLATE: not included in any glyphset definition</li>
<li>U+2067 RIGHT-TO-LEFT ISOLATE: not included in any glyphset definition</li>
<li>U+2068 FIRST STRONG ISOLATE: not included in any glyphset definition</li>
<li>U+2069 POP DIRECTIONAL ISOLATE: not included in any glyphset definition</li>
<li>U+206A INHIBIT SYMMETRIC SWAPPING: not included in any glyphset definition</li>
<li>U+206B ACTIVATE SYMMETRIC SWAPPING: not included in any glyphset definition</li>
<li>U+206C INHIBIT ARABIC FORM SHAPING: not included in any glyphset definition</li>
<li>U+206D ACTIVATE ARABIC FORM SHAPING: not included in any glyphset definition</li>
<li>U+206E NATIONAL DIGIT SHAPES: not included in any glyphset definition</li>
<li>U+206F NOMINAL DIGIT SHAPES: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2102 DOUBLE-STRUCK CAPITAL C: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+2104 CENTRE LINE SYMBOL: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2107 EULER CONSTANT: try adding math</li>
<li>U+2108 SCRUPLE: try adding math</li>
<li>U+2109 DEGREE FAHRENHEIT: try adding math</li>
<li>U+210A SCRIPT SMALL G: try adding math</li>
<li>U+210B SCRIPT CAPITAL H: try adding math</li>
<li>U+210C BLACK-LETTER CAPITAL H: try adding math</li>
<li>U+210D DOUBLE-STRUCK CAPITAL H: try adding math</li>
<li>U+210E PLANCK CONSTANT: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2110 SCRIPT CAPITAL I: try adding math</li>
<li>U+2111 BLACK-LETTER CAPITAL I: try adding math</li>
<li>U+2112 SCRIPT CAPITAL L: try adding math</li>
<li>U+2114 L B BAR SYMBOL: try adding math</li>
<li>U+2115 DOUBLE-STRUCK CAPITAL N: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2118 SCRIPT CAPITAL P: try adding math</li>
<li>U+2119 DOUBLE-STRUCK CAPITAL P: try adding math</li>
<li>U+211A DOUBLE-STRUCK CAPITAL Q: try adding math</li>
<li>U+211B SCRIPT CAPITAL R: try adding math</li>
<li>U+211C BLACK-LETTER CAPITAL R: try adding math</li>
<li>U+211D DOUBLE-STRUCK CAPITAL R: try adding math</li>
<li>U+211E PRESCRIPTION TAKE: try adding math</li>
<li>U+211F RESPONSE: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2121 TELEPHONE SIGN: try adding math</li>
<li>U+2123 VERSICLE: try adding math</li>
<li>U+2124 DOUBLE-STRUCK CAPITAL Z: try adding math</li>
<li>U+2125 OUNCE SIGN: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+2128 BLACK-LETTER CAPITAL Z: try adding math</li>
<li>U+2129 TURNED GREEK SMALL LETTER IOTA: try adding math</li>
<li>U+212A KELVIN SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+212C SCRIPT CAPITAL B: try adding math</li>
<li>U+212D BLACK-LETTER CAPITAL C: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+212F SCRIPT SMALL E: try adding math</li>
<li>U+2130 SCRIPT CAPITAL E: try adding math</li>
<li>U+2131 SCRIPT CAPITAL F: try adding math</li>
<li>U+2132 TURNED CAPITAL F: try adding math</li>
<li>U+2133 SCRIPT CAPITAL M: try adding math</li>
<li>U+2134 SCRIPT SMALL O: try adding math</li>
<li>U+2135 ALEF SYMBOL: try adding math</li>
<li>U+2136 BET SYMBOL: try adding math</li>
<li>U+2137 GIMEL SYMBOL: try adding math</li>
<li>U+2138 DALET SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+213A ROTATED CAPITAL Q: try adding math</li>
<li>U+213B FACSIMILE SIGN: try adding math</li>
<li>U+213C DOUBLE-STRUCK SMALL PI: try adding math</li>
<li>U+213D DOUBLE-STRUCK SMALL GAMMA: try adding math</li>
<li>U+213E DOUBLE-STRUCK CAPITAL GAMMA: try adding math</li>
<li>U+213F DOUBLE-STRUCK CAPITAL PI: try adding math</li>
<li>U+2140 DOUBLE-STRUCK N-ARY SUMMATION: try adding math</li>
<li>U+2141 TURNED SANS-SERIF CAPITAL G: try adding math</li>
<li>U+2142 TURNED SANS-SERIF CAPITAL L: try adding math</li>
<li>U+2143 REVERSED SANS-SERIF CAPITAL L: try adding math</li>
<li>U+2144 TURNED SANS-SERIF CAPITAL Y: try adding math</li>
<li>U+2145 DOUBLE-STRUCK ITALIC CAPITAL D: try adding math</li>
<li>U+2146 DOUBLE-STRUCK ITALIC SMALL D: try adding math</li>
<li>U+2147 DOUBLE-STRUCK ITALIC SMALL E: try adding math</li>
<li>U+2148 DOUBLE-STRUCK ITALIC SMALL I: try adding math</li>
<li>U+2149 DOUBLE-STRUCK ITALIC SMALL J: try adding math</li>
<li>U+214A PROPERTY LINE: try adding math</li>
<li>U+214B TURNED AMPERSAND: try adding math</li>
<li>U+214C PER SIGN: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+214E TURNED SMALL F: try adding math</li>
<li>U+214F SYMBOL FOR SAMARITAN SOURCE: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2184 LATIN SMALL LETTER REVERSED C: not included in any glyphset definition</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2E00 RIGHT ANGLE SUBSTITUTION MARKER: not included in any glyphset definition</li>
<li>U+2E01 RIGHT ANGLE DOTTED SUBSTITUTION MARKER: not included in any glyphset definition</li>
<li>U+2E02 LEFT SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E03 RIGHT SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E04 LEFT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E05 RIGHT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E06 RAISED INTERPOLATION MARKER: not included in any glyphset definition</li>
<li>U+2E07 RAISED DOTTED INTERPOLATION MARKER: not included in any glyphset definition</li>
<li>U+2E08 DOTTED TRANSPOSITION MARKER: not included in any glyphset definition</li>
<li>U+2E09 LEFT TRANSPOSITION BRACKET: not included in any glyphset definition</li>
<li>U+2E0A RIGHT TRANSPOSITION BRACKET: not included in any glyphset definition</li>
<li>U+2E0B RAISED SQUARE: not included in any glyphset definition</li>
<li>U+2E0C LEFT RAISED OMISSION BRACKET: not included in any glyphset definition</li>
<li>U+2E0D RIGHT RAISED OMISSION BRACKET: not included in any glyphset definition</li>
<li>U+2E0E EDITORIAL CORONIS: not included in any glyphset definition</li>
<li>U+2E0F PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E10 FORKED PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E11 REVERSED FORKED PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E12 HYPODIASTOLE: not included in any glyphset definition</li>
<li>U+2E13 DOTTED OBELOS: not included in any glyphset definition</li>
<li>U+2E14 DOWNWARDS ANCORA: not included in any glyphset definition</li>
<li>U+2E15 UPWARDS ANCORA: not included in any glyphset definition</li>
<li>U+2E16 DOTTED RIGHT-POINTING ANGLE: not included in any glyphset definition</li>
<li>U+2E17 DOUBLE OBLIQUE HYPHEN: try adding coptic</li>
<li>U+2E18 INVERTED INTERROBANG: not included in any glyphset definition</li>
<li>U+2E19 PALM BRANCH: not included in any glyphset definition</li>
<li>U+2E1A HYPHEN WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+2E1B TILDE WITH RING ABOVE: not included in any glyphset definition</li>
<li>U+2E1C LEFT LOW PARAPHRASE BRACKET: try adding nko</li>
<li>U+2E1D RIGHT LOW PARAPHRASE BRACKET: try adding nko</li>
<li>U+2E1E TILDE WITH DOT ABOVE: not included in any glyphset definition</li>
<li>U+2E1F TILDE WITH DOT BELOW: not included in any glyphset definition</li>
<li>U+2E20 LEFT VERTICAL BAR WITH QUILL: not included in any glyphset definition</li>
<li>U+2E21 RIGHT VERTICAL BAR WITH QUILL: not included in any glyphset definition</li>
<li>U+2E22 TOP LEFT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E23 TOP RIGHT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E24 BOTTOM LEFT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E25 BOTTOM RIGHT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E26 LEFT SIDEWAYS U BRACKET: not included in any glyphset definition</li>
<li>U+2E27 RIGHT SIDEWAYS U BRACKET: not included in any glyphset definition</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E2A TWO DOTS OVER ONE DOT PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2B ONE DOT OVER TWO DOTS PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2C SQUARED FOUR DOT PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2D FIVE DOT MARK: not included in any glyphset definition</li>
<li>U+2E2E REVERSED QUESTION MARK: not included in any glyphset definition</li>
<li>U+2E2F VERTICAL TILDE: not included in any glyphset definition</li>
<li>U+2E30 RING POINT: try adding one of: old-turkic, avestan</li>
<li>U+2E31 WORD SEPARATOR MIDDLE DOT: try adding one of: samaritan, old-hungarian, lydian, kaithi, avestan, carian, georgian</li>
<li>U+2E32 TURNED COMMA: not included in any glyphset definition</li>
<li>U+2E33 RAISED DOT: try adding coptic</li>
<li>U+2E34 RAISED COMMA: try adding coptic</li>
<li>U+2E35 TURNED SEMICOLON: not included in any glyphset definition</li>
<li>U+2E36 DAGGER WITH LEFT GUARD: not included in any glyphset definition</li>
<li>U+2E37 DAGGER WITH RIGHT GUARD: not included in any glyphset definition</li>
<li>U+2E38 TURNED DAGGER: not included in any glyphset definition</li>
<li>U+2E39 TOP HALF SECTION SIGN: not included in any glyphset definition</li>
<li>U+2E3A TWO-EM DASH: not included in any glyphset definition</li>
<li>U+2E3B THREE-EM DASH: not included in any glyphset definition</li>
<li>U+2E3C STENOGRAPHIC FULL STOP: try adding duployan</li>
<li>U+2E3D VERTICAL SIX DOTS: not included in any glyphset definition</li>
<li>U+2E3E WIGGLY VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2E3F CAPITULUM: not included in any glyphset definition</li>
<li>U+2E40 DOUBLE HYPHEN: not included in any glyphset definition</li>
<li>U+2E41 REVERSED COMMA: try adding one of: old-hungarian, arabic, adlam</li>
<li>U+2E42 DOUBLE LOW-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2E43 DASH WITH LEFT UPTURN: try adding glagolitic</li>
<li>U+2E44 DOUBLE SUSPENSION MARK: not included in any glyphset definition</li>
<li>U+2E45 INVERTED LOW KAVYKA: not included in any glyphset definition</li>
<li>U+2E46 INVERTED LOW KAVYKA WITH KAVYKA ABOVE: not included in any glyphset definition</li>
<li>U+2E47 LOW KAVYKA: not included in any glyphset definition</li>
<li>U+2E48 LOW KAVYKA WITH DOT: not included in any glyphset definition</li>
<li>U+2E49 DOUBLE STACKED COMMA: not included in any glyphset definition</li>
<li>U+2E4A DOTTED SOLIDUS: not included in any glyphset definition</li>
<li>U+2E4B TRIPLE DAGGER: not included in any glyphset definition</li>
<li>U+2E4C MEDIEVAL COMMA: not included in any glyphset definition</li>
<li>U+2E4D PARAGRAPHUS MARK: not included in any glyphset definition</li>
<li>U+2E4E PUNCTUS ELEVATUS MARK: not included in any glyphset definition</li>
<li>U+2E4F CORNISH VERSE DIVIDER: not included in any glyphset definition</li>
<li>U+2E50 CROSS PATTY WITH RIGHT CROSSBAR: not included in any glyphset definition</li>
<li>U+2E51 CROSS PATTY WITH LEFT CROSSBAR: not included in any glyphset definition</li>
<li>U+2E52 TIRONIAN SIGN CAPITAL ET: not included in any glyphset definition</li>
<li>U+2E53 MEDIEVAL EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+2E54 MEDIEVAL QUESTION MARK: not included in any glyphset definition</li>
<li>U+2E55 LEFT SQUARE BRACKET WITH STROKE: not included in any glyphset definition</li>
<li>U+2E56 RIGHT SQUARE BRACKET WITH STROKE: not included in any glyphset definition</li>
<li>U+2E57 LEFT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition</li>
<li>U+2E58 RIGHT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition</li>
<li>U+2E59 TOP HALF LEFT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5A TOP HALF RIGHT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5B BOTTOM HALF LEFT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5C BOTTOM HALF RIGHT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5D OBLIQUE HYPHEN: not included in any glyphset definition</li>
<li>U+A700 MODIFIER LETTER CHINESE TONE YIN PING: not included in any glyphset definition</li>
<li>U+A701 MODIFIER LETTER CHINESE TONE YANG PING: not included in any glyphset definition</li>
<li>U+A702 MODIFIER LETTER CHINESE TONE YIN SHANG: not included in any glyphset definition</li>
<li>U+A703 MODIFIER LETTER CHINESE TONE YANG SHANG: not included in any glyphset definition</li>
<li>U+A704 MODIFIER LETTER CHINESE TONE YIN QU: not included in any glyphset definition</li>
<li>U+A705 MODIFIER LETTER CHINESE TONE YANG QU: not included in any glyphset definition</li>
<li>U+A706 MODIFIER LETTER CHINESE TONE YIN RU: not included in any glyphset definition</li>
<li>U+A707 MODIFIER LETTER CHINESE TONE YANG RU: not included in any glyphset definition</li>
<li>U+A708 MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A709 MODIFIER LETTER HIGH DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70A MODIFIER LETTER MID DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70B MODIFIER LETTER LOW DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70C MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70D MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A70E MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A70F MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A710 MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A711 MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A712 MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A713 MODIFIER LETTER HIGH LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A714 MODIFIER LETTER MID LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A715 MODIFIER LETTER LOW LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A716 MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A717 MODIFIER LETTER DOT VERTICAL BAR: not included in any glyphset definition</li>
<li>U+A718 MODIFIER LETTER DOT SLASH: not included in any glyphset definition</li>
<li>U+A719 MODIFIER LETTER DOT HORIZONTAL BAR: not included in any glyphset definition</li>
<li>U+A71A MODIFIER LETTER LOWER RIGHT CORNER ANGLE: not included in any glyphset definition</li>
<li>U+A71B MODIFIER LETTER RAISED UP ARROW: not included in any glyphset definition</li>
<li>U+A71C MODIFIER LETTER RAISED DOWN ARROW: not included in any glyphset definition</li>
<li>U+A71D MODIFIER LETTER RAISED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A71E MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A71F MODIFIER LETTER LOW INVERTED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A92E KAYAH LI SIGN CWI: try adding one of: kayah-li, myanmar</li>
<li>U+AB30 LATIN SMALL LETTER BARRED ALPHA: not included in any glyphset definition</li>
<li>U+AB31 LATIN SMALL LETTER A REVERSED-SCHWA: not included in any glyphset definition</li>
<li>U+AB32 LATIN SMALL LETTER BLACKLETTER E: not included in any glyphset definition</li>
<li>U+AB33 LATIN SMALL LETTER BARRED E: not included in any glyphset definition</li>
<li>U+AB34 LATIN SMALL LETTER E WITH FLOURISH: not included in any glyphset definition</li>
<li>U+AB35 LATIN SMALL LETTER LENIS F: not included in any glyphset definition</li>
<li>U+AB36 LATIN SMALL LETTER SCRIPT G WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB37 LATIN SMALL LETTER L WITH INVERTED LAZY S: not included in any glyphset definition</li>
<li>U+AB38 LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB39 LATIN SMALL LETTER L WITH MIDDLE RING: not included in any glyphset definition</li>
<li>U+AB3A LATIN SMALL LETTER M WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3B LATIN SMALL LETTER N WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3C LATIN SMALL LETTER ENG WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3D LATIN SMALL LETTER BLACKLETTER O: not included in any glyphset definition</li>
<li>U+AB3E LATIN SMALL LETTER BLACKLETTER O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB3F LATIN SMALL LETTER OPEN O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB40 LATIN SMALL LETTER INVERTED OE: not included in any glyphset definition</li>
<li>U+AB41 LATIN SMALL LETTER TURNED OE WITH STROKE: not included in any glyphset definition</li>
<li>U+AB42 LATIN SMALL LETTER TURNED OE WITH HORIZONTAL STROKE: not included in any glyphset definition</li>
<li>U+AB43 LATIN SMALL LETTER TURNED O OPEN-O: not included in any glyphset definition</li>
<li>U+AB44 LATIN SMALL LETTER TURNED O OPEN-O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB45 LATIN SMALL LETTER STIRRUP R: not included in any glyphset definition</li>
<li>U+AB46 LATIN LETTER SMALL CAPITAL R WITH RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB47 LATIN SMALL LETTER R WITHOUT HANDLE: not included in any glyphset definition</li>
<li>U+AB48 LATIN SMALL LETTER DOUBLE R: not included in any glyphset definition</li>
<li>U+AB49 LATIN SMALL LETTER R WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB4A LATIN SMALL LETTER DOUBLE R WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB4B LATIN SMALL LETTER SCRIPT R: not included in any glyphset definition</li>
<li>U+AB4C LATIN SMALL LETTER SCRIPT R WITH RING: not included in any glyphset definition</li>
<li>U+AB4D LATIN SMALL LETTER BASELINE ESH: not included in any glyphset definition</li>
<li>U+AB4E LATIN SMALL LETTER U WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB4F LATIN SMALL LETTER U BAR WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB50 LATIN SMALL LETTER UI: not included in any glyphset definition</li>
<li>U+AB51 LATIN SMALL LETTER TURNED UI: not included in any glyphset definition</li>
<li>U+AB52 LATIN SMALL LETTER U WITH LEFT HOOK: not included in any glyphset definition</li>
<li>U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition</li>
<li>U+AB54 LATIN SMALL LETTER CHI WITH LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB55 LATIN SMALL LETTER CHI WITH LOW LEFT SERIF: not included in any glyphset definition</li>
<li>U+AB56 LATIN SMALL LETTER X WITH LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB57 LATIN SMALL LETTER X WITH LONG LEFT LEG: not included in any glyphset definition</li>
<li>U+AB58 LATIN SMALL LETTER X WITH LONG LEFT LEG AND LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB59 LATIN SMALL LETTER X WITH LONG LEFT LEG WITH SERIF: not included in any glyphset definition</li>
<li>U+AB5A LATIN SMALL LETTER Y WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB5B MODIFIER BREVE WITH INVERTED BREVE: not included in any glyphset definition</li>
<li>U+AB5C MODIFIER LETTER SMALL HENG: not included in any glyphset definition</li>
<li>U+AB5D MODIFIER LETTER SMALL L WITH INVERTED LAZY S: not included in any glyphset definition</li>
<li>U+AB5E MODIFIER LETTER SMALL L WITH MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB5F MODIFIER LETTER SMALL U WITH LEFT HOOK: not included in any glyphset definition</li>
<li>U+AB60 LATIN SMALL LETTER SAKHA YAT: not included in any glyphset definition</li>
<li>U+AB61 LATIN SMALL LETTER IOTIFIED E: not included in any glyphset definition</li>
<li>U+AB62 LATIN SMALL LETTER OPEN OE: not included in any glyphset definition</li>
<li>U+AB63 LATIN SMALL LETTER UO: not included in any glyphset definition</li>
<li>U+AB64 LATIN SMALL LETTER INVERTED ALPHA: not included in any glyphset definition</li>
<li>U+AB65 GREEK LETTER SMALL CAPITAL OMEGA: not included in any glyphset definition</li>
<li>U+AB66 LATIN SMALL LETTER DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+AB67 LATIN SMALL LETTER TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+AB68 LATIN SMALL LETTER TURNED R WITH MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB69 MODIFIER LETTER SMALL TURNED W: not included in any glyphset definition</li>
<li>U+AB6A MODIFIER LETTER LEFT TACK: not included in any glyphset definition</li>
<li>U+AB6B MODIFIER LETTER RIGHT TACK: not included in any glyphset definition</li>
<li>U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition</li>
<li>U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition</li>
<li>U+FB05 LATIN SMALL LIGATURE LONG S T: not included in any glyphset definition</li>
<li>U+FB06 LATIN SMALL LIGATURE ST: not included in any glyphset definition</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, yi, phags-pa</li>
<li>U+FE20 COMBINING LIGATURE LEFT HALF: try adding caucasian-albanian</li>
<li>U+FE21 COMBINING LIGATURE RIGHT HALF: try adding caucasian-albanian</li>
<li>U+FE22 COMBINING DOUBLE TILDE LEFT HALF: try adding caucasian-albanian</li>
<li>U+FE23 COMBINING DOUBLE TILDE RIGHT HALF: try adding caucasian-albanian</li>
<li>U+FE24 COMBINING MACRON LEFT HALF: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE25 COMBINING MACRON RIGHT HALF: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE26 COMBINING CONJOINING MACRON: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE27 COMBINING LIGATURE LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE28 COMBINING LIGATURE RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE29 COMBINING TILDE LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2A COMBINING TILDE RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2B COMBINING MACRON LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2C COMBINING MACRON RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2D COMBINING CONJOINING MACRON BELOW: try adding caucasian-albanian</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+10780 MODIFIER LETTER SMALL CAPITAL AA: not included in any glyphset definition</li>
<li>U+10781 MODIFIER LETTER SUPERSCRIPT TRIANGULAR COLON: not included in any glyphset definition</li>
<li>U+10782 MODIFIER LETTER SUPERSCRIPT HALF TRIANGULAR COLON: not included in any glyphset definition</li>
<li>U+10783 MODIFIER LETTER SMALL AE: not included in any glyphset definition</li>
<li>U+10784 MODIFIER LETTER SMALL CAPITAL B: not included in any glyphset definition</li>
<li>U+10785 MODIFIER LETTER SMALL B WITH HOOK: not included in any glyphset definition</li>
<li>U+10787 MODIFIER LETTER SMALL DZ DIGRAPH: not included in any glyphset definition</li>
<li>U+10788 MODIFIER LETTER SMALL DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+10789 MODIFIER LETTER SMALL DZ DIGRAPH WITH CURL: not included in any glyphset definition</li>
<li>U+1078A MODIFIER LETTER SMALL DEZH DIGRAPH: not included in any glyphset definition</li>
<li>U+1078B MODIFIER LETTER SMALL D WITH TAIL: not included in any glyphset definition</li>
<li>U+1078C MODIFIER LETTER SMALL D WITH HOOK: not included in any glyphset definition</li>
<li>U+1078D MODIFIER LETTER SMALL D WITH HOOK AND TAIL: not included in any glyphset definition</li>
<li>U+1078E MODIFIER LETTER SMALL REVERSED E: not included in any glyphset definition</li>
<li>U+1078F MODIFIER LETTER SMALL CLOSED REVERSED OPEN E: not included in any glyphset definition</li>
<li>U+10790 MODIFIER LETTER SMALL FENG DIGRAPH: not included in any glyphset definition</li>
<li>U+10791 MODIFIER LETTER SMALL RAMS HORN: not included in any glyphset definition</li>
<li>U+10792 MODIFIER LETTER SMALL CAPITAL G: not included in any glyphset definition</li>
<li>U+10793 MODIFIER LETTER SMALL G WITH HOOK: not included in any glyphset definition</li>
<li>U+10794 MODIFIER LETTER SMALL CAPITAL G WITH HOOK: not included in any glyphset definition</li>
<li>U+10795 MODIFIER LETTER SMALL H WITH STROKE: not included in any glyphset definition</li>
<li>U+10796 MODIFIER LETTER SMALL CAPITAL H: not included in any glyphset definition</li>
<li>U+10797 MODIFIER LETTER SMALL HENG WITH HOOK: not included in any glyphset definition</li>
<li>U+10798 MODIFIER LETTER SMALL DOTLESS J WITH STROKE AND HOOK: not included in any glyphset definition</li>
<li>U+10799 MODIFIER LETTER SMALL LS DIGRAPH: not included in any glyphset definition</li>
<li>U+1079A MODIFIER LETTER SMALL LZ DIGRAPH: not included in any glyphset definition</li>
<li>U+1079B MODIFIER LETTER SMALL L WITH BELT: not included in any glyphset definition</li>
<li>U+1079C MODIFIER LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition</li>
<li>U+1079D MODIFIER LETTER SMALL L WITH RETROFLEX HOOK AND BELT: not included in any glyphset definition</li>
<li>U+1079E MODIFIER LETTER SMALL LEZH: not included in any glyphset definition</li>
<li>U+1079F MODIFIER LETTER SMALL LEZH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107A0 MODIFIER LETTER SMALL TURNED Y: not included in any glyphset definition</li>
<li>U+107A1 MODIFIER LETTER SMALL TURNED Y WITH BELT: not included in any glyphset definition</li>
<li>U+107A2 MODIFIER LETTER SMALL O WITH STROKE: not included in any glyphset definition</li>
<li>U+107A3 MODIFIER LETTER SMALL CAPITAL OE: not included in any glyphset definition</li>
<li>U+107A4 MODIFIER LETTER SMALL CLOSED OMEGA: not included in any glyphset definition</li>
<li>U+107A5 MODIFIER LETTER SMALL Q: not included in any glyphset definition</li>
<li>U+107A6 MODIFIER LETTER SMALL TURNED R WITH LONG LEG: not included in any glyphset definition</li>
<li>U+107A7 MODIFIER LETTER SMALL TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107A8 MODIFIER LETTER SMALL R WITH TAIL: not included in any glyphset definition</li>
<li>U+107A9 MODIFIER LETTER SMALL R WITH FISHHOOK: not included in any glyphset definition</li>
<li>U+107AA MODIFIER LETTER SMALL CAPITAL R: not included in any glyphset definition</li>
<li>U+107AB MODIFIER LETTER SMALL TC DIGRAPH WITH CURL: not included in any glyphset definition</li>
<li>U+107AC MODIFIER LETTER SMALL TS DIGRAPH: not included in any glyphset definition</li>
<li>U+107AD MODIFIER LETTER SMALL TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107AE MODIFIER LETTER SMALL TESH DIGRAPH: not included in any glyphset definition</li>
<li>U+107AF MODIFIER LETTER SMALL T WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107B0 MODIFIER LETTER SMALL V WITH RIGHT HOOK: not included in any glyphset definition</li>
<li>U+107B2 MODIFIER LETTER SMALL CAPITAL Y: not included in any glyphset definition</li>
<li>U+107B3 MODIFIER LETTER GLOTTAL STOP WITH STROKE: not included in any glyphset definition</li>
<li>U+107B4 MODIFIER LETTER REVERSED GLOTTAL STOP WITH STROKE: not included in any glyphset definition</li>
<li>U+107B5 MODIFIER LETTER BILABIAL CLICK: not included in any glyphset definition</li>
<li>U+107B6 MODIFIER LETTER DENTAL CLICK: not included in any glyphset definition</li>
<li>U+107B7 MODIFIER LETTER LATERAL CLICK: not included in any glyphset definition</li>
<li>U+107B8 MODIFIER LETTER ALVEOLAR CLICK: not included in any glyphset definition</li>
<li>U+107B9 MODIFIER LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107BA MODIFIER LETTER SMALL S WITH CURL: not included in any glyphset definition</li>
<li>U+1DF00 LATIN SMALL LETTER FENG DIGRAPH WITH TRILL: not included in any glyphset definition</li>
<li>U+1DF01 LATIN SMALL LETTER REVERSED SCRIPT G: not included in any glyphset definition</li>
<li>U+1DF02 LATIN LETTER SMALL CAPITAL TURNED G: not included in any glyphset definition</li>
<li>U+1DF03 LATIN SMALL LETTER REVERSED K: not included in any glyphset definition</li>
<li>U+1DF04 LATIN LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition</li>
<li>U+1DF05 LATIN SMALL LETTER LEZH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF06 LATIN SMALL LETTER TURNED Y WITH BELT: not included in any glyphset definition</li>
<li>U+1DF07 LATIN SMALL LETTER REVERSED ENG: not included in any glyphset definition</li>
<li>U+1DF08 LATIN SMALL LETTER TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF09 LATIN SMALL LETTER T WITH HOOK AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF0A LATIN LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF0B LATIN SMALL LETTER ESH WITH DOUBLE BAR: not included in any glyphset definition</li>
<li>U+1DF0C LATIN SMALL LETTER ESH WITH DOUBLE BAR AND CURL: not included in any glyphset definition</li>
<li>U+1DF0D LATIN SMALL LETTER TURNED T WITH CURL: not included in any glyphset definition</li>
<li>U+1DF0E LATIN LETTER INVERTED GLOTTAL STOP WITH CURL: not included in any glyphset definition</li>
<li>U+1DF0F LATIN LETTER STRETCHED C WITH CURL: not included in any glyphset definition</li>
<li>U+1DF10 LATIN LETTER SMALL CAPITAL TURNED K: not included in any glyphset definition</li>
<li>U+1DF11 LATIN SMALL LETTER L WITH FISHHOOK: not included in any glyphset definition</li>
<li>U+1DF12 LATIN SMALL LETTER DEZH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF13 LATIN SMALL LETTER L WITH BELT AND PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF14 LATIN SMALL LETTER ENG WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF15 LATIN SMALL LETTER TURNED R WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF16 LATIN SMALL LETTER R WITH FISHHOOK AND PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF17 LATIN SMALL LETTER TESH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF18 LATIN SMALL LETTER EZH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF19 LATIN SMALL LETTER DEZH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1A LATIN SMALL LETTER I WITH STROKE AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1B LATIN SMALL LETTER O WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1C LATIN SMALL LETTER TESH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1D LATIN SMALL LETTER C WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1E LATIN SMALL LETTER S WITH CURL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>devanagari</code>, <code>greek</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[15] NotoSans[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 508, but got 395 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Greek_Expert glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɤ̄, Ɤ̂, Ɤ́, Ɤ̏, Ɤ̋, Ɤ̀, Ɤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030F to .notdef when shaping the text 'Ɤ̏'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to .notdef when shaping the text 'Ɤ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0304 to .notdef when shaping the text 'Ɤ̄'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to .notdef when shaping the text 'Ɤ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030B to .notdef when shaping the text 'Ɤ̋'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to .notdef when shaping the text 'Ɤ̂'</td>
<td align="left">dnj_Latn (Dan)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɤ̂, Ɤ́, Ɤ, Ɤ̀</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to .notdef when shaping the text 'Ɤ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to .notdef when shaping the text 'Ɤ̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to .notdef when shaping the text 'Ɤ̀'</td>
<td align="left">gov_Latn (Goo)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uniA78D when shaping the text 'Ɥ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uniA78D when shaping the text 'Ɥ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uniA78D when shaping the text 'Ɥ̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA78D when shaping the text 'Ɥ̃̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uniA78D when shaping the text 'Ɥ̃́'</td>
<td align="left">dnj_Latn_LR (Liberian Dan)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Greek_Expert glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ſ' and shaping the text 'ſ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">de_Latn (German)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǥ' and shaping the text 'ǥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȟ' and shaping the text 'ȟ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǩ' and shaping the text 'ǩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǯ' and shaping the text 'ǯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ſ' and shaping the text 'ſ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fr_Latn (French)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lt_Latn (Lithuanian), sad_Latn (Sandawe), kbo_Latn (Keliko) and umb_Latn (Umbundu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nb_Latn (Norwegian Bokmål) and bkv_Latn (Bekwarra)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tr_Latn (Turkish)</td>
</tr>
<tr>
<td align="left">Small caps i should be dotted:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'i' with features: smcp and shaping the text 'i' in language 'tr' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tr_Latn (Turkish)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bm_Latn (Bambara), dyu_Latn (Dyula), bm_Latn (Bambara), bzx_Latn (Bozo, Hainyaxo), dyu_Latn (Dyula), sus_Latn (Susu), man_Latn (Mandingo), kqs_Latn (Kissi, Northern), mwk_Latn (Kita Maninkakan), dtm_Latn (Tomo Kan Dogon), myk_Latn (Mamara Senoufo), emk_Latn (Maninkakan, Eastern), dts_Latn (Dogon, Toro So), bwq_Latn (Southern Bobo Madaré) and boz_Latn (Tiéyaxo Bozo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fat_Latn (Fanti), tw_akuapem_Latn (Akuapem Twi), suq_Latn (Suri, Tirmaga-Chai), dga_Latn (Dagaare, Southern), ekm_Latn (Elip), cbj_Latn (Ede Cabe), saf_Latn (Safaliba), nym_Latn (Nyamwezi), idd_Latn (Ede Idaca), tw_akuapem_Latn (Akuapem Twi), fat_Latn (Fanti), ngb_Latn (Ngbandi, Northern), lok_Latn (Loko), ncu_Latn (Chumburung), mfq_Latn (Moba), agc_Latn (Agatu), bov_Latn (Tuwuli), bci_Latn (Baoulé), maw_Latn (Mampruli), nzi_Latn (Nzima), bba_Latn (Baatonum), utr_Latn (Etulo), etx_Latn (Iten), ica_Latn (Ede Ica), adj_Latn (Adioukrou), ada_Latn (Adangme), nfr_Latn (Nafaanra), lia_Latn (Limba, West-Central), tvu_Latn (Tunen), abr_Latn (Abron), mkl_Latn (Mokole), yas_Latn (Nugunu), sef_Latn (Cebaara Senoufo), ati_Latn (Attié), mym_Latn (Me’en), ijj_Latn (Ede Ije), lem_Latn (Nomaande), bhy_Latn (Bhele), ich_Latn (Etkywan), hag_Latn (Hanga), cko_Latn (Anufo), wwa_Latn (Waama), mfo_Latn (Mbe), nhb_Latn (Beng), mzw_Latn (Deg), cme_Latn (Cerma), xrb_Latn (Karaboro, Eastern), ntr_Latn (Delo), vag_Latn (Vagla), bet_Latn (Bété, Guiberoua), idu_Latn (Idoma), wan_Latn (Wan), bqp_Latn (Bisã), kez_Latn (Kukele), mur_Latn (Murle), kri_Latn (Krio), lig_Latn (Ligbi), mmu_Latn (Mmaala), ddn_Latn (Dendi), lu_Latn (Luba-Katanga), yba_Latn (Yala), men_Latn (Mende), gjn_Latn (Gonja), moa_Latn (Mwan) and guk_Latn (Gumuz)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ff_Latn (Fulah), fub_Latn (Fulfulde, Adamawa), daa_Latn (Dangaléat), fuc_Latn (Pulaar), sav_Latn (Saafi-Saafi), tnr_Latn (Ménik), ff_Latn (Fulah), djc_Latn (Dar Daju Daju), fuh_Latn (Fulfulde, Western Niger) and fue_Latn (Fulfulde, Borgu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ha_Latn (Hausa) and ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɵ' and shaping the text 'ɵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ig_Latn (Igbo) and ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yo_Latn (Yoruba) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ả' and shaping the text 'ả' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ằ' and shaping the text 'ằ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẳ' and shaping the text 'ẳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẵ' and shaping the text 'ẵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ắ' and shaping the text 'ắ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ặ' and shaping the text 'ặ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ầ' and shaping the text 'ầ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẩ' and shaping the text 'ẩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẫ' and shaping the text 'ẫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ấ' and shaping the text 'ấ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ậ' and shaping the text 'ậ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẻ' and shaping the text 'ẻ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ề' and shaping the text 'ề' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ể' and shaping the text 'ể' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ễ' and shaping the text 'ễ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ế' and shaping the text 'ế' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỉ' and shaping the text 'ỉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỏ' and shaping the text 'ỏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ồ' and shaping the text 'ồ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ổ' and shaping the text 'ổ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỗ' and shaping the text 'ỗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ố' and shaping the text 'ố' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ơ' and shaping the text 'ơ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ờ' and shaping the text 'ờ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ở' and shaping the text 'ở' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỡ' and shaping the text 'ỡ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ớ' and shaping the text 'ớ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ợ' and shaping the text 'ợ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ủ' and shaping the text 'ủ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ư' and shaping the text 'ư' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ừ' and shaping the text 'ừ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ử' and shaping the text 'ử' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ữ' and shaping the text 'ữ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ứ' and shaping the text 'ứ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ự' and shaping the text 'ự' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỷ' and shaping the text 'ỷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỵ' and shaping the text 'ỵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vi_Latn (Vietnamese)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">igb_Latn (Ebira) and ekp_Latn (Ekpeye)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kyq_Latn (Kenga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nmg_Latn (Kwasio)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nza_Latn (Tigon Mbembe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ahs_Latn (Ashe), bqv_Latn (Koro Wachi) and ldb_Latn (Duya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʈ' and shaping the text 'ʈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nus_Latn (Nuer)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snf_Latn (Noon) and fuq_Latn (Central-Eastern Niger Fulfulde)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tsw_Latn (Tsishingini) and kdl_Latn (Tsikimba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ồ' and shaping the text 'ồ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mg_Latn (Malagasy)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yam_Latn (Yamba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ybb_Latn (Yemba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aks_Latn (Akeselem) and kdh_Latn (Tem)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʈ' and shaping the text 'ʈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">luo_Latn (Luo) and ach_Latn (Acoli)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gng_Latn (Ngangam)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɂ' and shaping the text 'ɂ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mfd_Latn (Mendankwe-Nkwen)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mas_Latn (Masai), buu_Latn (Budu), niy_Latn (Ngiti), mdj_Latn (Mangbetu), teo_Latn (Teso) and kdj_Latn (Karamojong)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bev_Latn (Bété, Daloa), nko_Latn (Nkonya), nwb_Latn (Nyabwa), ted_Latn (Krumen, Tepo), sig_Latn (Paasaal), yre_Latn (Yaouré), god_Latn (Godié), wob_Latn (Wè Northern), kye_Latn (Krache), ade_Latn (Adele), gud_Latn (Dida, Yocoboué), sil_Latn (Sisaala, Tumulung) and lor_Latn (Téén)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dow_Latn (Doyayo), gmm_Latn (Gbaya-Mbodomo), dua_Latn (Duala), kkj_Latn (Kako) and bkc_Latn (Baka, Cameroon/Gabon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȁ' and shaping the text 'ȁ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǣ' and shaping the text 'ǣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȅ' and shaping the text 'ȅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȉ' and shaping the text 'ȉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȍ' and shaping the text 'ȍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɤ' and shaping the text 'ɤ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȕ' and shaping the text 'ȕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɯ' and shaping the text 'ɯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dnj_Latn (Dan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snw_Latn (Selee), dyi_Latn (Sénoufo, Djimini), anv_Latn (Denya) and tpm_Latn (Tampulma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">hia_Latn (Lamang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xsm_Latn (Kasem)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kus_Latn (Kusaal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǜ' and shaping the text 'ǜ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǘ' and shaping the text 'ǘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǚ' and shaping the text 'ǚ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǖ' and shaping the text 'ǖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bax_Latn (Bamun (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɪ' and shaping the text 'ɪ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞷ' and shaping the text 'ꞷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kzc_Latn (Bondoukou Kulango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">acd_Latn (Gikyode)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">swb_Latn (Maore Comorian, Latin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dag_Latn (Dagbani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tik_Latn (Tikar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dbd_Latn (Dadiya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ank_Latn (Goemai), pip_Latn (Pero), wja_Latn (Waja), wji_Latn (Warji) and tal_Latn (Tal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bbo_Latn (Northern Bobo Madaré) and nku_Latn (Kulango, Bouna)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bfd_Latn (Bafut)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nhu_Latn (Noone), yo_Latn_BJ (Yoruba, Benin) and bzw_Latn (Basa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">snk_Latn (Soninke) and kao_Latn (Xaasongaxango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dgi_Latn (Northern Dagara)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kzr_Latn (Karang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bze_Latn (Jenaama Bozo), msc_Latn (Maninka, Sankaran), shz_Latn (Syenara Senoufo), spp_Latn (Sénoufo, Supyire) and yal_Latn (Yalunka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">muy_Latn (Muyang) and maf_Latn (Mafa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgo_Latn (Metaʼ) and bum_Latn (Bulu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aha_Latn (Ahanta)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">goa_Latn (Guro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">did_Latn (Didinga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mcp_Latn (Makaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xuo_Latn (Kuo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sok_Latn (Sokoro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tuz_Latn (Turka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">les_Latn (Lese), led_Latn (Lendu), nzk_Latn (Nzakara) and lag_Latn (Langi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ee_Latn (Ewe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mhi_Latn (Ma’di)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xed_Latn (Hdi), dbq_Latn (Daba), gnd_Latn (Zulgo-Gemzek), mqb_Latn (Mbuko), gde_Latn (Gude), hig_Latn (Kamwe), yer_Latn (Tarok) and bwr_Latn (Bura-Pabir)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nuv_Latn (Nuni, Northern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pnz_Latn (Pana, Central African Republic)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sba_Latn (Ngambay)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ln_Latn (Lingala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ksf_Latn (Bafia)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sbd_Latn (Southern Samo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fod_Latn (Foodo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bjv_Latn (Bedjond)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">izz_Latn (Izii) and yaz_Latn (Lokaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ffm_Latn (Maasina Fulfulde)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dop_Latn (Lukpa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ktj_Latn (Krumen, Plapo), kyf_Latn (Kouya), any_Latn (Anyin), kvf_Latn (Kabalai) and naw_Latn (Nawuri)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tda_Latn (Tagdal)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dur_Latn (Dii)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʕ' and shaping the text 'ʕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tsb_Latn (Tsamai) and gwd_Latn (Gawwada)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mfi_Latn (Wandala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yay_Latn (Agwagwune), cla_Latn (Ron), fuv_Latn (Nigerian Fulfulde), asg_Latn (Cishingini), giz_Latn (Southern Giziga), enn_Latn (Engenni), ttr_Latn (Tera), mne_Latn (Naba) and bys_Latn (Burak)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƃ' and shaping the text 'ƃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lom_Latn (Loma, Liberia)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƈ' and shaping the text 'ƈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƥ' and shaping the text 'ƥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṕ' and shaping the text 'ṕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">srr_Latn (Serer)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcn_Latn (Bali)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sld_Latn (Sissala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgc_Latn (Morokodo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">meq_Latn (Merey) and pbi_Latn (Parkwa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƀ' and shaping the text 'ƀ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẑ' and shaping the text 'ẑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">buc_Latn (Bushi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʘ' and shaping the text 'ʘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ngh_Latn (Nǁng) and nmn_Latn (ǃXoon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">shi_Latn (Tachelhit (Latin)) and tzm_Latn (Central Atlas Tamazight)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ⓐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ⓐ</td>
<td align="left">kib_Latn (Koalib)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɽ' and shaping the text 'ɽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɐ' and shaping the text 'ɐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kib_Latn (Koalib)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dje_Latn (Zarma), twq_Latn (Tasawaq), ses_Latn (Koyraboro Senni) and khq_Latn (Koyra Chiini)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kst_Latn (Winyé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">eto_Latn (Eton, Cameroon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">abi_Latn (Abidji)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ndv_Latn (Ndut)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pil_Latn (Yom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mwm_Latn (Sar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɤ' and shaping the text 'ɤ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gov_Latn (Goo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">din_Latn (Dinka), bza_Latn (Bandi) and dip_Latn (Dinka, Northeastern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cky_Latn (Cakfem-Mushere) and sur_Latn (Mwaghavul)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pym_Latn (Pyam)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lgg_Latn (Lugbara)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gby_Latn (Gbari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȳ' and shaping the text 'ȳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mge_Latn (Mango)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">box_Latn (Buamu) and bwj_Latn (Láá Láá Bwamu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gkn_Latn (Gokana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">she_Latn (Sheko), beh_Latn (Biali) and lns_Latn (Lamnso’)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṳ' and shaping the text 'ṳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fan_Latn (Fang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ⱳ' and shaping the text 'ⱳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">pug_Latn (Phuie)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">guw_Latn (Gun) and ayb_Latn (Ayizo Gbe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kia_Latn (Kim)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ajg_Latn (Aja)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jab_Latn (Hyam) and btt_Latn (Bete-Bendi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ndz_Latn (Ndogo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">okr_Latn (Kirike), pkb_Latn (Pokomo) and ijs_Latn (Ijo, Southeast)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bbj_Latn (Ghomala)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">muh_Latn (Mündü), cdr_Latn (Kamuku) and png_Latn (Pangu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tmh_Latn (Tamashek)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">avn_Latn (Avatime)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꟈ' and shaping the text 'ꟈ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɽ' and shaping the text 'ɽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mor_Latn (Moro)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƹ' and shaping the text 'ƹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȓ' and shaping the text 'ȓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">rif_Latn (Riffian (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḯ' and shaping the text 'ḯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǘ' and shaping the text 'ǘ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bvi_Latn (Belanda Viri, Latin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṿ' and shaping the text 'ṿ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bdh_Latn (Baka, DRC/South Sudan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsq_Latn (Bassa (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǫ' and shaping the text 'ǫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gkp_Latn (Kpelle, Guinea)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dzg_Latn (Dazaga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ibb_Latn (Ibibio)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ⱳ' and shaping the text 'ⱳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lob_Latn (Lobi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɍ' and shaping the text 'ɍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kr_Latn (Kanuri), knc_Latn (Kanuri, Central) and kby_Latn (Kanuri, Manga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dya_Latn (Dyan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jbu_Latn (Jukun Takum)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bfo_Latn (Malba Birifor)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ife_Latn (Ifè)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">awc_Latn (Cicipu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɍ' and shaping the text 'ɍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mdt_Latn (Mbere)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dno_Latn (Ndrulo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ahl_Latn (Igo), fon_Latn (Fon) and tfi_Latn (Gbe, Tofin)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">neb_Latn (Toura)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cae_Latn (Lehar)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wib_Latn (Toussian, Southern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">etu_Latn (Ejagham)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gqr_Latn (Gor)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">buw_Latn (gevové)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nnw_Latn (Southern Nuni)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">anc_Latn (Ngas)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gej_Latn (Gen)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kai_Latn (Karekare)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcw_Latn (Bana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">agq_Latn (Aghem) and ken_Latn (Kenyang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsp_Latn (Baga Sitemu) and ksp_Latn (Kabba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kbp_Latn (Kabiyé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">keu_Latn (Akebu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">loq_Latn (Lobala) and mbo_Latn (Mbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bud_Latn (Ntcham), xon_Latn (Konkomba), bim_Latn (Bimoba) and mcu_Latn (Mambila, Cameroon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lol_Latn (Mongo) and krw_Latn (Western Krahn)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tcd_Latn (Tafi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ann_Latn (Obolo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mnf_Latn (Mundani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wci_Latn (Gbe, Waci)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kmy_Latn (Koma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƭ' and shaping the text 'ƭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẉ' and shaping the text 'ẉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ttq_Latn (Tawallammat Tamajaq)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gna_Latn (Kaansa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yav_Latn (Yangben)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">blo_Latn (Anii)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">byv_Latn (Medumba)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ckl_Latn (Kibaku)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bjt_Latn (Balanta-Ganja) and dgh_Latn (Dghwede)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṽ' and shaping the text 'ṽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mua_Latn (Mundang)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḓ' and shaping the text 'ḓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṋ' and shaping the text 'ṋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṱ' and shaping the text 'ṱ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">hz_Latn (Herero)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">las_Latn (Lama, Togo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ậ' and shaping the text 'ậ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">avu_Latn (Avokaya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ệ' and shaping the text 'ệ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ộ' and shaping the text 'ộ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ikw_Latn (Ikwere)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nnh_Latn (Ngiemboon)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mos_Latn (Mossi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȩ' and shaping the text 'ȩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vut_Latn (Vute)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ozm_Latn (Koonzime)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mda_Latn (Mada) and ewo_Latn (Ewondo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḕ' and shaping the text 'ḕ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">aeb_Latn (Tunisian Darija)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bkm_Latn (Kom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">sxw_Latn (Saxwe Gbe) and xwe_Latn (Gbe, Xwela)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jen_Latn (Dza)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bmq_Latn (Bomu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">knp_Latn (Kwanja)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mql_Latn (Mbelime) and ntm_Latn (Nateni)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">cou_Latn (Wamey)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gaa_Latn (Ga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṵ' and shaping the text 'ṵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mev_Latn (Mano)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṫ' and shaping the text 'ṫ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṡ' and shaping the text 'ṡ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḋ' and shaping the text 'ḋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȧ' and shaping the text 'ȧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḣ' and shaping the text 'ḣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">har_Latn (Harari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">iby_Latn (Ibani)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṇ' and shaping the text 'ṇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḳ' and shaping the text 'ḳ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tan_Latn (Tangale)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḵ' and shaping the text 'ḵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṯ' and shaping the text 'ṯ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẖ' and shaping the text 'ẖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">udu_Latn (Uduk)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">azo_Latn (Awing)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ᵽ' and shaping the text 'ᵽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bqj_Latn (Bandial)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɑ' and shaping the text 'ɑ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fmp_Latn (Fe’fe’)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">xsm_Latn_BF (Kasem, Burkina Faso)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mbu_Latn (Mbula-Bwazza)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɉ' and shaping the text 'ɉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsc_Latn_GN (Guinean Bassari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">biv_Latn (Birifor, Southern)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḓ' and shaping the text 'ḓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḽ' and shaping the text 'ḽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṋ' and shaping the text 'ṋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṱ' and shaping the text 'ṱ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ve_Latn (Venda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tbz_Latn (Ditammari) and bqc_Latn (Boko)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fuf_Latn (Pular)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nga_Latn (Ngbaka)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">yat_Latn (Yambeta) and tuq_Latn (Tedaga)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɵ' and shaping the text 'ɵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɥ' and shaping the text 'ɥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƃ' and shaping the text 'ƃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">dnj_Latn_LR (Liberian Dan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lee_Latn (Lyélé)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṉ' and shaping the text 'ṉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lnu_Latn (Longuda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lip_Latn (Sekpele)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">vai_Latn (Vai (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lmp_Latn (Limbum)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nin_Latn (Ninzo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">log_Latn (Logo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɠ' and shaping the text 'ɠ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tod_Latn (Toma)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƴ' and shaping the text 'ƴ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bsc_Latn (Bassari)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞵ' and shaping the text 'ꞵ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">puu_Latn (Punu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bss_Latn (Akoose)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kpo_Latn (Ikposo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḇ' and shaping the text 'ḇ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḏ' and shaping the text 'ḏ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mcn_Latn (Masana)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḭ' and shaping the text 'ḭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ỹ' and shaping the text 'ỹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">wok_Latn (Longto)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǰ' and shaping the text 'ǰ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʃ' and shaping the text 'ʃ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">taq_Latn (Tamasheq (Latin))</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">akp_Latn (Siwu)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nfu_Latn (Mfumte)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẋ' and shaping the text 'ẋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mey_Latn (Hassaniyya)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">lnl_Latn (South Central Banda)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kss_Latn (Southern Kisi)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ebo_Latn (Teke-Ebo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʝ' and shaping the text 'ʝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƙ' and shaping the text 'ƙ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">ikx_Latn (Ik)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bas_Latn (Basaa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bom_Latn (Berom)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṍ' and shaping the text 'ṍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">soy_Latn (Miyobe)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɖ' and shaping the text 'ɖ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ƒ' and shaping the text 'ƒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nyb_Latn (Nyangbo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kpe_Latn (Kpelle)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kqp_Latn (Kimré)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḷ' and shaping the text 'ḷ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">krs_Latn (Gbaya, Sudan)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bav_Latn (Vengo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gur_Latn (Frafra)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ạ' and shaping the text 'ạ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḅ' and shaping the text 'ḅ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">abn_Latn (Abua)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">gvl_Latn (Gulay)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bcy_Latn (Bacama)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṹ' and shaping the text 'ṹ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mzm_Latn (Mumuye)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɦ' and shaping the text 'ɦ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">nmz_Latn (Nawdm)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bex_Latn (Jur Modo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">mgd_Latn (Moru)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḛ' and shaping the text 'ḛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">grb_Latn (Grebo)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḍ' and shaping the text 'ḍ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɣ' and shaping the text 'ɣ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ḥ' and shaping the text 'ḥ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṛ' and shaping the text 'ṛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ṭ' and shaping the text 'ṭ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ẓ' and shaping the text 'ẓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">kab_Latn (Kabyle)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɓ' and shaping the text 'ɓ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɗ' and shaping the text 'ɗ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǝ' and shaping the text 'ǝ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jgk_Latn (Gwak)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɨ' and shaping the text 'ɨ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǒ' and shaping the text 'ǒ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">fvr_Latn (Fur)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɩ' and shaping the text 'ɩ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɲ' and shaping the text 'ɲ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʋ' and shaping the text 'ʋ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʊ' and shaping the text 'ʊ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">bib_Latn (Bissa)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʌ' and shaping the text 'ʌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ə' and shaping the text 'ə' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ȧ' and shaping the text 'ȧ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">tem_Latn (Timne)</td>
</tr>
<tr>
<td align="left">Small caps for Latin letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɛ' and shaping the text 'ɛ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǐ' and shaping the text 'ǐ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ɔ' and shaping the text 'ɔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ʉ' and shaping the text 'ʉ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ꞌ' and shaping the text 'ꞌ' with features: smcp, the output is expected to be different, but was the same</td>
<td align="left">jgo_Latn (Ngomba)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-article">googlefonts/description/has_article</a></summary>
    <div>







* 🔥 **FAIL** <p>This is a Noto font but it lacks an ARTICLE.en_us.html file.</p>
 [code: missing-article]



* 🔥 **FAIL** <p>This is a Noto font but it lacks a DESCRIPTION.en_us.html file.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- uni0334

- uni0335

- uni0336

- uni0337

- uni0338

- uni1ABE
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni031A (U+031A), uni1ACC (U+1ACC), uni1ACD (U+1ACD) and uni1ACE (U+1ACE)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#file-size">file_size</a></summary>
    <div>







* ⚠️ **WARN** <p>Font file is 2.0Mb; ideally it should be less than 1.0Mb</p>
 [code: large-font]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uniA729 (U+A729): L&lt;&lt;335.0,467.0&gt;--&lt;335.0,537.0&gt;&gt; has the same coordinates as a previous segment.

* uniA664 (U+A664): L&lt;&lt;601.0,0.0&gt;--&lt;511.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uniA665 (U+A665): L&lt;&lt;502.0,0.0&gt;--&lt;414.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni2E3B (U+2E3B): L&lt;&lt;1880.0,307.0&gt;--&lt;1880.0,229.0&gt;&gt; has the same coordinates as a previous segment.

* uni2E3B (U+2E3B): L&lt;&lt;960.0,307.0&gt;--&lt;960.0,229.0&gt;&gt; has the same coordinates as a previous segment.

* uni2E3A (U+2E3A): L&lt;&lt;960.0,307.0&gt;--&lt;960.0,229.0&gt;&gt; has the same coordinates as a previous segment.

* uni1DF11 (U+1DF11): L&lt;&lt;173.0,0.0&gt;--&lt;85.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _Comp_candraBindudeva.02

- _Comp_nga_Shortdeva

- _Comp_nukta_rakar_matradeva

- _Comp_rakar_matradeva

- dasiaoxia_macronmod

- dasiavaria_macronmod

- psilioxia_macronmod

- psilivaria_macronmod

- uni03C5030803060301

- uni0903.alt

- uni1FD8.salt

- uni1FD9.salt
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
kavykawithkavykaaboveinvertedlow</p>
 [code: legacy-long-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/NotoSans/googlefonts/variable-ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02CD MODIFIER LETTER LOW MACRON: try adding lisu</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, math, coptic</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: math, glagolitic, coptic, gothic, elbasan</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: tifinagh, math, hebrew, old-permic, coptic, syriac, todhri, malayalam, canadian-aboriginal, tai-le, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: math, sunuwar</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+0316 COMBINING GRAVE ACCENT BELOW: not included in any glyphset definition</li>
<li>U+0317 COMBINING ACUTE ACCENT BELOW: not included in any glyphset definition</li>
<li>U+0318 COMBINING LEFT TACK BELOW: not included in any glyphset definition</li>
<li>U+0319 COMBINING RIGHT TACK BELOW: not included in any glyphset definition</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+031C COMBINING LEFT HALF RING BELOW: not included in any glyphset definition</li>
<li>U+031D COMBINING UP TACK BELOW: not included in any glyphset definition</li>
<li>U+031E COMBINING DOWN TACK BELOW: not included in any glyphset definition</li>
<li>U+031F COMBINING PLUS SIGN BELOW: not included in any glyphset definition</li>
<li>U+0320 COMBINING MINUS SIGN BELOW: try adding syriac</li>
<li>U+0321 COMBINING PALATALIZED HOOK BELOW: not included in any glyphset definition</li>
<li>U+0322 COMBINING RETROFLEX HOOK BELOW: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: syriac, sunuwar</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, caucasian-albanian, sunuwar, syriac, cherokee, gothic, thai</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0333 COMBINING DOUBLE LOW LINE: try adding math</li>
<li>U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0339 COMBINING RIGHT HALF RING BELOW: not included in any glyphset definition</li>
<li>U+033A COMBINING INVERTED BRIDGE BELOW: try adding math</li>
<li>U+033B COMBINING SQUARE BELOW: not included in any glyphset definition</li>
<li>U+033C COMBINING SEAGULL BELOW: not included in any glyphset definition</li>
<li>U+033D COMBINING X ABOVE: not included in any glyphset definition</li>
<li>U+033E COMBINING VERTICAL TILDE: not included in any glyphset definition</li>
<li>U+033F COMBINING DOUBLE OVERLINE: try adding coptic</li>
<li>U+0340 COMBINING GRAVE TONE MARK: not included in any glyphset definition</li>
<li>U+0341 COMBINING ACUTE TONE MARK: not included in any glyphset definition</li>
<li>U+0342 COMBINING GREEK PERISPOMENI: not included in any glyphset definition</li>
<li>U+0343 COMBINING GREEK KORONIS: not included in any glyphset definition</li>
<li>U+0344 COMBINING GREEK DIALYTIKA TONOS: not included in any glyphset definition</li>
<li>U+0345 COMBINING GREEK YPOGEGRAMMENI: not included in any glyphset definition</li>
<li>U+0346 COMBINING BRIDGE ABOVE: try adding math</li>
<li>U+0347 COMBINING EQUALS SIGN BELOW: not included in any glyphset definition</li>
<li>U+0348 COMBINING DOUBLE VERTICAL LINE BELOW: not included in any glyphset definition</li>
<li>U+0349 COMBINING LEFT ANGLE BELOW: not included in any glyphset definition</li>
<li>U+034A COMBINING NOT TILDE ABOVE: not included in any glyphset definition</li>
<li>U+034B COMBINING HOMOTHETIC ABOVE: not included in any glyphset definition</li>
<li>U+034C COMBINING ALMOST EQUAL TO ABOVE: not included in any glyphset definition</li>
<li>U+034D COMBINING LEFT RIGHT ARROW BELOW: try adding math</li>
<li>U+034E COMBINING UPWARDS ARROW BELOW: not included in any glyphset definition</li>
<li>U+034F COMBINING GRAPHEME JOINER: not included in any glyphset definition</li>
<li>U+0350 COMBINING RIGHT ARROWHEAD ABOVE: not included in any glyphset definition</li>
<li>U+0351 COMBINING LEFT HALF RING ABOVE: not included in any glyphset definition</li>
<li>U+0352 COMBINING FERMATA: not included in any glyphset definition</li>
<li>U+0353 COMBINING X BELOW: not included in any glyphset definition</li>
<li>U+0354 COMBINING LEFT ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0355 COMBINING RIGHT ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0356 COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+0357 COMBINING RIGHT HALF RING ABOVE: not included in any glyphset definition</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0359 COMBINING ASTERISK BELOW: not included in any glyphset definition</li>
<li>U+035A COMBINING DOUBLE RING BELOW: not included in any glyphset definition</li>
<li>U+035B COMBINING ZIGZAG ABOVE: not included in any glyphset definition</li>
<li>U+035C COMBINING DOUBLE BREVE BELOW: not included in any glyphset definition</li>
<li>U+035D COMBINING DOUBLE BREVE: not included in any glyphset definition</li>
<li>U+035E COMBINING DOUBLE MACRON: try adding one of: todhri, coptic, caucasian-albanian</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0360 COMBINING DOUBLE TILDE: not included in any glyphset definition</li>
<li>U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic</li>
<li>U+0362 COMBINING DOUBLE RIGHTWARDS ARROW BELOW: not included in any glyphset definition</li>
<li>U+0363 COMBINING LATIN SMALL LETTER A: not included in any glyphset definition</li>
<li>U+0364 COMBINING LATIN SMALL LETTER E: not included in any glyphset definition</li>
<li>U+0365 COMBINING LATIN SMALL LETTER I: not included in any glyphset definition</li>
<li>U+0366 COMBINING LATIN SMALL LETTER O: not included in any glyphset definition</li>
<li>U+0367 COMBINING LATIN SMALL LETTER U: not included in any glyphset definition</li>
<li>U+0368 COMBINING LATIN SMALL LETTER C: not included in any glyphset definition</li>
<li>U+0369 COMBINING LATIN SMALL LETTER D: not included in any glyphset definition</li>
<li>U+036A COMBINING LATIN SMALL LETTER H: not included in any glyphset definition</li>
<li>U+036B COMBINING LATIN SMALL LETTER M: not included in any glyphset definition</li>
<li>U+036C COMBINING LATIN SMALL LETTER R: not included in any glyphset definition</li>
<li>U+036D COMBINING LATIN SMALL LETTER T: not included in any glyphset definition</li>
<li>U+036E COMBINING LATIN SMALL LETTER V: not included in any glyphset definition</li>
<li>U+036F COMBINING LATIN SMALL LETTER X: not included in any glyphset definition</li>
<li>U+10FB GEORGIAN PARAGRAPH SEPARATOR: try adding one of: glagolitic, georgian</li>
<li>U+1AB0 COMBINING DOUBLED CIRCUMFLEX ACCENT: not included in any glyphset definition</li>
<li>U+1AB1 COMBINING DIAERESIS-RING: not included in any glyphset definition</li>
<li>U+1AB2 COMBINING INFINITY: not included in any glyphset definition</li>
<li>U+1AB3 COMBINING DOWNWARDS ARROW: not included in any glyphset definition</li>
<li>U+1AB4 COMBINING TRIPLE DOT: not included in any glyphset definition</li>
<li>U+1AB5 COMBINING X-X BELOW: not included in any glyphset definition</li>
<li>U+1AB6 COMBINING WIGGLY LINE BELOW: not included in any glyphset definition</li>
<li>U+1AB7 COMBINING OPEN MARK BELOW: not included in any glyphset definition</li>
<li>U+1AB8 COMBINING DOUBLE OPEN MARK BELOW: not included in any glyphset definition</li>
<li>U+1AB9 COMBINING LIGHT CENTRALIZATION STROKE BELOW: not included in any glyphset definition</li>
<li>U+1ABA COMBINING STRONG CENTRALIZATION STROKE BELOW: not included in any glyphset definition</li>
<li>U+1ABB COMBINING PARENTHESES ABOVE: not included in any glyphset definition</li>
<li>U+1ABC COMBINING DOUBLE PARENTHESES ABOVE: not included in any glyphset definition</li>
<li>U+1ABD COMBINING PARENTHESES BELOW: not included in any glyphset definition</li>
<li>U+1ABE COMBINING PARENTHESES OVERLAY: not included in any glyphset definition</li>
<li>U+1ABF COMBINING LATIN SMALL LETTER W BELOW: not included in any glyphset definition</li>
<li>U+1AC0 COMBINING LATIN SMALL LETTER TURNED W BELOW: not included in any glyphset definition</li>
<li>U+1AC5 COMBINING SQUARE BRACKETS ABOVE: not included in any glyphset definition</li>
<li>U+1AC7 COMBINING INVERTED DOUBLE ARCH ABOVE: not included in any glyphset definition</li>
<li>U+1AC8 COMBINING PLUS SIGN ABOVE: not included in any glyphset definition</li>
<li>U+1AC9 COMBINING DOUBLE PLUS SIGN ABOVE: not included in any glyphset definition</li>
<li>U+1ACA COMBINING DOUBLE PLUS SIGN BELOW: not included in any glyphset definition</li>
<li>U+1ACB COMBINING TRIPLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+1ACC COMBINING LATIN SMALL LETTER INSULAR G: not included in any glyphset definition</li>
<li>U+1ACD COMBINING LATIN SMALL LETTER INSULAR R: not included in any glyphset definition</li>
<li>U+1ACE COMBINING LATIN SMALL LETTER INSULAR T: not included in any glyphset definition</li>
<li>U+1DC0 COMBINING DOTTED GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+1DC1 COMBINING DOTTED ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+1DC2 COMBINING SNAKE BELOW: not included in any glyphset definition</li>
<li>U+1DC3 COMBINING SUSPENSION MARK: not included in any glyphset definition</li>
<li>U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition</li>
<li>U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition</li>
<li>U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition</li>
<li>U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition</li>
<li>U+1DC8 COMBINING GRAVE-ACUTE-GRAVE: not included in any glyphset definition</li>
<li>U+1DC9 COMBINING ACUTE-GRAVE-ACUTE: not included in any glyphset definition</li>
<li>U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition</li>
<li>U+1DCB COMBINING BREVE-MACRON: not included in any glyphset definition</li>
<li>U+1DCC COMBINING MACRON-BREVE: not included in any glyphset definition</li>
<li>U+1DCD COMBINING DOUBLE CIRCUMFLEX ABOVE: try adding coptic</li>
<li>U+1DCE COMBINING OGONEK ABOVE: not included in any glyphset definition</li>
<li>U+1DCF COMBINING ZIGZAG BELOW: not included in any glyphset definition</li>
<li>U+1DD0 COMBINING IS BELOW: not included in any glyphset definition</li>
<li>U+1DD1 COMBINING UR ABOVE: not included in any glyphset definition</li>
<li>U+1DD2 COMBINING US ABOVE: not included in any glyphset definition</li>
<li>U+1DD3 COMBINING LATIN SMALL LETTER FLATTENED OPEN A ABOVE: not included in any glyphset definition</li>
<li>U+1DD4 COMBINING LATIN SMALL LETTER AE: not included in any glyphset definition</li>
<li>U+1DD5 COMBINING LATIN SMALL LETTER AO: not included in any glyphset definition</li>
<li>U+1DD6 COMBINING LATIN SMALL LETTER AV: not included in any glyphset definition</li>
<li>U+1DD7 COMBINING LATIN SMALL LETTER C CEDILLA: not included in any glyphset definition</li>
<li>U+1DD8 COMBINING LATIN SMALL LETTER INSULAR D: not included in any glyphset definition</li>
<li>U+1DD9 COMBINING LATIN SMALL LETTER ETH: not included in any glyphset definition</li>
<li>U+1DDA COMBINING LATIN SMALL LETTER G: not included in any glyphset definition</li>
<li>U+1DDB COMBINING LATIN LETTER SMALL CAPITAL G: not included in any glyphset definition</li>
<li>U+1DDC COMBINING LATIN SMALL LETTER K: not included in any glyphset definition</li>
<li>U+1DDD COMBINING LATIN SMALL LETTER L: not included in any glyphset definition</li>
<li>U+1DDE COMBINING LATIN LETTER SMALL CAPITAL L: not included in any glyphset definition</li>
<li>U+1DDF COMBINING LATIN LETTER SMALL CAPITAL M: not included in any glyphset definition</li>
<li>U+1DE0 COMBINING LATIN SMALL LETTER N: not included in any glyphset definition</li>
<li>U+1DE1 COMBINING LATIN LETTER SMALL CAPITAL N: not included in any glyphset definition</li>
<li>U+1DE2 COMBINING LATIN LETTER SMALL CAPITAL R: not included in any glyphset definition</li>
<li>U+1DE3 COMBINING LATIN SMALL LETTER R ROTUNDA: not included in any glyphset definition</li>
<li>U+1DE4 COMBINING LATIN SMALL LETTER S: not included in any glyphset definition</li>
<li>U+1DE5 COMBINING LATIN SMALL LETTER LONG S: not included in any glyphset definition</li>
<li>U+1DE6 COMBINING LATIN SMALL LETTER Z: not included in any glyphset definition</li>
<li>U+1DE7 COMBINING LATIN SMALL LETTER ALPHA: not included in any glyphset definition</li>
<li>U+1DE8 COMBINING LATIN SMALL LETTER B: not included in any glyphset definition</li>
<li>U+1DE9 COMBINING LATIN SMALL LETTER BETA: not included in any glyphset definition</li>
<li>U+1DEA COMBINING LATIN SMALL LETTER SCHWA: not included in any glyphset definition</li>
<li>U+1DEB COMBINING LATIN SMALL LETTER F: not included in any glyphset definition</li>
<li>U+1DEC COMBINING LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+1DED COMBINING LATIN SMALL LETTER O WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition</li>
<li>U+1DEE COMBINING LATIN SMALL LETTER P: not included in any glyphset definition</li>
<li>U+1DEF COMBINING LATIN SMALL LETTER ESH: not included in any glyphset definition</li>
<li>U+1DF0 COMBINING LATIN SMALL LETTER U WITH LIGHT CENTRALIZATION STROKE: not included in any glyphset definition</li>
<li>U+1DF1 COMBINING LATIN SMALL LETTER W: not included in any glyphset definition</li>
<li>U+1DF2 COMBINING LATIN SMALL LETTER A WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF3 COMBINING LATIN SMALL LETTER O WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF4 COMBINING LATIN SMALL LETTER U WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+1DF5 COMBINING UP TACK ABOVE: not included in any glyphset definition</li>
<li>U+1DF6 COMBINING KAVYKA ABOVE RIGHT: not included in any glyphset definition</li>
<li>U+1DF7 COMBINING KAVYKA ABOVE LEFT: not included in any glyphset definition</li>
<li>U+1DF8 COMBINING DOT ABOVE LEFT: try adding syriac</li>
<li>U+1DF9 COMBINING WIDE INVERTED BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+1DFB COMBINING DELETION MARK: try adding newa</li>
<li>U+1DFC COMBINING DOUBLE INVERTED BREVE BELOW: not included in any glyphset definition</li>
<li>U+1DFD COMBINING ALMOST EQUAL TO BELOW: not included in any glyphset definition</li>
<li>U+1DFE COMBINING LEFT ARROWHEAD ABOVE: not included in any glyphset definition</li>
<li>U+1DFF COMBINING RIGHT ARROWHEAD AND DOWN ARROWHEAD BELOW: not included in any glyphset definition</li>
<li>U+2000 EN QUAD: try adding symbols2</li>
<li>U+2001 EM QUAD: try adding symbols2</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2004 THREE-PER-EM SPACE: try adding symbols2</li>
<li>U+2005 FOUR-PER-EM SPACE: try adding symbols2</li>
<li>U+2006 SIX-PER-EM SPACE: try adding symbols2</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+200A HAIR SPACE: try adding symbols2</li>
<li>U+200E LEFT-TO-RIGHT MARK: try adding one of: thaana, nko, hebrew, syriac, arabic, phags-pa</li>
<li>U+200F RIGHT-TO-LEFT MARK: try adding one of: thaana, nko, hebrew, syriac, phags-pa</li>
<li>U+2010 HYPHEN: try adding one of: lisu, yi, sundanese, armenian, hebrew, kayah-li, coptic, cham, kaithi, kharoshthi, arabic, syloti-nagri, sora-sompeng</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2017 DOUBLE LOW LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2028 LINE SEPARATOR: not included in any glyphset definition</li>
<li>U+2029 PARAGRAPH SEPARATOR: not included in any glyphset definition</li>
<li>U+202A LEFT-TO-RIGHT EMBEDDING: not included in any glyphset definition</li>
<li>U+202B RIGHT-TO-LEFT EMBEDDING: not included in any glyphset definition</li>
<li>U+202C POP DIRECTIONAL FORMATTING: not included in any glyphset definition</li>
<li>U+202D LEFT-TO-RIGHT OVERRIDE: not included in any glyphset definition</li>
<li>U+202E RIGHT-TO-LEFT OVERRIDE: try adding tifinagh</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: mongolian, yi, phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+2035 REVERSED PRIME: try adding math</li>
<li>U+2036 REVERSED DOUBLE PRIME: try adding math</li>
<li>U+2037 REVERSED TRIPLE PRIME: try adding math</li>
<li>U+2038 CARET: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+203F UNDERTIE: not included in any glyphset definition</li>
<li>U+2040 CHARACTER TIE: try adding math</li>
<li>U+2041 CARET INSERTION POINT: not included in any glyphset definition</li>
<li>U+2042 ASTERISM: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2045 LEFT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2046 RIGHT SQUARE BRACKET WITH QUILL: not included in any glyphset definition</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+204A TIRONIAN SIGN ET: not included in any glyphset definition</li>
<li>U+204B REVERSED PILCROW SIGN: not included in any glyphset definition</li>
<li>U+204C BLACK LEFTWARDS BULLET: not included in any glyphset definition</li>
<li>U+204D BLACK RIGHTWARDS BULLET: not included in any glyphset definition</li>
<li>U+204E LOW ASTERISK: not included in any glyphset definition</li>
<li>U+204F REVERSED SEMICOLON: try adding one of: arabic, adlam</li>
<li>U+2050 CLOSE UP: try adding math</li>
<li>U+2051 TWO ASTERISKS ALIGNED VERTICALLY: not included in any glyphset definition</li>
<li>U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition</li>
<li>U+2053 SWUNG DASH: try adding coptic</li>
<li>U+2054 INVERTED UNDERTIE: not included in any glyphset definition</li>
<li>U+2055 FLOWER PUNCTUATION MARK: try adding syloti-nagri</li>
<li>U+2056 THREE DOT PUNCTUATION: try adding coptic</li>
<li>U+2057 QUADRUPLE PRIME: try adding math</li>
<li>U+2058 FOUR DOT PUNCTUATION: try adding coptic</li>
<li>U+2059 FIVE DOT PUNCTUATION: try adding coptic</li>
<li>U+205A TWO DOT PUNCTUATION: try adding one of: old-hungarian, glagolitic, old-turkic, lycian, carian, georgian</li>
<li>U+205B FOUR DOT MARK: not included in any glyphset definition</li>
<li>U+205C DOTTED CROSS: not included in any glyphset definition</li>
<li>U+205D TRICOLON: try adding one of: carian, meroitic, old-hungarian, meroitic-hieroglyphs</li>
<li>U+205E VERTICAL FOUR DOTS: try adding old-hungarian</li>
<li>U+205F MEDIUM MATHEMATICAL SPACE: try adding math</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2061 FUNCTION APPLICATION: not included in any glyphset definition</li>
<li>U+2062 INVISIBLE TIMES: not included in any glyphset definition</li>
<li>U+2063 INVISIBLE SEPARATOR: not included in any glyphset definition</li>
<li>U+2064 INVISIBLE PLUS: not included in any glyphset definition</li>
<li>U+2066 LEFT-TO-RIGHT ISOLATE: not included in any glyphset definition</li>
<li>U+2067 RIGHT-TO-LEFT ISOLATE: not included in any glyphset definition</li>
<li>U+2068 FIRST STRONG ISOLATE: not included in any glyphset definition</li>
<li>U+2069 POP DIRECTIONAL ISOLATE: not included in any glyphset definition</li>
<li>U+206A INHIBIT SYMMETRIC SWAPPING: not included in any glyphset definition</li>
<li>U+206B ACTIVATE SYMMETRIC SWAPPING: not included in any glyphset definition</li>
<li>U+206C INHIBIT ARABIC FORM SHAPING: not included in any glyphset definition</li>
<li>U+206D ACTIVATE ARABIC FORM SHAPING: not included in any glyphset definition</li>
<li>U+206E NATIONAL DIGIT SHAPES: not included in any glyphset definition</li>
<li>U+206F NOMINAL DIGIT SHAPES: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2102 DOUBLE-STRUCK CAPITAL C: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+2104 CENTRE LINE SYMBOL: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2107 EULER CONSTANT: try adding math</li>
<li>U+2108 SCRUPLE: try adding math</li>
<li>U+2109 DEGREE FAHRENHEIT: try adding math</li>
<li>U+210A SCRIPT SMALL G: try adding math</li>
<li>U+210B SCRIPT CAPITAL H: try adding math</li>
<li>U+210C BLACK-LETTER CAPITAL H: try adding math</li>
<li>U+210D DOUBLE-STRUCK CAPITAL H: try adding math</li>
<li>U+210E PLANCK CONSTANT: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2110 SCRIPT CAPITAL I: try adding math</li>
<li>U+2111 BLACK-LETTER CAPITAL I: try adding math</li>
<li>U+2112 SCRIPT CAPITAL L: try adding math</li>
<li>U+2114 L B BAR SYMBOL: try adding math</li>
<li>U+2115 DOUBLE-STRUCK CAPITAL N: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2118 SCRIPT CAPITAL P: try adding math</li>
<li>U+2119 DOUBLE-STRUCK CAPITAL P: try adding math</li>
<li>U+211A DOUBLE-STRUCK CAPITAL Q: try adding math</li>
<li>U+211B SCRIPT CAPITAL R: try adding math</li>
<li>U+211C BLACK-LETTER CAPITAL R: try adding math</li>
<li>U+211D DOUBLE-STRUCK CAPITAL R: try adding math</li>
<li>U+211E PRESCRIPTION TAKE: try adding math</li>
<li>U+211F RESPONSE: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2121 TELEPHONE SIGN: try adding math</li>
<li>U+2123 VERSICLE: try adding math</li>
<li>U+2124 DOUBLE-STRUCK CAPITAL Z: try adding math</li>
<li>U+2125 OUNCE SIGN: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+2128 BLACK-LETTER CAPITAL Z: try adding math</li>
<li>U+2129 TURNED GREEK SMALL LETTER IOTA: try adding math</li>
<li>U+212A KELVIN SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+212C SCRIPT CAPITAL B: try adding math</li>
<li>U+212D BLACK-LETTER CAPITAL C: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+212F SCRIPT SMALL E: try adding math</li>
<li>U+2130 SCRIPT CAPITAL E: try adding math</li>
<li>U+2131 SCRIPT CAPITAL F: try adding math</li>
<li>U+2132 TURNED CAPITAL F: try adding math</li>
<li>U+2133 SCRIPT CAPITAL M: try adding math</li>
<li>U+2134 SCRIPT SMALL O: try adding math</li>
<li>U+2135 ALEF SYMBOL: try adding math</li>
<li>U+2136 BET SYMBOL: try adding math</li>
<li>U+2137 GIMEL SYMBOL: try adding math</li>
<li>U+2138 DALET SYMBOL: try adding math</li>
<li>U+2139 INFORMATION SOURCE: try adding math</li>
<li>U+213A ROTATED CAPITAL Q: try adding math</li>
<li>U+213B FACSIMILE SIGN: try adding math</li>
<li>U+213C DOUBLE-STRUCK SMALL PI: try adding math</li>
<li>U+213D DOUBLE-STRUCK SMALL GAMMA: try adding math</li>
<li>U+213E DOUBLE-STRUCK CAPITAL GAMMA: try adding math</li>
<li>U+213F DOUBLE-STRUCK CAPITAL PI: try adding math</li>
<li>U+2140 DOUBLE-STRUCK N-ARY SUMMATION: try adding math</li>
<li>U+2141 TURNED SANS-SERIF CAPITAL G: try adding math</li>
<li>U+2142 TURNED SANS-SERIF CAPITAL L: try adding math</li>
<li>U+2143 REVERSED SANS-SERIF CAPITAL L: try adding math</li>
<li>U+2144 TURNED SANS-SERIF CAPITAL Y: try adding math</li>
<li>U+2145 DOUBLE-STRUCK ITALIC CAPITAL D: try adding math</li>
<li>U+2146 DOUBLE-STRUCK ITALIC SMALL D: try adding math</li>
<li>U+2147 DOUBLE-STRUCK ITALIC SMALL E: try adding math</li>
<li>U+2148 DOUBLE-STRUCK ITALIC SMALL I: try adding math</li>
<li>U+2149 DOUBLE-STRUCK ITALIC SMALL J: try adding math</li>
<li>U+214A PROPERTY LINE: try adding math</li>
<li>U+214B TURNED AMPERSAND: try adding math</li>
<li>U+214C PER SIGN: try adding math</li>
<li>U+214D AKTIESELSKAB: try adding math</li>
<li>U+214E TURNED SMALL F: try adding math</li>
<li>U+214F SYMBOL FOR SAMARITAN SOURCE: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2183 ROMAN NUMERAL REVERSED ONE HUNDRED: try adding symbols</li>
<li>U+2184 LATIN SMALL LETTER REVERSED C: not included in any glyphset definition</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2E00 RIGHT ANGLE SUBSTITUTION MARKER: not included in any glyphset definition</li>
<li>U+2E01 RIGHT ANGLE DOTTED SUBSTITUTION MARKER: not included in any glyphset definition</li>
<li>U+2E02 LEFT SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E03 RIGHT SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E04 LEFT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E05 RIGHT DOTTED SUBSTITUTION BRACKET: not included in any glyphset definition</li>
<li>U+2E06 RAISED INTERPOLATION MARKER: not included in any glyphset definition</li>
<li>U+2E07 RAISED DOTTED INTERPOLATION MARKER: not included in any glyphset definition</li>
<li>U+2E08 DOTTED TRANSPOSITION MARKER: not included in any glyphset definition</li>
<li>U+2E09 LEFT TRANSPOSITION BRACKET: not included in any glyphset definition</li>
<li>U+2E0A RIGHT TRANSPOSITION BRACKET: not included in any glyphset definition</li>
<li>U+2E0B RAISED SQUARE: not included in any glyphset definition</li>
<li>U+2E0C LEFT RAISED OMISSION BRACKET: not included in any glyphset definition</li>
<li>U+2E0D RIGHT RAISED OMISSION BRACKET: not included in any glyphset definition</li>
<li>U+2E0E EDITORIAL CORONIS: not included in any glyphset definition</li>
<li>U+2E0F PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E10 FORKED PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E11 REVERSED FORKED PARAGRAPHOS: not included in any glyphset definition</li>
<li>U+2E12 HYPODIASTOLE: not included in any glyphset definition</li>
<li>U+2E13 DOTTED OBELOS: not included in any glyphset definition</li>
<li>U+2E14 DOWNWARDS ANCORA: not included in any glyphset definition</li>
<li>U+2E15 UPWARDS ANCORA: not included in any glyphset definition</li>
<li>U+2E16 DOTTED RIGHT-POINTING ANGLE: not included in any glyphset definition</li>
<li>U+2E17 DOUBLE OBLIQUE HYPHEN: try adding coptic</li>
<li>U+2E18 INVERTED INTERROBANG: not included in any glyphset definition</li>
<li>U+2E19 PALM BRANCH: not included in any glyphset definition</li>
<li>U+2E1A HYPHEN WITH DIAERESIS: not included in any glyphset definition</li>
<li>U+2E1B TILDE WITH RING ABOVE: not included in any glyphset definition</li>
<li>U+2E1C LEFT LOW PARAPHRASE BRACKET: try adding nko</li>
<li>U+2E1D RIGHT LOW PARAPHRASE BRACKET: try adding nko</li>
<li>U+2E1E TILDE WITH DOT ABOVE: not included in any glyphset definition</li>
<li>U+2E1F TILDE WITH DOT BELOW: not included in any glyphset definition</li>
<li>U+2E20 LEFT VERTICAL BAR WITH QUILL: not included in any glyphset definition</li>
<li>U+2E21 RIGHT VERTICAL BAR WITH QUILL: not included in any glyphset definition</li>
<li>U+2E22 TOP LEFT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E23 TOP RIGHT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E24 BOTTOM LEFT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E25 BOTTOM RIGHT HALF BRACKET: not included in any glyphset definition</li>
<li>U+2E26 LEFT SIDEWAYS U BRACKET: not included in any glyphset definition</li>
<li>U+2E27 RIGHT SIDEWAYS U BRACKET: not included in any glyphset definition</li>
<li>U+2E28 LEFT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E29 RIGHT DOUBLE PARENTHESIS: try adding adlam</li>
<li>U+2E2A TWO DOTS OVER ONE DOT PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2B ONE DOT OVER TWO DOTS PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2C SQUARED FOUR DOT PUNCTUATION: not included in any glyphset definition</li>
<li>U+2E2D FIVE DOT MARK: not included in any glyphset definition</li>
<li>U+2E2E REVERSED QUESTION MARK: not included in any glyphset definition</li>
<li>U+2E2F VERTICAL TILDE: not included in any glyphset definition</li>
<li>U+2E30 RING POINT: try adding one of: old-turkic, avestan</li>
<li>U+2E31 WORD SEPARATOR MIDDLE DOT: try adding one of: samaritan, old-hungarian, lydian, kaithi, avestan, carian, georgian</li>
<li>U+2E32 TURNED COMMA: not included in any glyphset definition</li>
<li>U+2E33 RAISED DOT: try adding coptic</li>
<li>U+2E34 RAISED COMMA: try adding coptic</li>
<li>U+2E35 TURNED SEMICOLON: not included in any glyphset definition</li>
<li>U+2E36 DAGGER WITH LEFT GUARD: not included in any glyphset definition</li>
<li>U+2E37 DAGGER WITH RIGHT GUARD: not included in any glyphset definition</li>
<li>U+2E38 TURNED DAGGER: not included in any glyphset definition</li>
<li>U+2E39 TOP HALF SECTION SIGN: not included in any glyphset definition</li>
<li>U+2E3A TWO-EM DASH: not included in any glyphset definition</li>
<li>U+2E3B THREE-EM DASH: not included in any glyphset definition</li>
<li>U+2E3C STENOGRAPHIC FULL STOP: try adding duployan</li>
<li>U+2E3D VERTICAL SIX DOTS: not included in any glyphset definition</li>
<li>U+2E3E WIGGLY VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2E3F CAPITULUM: not included in any glyphset definition</li>
<li>U+2E40 DOUBLE HYPHEN: not included in any glyphset definition</li>
<li>U+2E41 REVERSED COMMA: try adding one of: old-hungarian, arabic, adlam</li>
<li>U+2E42 DOUBLE LOW-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2E43 DASH WITH LEFT UPTURN: try adding glagolitic</li>
<li>U+2E44 DOUBLE SUSPENSION MARK: not included in any glyphset definition</li>
<li>U+2E45 INVERTED LOW KAVYKA: not included in any glyphset definition</li>
<li>U+2E46 INVERTED LOW KAVYKA WITH KAVYKA ABOVE: not included in any glyphset definition</li>
<li>U+2E47 LOW KAVYKA: not included in any glyphset definition</li>
<li>U+2E48 LOW KAVYKA WITH DOT: not included in any glyphset definition</li>
<li>U+2E49 DOUBLE STACKED COMMA: not included in any glyphset definition</li>
<li>U+2E4A DOTTED SOLIDUS: not included in any glyphset definition</li>
<li>U+2E4B TRIPLE DAGGER: not included in any glyphset definition</li>
<li>U+2E4C MEDIEVAL COMMA: not included in any glyphset definition</li>
<li>U+2E4D PARAGRAPHUS MARK: not included in any glyphset definition</li>
<li>U+2E4E PUNCTUS ELEVATUS MARK: not included in any glyphset definition</li>
<li>U+2E4F CORNISH VERSE DIVIDER: not included in any glyphset definition</li>
<li>U+2E50 CROSS PATTY WITH RIGHT CROSSBAR: not included in any glyphset definition</li>
<li>U+2E51 CROSS PATTY WITH LEFT CROSSBAR: not included in any glyphset definition</li>
<li>U+2E52 TIRONIAN SIGN CAPITAL ET: not included in any glyphset definition</li>
<li>U+2E53 MEDIEVAL EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+2E54 MEDIEVAL QUESTION MARK: not included in any glyphset definition</li>
<li>U+2E55 LEFT SQUARE BRACKET WITH STROKE: not included in any glyphset definition</li>
<li>U+2E56 RIGHT SQUARE BRACKET WITH STROKE: not included in any glyphset definition</li>
<li>U+2E57 LEFT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition</li>
<li>U+2E58 RIGHT SQUARE BRACKET WITH DOUBLE STROKE: not included in any glyphset definition</li>
<li>U+2E59 TOP HALF LEFT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5A TOP HALF RIGHT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5B BOTTOM HALF LEFT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5C BOTTOM HALF RIGHT PARENTHESIS: not included in any glyphset definition</li>
<li>U+2E5D OBLIQUE HYPHEN: not included in any glyphset definition</li>
<li>U+A700 MODIFIER LETTER CHINESE TONE YIN PING: not included in any glyphset definition</li>
<li>U+A701 MODIFIER LETTER CHINESE TONE YANG PING: not included in any glyphset definition</li>
<li>U+A702 MODIFIER LETTER CHINESE TONE YIN SHANG: not included in any glyphset definition</li>
<li>U+A703 MODIFIER LETTER CHINESE TONE YANG SHANG: not included in any glyphset definition</li>
<li>U+A704 MODIFIER LETTER CHINESE TONE YIN QU: not included in any glyphset definition</li>
<li>U+A705 MODIFIER LETTER CHINESE TONE YANG QU: not included in any glyphset definition</li>
<li>U+A706 MODIFIER LETTER CHINESE TONE YIN RU: not included in any glyphset definition</li>
<li>U+A707 MODIFIER LETTER CHINESE TONE YANG RU: not included in any glyphset definition</li>
<li>U+A708 MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A709 MODIFIER LETTER HIGH DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70A MODIFIER LETTER MID DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70B MODIFIER LETTER LOW DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70C MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR: not included in any glyphset definition</li>
<li>U+A70D MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A70E MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A70F MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A710 MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A711 MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A712 MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A713 MODIFIER LETTER HIGH LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A714 MODIFIER LETTER MID LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A715 MODIFIER LETTER LOW LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A716 MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR: not included in any glyphset definition</li>
<li>U+A717 MODIFIER LETTER DOT VERTICAL BAR: not included in any glyphset definition</li>
<li>U+A718 MODIFIER LETTER DOT SLASH: not included in any glyphset definition</li>
<li>U+A719 MODIFIER LETTER DOT HORIZONTAL BAR: not included in any glyphset definition</li>
<li>U+A71A MODIFIER LETTER LOWER RIGHT CORNER ANGLE: not included in any glyphset definition</li>
<li>U+A71B MODIFIER LETTER RAISED UP ARROW: not included in any glyphset definition</li>
<li>U+A71C MODIFIER LETTER RAISED DOWN ARROW: not included in any glyphset definition</li>
<li>U+A71D MODIFIER LETTER RAISED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A71E MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A71F MODIFIER LETTER LOW INVERTED EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+A92E KAYAH LI SIGN CWI: try adding one of: kayah-li, myanmar</li>
<li>U+AB30 LATIN SMALL LETTER BARRED ALPHA: not included in any glyphset definition</li>
<li>U+AB31 LATIN SMALL LETTER A REVERSED-SCHWA: not included in any glyphset definition</li>
<li>U+AB32 LATIN SMALL LETTER BLACKLETTER E: not included in any glyphset definition</li>
<li>U+AB33 LATIN SMALL LETTER BARRED E: not included in any glyphset definition</li>
<li>U+AB34 LATIN SMALL LETTER E WITH FLOURISH: not included in any glyphset definition</li>
<li>U+AB35 LATIN SMALL LETTER LENIS F: not included in any glyphset definition</li>
<li>U+AB36 LATIN SMALL LETTER SCRIPT G WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB37 LATIN SMALL LETTER L WITH INVERTED LAZY S: not included in any glyphset definition</li>
<li>U+AB38 LATIN SMALL LETTER L WITH DOUBLE MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB39 LATIN SMALL LETTER L WITH MIDDLE RING: not included in any glyphset definition</li>
<li>U+AB3A LATIN SMALL LETTER M WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3B LATIN SMALL LETTER N WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3C LATIN SMALL LETTER ENG WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB3D LATIN SMALL LETTER BLACKLETTER O: not included in any glyphset definition</li>
<li>U+AB3E LATIN SMALL LETTER BLACKLETTER O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB3F LATIN SMALL LETTER OPEN O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB40 LATIN SMALL LETTER INVERTED OE: not included in any glyphset definition</li>
<li>U+AB41 LATIN SMALL LETTER TURNED OE WITH STROKE: not included in any glyphset definition</li>
<li>U+AB42 LATIN SMALL LETTER TURNED OE WITH HORIZONTAL STROKE: not included in any glyphset definition</li>
<li>U+AB43 LATIN SMALL LETTER TURNED O OPEN-O: not included in any glyphset definition</li>
<li>U+AB44 LATIN SMALL LETTER TURNED O OPEN-O WITH STROKE: not included in any glyphset definition</li>
<li>U+AB45 LATIN SMALL LETTER STIRRUP R: not included in any glyphset definition</li>
<li>U+AB46 LATIN LETTER SMALL CAPITAL R WITH RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB47 LATIN SMALL LETTER R WITHOUT HANDLE: not included in any glyphset definition</li>
<li>U+AB48 LATIN SMALL LETTER DOUBLE R: not included in any glyphset definition</li>
<li>U+AB49 LATIN SMALL LETTER R WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB4A LATIN SMALL LETTER DOUBLE R WITH CROSSED-TAIL: not included in any glyphset definition</li>
<li>U+AB4B LATIN SMALL LETTER SCRIPT R: not included in any glyphset definition</li>
<li>U+AB4C LATIN SMALL LETTER SCRIPT R WITH RING: not included in any glyphset definition</li>
<li>U+AB4D LATIN SMALL LETTER BASELINE ESH: not included in any glyphset definition</li>
<li>U+AB4E LATIN SMALL LETTER U WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB4F LATIN SMALL LETTER U BAR WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB50 LATIN SMALL LETTER UI: not included in any glyphset definition</li>
<li>U+AB51 LATIN SMALL LETTER TURNED UI: not included in any glyphset definition</li>
<li>U+AB52 LATIN SMALL LETTER U WITH LEFT HOOK: not included in any glyphset definition</li>
<li>U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition</li>
<li>U+AB54 LATIN SMALL LETTER CHI WITH LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB55 LATIN SMALL LETTER CHI WITH LOW LEFT SERIF: not included in any glyphset definition</li>
<li>U+AB56 LATIN SMALL LETTER X WITH LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB57 LATIN SMALL LETTER X WITH LONG LEFT LEG: not included in any glyphset definition</li>
<li>U+AB58 LATIN SMALL LETTER X WITH LONG LEFT LEG AND LOW RIGHT RING: not included in any glyphset definition</li>
<li>U+AB59 LATIN SMALL LETTER X WITH LONG LEFT LEG WITH SERIF: not included in any glyphset definition</li>
<li>U+AB5A LATIN SMALL LETTER Y WITH SHORT RIGHT LEG: not included in any glyphset definition</li>
<li>U+AB5B MODIFIER BREVE WITH INVERTED BREVE: not included in any glyphset definition</li>
<li>U+AB5C MODIFIER LETTER SMALL HENG: not included in any glyphset definition</li>
<li>U+AB5D MODIFIER LETTER SMALL L WITH INVERTED LAZY S: not included in any glyphset definition</li>
<li>U+AB5E MODIFIER LETTER SMALL L WITH MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB5F MODIFIER LETTER SMALL U WITH LEFT HOOK: not included in any glyphset definition</li>
<li>U+AB60 LATIN SMALL LETTER SAKHA YAT: not included in any glyphset definition</li>
<li>U+AB61 LATIN SMALL LETTER IOTIFIED E: not included in any glyphset definition</li>
<li>U+AB62 LATIN SMALL LETTER OPEN OE: not included in any glyphset definition</li>
<li>U+AB63 LATIN SMALL LETTER UO: not included in any glyphset definition</li>
<li>U+AB64 LATIN SMALL LETTER INVERTED ALPHA: not included in any glyphset definition</li>
<li>U+AB65 GREEK LETTER SMALL CAPITAL OMEGA: not included in any glyphset definition</li>
<li>U+AB66 LATIN SMALL LETTER DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+AB67 LATIN SMALL LETTER TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+AB68 LATIN SMALL LETTER TURNED R WITH MIDDLE TILDE: not included in any glyphset definition</li>
<li>U+AB69 MODIFIER LETTER SMALL TURNED W: not included in any glyphset definition</li>
<li>U+AB6A MODIFIER LETTER LEFT TACK: not included in any glyphset definition</li>
<li>U+AB6B MODIFIER LETTER RIGHT TACK: not included in any glyphset definition</li>
<li>U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition</li>
<li>U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition</li>
<li>U+FB05 LATIN SMALL LIGATURE LONG S T: not included in any glyphset definition</li>
<li>U+FB06 LATIN SMALL LIGATURE ST: not included in any glyphset definition</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: manichaean, yi, phags-pa</li>
<li>U+FE20 COMBINING LIGATURE LEFT HALF: try adding caucasian-albanian</li>
<li>U+FE21 COMBINING LIGATURE RIGHT HALF: try adding caucasian-albanian</li>
<li>U+FE22 COMBINING DOUBLE TILDE LEFT HALF: try adding caucasian-albanian</li>
<li>U+FE23 COMBINING DOUBLE TILDE RIGHT HALF: try adding caucasian-albanian</li>
<li>U+FE24 COMBINING MACRON LEFT HALF: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE25 COMBINING MACRON RIGHT HALF: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE26 COMBINING CONJOINING MACRON: try adding one of: coptic, caucasian-albanian</li>
<li>U+FE27 COMBINING LIGATURE LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE28 COMBINING LIGATURE RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE29 COMBINING TILDE LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2A COMBINING TILDE RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2B COMBINING MACRON LEFT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2C COMBINING MACRON RIGHT HALF BELOW: try adding caucasian-albanian</li>
<li>U+FE2D COMBINING CONJOINING MACRON BELOW: try adding caucasian-albanian</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+10780 MODIFIER LETTER SMALL CAPITAL AA: not included in any glyphset definition</li>
<li>U+10781 MODIFIER LETTER SUPERSCRIPT TRIANGULAR COLON: not included in any glyphset definition</li>
<li>U+10782 MODIFIER LETTER SUPERSCRIPT HALF TRIANGULAR COLON: not included in any glyphset definition</li>
<li>U+10783 MODIFIER LETTER SMALL AE: not included in any glyphset definition</li>
<li>U+10784 MODIFIER LETTER SMALL CAPITAL B: not included in any glyphset definition</li>
<li>U+10785 MODIFIER LETTER SMALL B WITH HOOK: not included in any glyphset definition</li>
<li>U+10787 MODIFIER LETTER SMALL DZ DIGRAPH: not included in any glyphset definition</li>
<li>U+10788 MODIFIER LETTER SMALL DZ DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+10789 MODIFIER LETTER SMALL DZ DIGRAPH WITH CURL: not included in any glyphset definition</li>
<li>U+1078A MODIFIER LETTER SMALL DEZH DIGRAPH: not included in any glyphset definition</li>
<li>U+1078B MODIFIER LETTER SMALL D WITH TAIL: not included in any glyphset definition</li>
<li>U+1078C MODIFIER LETTER SMALL D WITH HOOK: not included in any glyphset definition</li>
<li>U+1078D MODIFIER LETTER SMALL D WITH HOOK AND TAIL: not included in any glyphset definition</li>
<li>U+1078E MODIFIER LETTER SMALL REVERSED E: not included in any glyphset definition</li>
<li>U+1078F MODIFIER LETTER SMALL CLOSED REVERSED OPEN E: not included in any glyphset definition</li>
<li>U+10790 MODIFIER LETTER SMALL FENG DIGRAPH: not included in any glyphset definition</li>
<li>U+10791 MODIFIER LETTER SMALL RAMS HORN: not included in any glyphset definition</li>
<li>U+10792 MODIFIER LETTER SMALL CAPITAL G: not included in any glyphset definition</li>
<li>U+10793 MODIFIER LETTER SMALL G WITH HOOK: not included in any glyphset definition</li>
<li>U+10794 MODIFIER LETTER SMALL CAPITAL G WITH HOOK: not included in any glyphset definition</li>
<li>U+10795 MODIFIER LETTER SMALL H WITH STROKE: not included in any glyphset definition</li>
<li>U+10796 MODIFIER LETTER SMALL CAPITAL H: not included in any glyphset definition</li>
<li>U+10797 MODIFIER LETTER SMALL HENG WITH HOOK: not included in any glyphset definition</li>
<li>U+10798 MODIFIER LETTER SMALL DOTLESS J WITH STROKE AND HOOK: not included in any glyphset definition</li>
<li>U+10799 MODIFIER LETTER SMALL LS DIGRAPH: not included in any glyphset definition</li>
<li>U+1079A MODIFIER LETTER SMALL LZ DIGRAPH: not included in any glyphset definition</li>
<li>U+1079B MODIFIER LETTER SMALL L WITH BELT: not included in any glyphset definition</li>
<li>U+1079C MODIFIER LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition</li>
<li>U+1079D MODIFIER LETTER SMALL L WITH RETROFLEX HOOK AND BELT: not included in any glyphset definition</li>
<li>U+1079E MODIFIER LETTER SMALL LEZH: not included in any glyphset definition</li>
<li>U+1079F MODIFIER LETTER SMALL LEZH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107A0 MODIFIER LETTER SMALL TURNED Y: not included in any glyphset definition</li>
<li>U+107A1 MODIFIER LETTER SMALL TURNED Y WITH BELT: not included in any glyphset definition</li>
<li>U+107A2 MODIFIER LETTER SMALL O WITH STROKE: not included in any glyphset definition</li>
<li>U+107A3 MODIFIER LETTER SMALL CAPITAL OE: not included in any glyphset definition</li>
<li>U+107A4 MODIFIER LETTER SMALL CLOSED OMEGA: not included in any glyphset definition</li>
<li>U+107A5 MODIFIER LETTER SMALL Q: not included in any glyphset definition</li>
<li>U+107A6 MODIFIER LETTER SMALL TURNED R WITH LONG LEG: not included in any glyphset definition</li>
<li>U+107A7 MODIFIER LETTER SMALL TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107A8 MODIFIER LETTER SMALL R WITH TAIL: not included in any glyphset definition</li>
<li>U+107A9 MODIFIER LETTER SMALL R WITH FISHHOOK: not included in any glyphset definition</li>
<li>U+107AA MODIFIER LETTER SMALL CAPITAL R: not included in any glyphset definition</li>
<li>U+107AB MODIFIER LETTER SMALL TC DIGRAPH WITH CURL: not included in any glyphset definition</li>
<li>U+107AC MODIFIER LETTER SMALL TS DIGRAPH: not included in any glyphset definition</li>
<li>U+107AD MODIFIER LETTER SMALL TS DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107AE MODIFIER LETTER SMALL TESH DIGRAPH: not included in any glyphset definition</li>
<li>U+107AF MODIFIER LETTER SMALL T WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107B0 MODIFIER LETTER SMALL V WITH RIGHT HOOK: not included in any glyphset definition</li>
<li>U+107B2 MODIFIER LETTER SMALL CAPITAL Y: not included in any glyphset definition</li>
<li>U+107B3 MODIFIER LETTER GLOTTAL STOP WITH STROKE: not included in any glyphset definition</li>
<li>U+107B4 MODIFIER LETTER REVERSED GLOTTAL STOP WITH STROKE: not included in any glyphset definition</li>
<li>U+107B5 MODIFIER LETTER BILABIAL CLICK: not included in any glyphset definition</li>
<li>U+107B6 MODIFIER LETTER DENTAL CLICK: not included in any glyphset definition</li>
<li>U+107B7 MODIFIER LETTER LATERAL CLICK: not included in any glyphset definition</li>
<li>U+107B8 MODIFIER LETTER ALVEOLAR CLICK: not included in any glyphset definition</li>
<li>U+107B9 MODIFIER LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+107BA MODIFIER LETTER SMALL S WITH CURL: not included in any glyphset definition</li>
<li>U+1DF00 LATIN SMALL LETTER FENG DIGRAPH WITH TRILL: not included in any glyphset definition</li>
<li>U+1DF01 LATIN SMALL LETTER REVERSED SCRIPT G: not included in any glyphset definition</li>
<li>U+1DF02 LATIN LETTER SMALL CAPITAL TURNED G: not included in any glyphset definition</li>
<li>U+1DF03 LATIN SMALL LETTER REVERSED K: not included in any glyphset definition</li>
<li>U+1DF04 LATIN LETTER SMALL CAPITAL L WITH BELT: not included in any glyphset definition</li>
<li>U+1DF05 LATIN SMALL LETTER LEZH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF06 LATIN SMALL LETTER TURNED Y WITH BELT: not included in any glyphset definition</li>
<li>U+1DF07 LATIN SMALL LETTER REVERSED ENG: not included in any glyphset definition</li>
<li>U+1DF08 LATIN SMALL LETTER TURNED R WITH LONG LEG AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF09 LATIN SMALL LETTER T WITH HOOK AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF0A LATIN LETTER RETROFLEX CLICK WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF0B LATIN SMALL LETTER ESH WITH DOUBLE BAR: not included in any glyphset definition</li>
<li>U+1DF0C LATIN SMALL LETTER ESH WITH DOUBLE BAR AND CURL: not included in any glyphset definition</li>
<li>U+1DF0D LATIN SMALL LETTER TURNED T WITH CURL: not included in any glyphset definition</li>
<li>U+1DF0E LATIN LETTER INVERTED GLOTTAL STOP WITH CURL: not included in any glyphset definition</li>
<li>U+1DF0F LATIN LETTER STRETCHED C WITH CURL: not included in any glyphset definition</li>
<li>U+1DF10 LATIN LETTER SMALL CAPITAL TURNED K: not included in any glyphset definition</li>
<li>U+1DF11 LATIN SMALL LETTER L WITH FISHHOOK: not included in any glyphset definition</li>
<li>U+1DF12 LATIN SMALL LETTER DEZH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF13 LATIN SMALL LETTER L WITH BELT AND PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF14 LATIN SMALL LETTER ENG WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF15 LATIN SMALL LETTER TURNED R WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF16 LATIN SMALL LETTER R WITH FISHHOOK AND PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF17 LATIN SMALL LETTER TESH DIGRAPH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF18 LATIN SMALL LETTER EZH WITH PALATAL HOOK: not included in any glyphset definition</li>
<li>U+1DF19 LATIN SMALL LETTER DEZH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1A LATIN SMALL LETTER I WITH STROKE AND RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1B LATIN SMALL LETTER O WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1C LATIN SMALL LETTER TESH DIGRAPH WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1D LATIN SMALL LETTER C WITH RETROFLEX HOOK: not included in any glyphset definition</li>
<li>U+1DF1E LATIN SMALL LETTER S WITH CURL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>devanagari</code>, <code>greek</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* uniA7D3 (U+A7D3) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 11 | 22 | 165 | 11 | 246 | 0 | 
| 0% | 0% | 2% | 5% | 36% | 2% | 54% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
