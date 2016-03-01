(TeX-add-style-hook
 "new"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11")
   (LaTeX-add-labels
    "h1")))

