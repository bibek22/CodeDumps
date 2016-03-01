(TeX-add-style-hook
 "3rd"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "margin=.8in" "paperwidth=5in" "paperheight=6.7in")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "geometry"
    "amsfonts"
    "graphicx")
   (TeX-add-symbols
    "eq")))

