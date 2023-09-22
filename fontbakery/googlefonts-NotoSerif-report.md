## FontBakery report

fontbakery version: 0.9.1

<details><summary><b>[1] Family checks</b></summary><div><details><summary>⚠ <b>WARN:</b> Make sure all font files have the same version value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions">com.google.fonts/check/family/equal_font_versions</a>)</summary><div>


* ⚠ **WARN** Version info differs among font files of the same font project.
These were the version values found:
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Black.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-BlackItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Bold.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-BoldItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-ExtraBold.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-ExtraBoldItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-ExtraLight.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-ExtraLightItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Italic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Light.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-LightItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Medium.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-MediumItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Regular.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-SemiBold.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-SemiBoldItalic.ttf: 2.0110015869140625
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-Thin.ttf: 2.011993408203125
* fonts/NotoSerif/googlefonts/ttf/NotoSerif-ThinItalic.ttf: 2.0110015869140625
 [code: mismatch]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component breve)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component breve)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component breve)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Fstroke
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana and 342 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 43 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 569 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<675.0,229.0>--<670.0,0.0>> -> L<<670.0,0.0>--<670.0,-36.0>>

	* beta (U+03B2): L<<64.0,-220.0>--<66.0,100.0>> -> L<<66.0,100.0>--<64.0,494.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1088.0,195.0>--<1083.0,0.0>> -> L<<1083.0,0.0>--<1083.0,-22.0>>

	* rho (U+03C1): L<<49.0,-221.0>--<51.0,53.0>> -> L<<51.0,53.0>--<51.0,263.0>>

	* u10788 (U+10788): L<<707.2265625,403.9952392578125>--<703.9764404296875,287.0>> -> L<<703.9764404296875,287.0>--<703.9764404296875,273.800537109375>>

	* uni03BC (U+03BC): L<<66.0,-221.0>--<68.0,225.0>> -> L<<68.0,225.0>--<64.0,536.0>>

	* uni03FC (U+03FC): L<<50.0,-82.0>--<51.0,53.0>> -> L<<51.0,53.0>--<51.0,263.0>>

	* uni1D5D (U+1D5D): L<<41.6015625,155.00537109375>--<42.901611328125,346.99755859375>> -> L<<42.901611328125,346.99755859375>--<41.6015625,583.387939453125>>

	* uni1D66 (U+1D66): L<<41.6015625,-131.99462890625>--<42.901611328125,59.99755859375>> -> L<<42.901611328125,59.99755859375>--<41.6015625,296.387939453125>>

	* uni1D68 (U+1D68): L<<31.8511962890625,-132.5946044921875>--<33.1512451171875,31.7987060546875>> -> L<<33.1512451171875,31.7987060546875>--<33.1512451171875,157.7935791015625>>

	* 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* V (U+0056): B<<402.5,227.0>-<406.0,208.0>-<407.0,194.0>>/B<<407.0,194.0>-<409.0,211.0>-<416.0,238.5>> = 10.79545358773178

	* eogonek (U+0119): B<<282.5,-58.0>-<309.0,-25.0>-<346.0,-9.0>>/B<<346.0,-9.0>-<340.0,-10.0>-<333.5,-10.0>> = 13.922898849188117

	* u107A0 (U+107A0): B<<162.591796875,496.8045654296875>-<158.691650390625,513.00390625>-<158.0416259765625,523.803466796875>>/B<<158.0416259765625,523.803466796875>-<156.091552734375,510.60400390625>-<153.81646728515625,501.00439453125>> = 11.84849067812603

	* uni01B4 (U+01B4): B<<336.0,187.0>-<342.0,160.0>-<343.0,142.0>>/B<<343.0,142.0>-<346.0,164.0>-<349.5,180.0>> = 10.944996138289511

	* uni0233 (U+0233): B<<336.0,187.0>-<342.0,160.0>-<343.0,142.0>>/B<<343.0,142.0>-<346.0,164.0>-<349.5,180.0>> = 10.944996138289511

	* uni024F (U+024F): B<<336.0,187.0>-<342.0,160.0>-<343.0,142.0>>/B<<343.0,142.0>-<346.0,164.0>-<349.5,180.0>> = 10.944996138289511

	* uni028E (U+028E): B<<250.0,349.0>-<244.0,376.0>-<243.0,394.0>>/B<<243.0,394.0>-<240.0,372.0>-<236.5,356.0>> = 10.944996138289511

	* uni02B8 (U+02B8): B<<218.408203125,399.1954345703125>-<222.308349609375,382.99609375>-<222.9583740234375,372.196533203125>>/B<<222.9583740234375,372.196533203125>-<224.908447265625,385.39599609375>-<227.18353271484375,394.99560546875>> = 11.84849067812603

	* uni0377 (U+0377): B<<436.0,258.5>-<451.0,311.0>-<483.0,367.0>>/L<<483.0,367.0>--<198.0,0.0>> = 8.086843940697037

	* uni03D7 (U+03D7): B<<641.0,36.0>-<640.0,35.0>-<639.0,35.0>>/L<<639.0,35.0>--<646.0,36.0>> = 8.13010235415596

	* 32 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<64.0,-220.0>--<66.0,100.0>>

	* beta (U+03B2): L<<66.0,100.0>--<64.0,494.0>>

	* eta (U+03B7): L<<627.0,360.0>--<630.0,-221.0>>

	* etatonos (U+03AE): L<<627.0,360.0>--<630.0,-221.0>>

	* iota (U+03B9): L<<65.0,175.0>--<64.0,536.0>>

	* iotadieresis (U+03CA): L<<65.0,175.0>--<64.0,536.0>>

	* iotadieresistonos (U+0390): L<<65.0,175.0>--<64.0,536.0>>

	* iotatonos (U+03AF): L<<65.0,175.0>--<64.0,536.0>>

	* kappa (U+03BA): L<<46.0,0.0>--<44.0,536.0>>

	* rho (U+03C1): L<<49.0,-221.0>--<51.0,53.0>>

	* 61 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-BlackItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* A
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Aglottal
	* Agrave
	* Alpha
	* Alphatonos
	* Amacron and 389 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 43 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 569 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* beta (U+03B2): L<<-57.0,-220.0>--<13.0,100.0>> -> L<<13.0,100.0>--<93.0,494.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1059.0,195.0>--<1013.0,0.0>> -> L<<1013.0,0.0>--<1008.0,-22.0>>

	* f_f (U+FB00): L<<358.0,536.0>--<511.0,536.0>> -> L<<511.0,536.0>--<511.0,536.0>>

	* f_f (U+FB00): L<<511.0,536.0>--<511.0,536.0>> -> L<<511.0,536.0>--<512.0,536.0>>

	* rho (U+03C1): L<<-79.0,-221.0>--<-20.0,53.0>> -> L<<-20.0,53.0>--<24.0,263.0>>

	* u10788 (U+10788): L<<739.3758544921875,403.9952392578125>--<709.4747314453125,287.0>> -> L<<709.4747314453125,287.0>--<706.224609375,273.800537109375>>

	* uni03BC (U+03BC): L<<-54.0,-221.0>--<41.0,225.0>> -> L<<41.0,225.0>--<102.0,536.0>>

	* uni03FC (U+03FC): L<<-49.0,-82.0>--<-20.0,53.0>> -> L<<-20.0,53.0>--<24.0,263.0>>

	* uni1D0B (U+1D0B): L<<342.0,445.0>--<314.0,327.0>> -> L<<314.0,327.0>--<307.0,300.0>>

	* uni1D27 (U+1D27): L<<328.0,99.0>--<328.0,126.0>> -> L<<328.0,126.0>--<316.0,366.0>>

	* 9 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<533.5,403.5>-<488.0,379.0>-<431.0,372.0>>/B<<431.0,372.0>-<463.0,369.0>-<498.5,351.5>> = 12.357092600350505

	* uni0246 (U+0246): L<<335.0,339.0>--<295.0,151.0>>/L<<295.0,151.0>--<379.0,339.0>> = 12.064019868713396

	* uni024A (U+024A): L<<556.0,29.0>--<587.0,135.0>>/B<<587.0,135.0>-<568.0,101.0>-<528.5,68.0>> = 12.89577770175709

	* uni0377 (U+0377): B<<469.0,344.0>-<483.0,374.0>-<492.0,393.0>>/L<<492.0,393.0>--<197.0,0.0>> = 11.54704110819093

	* uni03F0 (U+03F0): B<<347.0,230.0>-<326.0,180.0>-<305.0,136.0>>/L<<305.0,136.0>--<596.0,536.0>> = 10.522018977053735

	* uni03F0 (U+03F0): B<<554.0,344.0>-<568.0,374.0>-<577.0,393.0>>/L<<577.0,393.0>--<282.0,0.0>> = 11.54704110819093

	* uni046E (U+046E): B<<516.5,403.5>-<471.0,379.0>-<414.0,372.0>>/B<<414.0,372.0>-<446.0,369.0>-<481.5,351.5>> = 12.357092600350505

	* uni0498 (U+0498): B<<533.5,403.5>-<488.0,379.0>-<431.0,372.0>>/B<<431.0,372.0>-<463.0,369.0>-<498.5,351.5>> = 12.357092600350505

	* uni049B (U+049B): B<<354.5,311.0>-<337.0,299.0>-<317.0,294.0>>/B<<317.0,294.0>-<378.0,296.0>-<417.0,270.0>> = 12.158366020641097

	* uni049D (U+049D): B<<320.0,203.0>-<317.0,210.0>-<319.0,214.0>>/L<<319.0,214.0>--<302.0,137.0>> = 14.115054669271364

	* 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[18] NotoSerif-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Noto Serif Bold | Noto Serif |
| Subfamily Name | Regular | Bold |
| Full Name | Noto Serif Bold | Noto Serif Bold |
| Poscript Name | NotoSerif-Bold | NotoSerif-Bold |
| Typographic Family Name | Noto Serif | N/A |
| Typographic Subfamily Name | Bold | N/A | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component breve)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component breve)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component breve)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Fstroke
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana and 321 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<622.0,206.0>--<617.0,0.0>> -> L<<617.0,0.0>--<617.0,-61.0>>

	* beta (U+03B2): L<<73.0,-240.0>--<77.0,126.0>> -> L<<77.0,126.0>--<68.0,527.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1010.0,181.0>--<1005.0,0.0>> -> L<<1005.0,0.0>--<1005.0,-51.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<57.0,122.0>> -> L<<57.0,122.0>--<57.0,263.0>>

	* u10788 (U+10788): L<<656.524658203125,395.5955810546875>--<653.2745361328125,287.0>> -> L<<653.2745361328125,287.0>--<653.2745361328125,256.4012451171875>>

	* u107A1 (U+107A1): L<<143.6553955078125,606.7869873046875>--<149.505615234375,606.7869873046875>> -> L<<149.505615234375,606.7869873046875>--<149.505615234375,606.7869873046875>>

	* uni03BC (U+03BC): L<<71.0,-240.0>--<75.0,75.0>> -> L<<75.0,75.0>--<68.0,536.0>>

	* uni03FC (U+03FC): L<<55.0,-81.0>--<57.0,122.0>> -> L<<57.0,122.0>--<57.0,263.0>>

	* uni1D5D (U+1D5D): L<<47.4517822265625,143.005859375>--<50.0518798828125,362.596923828125>> -> L<<50.0518798828125,362.596923828125>--<44.20166015625,603.1871337890625>>

	* uni1D66 (U+1D66): L<<47.4517822265625,-143.994140625>--<50.0518798828125,75.596923828125>> -> L<<50.0518798828125,75.596923828125>--<44.20166015625,316.1871337890625>>

	* 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* u107A0 (U+107A0): B<<167.3421630859375,511.803955078125>-<163.4420166015625,526.203369140625>-<162.1419677734375,538.202880859375>>/B<<162.1419677734375,538.202880859375>-<160.8419189453125,525.6033935546875>-<155.31671142578125,510.0040283203125>> = 12.074494389132889

	* u107A1 (U+107A1): B<<167.706298828125,511.390869140625>-<163.80615234375,525.790283203125>-<162.506103515625,537.789794921875>>/B<<162.506103515625,537.789794921875>-<161.8560791015625,525.1903076171875>-<156.005859375,509.89093017578125>> = 9.136757789030913

	* uni01B4 (U+01B4): B<<320.0,162.5>-<327.0,138.0>-<329.0,118.0>>/B<<329.0,118.0>-<330.0,132.0>-<335.0,149.0>> = 9.796209917474465

	* uni0233 (U+0233): B<<321.0,162.0>-<327.0,138.0>-<329.0,118.0>>/B<<329.0,118.0>-<331.0,139.0>-<339.5,165.0>> = 11.150925168505127

	* uni0246 (U+0246): L<<280.0,343.0>--<280.0,94.0>>/L<<280.0,94.0>--<341.0,343.0>> = 13.765215312007642

	* uni024F (U+024F): B<<321.0,162.0>-<327.0,138.0>-<329.0,118.0>>/B<<329.0,118.0>-<331.0,139.0>-<339.5,165.0>> = 11.150925168505127

	* uni028E (U+028E): B<<258.0,374.0>-<252.0,398.0>-<250.0,418.0>>/B<<250.0,418.0>-<248.0,397.0>-<239.5,371.0>> = 11.150925168505127

	* uni02B8 (U+02B8): B<<208.6578369140625,384.196044921875>-<212.5579833984375,369.796630859375>-<213.8580322265625,357.797119140625>>/B<<213.8580322265625,357.797119140625>-<215.1580810546875,370.3966064453125>-<220.68328857421875,385.9959716796875>> = 12.074494389132889

	* uni03F0 (U+03F0): B<<233.5,219.0>-<220.0,180.0>-<208.0,155.0>>/L<<208.0,155.0>--<481.0,536.0>> = 9.981933481390366

	* uni0478 (U+0478): B<<1047.0,162.0>-<1053.0,138.0>-<1055.0,118.0>>/B<<1055.0,118.0>-<1057.0,139.0>-<1065.5,165.0>> = 11.150925168505127

	* 20 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<578.0,356.0>--<583.0,-240.0>>

	* etatonos (U+03AE): L<<578.0,356.0>--<583.0,-240.0>>

	* h (U+0068): L<<101.0,122.0>--<100.0,646.0>>

	* h (U+0068): L<<252.0,309.0>--<253.0,118.0>>

	* hcircumflex (U+0125): L<<101.0,122.0>--<100.0,646.0>>

	* hcircumflex (U+0125): L<<252.0,309.0>--<253.0,118.0>>

	* hpalatalhook (U+A795): L<<101.0,122.0>--<100.0,646.0>>

	* hpalatalhook (U+A795): L<<252.0,309.0>--<253.0,118.0>>

	* kappa (U+03BA): L<<52.0,0.0>--<48.0,536.0>>

	* sterling (U+00A3): L<<428.0,346.0>--<270.0,347.0>>

	* 52 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* A
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Aglottal
	* Agrave
	* Alpha
	* Alphatonos
	* Amacron and 270 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<621.0,206.0>--<573.0,1.0>> -> L<<573.0,1.0>--<560.0,-61.0>>

	* beta (U+03B2): L<<-48.0,-240.0>--<32.0,126.0>> -> L<<32.0,126.0>--<109.0,527.0>>

	* dzdigraphretroflexhook (U+AB66): L<<987.0,181.0>--<946.0,7.0>> -> L<<946.0,7.0>--<938.0,-26.0>>

	* rho (U+03C1): L<<-74.0,-240.0>--<6.0,122.0>> -> L<<6.0,122.0>--<35.0,263.0>>

	* u10788 (U+10788): L<<693.5740966796875,395.5955810546875>--<666.923095703125,291.1998291015625>> -> L<<666.923095703125,291.1998291015625>--<661.722900390625,271.400634765625>>

	* uni03BC (U+03BC): L<<-48.0,-240.0>--<22.0,75.0>> -> L<<22.0,75.0>--<111.0,536.0>>

	* uni03FC (U+03FC): L<<-39.0,-81.0>--<6.0,122.0>> -> L<<6.0,122.0>--<35.0,263.0>>

	* uni1D0B (U+1D0B): L<<304.0,444.0>--<276.0,322.0>> -> L<<276.0,322.0>--<268.0,285.0>>

	* uni1D5D (U+1D5D): L<<21.798828125,143.005859375>--<73.80078125,362.596923828125>> -> L<<73.80078125,362.596923828125>--<123.8526611328125,603.1871337890625>>

	* uni1D66 (U+1D66): L<<-83.201171875,-239.994140625>--<-31.19921875,-20.403076171875>> -> L<<-31.19921875,-20.403076171875>--<18.8526611328125,220.1871337890625>>

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<508.0,402.0>-<462.0,377.0>-<405.0,370.0>>/B<<405.0,370.0>-<437.0,367.0>-<472.5,349.5>> = 12.357092600350505

	* uni0246 (U+0246): L<<299.0,343.0>--<242.0,73.0>>/L<<242.0,73.0>--<364.0,343.0>> = 12.395181192130876

	* uni03F0 (U+03F0): B<<282.5,231.5>-<262.0,182.0>-<240.0,135.0>>/L<<240.0,135.0>--<555.0,536.0>> = 13.067321778305404

	* uni046E (U+046E): B<<498.0,402.0>-<452.0,377.0>-<395.0,370.0>>/B<<395.0,370.0>-<427.0,367.0>-<462.5,349.5>> = 12.357092600350505

	* uni0498 (U+0498): B<<508.0,402.0>-<462.0,377.0>-<405.0,370.0>>/B<<405.0,370.0>-<437.0,367.0>-<472.5,349.5>> = 12.357092600350505

	* uni0506 (U+0506): B<<476.0,402.0>-<430.0,377.0>-<373.0,370.0>>/B<<373.0,370.0>-<394.0,368.0>-<419.0,362.5>> = 12.4415995885008

	* uni1D95 (U+1D95): L<<449.0,-39.0>--<496.0,217.0>>/B<<496.0,217.0>-<474.0,159.0>-<431.5,107.0>> = 10.368961953607531

	* uni1DEC (U+1DEC): B<<135.62881469726562,769.609130859375>-<131.8037109375,770.0091552734375>-<128.65362548828125,770.4091796875>>/L<<128.65362548828125,770.4091796875>--<128.65362548828125,770.4091796875>> = 7.237164810205877

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component breve)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component breve)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component breve)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Fstroke
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana and 331 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 564 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<651.0,219.0>--<646.0,0.0>> -> L<<646.0,0.0>--<646.0,-47.0>>

	* beta (U+03B2): L<<68.0,-229.0>--<71.0,112.0>> -> L<<71.0,112.0>--<66.0,509.0>>

	* cpalatalhook (U+A794): L<<503.0,105.0>--<503.0,105.0>> -> L<<503.0,105.0>--<503.0,105.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1053.0,189.0>--<1048.0,0.0>> -> L<<1048.0,0.0>--<1048.0,-35.0>>

	* rho (U+03C1): L<<51.0,-230.0>--<54.0,84.0>> -> L<<54.0,84.0>--<54.0,263.0>>

	* u10788 (U+10788): L<<684.4757080078125,400.3953857421875>--<681.2255859375,287.0>> -> L<<681.2255859375,287.0>--<681.2255859375,266.0008544921875>>

	* uni03BC (U+03BC): L<<68.0,-230.0>--<71.0,157.0>> -> L<<71.0,157.0>--<66.0,536.0>>

	* uni03FC (U+03FC): L<<52.0,-82.0>--<54.0,84.0>> -> L<<54.0,84.0>--<54.0,263.0>>

	* uni04B1 (U+04B1): L<<103.0,7.0>--<234.0,7.0>> -> L<<234.0,7.0>--<234.0,7.0>>

	* uni1D5D (U+1D5D): L<<44.20166015625,149.6055908203125>--<46.1517333984375,354.197265625>> -> L<<46.1517333984375,354.197265625>--<42.901611328125,592.3875732421875>>

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* eogonek (U+0119): B<<270.5,-58.5>-<297.0,-26.0>-<333.0,-9.0>>/B<<333.0,-9.0>-<329.0,-10.0>-<324.0,-10.0>> = 11.24147876762648

	* u107A0 (U+107A0): B<<165.1419677734375,503.70428466796875>-<161.2418212890625,519.003662109375>-<159.9417724609375,530.4031982421875>>/B<<159.9417724609375,530.4031982421875>-<158.6417236328125,517.2037353515625>-<154.7415771484375,505.2042236328125>> = 12.131196733131743

	* u107A1 (U+107A1): B<<165.106201171875,503.29119873046875>-<161.2060546875,518.590576171875>-<159.906005859375,529.9901123046875>>/B<<159.906005859375,529.9901123046875>-<158.60595703125,516.7906494140625>-<154.705810546875,504.7911376953125>> = 12.131196733131743

	* uni01B4 (U+01B4): B<<328.5,175.5>-<335.0,150.0>-<337.0,131.0>>/B<<337.0,131.0>-<339.0,153.0>-<345.0,173.0>> = 11.203434865229296

	* uni0233 (U+0233): B<<329.0,175.5>-<335.0,150.0>-<337.0,131.0>>/B<<337.0,131.0>-<339.0,153.0>-<345.0,173.0>> = 11.203434865229296

	* uni024F (U+024F): B<<329.0,175.5>-<335.0,150.0>-<337.0,131.0>>/B<<337.0,131.0>-<339.0,153.0>-<345.0,173.0>> = 11.203434865229296

	* uni028E (U+028E): B<<254.0,360.5>-<248.0,386.0>-<246.0,405.0>>/B<<246.0,405.0>-<244.0,383.0>-<238.0,363.0>> = 11.203434865229296

	* uni02B8 (U+02B8): B<<213.8580322265625,392.29571533203125>-<217.7581787109375,376.996337890625>-<219.0582275390625,365.5968017578125>>/B<<219.0582275390625,365.5968017578125>-<220.3582763671875,378.7962646484375>-<224.2584228515625,390.7957763671875>> = 12.131196733131743

	* uni0377 (U+0377): B<<443.5,261.5>-<460.0,318.0>-<487.0,376.0>>/L<<487.0,376.0>--<199.0,0.0>> = 12.487788400929684

	* uni03F0 (U+03F0): B<<255.0,221.5>-<239.0,183.0>-<226.0,159.0>>/L<<226.0,159.0>--<509.0,536.0>> = 8.451277793680566

	* 23 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<605.0,358.0>--<609.0,-230.0>>

	* etatonos (U+03AE): L<<605.0,358.0>--<609.0,-230.0>>

	* iota (U+03B9): L<<69.0,166.0>--<66.0,536.0>>

	* iotadieresis (U+03CA): L<<69.0,166.0>--<66.0,536.0>>

	* iotadieresistonos (U+0390): L<<69.0,166.0>--<66.0,536.0>>

	* iotatonos (U+03AF): L<<69.0,166.0>--<66.0,536.0>>

	* kappa (U+03BA): L<<49.0,0.0>--<46.0,536.0>>

	* sterling (U+00A3): L<<442.0,340.0>--<284.0,341.0>>

	* uni0269 (U+0269): L<<69.0,166.0>--<66.0,536.0>>

	* uni03BC (U+03BC): L<<388.0,235.0>--<386.0,536.0>>

	* 50 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* A
	* Aacute
	* Abreve
	* Acircumflex
	* Adieresis
	* Aglottal
	* Agrave
	* Alpha
	* Alphatonos
	* Amacron and 372 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 564 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* beta (U+03B2): L<<-53.0,-229.0>--<22.0,112.0>> -> L<<22.0,112.0>--<100.0,509.0>>

	* dzdigraphretroflexhook (U+AB66): L<<1026.0,189.0>--<982.0,1.0>> -> L<<982.0,1.0>--<976.0,-24.0>>

	* f_f (U+FB00): L<<338.0,536.0>--<500.0,536.0>> -> L<<500.0,536.0>--<500.0,536.0>>

	* f_f (U+FB00): L<<500.0,536.0>--<500.0,536.0>> -> L<<500.0,536.0>--<500.0,536.0>>

	* rho (U+03C1): L<<-77.0,-230.0>--<-8.0,84.0>> -> L<<-8.0,84.0>--<29.0,263.0>>

	* u10788 (U+10788): L<<717.925048828125,400.3953857421875>--<689.323974609375,287.5999755859375>> -> L<<689.323974609375,287.5999755859375>--<685.423828125,272.6005859375>>

	* uni03BC (U+03BC): L<<-51.0,-230.0>--<32.0,157.0>> -> L<<32.0,157.0>--<106.0,536.0>>

	* uni03FC (U+03FC): L<<-44.0,-82.0>--<-8.0,84.0>> -> L<<-8.0,84.0>--<29.0,263.0>>

	* uni1D0B (U+1D0B): L<<325.0,445.0>--<297.0,325.0>> -> L<<297.0,325.0>--<289.0,293.0>>

	* uni1D5D (U+1D5D): L<<18.5487060546875,149.6055908203125>--<67.300537109375,354.197265625>> -> L<<67.300537109375,354.197265625>--<118.00244140625,592.3875732421875>>

	* 9 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<521.5,402.5>-<476.0,378.0>-<419.0,371.0>>/B<<419.0,371.0>-<451.0,368.0>-<486.5,350.5>> = 12.357092600350505

	* uni0246 (U+0246): L<<319.0,341.0>--<271.0,116.0>>/L<<271.0,116.0>--<372.0,341.0>> = 12.132206814749741

	* uni03F0 (U+03F0): B<<317.5,231.0>-<297.0,181.0>-<276.0,136.0>>/L<<276.0,136.0>--<577.0,536.0>> = 11.944567460972712

	* uni046E (U+046E): B<<507.5,402.5>-<462.0,378.0>-<405.0,371.0>>/B<<405.0,371.0>-<437.0,368.0>-<473.0,350.5>> = 12.357092600350505

	* uni0498 (U+0498): B<<521.5,402.5>-<476.0,378.0>-<419.0,371.0>>/B<<419.0,371.0>-<451.0,368.0>-<486.5,350.5>> = 12.357092600350505

	* uni0506 (U+0506): B<<490.5,402.5>-<445.0,378.0>-<388.0,371.0>>/B<<388.0,371.0>-<409.0,369.0>-<434.0,364.0>> = 12.4415995885008

	* uni1D95 (U+1D95): L<<479.0,-35.0>--<522.0,215.0>>/B<<522.0,215.0>-<499.0,157.0>-<454.0,105.5>> = 11.871505568848043

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni211F (U+211F): L<<388.0,651.0>--<338.0,433.0>>/L<<338.0,433.0>--<436.0,651.0>> = 11.288072200562377

	* 5 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[16] NotoSerif-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredsmall
	* Ereversedmod
	* Tsereversedcy
	* exclamdown.sc
	* summationDoubleStruck.mir
	* tsereversedcy
	* u10780
	* u10784
	* uni018E
	* uni0281 and 143 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Noto Serif ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/fonttools/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<478.0,143.0>--<473.0,0.0>> -> L<<473.0,0.0>--<473.0,-98.0>>

	* beta (U+03B2): L<<59.0,-240.0>--<61.0,120.0>> -> L<<61.0,120.0>--<60.0,560.0>>

	* dzdigraphretroflexhook (U+AB66): L<<823.0,143.0>--<818.0,0.0>> -> L<<818.0,0.0>--<818.0,-93.0>>

	* rho (U+03C1): L<<44.0,-240.0>--<46.0,63.0>> -> L<<46.0,63.0>--<46.0,287.0>>

	* tripledagger (U+2E4B): L<<383.0,304.0>--<220.0,319.0>> -> L<<220.0,319.0>--<218.0,319.0>>

	* u10788 (U+10788): L<<534.9700927734375,372.7965087890625>--<531.719970703125,287.0>> -> L<<531.719970703125,287.0>--<531.719970703125,231.2022705078125>>

	* uni023E (U+023E): L<<449.0,684.0>--<447.0,684.0>> -> L<<447.0,684.0>--<306.0,684.0>>

	* uni0246 (U+0246): L<<414.0,684.0>--<410.0,684.0>> -> L<<410.0,684.0>--<189.0,684.0>>

	* uni0290 (U+0290): L<<413.0,143.0>--<408.0,0.0>> -> L<<408.0,0.0>--<408.0,-82.0>>

	* uni03BC (U+03BC): L<<59.0,-240.0>--<61.0,134.0>> -> L<<61.0,134.0>--<59.0,536.0>>

	* 13 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* eth (U+00F0): B<<356.5,474.5>-<399.0,456.0>-<423.0,417.0>>/B<<423.0,417.0>-<401.0,487.0>-<370.5,540.5>> = 14.160313822966648

	* uni1D7A (U+1D7A): B<<463.0,439.0>-<468.0,454.0>-<476.0,467.0>>/L<<476.0,467.0>--<461.0,447.0>> = 5.2623953995950545

	* uni1D7A (U+1D7A): L<<694.0,760.0>--<495.0,493.0>>/B<<495.0,493.0>-<515.0,515.0>-<547.5,529.0>> = 5.575850240977497

	* uni1D95 (U+1D95): L<<435.0,-87.0>--<435.0,229.0>>/B<<435.0,229.0>-<428.0,109.0>-<377.0,49.5>> = 3.338470543764357

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<59.0,-240.0>--<61.0,120.0>>

	* beta (U+03B2): L<<61.0,120.0>--<60.0,560.0>>

	* eta (U+03B7): L<<442.0,-240.0>--<447.0,354.0>>

	* eta (U+03B7): L<<485.0,356.0>--<489.0,-240.0>>

	* etatonos (U+03AE): L<<442.0,-240.0>--<447.0,354.0>>

	* etatonos (U+03AE): L<<485.0,356.0>--<489.0,-240.0>>

	* iota (U+03B9): L<<105.0,536.0>--<102.0,138.0>>

	* iota (U+03B9): L<<61.0,139.0>--<59.0,536.0>>

	* iotadieresis (U+03CA): L<<105.0,536.0>--<102.0,138.0>>

	* iotadieresis (U+03CA): L<<61.0,139.0>--<59.0,536.0>>

	* 136 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FCE0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* stackedcommadbl
	* summationDoubleStruck.mir
	* u10780
	* u10784
	* uni0409
	* uni1DF0F
	* uni20A5
	* uniA714
	* uniA716
	* uniA7D3
	* uniAB5A and uniFE27
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<491.0,143.0>--<457.0,9.0>> -> L<<457.0,9.0>--<435.0,-98.0>>

	* beta (U+03B2): L<<-41.0,-240.0>--<36.0,120.0>> -> L<<36.0,120.0>--<129.0,560.0>>

	* rho (U+03C1): L<<-61.0,-240.0>--<4.0,63.0>> -> L<<4.0,63.0>--<52.0,287.0>>

	* tripledagger (U+2E4B): L<<231.0,338.0>--<234.0,338.0>> -> L<<234.0,338.0>--<397.0,347.0>>

	* tripledagger (U+2E4B): L<<387.0,305.0>--<230.0,313.0>> -> L<<230.0,313.0>--<225.0,313.0>>

	* tripledagger (U+2E4B): L<<49.0,347.0>--<207.0,338.0>> -> L<<207.0,338.0>--<207.0,338.0>>

	* uni0246 (U+0246): L<<496.0,684.0>--<490.0,684.0>> -> L<<490.0,684.0>--<272.0,684.0>>

	* uni03BC (U+03BC): L<<-38.0,-240.0>--<42.0,134.0>> -> L<<42.0,134.0>--<124.0,536.0>>

	* uni03FC (U+03FC): L<<-28.0,-88.0>--<4.0,63.0>> -> L<<4.0,63.0>--<52.0,287.0>>

	* uni1D0B (U+1D0B): L<<176.0,451.0>--<141.0,285.0>> -> L<<141.0,285.0>--<130.0,232.0>>

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* three (U+0033): B<<427.5,442.5>-<381.0,387.0>-<288.0,375.0>>/B<<288.0,375.0>-<323.0,372.0>-<354.0,353.0>> = 12.251471813680151

	* uni0504 (U+0504): B<<404.5,401.5>-<364.0,375.0>-<314.0,368.0>>/B<<314.0,368.0>-<364.0,365.0>-<398.5,340.0>> = 11.403240756771877

	* uni1D95 (U+1D95): L<<313.0,-33.0>--<371.0,217.0>>/B<<371.0,217.0>-<354.0,156.0>-<320.0,104.0>> = 2.51099251348214

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uniA737 (U+A737): B<<334.0,119.5>-<336.0,132.0>-<339.0,145.0>>/B<<339.0,145.0>-<301.0,70.0>-<252.0,30.0>> = 13.87519629558255

	* uniA7A0 (U+A7A0): L<<650.0,354.0>--<492.0,319.0>>/L<<492.0,319.0>--<645.0,319.0>> = 12.49040571790919 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FCE0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredsmall
	* Dmiddlestroke
	* Euro
	* Hbar
	* Oslash
	* Oslashacute
	* Smiddlestroke
	* Ustroke
	* Wanglicana
	* colonmonetary and 83 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<553.0,175.0>--<518.0,29.0>> -> L<<518.0,29.0>--<498.0,-62.0>>

	* beta (U+03B2): L<<-38.0,-240.0>--<42.0,126.0>> -> L<<42.0,126.0>--<127.0,543.0>>

	* dzdigraphretroflexhook (U+AB66): L<<890.0,162.0>--<851.0,1.0>> -> L<<851.0,1.0>--<844.0,-31.0>>

	* f_f (U+FB00): L<<251.0,536.0>--<454.0,536.0>> -> L<<454.0,536.0>--<454.0,536.0>>

	* f_f (U+FB00): L<<454.0,536.0>--<454.0,536.0>> -> L<<454.0,536.0>--<455.0,536.0>>

	* rho (U+03C1): L<<-59.0,-240.0>--<17.0,109.0>> -> L<<17.0,109.0>--<47.0,253.0>>

	* u10788 (U+10788): L<<631.521728515625,384.196044921875>--<606.1707763671875,287.5999755859375>> -> L<<606.1707763671875,287.5999755859375>--<601.62060546875,268.4007568359375>>

	* uni03BC (U+03BC): L<<-34.0,-240.0>--<45.0,126.0>> -> L<<45.0,126.0>--<126.0,536.0>>

	* uni03FC (U+03FC): L<<-24.0,-80.0>--<17.0,109.0>> -> L<<17.0,109.0>--<47.0,253.0>>

	* uni049D (U+049D): L<<200.0,294.0>--<252.0,294.0>> -> L<<252.0,294.0>--<252.0,294.0>>

	* 10 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<473.5,399.0>-<427.0,374.0>-<370.0,367.0>>/B<<370.0,367.0>-<402.0,364.0>-<437.5,347.0>> = 12.357092600350505

	* uni03D0 (U+03D0): B<<316.0,703.0>-<273.0,681.0>-<238.0,624.0>>/L<<238.0,624.0>--<240.0,627.0>> = 2.1386825776662226

	* uni046E (U+046E): B<<473.5,399.0>-<427.0,374.0>-<370.0,367.0>>/B<<370.0,367.0>-<402.0,364.0>-<437.5,347.0>> = 12.357092600350505

	* uni0498 (U+0498): B<<473.5,399.0>-<427.0,374.0>-<370.0,367.0>>/B<<370.0,367.0>-<402.0,364.0>-<437.5,347.0>> = 12.357092600350505

	* uni0504 (U+0504): B<<438.5,399.0>-<392.0,374.0>-<335.0,367.0>>/B<<335.0,367.0>-<357.0,365.0>-<382.5,358.0>> = 12.19569646523012

	* uni0506 (U+0506): B<<438.5,399.0>-<392.0,374.0>-<335.0,367.0>>/B<<335.0,367.0>-<357.0,365.0>-<382.5,358.0>> = 12.19569646523012

	* uni1D95 (U+1D95): L<<374.0,-49.0>--<431.0,223.0>>/B<<431.0,223.0>-<412.0,163.0>-<374.5,110.0>> = 5.735691697844572

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni211F (U+211F): L<<242.0,315.0>--<203.0,134.0>>/L<<203.0,134.0>--<284.0,315.0>> = 11.949579509065014

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uniA7A0 (U+A7A0): L<<694.0,372.0>--<503.0,330.0>>/L<<503.0,330.0>--<698.0,330.0>> = 12.40169581672131 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredsmall
	* Ereversedmod
	* Tsereversedcy
	* Ustroke
	* colonmonetary
	* exclamdown.sc
	* summationDoubleStruck.mir
	* tsereversedcy
	* u10780
	* u10784 and 167 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<508.0,157.0>--<503.0,0.0>> -> L<<503.0,0.0>--<503.0,-83.0>>

	* beta (U+03B2): L<<63.0,-240.0>--<65.0,122.0>> -> L<<65.0,122.0>--<64.0,553.0>>

	* dzdigraphretroflexhook (U+AB66): L<<858.0,151.0>--<853.0,0.0>> -> L<<853.0,0.0>--<853.0,-80.0>>

	* rho (U+03C1): L<<48.0,-240.0>--<50.0,83.0>> -> L<<50.0,83.0>--<50.0,273.0>>

	* u10788 (U+10788): L<<557.720947265625,377.5963134765625>--<554.4708251953125,287.0>> -> L<<554.4708251953125,287.0>--<554.4708251953125,239.001953125>>

	* uni0290 (U+0290): L<<431.0,151.0>--<426.0,0.0>> -> L<<426.0,0.0>--<426.0,-68.0>>

	* uni03BC (U+03BC): L<<64.0,-240.0>--<66.0,131.0>> -> L<<66.0,131.0>--<63.0,536.0>>

	* uni03FC (U+03FC): L<<49.0,-85.0>--<50.0,83.0>> -> L<<50.0,83.0>--<50.0,273.0>>

	* uni04B1 (U+04B1): L<<312.0,0.0>--<312.0,0.0>> -> L<<312.0,0.0>--<438.0,0.0>>

	* uni1D5D (U+1D5D): L<<40.9515380859375,143.005859375>--<42.2515869140625,360.197021484375>> -> L<<42.2515869140625,360.197021484375>--<41.6015625,618.7864990234375>>

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni1D95 (U+1D95): L<<453.0,-71.0>--<453.0,226.0>>/B<<453.0,226.0>-<445.0,108.0>-<391.5,49.0>> = 3.8785245028476374

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2C66 (U+2C66): B<<159.0,137.0>-<159.0,130.0>-<159.0,124.0>>/L<<159.0,124.0>--<243.0,494.0>> = 12.790879201158143

	* uniA7A0 (U+A7A0): L<<676.0,376.0>--<456.0,326.0>>/L<<456.0,326.0>--<669.0,326.0>> = 12.80426606528674 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<63.0,-240.0>--<65.0,122.0>>

	* beta (U+03B2): L<<65.0,122.0>--<64.0,553.0>>

	* eta (U+03B7): L<<191.0,326.0>--<193.0,0.0>>

	* eta (U+03B7): L<<509.0,353.0>--<513.0,-240.0>>

	* etatonos (U+03AE): L<<191.0,326.0>--<193.0,0.0>>

	* etatonos (U+03AE): L<<509.0,353.0>--<513.0,-240.0>>

	* iota (U+03B9): L<<65.0,141.0>--<63.0,536.0>>

	* iotadieresis (U+03CA): L<<65.0,141.0>--<63.0,536.0>>

	* iotadieresistonos (U+0390): L<<65.0,141.0>--<63.0,536.0>>

	* iotatonos (U+03AF): L<<65.0,141.0>--<63.0,536.0>>

	* 92 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FCE0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredsmall
	* Ustroke
	* summationDoubleStruck.mir
	* u10780
	* u10784
	* uni023A
	* uni023E
	* uni0409
	* uni0416
	* uni0424 and 17 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<517.0,156.0>--<483.0,19.0>> -> L<<483.0,19.0>--<462.0,-83.0>>

	* beta (U+03B2): L<<-40.0,-240.0>--<39.0,122.0>> -> L<<39.0,122.0>--<128.0,553.0>>

	* f_f (U+FB00): L<<221.0,536.0>--<439.0,536.0>> -> L<<439.0,536.0>--<439.0,536.0>>

	* f_f (U+FB00): L<<439.0,536.0>--<439.0,536.0>> -> L<<439.0,536.0>--<439.0,536.0>>

	* rho (U+03C1): L<<-60.0,-240.0>--<10.0,83.0>> -> L<<10.0,83.0>--<50.0,273.0>>

	* s_t (U+FB06): L<<403.0,443.0>--<403.0,443.0>> -> L<<403.0,443.0>--<403.0,443.0>>

	* tripledagger (U+2E4B): L<<242.0,339.0>--<249.0,339.0>> -> L<<249.0,339.0>--<416.0,355.0>>

	* uni0246 (U+0246): L<<494.0,675.0>--<488.0,675.0>> -> L<<488.0,675.0>--<291.0,675.0>>

	* uni03BC (U+03BC): L<<-36.0,-240.0>--<43.0,131.0>> -> L<<43.0,131.0>--<125.0,536.0>>

	* uni03FC (U+03FC): L<<-27.0,-85.0>--<10.0,83.0>> -> L<<10.0,83.0>--<50.0,273.0>>

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni0504 (U+0504): B<<419.0,401.0>-<376.0,375.0>-<323.0,367.0>>/B<<323.0,367.0>-<354.0,365.0>-<384.5,353.5>> = 12.275007466565206

	* uni1D95 (U+1D95): L<<339.0,-40.0>--<396.0,220.0>>/B<<396.0,220.0>-<378.0,159.0>-<342.5,106.5>> = 4.075006763141359

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni210B (U+210B): B<<466.5,433.0>-<506.0,504.0>-<569.0,581.0>>/B<<569.0,581.0>-<545.0,559.0>-<515.5,535.0>> = 8.200146059498772

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uniA7A0 (U+A7A0): L<<669.0,362.0>--<497.0,324.0>>/L<<497.0,324.0>--<668.0,324.0>> = 12.458246440004897 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component breve)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component breve)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component breve)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Fstroke
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana and 255 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<570.0,184.0>--<565.0,0.0>> -> L<<565.0,0.0>--<565.0,-62.0>>

	* beta (U+03B2): L<<69.0,-240.0>--<73.0,126.0>> -> L<<73.0,126.0>--<69.0,539.0>>

	* dzdigraphretroflexhook (U+AB66): L<<934.0,167.0>--<929.0,0.0>> -> L<<929.0,0.0>--<929.0,-59.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<56.0,113.0>> -> L<<56.0,113.0>--<56.0,256.0>>

	* u10788 (U+10788): L<<607.122802734375,387.1959228515625>--<603.8726806640625,287.0>> -> L<<603.8726806640625,287.0>--<603.8726806640625,251.6014404296875>>

	* uni0290 (U+0290): L<<466.0,167.0>--<463.0,0.0>> -> L<<463.0,0.0>--<463.0,-46.0>>

	* uni03BC (U+03BC): L<<70.0,-240.0>--<74.0,112.0>> -> L<<74.0,112.0>--<68.0,536.0>>

	* uni03FC (U+03FC): L<<54.0,-80.0>--<56.0,113.0>> -> L<<56.0,113.0>--<56.0,256.0>>

	* uni1D5D (U+1D5D): L<<44.8516845703125,143.005859375>--<47.4517822265625,362.596923828125>> -> L<<47.4517822265625,362.596923828125>--<44.8516845703125,610.3868408203125>>

	* uni1D66 (U+1D66): L<<44.8516845703125,-143.994140625>--<47.4517822265625,75.596923828125>> -> L<<47.4517822265625,75.596923828125>--<44.8516845703125,323.3868408203125>>

	* 7 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* onequarter (U+00BC): B<<636.5,319.5>-<638.0,338.0>-<640.0,356.0>>/B<<640.0,356.0>-<637.0,348.0>-<632.5,339.5>> = 14.21585347367354

	* threequarters (U+00BE): B<<636.5,319.5>-<638.0,338.0>-<640.0,356.0>>/B<<640.0,356.0>-<637.0,348.0>-<632.5,339.5>> = 14.21585347367354

	* uni03D7 (U+03D7): B<<550.0,28.0>-<548.0,26.0>-<546.0,25.0>>/L<<546.0,25.0>--<555.0,28.0>> = 8.13010235415587

	* uni1D95 (U+1D95): L<<490.0,-46.0>--<490.0,221.0>>/B<<490.0,221.0>-<479.0,106.0>-<420.5,48.0>> = 5.463842813236589

	* uni2074 (U+2074): B<<198.5,706.5>-<200.0,725.0>-<202.0,743.0>>/B<<202.0,743.0>-<199.0,735.0>-<194.5,726.5>> = 14.21585347367354

	* uni2084 (U+2084): B<<198.5,221.5>-<200.0,240.0>-<202.0,258.0>>/B<<202.0,258.0>-<199.0,250.0>-<194.5,241.5>> = 14.21585347367354

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2158 (U+2158): B<<198.5,606.5>-<200.0,625.0>-<202.0,643.0>>/B<<202.0,643.0>-<199.0,635.0>-<194.5,626.5>> = 14.21585347367354

	* uni2C66 (U+2C66): L<<205.0,476.0>--<205.0,282.0>>/L<<205.0,282.0>--<252.0,476.0>> = 13.618541661441057

	* uniA7A0 (U+A7A0): L<<708.0,377.0>--<506.0,332.0>>/L<<506.0,332.0>--<708.0,332.0>> = 12.558836940947579 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Lstrokesmall (U+1D0C): L<<475.0,171.0>--<474.0,0.0>>

	* eta (U+03B7): L<<236.0,317.0>--<237.0,0.0>>

	* eta (U+03B7): L<<552.0,352.0>--<556.0,-240.0>>

	* etatonos (U+03AE): L<<236.0,317.0>--<237.0,0.0>>

	* etatonos (U+03AE): L<<552.0,352.0>--<556.0,-240.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<56.0,113.0>>

	* sterling (U+00A3): L<<408.0,339.0>--<251.0,340.0>>

	* uni03BC (U+03BC): L<<391.0,191.0>--<388.0,536.0>>

	* uni03DD (U+03DD): L<<410.0,227.0>--<411.0,92.0>>

	* uni04AC (U+04AC): L<<370.0,661.0>--<369.0,111.0>>

	* 51 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Euro
	* Fstroke
	* Hbar
	* Oslash
	* Oslashacute
	* Smiddlestroke
	* Ustroke and 106 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<572.0,184.0>--<533.0,21.0>> -> L<<533.0,21.0>--<515.0,-62.0>>

	* beta (U+03B2): L<<-41.0,-240.0>--<39.0,126.0>> -> L<<39.0,126.0>--<122.0,539.0>>

	* dzdigraphretroflexhook (U+AB66): L<<917.0,167.0>--<877.0,3.0>> -> L<<877.0,3.0>--<870.0,-30.0>>

	* f_f (U+FB00): L<<268.0,536.0>--<463.0,536.0>> -> L<<463.0,536.0>--<463.0,536.0>>

	* f_f (U+FB00): L<<463.0,536.0>--<463.0,536.0>> -> L<<463.0,536.0>--<464.0,536.0>>

	* rho (U+03C1): L<<-63.0,-240.0>--<14.0,113.0>> -> L<<14.0,113.0>--<44.0,256.0>>

	* s_t (U+FB06): L<<451.0,451.0>--<451.0,451.0>> -> L<<451.0,451.0>--<451.0,451.0>>

	* u10788 (U+10788): L<<649.0723876953125,387.1959228515625>--<623.0714111328125,288.7999267578125>> -> L<<623.0714111328125,288.7999267578125>--<618.521240234375,269.000732421875>>

	* uni023E (U+023E): L<<547.0,661.0>--<546.0,661.0>> -> L<<546.0,661.0>--<454.0,661.0>>

	* uni03BC (U+03BC): L<<-38.0,-240.0>--<39.0,112.0>> -> L<<39.0,112.0>--<122.0,536.0>>

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<482.5,400.0>-<436.0,375.0>-<380.0,368.0>>/B<<380.0,368.0>-<412.0,364.0>-<447.5,347.5>> = 14.250032697803546

	* onequarter (U+00BC): B<<688.5,318.5>-<694.0,337.0>-<699.0,356.0>>/B<<699.0,356.0>-<694.0,347.0>-<683.5,334.0>> = 14.311041262606366

	* threequarters (U+00BE): B<<688.5,318.5>-<694.0,337.0>-<699.0,356.0>>/B<<699.0,356.0>-<694.0,347.0>-<683.5,334.0>> = 14.311041262606366

	* uni046E (U+046E): B<<479.5,400.0>-<433.0,375.0>-<377.0,368.0>>/B<<377.0,368.0>-<409.0,364.0>-<444.5,347.5>> = 14.250032697803546

	* uni0498 (U+0498): B<<482.5,400.0>-<436.0,375.0>-<380.0,368.0>>/B<<380.0,368.0>-<412.0,364.0>-<447.5,347.5>> = 14.250032697803546

	* uni0504 (U+0504): B<<448.5,400.0>-<402.0,375.0>-<345.0,368.0>>/B<<345.0,368.0>-<377.0,364.0>-<411.5,350.5>> = 14.126283906397104

	* uni0506 (U+0506): B<<448.5,400.0>-<402.0,375.0>-<345.0,368.0>>/B<<345.0,368.0>-<367.0,366.0>-<392.5,359.5>> = 12.19569646523012

	* uni1D95 (U+1D95): L<<395.0,-46.0>--<449.0,221.0>>/B<<449.0,221.0>-<429.0,162.0>-<390.0,109.0>> = 7.292106579845833

	* uni2074 (U+2074): B<<276.5,705.5>-<282.0,724.0>-<287.0,743.0>>/B<<287.0,743.0>-<282.0,734.0>-<271.5,721.0>> = 14.311041262606366

	* uni2084 (U+2084): B<<186.5,219.5>-<192.0,238.0>-<197.0,257.0>>/B<<197.0,257.0>-<192.0,248.0>-<181.5,235.0>> = 14.311041262606366

	* 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component tonos)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component tonos)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana
	* Yerubackyercy
	* colonmonetary and 239 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 43 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<550.0,175.0>--<545.0,0.0>> -> L<<545.0,0.0>--<545.0,-62.0>>

	* beta (U+03B2): L<<68.0,-240.0>--<71.0,126.0>> -> L<<71.0,126.0>--<69.0,543.0>>

	* dzdigraphretroflexhook (U+AB66): L<<905.0,162.0>--<900.0,0.0>> -> L<<900.0,0.0>--<900.0,-62.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<56.0,109.0>> -> L<<56.0,109.0>--<56.0,253.0>>

	* u10788 (U+10788): L<<588.2720947265625,384.196044921875>--<585.02197265625,287.0>> -> L<<585.02197265625,287.0>--<585.02197265625,249.801513671875>>

	* uni0290 (U+0290): L<<455.0,162.0>--<450.0,0.0>> -> L<<450.0,0.0>--<450.0,-49.0>>

	* uni03BC (U+03BC): L<<70.0,-240.0>--<73.0,126.0>> -> L<<73.0,126.0>--<68.0,536.0>>

	* uni03FC (U+03FC): L<<54.0,-80.0>--<56.0,109.0>> -> L<<56.0,109.0>--<56.0,253.0>>

	* uni051F (U+051F): L<<284.0,300.0>--<356.0,385.0>> -> L<<356.0,385.0>--<357.0,386.0>>

	* uni1D5D (U+1D5D): L<<44.20166015625,143.005859375>--<46.1517333984375,362.596923828125>> -> L<<46.1517333984375,362.596923828125>--<44.8516845703125,612.7867431640625>>

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni03D0 (U+03D0): B<<264.0,703.5>-<224.0,682.0>-<197.0,625.0>>/L<<197.0,625.0>--<198.0,627.0>> = 1.2188752351310335

	* uni03D7 (U+03D7): B<<531.0,29.0>-<527.0,26.0>-<524.0,24.0>>/L<<524.0,24.0>--<536.0,29.0>> = 11.070202577939344

	* uni1D95 (U+1D95): L<<478.0,-49.0>--<478.0,223.0>>/B<<478.0,223.0>-<468.0,107.0>-<411.5,48.5>> = 4.927109947648964

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2C66 (U+2C66): L<<189.0,479.0>--<189.0,209.0>>/L<<189.0,209.0>--<250.0,479.0>> = 12.730868789806387

	* uniA7A0 (U+A7A0): L<<695.0,373.0>--<503.0,330.0>>/L<<503.0,330.0>--<695.0,330.0>> = 12.623563597702594 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<68.0,-240.0>--<71.0,126.0>>

	* beta (U+03B2): L<<71.0,126.0>--<69.0,543.0>>

	* eta (U+03B7): L<<542.0,350.0>--<546.0,-240.0>>

	* etatonos (U+03AE): L<<542.0,350.0>--<546.0,-240.0>>

	* iota (U+03B9): L<<71.0,145.0>--<68.0,536.0>>

	* iotadieresis (U+03CA): L<<71.0,145.0>--<68.0,536.0>>

	* iotadieresistonos (U+0390): L<<71.0,145.0>--<68.0,536.0>>

	* iotatonos (U+03AF): L<<71.0,145.0>--<68.0,536.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<56.0,109.0>>

	* tau (U+03C4): L<<293.0,453.0>--<295.0,142.0>>

	* 53 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component breve)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component breve)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component breve)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dmiddlestroke
	* Ereversedmod
	* Euro
	* Fstroke
	* Smiddlestroke
	* Tsereversedcy
	* Ustroke
	* Wanglicana and 287 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 39 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Cpalatalhook (U+A7C4): L<<608.0,114.0>--<608.0,114.0>> -> L<<608.0,114.0>--<608.0,114.0>>

	* Zpalatalhook (U+A7C6): L<<595.0,194.0>--<590.0,0.0>> -> L<<590.0,0.0>--<590.0,-61.0>>

	* beta (U+03B2): L<<71.0,-240.0>--<75.0,126.0>> -> L<<75.0,126.0>--<68.0,533.0>>

	* dzdigraphretroflexhook (U+AB66): L<<970.0,174.0>--<965.0,0.0>> -> L<<965.0,0.0>--<965.0,-55.0>>

	* rho (U+03C1): L<<53.0,-240.0>--<57.0,117.0>> -> L<<57.0,117.0>--<57.0,259.0>>

	* u10788 (U+10788): L<<630.523681640625,391.395751953125>--<627.2735595703125,287.0>> -> L<<627.2735595703125,287.0>--<627.2735595703125,254.0013427734375>>

	* uni0290 (U+0290): L<<480.0,174.0>--<479.0,0.0>> -> L<<479.0,0.0>--<479.0,-43.0>>

	* uni03BC (U+03BC): L<<71.0,-240.0>--<74.0,94.0>> -> L<<74.0,94.0>--<68.0,536.0>>

	* uni03FC (U+03FC): L<<55.0,-81.0>--<57.0,117.0>> -> L<<57.0,117.0>--<57.0,259.0>>

	* uni04FF (U+04FF): L<<253.0,269.0>--<252.0,269.0>> -> L<<252.0,269.0>--<78.0,269.0>>

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni03F0 (U+03F0): B<<228.0,261.0>-<212.0,203.0>-<195.0,164.0>>/L<<195.0,164.0>--<478.0,536.0>> = 13.709896766824125

	* uni1D95 (U+1D95): L<<505.0,-43.0>--<505.0,219.0>>/B<<505.0,219.0>-<493.0,105.0>-<432.5,47.5>> = 6.009005957494474

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565

	* uni2C66 (U+2C66): L<<226.0,472.0>--<226.0,362.0>>/L<<226.0,362.0>--<254.0,472.0>> = 14.281095735970814

	* uniA7A0 (U+A7A0): L<<724.0,382.0>--<509.0,334.0>>/L<<509.0,334.0>--<724.0,334.0>> = 12.585228941050142 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* eta (U+03B7): L<<247.0,313.0>--<249.0,0.0>>

	* eta (U+03B7): L<<564.0,354.0>--<569.0,-240.0>>

	* etatonos (U+03AE): L<<247.0,313.0>--<249.0,0.0>>

	* etatonos (U+03AE): L<<564.0,354.0>--<569.0,-240.0>>

	* h (U+0068): L<<104.0,119.0>--<103.0,648.0>>

	* h (U+0068): L<<233.0,313.0>--<234.0,115.0>>

	* hcircumflex (U+0125): L<<104.0,119.0>--<103.0,648.0>>

	* hcircumflex (U+0125): L<<233.0,313.0>--<234.0,115.0>>

	* hpalatalhook (U+A795): L<<104.0,119.0>--<103.0,648.0>>

	* hpalatalhook (U+A795): L<<233.0,313.0>--<234.0,115.0>>

	* 81 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component breve)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* kavykawithdotlow (component medievalcomma)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Bbarredmod
	* Bbarredsmall
	* Dcroat
	* Dmiddlestroke
	* Dtail
	* Eth
	* Euro
	* Fstroke
	* Hbar
	* Lslash and 169 more.

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

	- l + f.ss02 [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<595.0,194.0>--<552.0,12.0>> -> L<<552.0,12.0>--<536.0,-61.0>>

	* beta (U+03B2): L<<-44.0,-240.0>--<36.0,126.0>> -> L<<36.0,126.0>--<116.0,533.0>>

	* dzdigraphretroflexhook (U+AB66): L<<950.0,174.0>--<910.0,4.0>> -> L<<910.0,4.0>--<902.0,-28.0>>

	* rho (U+03C1): L<<-68.0,-240.0>--<10.0,117.0>> -> L<<10.0,117.0>--<40.0,259.0>>

	* u10788 (U+10788): L<<669.523193359375,391.395751953125>--<643.522216796875,289.39990234375>> -> L<<643.522216796875,289.39990234375>--<638.322021484375,270.20068359375>>

	* u1079C (U+1079C): L<<138.00341796875,445.3935546875>--<139.9534912109375,452.59326171875>> -> L<<139.9534912109375,452.59326171875>--<142.5535888671875,462.7928466796875>>

	* uni03BC (U+03BC): L<<-43.0,-240.0>--<31.0,94.0>> -> L<<31.0,94.0>--<117.0,536.0>>

	* uni03FC (U+03FC): L<<-33.0,-81.0>--<10.0,117.0>> -> L<<10.0,117.0>--<40.0,259.0>>

	* uni049D (U+049D): L<<222.0,300.0>--<263.0,300.0>> -> L<<263.0,300.0>--<263.0,300.0>>

	* uni1D0B (U+1D0B): L<<279.0,444.0>--<251.0,319.0>> -> L<<251.0,319.0>--<242.0,277.0>>

	* 10 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eopenreversed (U+A7AB): B<<494.5,401.0>-<448.0,376.0>-<392.0,369.0>>/B<<392.0,369.0>-<424.0,365.0>-<459.5,348.0>> = 14.250032697803546

	* onequarter (U+00BC): B<<694.5,316.0>-<700.0,333.0>-<705.0,352.0>>/B<<705.0,352.0>-<700.0,343.0>-<691.5,332.5>> = 14.311041262606366

	* threequarters (U+00BE): B<<694.5,316.0>-<700.0,333.0>-<705.0,352.0>>/B<<705.0,352.0>-<700.0,343.0>-<691.5,332.5>> = 14.311041262606366

	* uni03F0 (U+03F0): B<<280.5,279.0>-<255.0,207.0>-<221.0,135.0>>/L<<221.0,135.0>--<547.0,536.0>> = 13.832270246884178

	* uni046E (U+046E): B<<488.0,401.0>-<442.0,376.0>-<386.0,369.0>>/B<<386.0,369.0>-<418.0,365.0>-<453.5,348.0>> = 14.250032697803546

	* uni0498 (U+0498): B<<494.5,401.0>-<448.0,376.0>-<392.0,369.0>>/B<<392.0,369.0>-<424.0,365.0>-<459.5,348.0>> = 14.250032697803546

	* uni0506 (U+0506): B<<461.5,401.0>-<415.0,376.0>-<359.0,369.0>>/B<<359.0,369.0>-<380.0,367.0>-<405.5,360.5>> = 12.565348379907268

	* uni1D95 (U+1D95): L<<421.0,-43.0>--<471.0,219.0>>/B<<471.0,219.0>-<450.0,160.0>-<409.5,107.5>> = 8.78788729351228

	* uni1DEC (U+1DEC): L<<65.1016845703125,764.4088134765625>--<65.1016845703125,764.0087890625>>/L<<65.1016845703125,764.0087890625>--<73.201904296875,797.61083984375>> = 13.553321491847997

	* uni2074 (U+2074): B<<283.5,703.0>-<289.0,720.0>-<294.0,739.0>>/B<<294.0,739.0>-<289.0,730.0>-<280.5,719.5>> = 14.311041262606366

	* 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* questiondown (component question)
* uni207F (component n)
* uni0500 (component P)
* uni018D (component delta)
* uni018E (component E)
* uni0250 (component a)
* uni0279 (component r)
* uni0281 (component uni0280)
* uni0287 (component t)
* uni028C (component v)
* uni028D (component w)
* uni028E (component y)
* uni0295 (component uni0294)
* uni0296 (component uni0294)
* uni029E (component k)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component r)
* uni02B5 (component uni027B)
* uni02B6 (component uni0280)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0294)
* uni02F5 (component hungarumlaut)
* uni0375 (component uni0374)
* aeturned (component ae)
* eturnedopen (component uni0511)
* osideways (component o)
* osidewaysopen (component c)
* oslashsideways (component oslash)
* oeturned (component oe)
* usideways (component u)
* udieresissideways (component u)
* udieresissideways (component dieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component a)
* uni1D45 (component uni0251)
* aeturnedmod (component ae)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni0511)
* eturnedopenmod (component uni0511)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* usidewaysmod (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D78 (component uni043D)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component iota)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni04E9)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component v)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni04E1)
* uni1DBF (component theta)
* uni1F02 (component tonos)
* uni1F03 (component tonos)
* uni1F0A (component tonos)
* uni1F0B (component tonos)
* uni1F12 (component tonos)
* uni1F13 (component tonos)
* uni1F1A (component tonos)
* uni1F1B (component tonos)
* uni1F22 (component tonos)
* uni1F23 (component tonos)
* uni1F2A (component tonos)
* uni1F2B (component tonos)
* uni1F32 (component tonos)
* uni1F33 (component tonos)
* uni1F3A (component tonos)
* uni1F3B (component tonos)
* uni1F42 (component tonos)
* uni1F43 (component tonos)
* uni1F4A (component tonos)
* uni1F4B (component tonos)
* uni1F52 (component tonos)
* uni1F53 (component tonos)
* uni1F5B (component tonos)
* uni1F62 (component tonos)
* uni1F63 (component tonos)
* uni1F6A (component tonos)
* uni1F6B (component tonos)
* uni1F70 (component tonos)
* uni1F72 (component tonos)
* uni1F74 (component tonos)
* uni1F76 (component tonos)
* uni1F78 (component tonos)
* uni1F7A (component tonos)
* uni1F7C (component tonos)
* uni1F82 (component tonos)
* uni1F83 (component tonos)
* uni1F8A (component tonos)
* uni1F8B (component tonos)
* uni1F92 (component tonos)
* uni1F93 (component tonos)
* uni1F9A (component tonos)
* uni1F9B (component tonos)
* uni1FA2 (component tonos)
* uni1FA3 (component tonos)
* uni1FAA (component tonos)
* uni1FAB (component tonos)
* uni1FB2 (component tonos)
* uni1FBA (component tonos)
* uni1FC2 (component tonos)
* uni1FC8 (component tonos)
* uni1FCA (component tonos)
* uni1FCD (component tonos)
* uni1FDA (component tonos)
* uni1FDD (component tonos)
* uni1FEA (component tonos)
* uni1FEF (component tonos)
* uni1FF2 (component tonos)
* uni1FF8 (component tonos)
* uni1FFA (component tonos)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni03B1030403130300 (component tonos)
* uni03B1030403140300 (component tonos)
* uni03B1030603130300 (component tonos)
* uni03B1030603130301 (component breve)
* uni03B1030603140300 (component tonos)
* uni03B1030603140301 (component breve)
* uni03B9030403130300 (component tonos)
* uni03B9030403140300 (component tonos)
* uni03B9030603130300 (component tonos)
* uni03B9030603130301 (component breve)
* uni03B9030603140300 (component tonos)
* uni03B9030603140301 (component breve)
* uni03C5030403130300 (component tonos)
* uni03C5030403140300 (component tonos)
* uni03C5030603130300 (component tonos)
* uni03C5030603130301 (component breve)
* uni03C5030603140300 (component tonos)
* uni03C5030603140301 (component breve)
* psilivaria_macronmod (component tonos)
* dasiavaria_macronmod (component tonos)
* uni1FDE0306 (component breve)
* uni1FDD0306 (component tonos)
* uni1FCE0306 (component breve)
* uni1FCD0306 (component tonos)
* uni2C6F (component A)
* uniA76E (component uni1EFC)
* uniA77E (component uniA77D)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* uniA730 (component uni214E)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7F7 (component I)
* uniA7FB (component F)
* uniA7FC (component P)
* uniA7FD (component M)
* Tsereversedcy (component uni0426)
* tsereversedcy (component uni0446)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA66E (component omonocularcy)
* uniA69C (component uni044A)
* uniA69D (component uni044C)
* uni2132 (component F)
* uniAB40 (component oe)
* uniAB51 (component uniAB50)
* uniAB64 (component uni0251)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniA7F9 (component oe)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E2E (component question)
* uni204F (component semicolon)
* uni2E32 (component comma)
* uni2E38 (component dagger)
* uni2E35 (component semicolon)
* uni2E15 (component uni2E14)
* uni2036 (component minute)
* uni2036 (component minute)
* uni2035 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* uni2037 (component minute)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni2127 (component uni03A9)
* uni214B (component ampersand)
* uni213A (component Q)
* uni2129 (component iota)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component a)
* uni1DF2 (component dieresis)
* uni1DF3 (component o)
* uni1DF3 (component dieresis)
* uni1DF4 (component u)
* uni1DF4 (component dieresis)
* uniFE2A (component uniFE22)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA678 (component uni044A)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69F (component uni0465)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component c)
* uni1DD7 (component cedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* uni2C7D (component V)
* uni1DFC (component uni035C)
* uni2C70 (component uni2C6D)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniA69E (component uni0444)
* summationDoubleStruck.mir (component uni2140)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* uniA704 (component uniA700)
* uniA705 (component uniA701)
* uniA706 (component uniA700)
* uniA707 (component uniA701)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* wbelowcomb (component w)
* wturnedbelowcomb (component w)
* wturnedmod (component w)
* uni1F8A.ad (component tonos)
* uni1F8B.ad (component tonos)
* uni1F9A.ad (component tonos)
* uni1F9B.ad (component tonos)
* uni1FAA.ad (component tonos)
* uni1FAB.ad (component tonos)
* uni1F02.sc.ss06 (component tonos)
* uni1F03.sc.ss06 (component tonos)
* uni1F70.sc.ss06 (component tonos)
* uni1FB2.sc.ss06 (component tonos)
* uni1F82.sc.ss06 (component tonos)
* uni1F83.sc.ss06 (component tonos)
* uni1F12.sc.ss06 (component tonos)
* uni1F13.sc.ss06 (component tonos)
* uni1F72.sc.ss06 (component tonos)
* uni1F22.sc.ss06 (component tonos)
* uni1F23.sc.ss06 (component tonos)
* uni1F74.sc.ss06 (component tonos)
* uni1FC2.sc.ss06 (component tonos)
* uni1F92.sc.ss06 (component tonos)
* uni1F93.sc.ss06 (component tonos)
* uni1F32.sc.ss06 (component tonos)
* uni1F33.sc.ss06 (component tonos)
* uni1F76.sc.ss06 (component tonos)
* uni1F42.sc.ss06 (component tonos)
* uni1F43.sc.ss06 (component tonos)
* uni1F78.sc.ss06 (component tonos)
* uni1F52.sc.ss06 (component tonos)
* uni1F53.sc.ss06 (component tonos)
* uni1F7A.sc.ss06 (component tonos)
* uni1F62.sc.ss06 (component tonos)
* uni1F63.sc.ss06 (component tonos)
* uni1F7C.sc.ss06 (component tonos)
* uni1FF2.sc.ss06 (component tonos)
* uni1FA2.sc.ss06 (component tonos)
* uni1FA3.sc.ss06 (component tonos)
* uni1FB2.sc.ad.ss06 (component tonos)
* uni1F82.sc.ad.ss06 (component tonos)
* uni1F83.sc.ad.ss06 (component tonos)
* uni1FC2.sc.ad.ss06 (component tonos)
* uni1F92.sc.ad.ss06 (component tonos)
* uni1F93.sc.ad.ss06 (component tonos)
* uni1FF2.sc.ad.ss06 (component tonos)
* uni1FA2.sc.ad.ss06 (component tonos)
* uni1FA3.sc.ad.ss06 (component tonos)
* uni10FB (component uni2056)
* uni1FDD.case (component tonos)
* uni1FEF.case (component tonos)
* uni1FCD.case (component tonos)
* uni1FCD.sc (component tonos)
* uni1FDD.sc (component tonos)
* uni1FEF.sc (component tonos)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* som (component uni0331)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component y)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni0475)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component O)
* u107B5 (component periodcentered)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component exclam)
* u107B9 (component uni0322)
* u107BA (component u1DF1E)
* uni1DF01 (component uni0261)
* uni1DF02 (component g.sc)
* uni1DF03 (component k)
* uni1DF07 (component eng)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Ereversedmod
	* Tsereversedcy
	* exclamdown.sc
	* stackedcommadbl
	* summationDoubleStruck.mir
	* tsereversedcy
	* u10780
	* uni018E
	* uni0281
	* uni0295 and 140 more.

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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- acutecomb.loclCYR.cap

	- beta.alt1

	- dasiaoxia_macronmod

	- dasiavaria_macronmod

	- psilioxia_macronmod

	- psilivaria_macronmod

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- 33 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Zpalatalhook (U+A7C6): L<<458.0,135.0>--<453.0,0.0>> -> L<<453.0,0.0>--<453.0,-108.0>>

	* beta (U+03B2): L<<56.0,-240.0>--<58.0,118.0>> -> L<<58.0,118.0>--<58.0,565.0>>

	* dzdigraphretroflexhook (U+AB66): L<<801.0,138.0>--<796.0,0.0>> -> L<<796.0,0.0>--<796.0,-101.0>>

	* rho (U+03C1): L<<41.0,-240.0>--<43.0,51.0>> -> L<<43.0,51.0>--<43.0,296.0>>

	* tripledagger (U+2E4B): L<<375.0,309.0>--<213.0,321.0>> -> L<<213.0,321.0>--<212.0,321.0>>

	* u10788 (U+10788): L<<520.6695556640625,369.796630859375>--<517.41943359375,287.0>> -> L<<517.41943359375,287.0>--<517.41943359375,226.4024658203125>>

	* uni023E (U+023E): L<<448.0,689.0>--<445.0,689.0>> -> L<<445.0,689.0>--<293.0,689.0>>

	* uni0290 (U+0290): L<<402.0,138.0>--<397.0,0.0>> -> L<<397.0,0.0>--<397.0,-91.0>>

	* uni03BC (U+03BC): L<<56.0,-240.0>--<58.0,136.0>> -> L<<58.0,136.0>--<56.0,536.0>>

	* uni03FC (U+03FC): L<<42.0,-90.0>--<43.0,51.0>> -> L<<43.0,51.0>--<43.0,296.0>>

	* 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* eth (U+00F0): B<<385.5,450.5>-<412.0,431.0>-<428.0,400.0>>/B<<428.0,400.0>-<403.0,480.0>-<371.5,537.5>> = 9.945547575071476

	* sterling (U+00A3): B<<192.0,89.0>-<173.0,58.0>-<145.0,40.0>>/L<<145.0,40.0>--<149.0,42.0>> = 6.170175095029526

	* uni1D95 (U+1D95): L<<424.0,-97.0>--<424.0,232.0>>/B<<424.0,232.0>-<417.0,110.0>-<368.0,50.0>> = 3.2838622879063513

	* uni1D9E (U+1D9E): B<<250.58441162109375,557.2890014648438>-<267.81005859375,545.5894775390625>-<278.21044921875,526.990234375>>/B<<278.21044921875,526.990234375>-<261.9598388671875,574.98828125>-<241.48406982421875,609.4868774414062>> = 10.508738448678587

	* uni1DD9 (U+1DD9): B<<64.47970581054688,800.2109985351562>-<76.405029296875,792.4105224609375>-<83.605224609375,780.009765625>>/B<<83.605224609375,780.009765625>-<72.35491943359375,812.01171875>-<58.179534912109375,835.0131225585938>> = 10.77138776512575

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* uni2133 (U+2133): B<<1101.5,668.0>-<1119.0,688.0>-<1125.0,694.0>>/B<<1125.0,694.0>-<1109.0,683.0>-<1066.5,648.5>> = 10.491477012331565 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<56.0,-240.0>--<58.0,118.0>>

	* beta (U+03B2): L<<86.0,83.0>--<88.0,-240.0>>

	* eta (U+03B7): L<<442.0,-240.0>--<445.0,357.0>>

	* eta (U+03B7): L<<470.0,357.0>--<474.0,-240.0>>

	* etatonos (U+03AE): L<<442.0,-240.0>--<445.0,357.0>>

	* etatonos (U+03AE): L<<470.0,357.0>--<474.0,-240.0>>

	* exclam (U+0021): L<<123.0,167.0>--<120.0,714.0>>

	* exclam (U+0021): L<<149.0,714.0>--<148.0,167.0>>

	* exclamdbl (U+203C): L<<123.0,167.0>--<120.0,714.0>>

	* exclamdbl (U+203C): L<<149.0,714.0>--<148.0,167.0>>

	* 183 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[15] NotoSerif-ThinItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* onequarter
	* onequarter
	* onehalf
	* onehalf
	* threequarters
	* threequarters
	* Alphatonos
	* Alphatonos
	* Epsilontonos
	* Epsilontonos and 957 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1080, but got 1069 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* uni207F (component n)
