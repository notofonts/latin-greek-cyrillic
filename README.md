# Noto My Font

[![][Fontbakery]](https://notofonts.github.io/noto-project-template/fontbakery/fontbakery-report.html)
[![][Universal]](https://notofonts.github.io/noto-project-template/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://notofonts.github.io/noto-project-template/fontbakery/fontbakery-report.html)
[![][Outline Correctness]](https://notofonts.github.io/noto-project-template/fontbakery/fontbakery-report.html)
[![][Shaping]](https://notofonts.github.io/noto-project-template/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Noto Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2FNotoFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnotofonts%2Fnoto-project-template%2Fgh-pages%2Fbadges%2FUniversal.json

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at `https://yourname.github.io/your-font-repository-name`.

For information on how to work on Noto fonts, how the build process
works and how to maintain it, see [the README file of the
notofonts.github.io
repository](https://github.com/notofonts/notofonts.github.io/blob/main/README.md)

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL
