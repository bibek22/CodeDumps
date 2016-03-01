(define PI 3.14159)
(define (third n)
     (/ n 3))
(define (cube n)
  (* n n n))
(define (sin-rec x)
  (define (a x)
    (* 3 (sin-rec (third x))))
  (define (b x)
    (let ((t (* 4 (sin-rec (third x)))))
      (* t t t)))

  (if (< (abs x) 0.01)
      x
      (- (a x) (b x))))

(sin-rec (/ PI 2))
