# Before and after library

| # | Town | Service | Files (in `photos/`) | Posted |
|---|---|---|---|---|
| 01 | Burgess Hill | Fascia, soffit and gutter clean | `2026-11-burgess-hill-fascia-gutter-01-*` (plain wide copy at `2026-11-fascia-gutter-before-after.jpg` is used by the live Google post) | Google 19 Nov 2026 (plain wide); Instagram reposted 19 Nov in branded template |
| 02 | Burgess Hill | Soffit and fascia clean | `2026-11-burgess-hill-soffit-fascia-02-*` | Not yet |
| 03 | Burgess Hill | Window clean: frames and sills | `2026-11-burgess-hill-windows-sills-03-*` | Not yet |
| 04 | Burgess Hill | Conservatory roof clean (before photo from inside, after video from above) | `photos/2025-07-burgess-hill-conservatory-roof-04-*` (tall = before/after), `videos/2025-07-burgess-hill-conservatory-roof-04-after.mp4` | Reel reposted 19 Nov 2026 with branded cover (`photos/2025-07-burgess-hill-conservatory-roof-04-reel-cover.jpg`). Before/after image: not yet |
| 05 | Burgess Hill | Conservatory roof clean (brown frame) | `photos/burgess-hill-conservatory-roof-05-*` (cropped: a framed family photo was visible inside) | Not yet |
| 06 | Burgess Hill | Conservatory roof clean (white lean-to) | `photos/burgess-hill-conservatory-roof-06-*` (cropped: storage boxes visible inside) | Reserve: difference is hard to see once cropped |


Notes: build branded images with `python3 brand/make_post.py`. For Instagram video use the jsDelivr address with a commit SHA (not `@main`, which is cached), and pass a branded `cover_url`.
Strip wording: always end the service with the word "clean" (e.g. "Conservatory roof clean · Burgess Hill"). Dan's instruction, 19 Nov 2026.

Wording: say "gutter vacuum", never a brand name (Dan, 20 Nov 2026).

Gutter posts: strip wording is "Gutter clearance", not "Gutter clean" (Dan, 20 Nov 2026). Single-photo posts get the strip too: `python3 brand/make_single.py`.

Strip wording for gutter posts: "Gutter clearance", not "Gutter clean" (Dan, 20 Nov 2026). Single-photo branded images: `python3 brand/make_single.py`.