* uni018D (component delta)
* uni0252 (component uni0251)
* uni02B0 (component h)
* uni02B1 (component uni0266)
* uni02B2 (component j)
* uni02B3 (component r)
* uni02B4 (component uni0279)
* uni02B5 (component uni027B)
* uni02B6 (component uni0281)
* uni02B7 (component w)
* uni02B8 (component y)
* uni02E0 (component uni0263)
* uni02E1 (component l)
* uni02E2 (component s)
* uni02E3 (component x)
* uni02E4 (component uni0295)
* usideways (component u)
* udieresissideways (component udieresis)
* msidewaysturned (component uni026F)
* uni1D2C (component A)
* AEmod (component AE)
* uni1D2E (component B)
* uni1D30 (component D)
* uni1D31 (component E)
* Ereversedmod (component uni018E)
* uni1D33 (component G)
* uni1D34 (component H)
* uni1D35 (component I)
* uni1D36 (component J)
* uni1D37 (component K)
* uni1D38 (component L)
* uni1D39 (component M)
* uni1D3A (component N)
* uni1D3C (component O)
* uni1D3D (component uni0222)
* uni1D3E (component P)
* uni1D3F (component R)
* uni1D40 (component T)
* uni1D41 (component U)
* uni1D42 (component W)
* uni1D43 (component a)
* aturnedmod (component uni0250)
* uni1D45 (component uni0251)
* aeturnedmod (component aeturned)
* uni1D47 (component b)
* uni1D48 (component d)
* uni1D49 (component e)
* uni1D4A (component uni0259)
* eopenmod (component uni025B)
* eturnedopenmod (component eturnedopen)
* uni1D4D (component g)
* iturnedmod (component iturned)
* uni1D4F (component k)
* uni1D50 (component m)
* uni1D51 (component eng)
* uni1D52 (component o)
* oopenmod (component uni0254)
* otophalfmod (component otophalf)
* obottomhalfmod (component obottomhalf)
* uni1D56 (component p)
* uni1D57 (component t)
* uni1D58 (component u)
* mturnedmod (component uni026F)
* uni1D5B (component v)
* uni1D5C (component uni1D25)
* uni1D5D (component beta)
* uni1D5E (component gamma)
* uni1D5F (component delta)
* uni1D60 (component phi)
* uni1D61 (component chi)
* uni1D62 (component i)
* uni1D63 (component r)
* uni1D64 (component u)
* uni1D65 (component v)
* uni1D66 (component beta)
* uni1D67 (component gamma)
* uni1D68 (component rho)
* uni1D69 (component phi)
* uni1D6A (component chi)
* uni1D77 (component g)
* uni1D9B (component uni0252)
* uni1D9C (component c)
* uni1D9D (component uni0255)
* uni1D9E (component eth)
* uni1DA0 (component f)
* uni1DA1 (component uni025F)
* uni1DA2 (component uni0261)
* uni1DA3 (component uni0265)
* uni1DA4 (component uni0268)
* uni1DA5 (component uni0269)
* iotaserifedmod (component iotaserifed)
* iotaserifedstrokemod (component iotaserifedstroke)
* uni1DA8 (component uni029D)
* uni1DA9 (component uni026D)
* uni1DAA (component uni1D85)
* uni1DAB (component uni029F)
* uni1DAC (component uni0271)
* uni1DAD (component uni0270)
* uni1DAE (component uni0272)
* uni1DAF (component uni0273)
* uni1DB0 (component uni0274)
* uni1DB1 (component uni0275)
* phimodlatin (component uni0278)
* uni1DB3 (component uni0282)
* uni1DB4 (component uni0283)
* uni1DB5 (component uni01AB)
* uni1DB6 (component uni0289)
* uni1DB7 (component uni028A)
* uni1DB8 (component uni1D1C)
* uni1DB9 (component uni028B)
* uni1DBA (component uni028C)
* uni1DBB (component z)
* uni1DBC (component uni0290)
* uni1DBD (component uni0291)
* uni1DBE (component uni0292)
* uni1DBF (component theta)
* uni2090 (component a)
* uni2091 (component e)
* uni2092 (component o)
* uni2093 (component x)
* uni2094 (component uni0259)
* uni1FDE0306 (component breve)
* uni1FCE0306 (component breve)
* uni2C6F (component A)
* uniA780 (component L)
* uniA7B0 (component K)
* uniA7B1 (component T)
* uni2C7C (component j)
* uni2C79 (component uni027D)
* uniA77F (component uni1D79)
* uniA781 (component l)
* uni2071 (component i)
* uniA7FD (component M)
* uniA7F9 (component oe)
* uniAB50 (component uniAB51)
* uni2095 (component h)
* uni2096 (component k)
* uni2097 (component l)
* uni2098 (component m)
* uni2099 (component n)
* uni209A (component p)
* uni209B (component s)
* uni209C (component t)
* uni1D59 (component usideways)
* uniA770 (component _con)
* uniA7F8 (component Hbar)
* uniAB5C (component uniA727)
* uniAB5D (component uniAB37)
* uniAB5E (component uni026B)
* uniAB5F (component uniAB52)
* uni2E18 (component uni203D)
* uni2054 (component uni035C)
* uni2E35 (component semicolon)
* uni2E46 (component kavykainvertedlow)
* kavykalow (component kavykainvertedlow)
* exclamdown.sc (component exclam.sc)
* questiondown.sc (component question.sc)
* uni214B (component ampersand)
* summationDoubleStruck.mir (component uni2140)
* uniA706 (component uniA700)
* uniA712 (component uni02E9)
* uniA713 (component uni02E8)
* uniA714 (component uni02E7)
* uniA715 (component uni02E6)
* uniA716 (component uni02E9)
* uni1DE7 (component uni0251)
* uni1DE8 (component b)
* uni1DE9 (component beta)
* uni1DEA (component uni0259)
* uni1DEB (component f)
* uni1DEC (component uniAB38)
* uni1DED (component o)
* uni1DED (component uni1AB9)
* uni1DEE (component p)
* uni1DEF (component uni0283)
* uni1DF0 (component u)
* uni1DF0 (component uni1AB9)
* uni1DF1 (component w)
* uni1DF2 (component adieresis)
* uni1DF3 (component odieresis)
* uni1DF4 (component udieresis)
* uni1DFC (component uni035C)
* becombcy (component uni0431)
* vecombcy (component uni0432)
* ghecombcy (component uni0433)
* decombcy (component uni0434)
* zhecombcy (component uni0436)
* zecombcy (component uni0437)
* kacombcy (component uni043A)
* elcombcy (component uni043B)
* emcombcy (component uni043C)
* encombcy (component uni043D)
* ocombcy (component uni043E)
* pecombcy (component uni043F)
* ercombcy (component uni0440)
* escombcy (component uni0441)
* tecombcy (component uni0442)
* hacombcy (component uni0445)
* tsecombcy (component uni0446)
* checombcy (component uni0447)
* shacombcy (component uni0448)
* shchacombcy (component uni0449)
* fitacombcy (component uni0473)
* acombcy (component uni0430)
* iecombcy (component uni0435)
* djervcombcy (component uniA649)
* monographukcombcy (component ukmonographcy)
* yatcombcy (component yattallcy)
* yucombcy (component uni044E)
* iotifiedacombcy (component uniA657)
* littleyuscombcy (component uni0467)
* bigyuscombcy (component uni046B)
* iotifiedbigyuscombcy (component uni046D)
* uniFE27 (component uniFE20)
* uniFE28 (component uniFE20)
* uniFE2A (component uniFE22)
* uniA674 (component uni0454)
* uniA675 (component uni0438)
* uniA676 (component uni0457)
* uniA677 (component uni0443)
* uniA679 (component uni044B)
* uniA67A (component uni044C)
* uniA67B (component uni0461)
* uniA69E (component uni0444)
* uniA69F (component uni0465)
* uni2C7D (component V)
* uni1DDB (component uni0262)
* uni1DDE (component uni029F)
* uni1DDF (component uni1D0D)
* uni1DE1 (component uni0274)
* uni1DE2 (component uni0280)
* uni0363 (component a)
* uni1DD4 (component ae)
* uni1DD5 (component uniA735)
* uni1DD6 (component uniA739)
* uni1DD7 (component ccedilla)
* uni0368 (component c)
* uni0369 (component d)
* uni0364 (component e)
* uni1DD9 (component eth)
* uni1DDA (component g)
* uni036A (component h)
* uni0365 (component i)
* uni1DD8 (component uniA77A)
* uni1DDC (component k)
* uni1DDD (component l)
* uni1DE5 (component longs)
* uni036B (component m)
* uni1DE0 (component n)
* uni0366 (component o)
* uni1DCA (component r)
* uni036C (component r)
* uni1DE3 (component uniA75B)
* uni1DE4 (component s)
* uni036D (component t)
* uni0367 (component u)
* uni036E (component v)
* uni036F (component x)
* uni1DE6 (component z)
* jmoddotless (component uni0237)
* isubscriptdotless (component dotlessi)
* jcrossedtailmoddotless (component jcrossedtaildotless)
* u11AB0 (component numbersign)
* u11AB1 (component dollar)
* ginsularcomb (component uni1D79)
* rinsularcomb (component uniA783)
* tinsularcomb (component uniA787)
* uniA7F2 (component C)
* uniA7F3 (component F)
* uniA7F4 (component Q)
* u10781 (component uni02D0)
* u10782 (component uni02D1)
* u10783 (component ae)
* u10784 (component uni0299)
* u10785 (component uni0253)
* u10787 (component uni02A3)
* u10788 (component dzdigraphretroflexhook)
* u10789 (component uni02A5)
* u1078A (component uni02A4)
* u1078B (component uni0256)
* u1078C (component uni0257)
* u1078D (component uni1D91)
* u1078E (component uni0258)
* u1078F (component uni025E)
* u10790 (component uni02A9)
* u10791 (component uni0264)
* u10792 (component uni0262)
* u10793 (component uni0260)
* u10794 (component uni029B)
* u10795 (component hbar)
* u10796 (component uni029C)
* u10797 (component uni0267)
* u10798 (component uni0284)
* u10799 (component uni02AA)
* u1079A (component uni02AB)
* u1079B (component uni026C)
* u1079C (component uni1DF04)
* u1079D (component uniA78E)
* u1079E (component uni026E)
* u1079F (component uni1DF05)
* u107A0 (component uni028E)
* u107A1 (component uni1DF06)
* u107A2 (component oslash)
* u107A3 (component uni0276)
* u107A4 (component uni0277)
* u107A5 (component q)
* u107A6 (component uni027A)
* u107A7 (component uni1DF08)
* u107A8 (component uni027D)
* u107A9 (component uni027E)
* u107AA (component uni0280)
* u107AB (component uni02A8)
* u107AC (component uni02A6)
* u107AD (component tsdigraphretroflexhook)
* u107AE (component uni02A7)
* u107AF (component uni0288)
* u107B0 (component uni2C71)
* u107B2 (component uni028F)
* u107B3 (component uni02A1)
* u107B4 (component uni02A2)
* u107B5 (component uni0298)
* u107B6 (component uni01C0)
* u107B7 (component uni01C1)
* u107B8 (component uni01C2)
* u107B9 (component uni1DF0A)
* u107BA (component u1DF1E)
* uni1DF02 (component g.sc)
* uni1DF10 (component kgreenlandic)
 [code: transformed-components]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* stackedcommadbl
	* summationDoubleStruck.mir
	* u10780
	* uni1DF0F
	* uniA714
	* uniA716
	* uniAB5A and uniFE27
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- beta.alt1

	- uni03B1030403130300

	- uni03B1030403130301

	- uni03B1030403140300

	- uni03B1030403140301

	- uni03B1030603130300

	- uni03B1030603130301

	- uni03B1030603140300

	- uni03B1030603140301

	- uni03B9030403130300

	- 23 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


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

	- 41 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 559 among a set of 8 math glyphs.
