(defun FIB (x) (if (<= x 2) 1 (+ (FIB (- x 1)) x)))
(format t (FIB 10) )
