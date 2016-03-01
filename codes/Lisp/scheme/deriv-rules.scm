(define deriv-rules
  (
   ( (dd (?c c) (? v))  0)
   ( (dd (?v v) (? v))  1)
   ( (dd (?v u) (? v))  0)

   ( (dd (+ (? x1) (? x2)) (? v))
     (+ (dd (: x1) (: v))
	(dd (: x2) (: v))))


   ( (dd (* (? x1) (? x2)) (? v))
     (+ (* (: x1) (dd (: x2) (: v)))
	(* (dd (: x1) (: v)) (: x2))))
   ))

(define (match pat exp dict)
  (cond ((eq? ))))