The following math glyphs have a different width, though:

Width = 310:
minus
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
* ⚠ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 ginsularcomb (U+1ACC), rinsularcomb (U+1ACD), tinsularcomb (U+1ACE) and uni031A (U+031A) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Cpalatalhook (U+A7C4): L<<484.0,82.0>--<484.0,82.0>> -> L<<484.0,82.0>--<484.0,82.0>>

	* Lslash (U+0141): L<<153.0,315.0>--<151.0,314.0>> -> L<<151.0,314.0>--<23.0,249.0>>

	* Ustroke (U+A7B8): L<<529.0,185.0>--<619.0,606.0>> -> L<<619.0,606.0>--<620.0,610.0>>

	* Zpalatalhook (U+A7C6): L<<474.0,134.0>--<441.0,2.0>> -> L<<441.0,2.0>--<418.0,-108.0>>

	* beta (U+03B2): L<<-42.0,-240.0>--<35.0,118.0>> -> L<<35.0,118.0>--<129.0,565.0>>

	* rho (U+03C1): L<<-62.0,-240.0>--<1.0,51.0>> -> L<<1.0,51.0>--<53.0,296.0>>

	* tripledagger (U+2E4B): L<<224.0,338.0>--<225.0,338.0>> -> L<<225.0,338.0>--<384.0,342.0>>

	* tripledagger (U+2E4B): L<<377.0,312.0>--<221.0,314.0>> -> L<<221.0,314.0>--<219.0,314.0>>

	* tripledagger (U+2E4B): L<<45.0,342.0>--<201.0,338.0>> -> L<<201.0,338.0>--<203.0,338.0>>

	* uni0246 (U+0246): L<<497.0,689.0>--<492.0,689.0>> -> L<<492.0,689.0>--<260.0,689.0>>

	* 12 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* three (U+0033): B<<417.0,440.0>-<372.0,385.0>-<280.0,375.0>>/B<<280.0,375.0>-<313.0,372.0>-<343.0,353.0>> = 11.397876809426648

	* tripledagger (U+2E4B): L<<197.0,314.0>--<197.0,314.0>>/L<<197.0,314.0>--<38.0,312.0>> = 0.7206636225178014

	* uni024A (U+024A): L<<431.0,-64.0>--<480.0,168.0>>/B<<480.0,168.0>-<439.0,80.0>-<379.5,33.5>> = 13.055247223796592

	* uni040B (U+040B): L<<381.0,689.0>--<314.0,373.0>>/L<<314.0,373.0>--<314.0,375.0>> = 11.970874503545183

	* uni04BF (U+04BF): B<<371.5,13.5>-<346.0,-3.0>-<310.0,-8.0>>/L<<310.0,-8.0>--<310.0,-8.0>> = 7.907162702958418

	* uni04BF (U+04BF): L<<310.0,-8.0>--<310.0,-8.0>>/B<<310.0,-8.0>-<287.0,-12.0>-<273.0,-18.0>> = 9.865806943084365

	* uni0504 (U+0504): B<<395.5,403.0>-<357.0,376.0>-<308.0,368.0>>/B<<308.0,368.0>-<361.0,366.0>-<390.0,341.0>> = 11.433681265426625

	* uni1D95 (U+1D95): L<<297.0,-29.0>--<355.0,216.0>>/B<<355.0,216.0>-<338.0,154.0>-<305.5,102.5>> = 2.0145810107512325

	* uni20A5 (U+20A5): B<<334.0,84.0>-<339.0,126.0>-<348.0,169.0>>/L<<348.0,169.0>--<235.0,-96.0>> = 11.272643255936822

	* uni210A (U+210A): B<<93.5,165.0>-<104.0,193.0>-<117.0,209.0>>/L<<117.0,209.0>--<52.0,145.0>> = 6.350285546882426

	* 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 66 | 209 | 2108 | 127 | 1701 | 0 |
| 0% | 2% | 5% | 50% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
