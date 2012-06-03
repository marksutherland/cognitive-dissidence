(define (value node) (if (< (length node) 1) '() (car node)))
(define (left node)  (if (< (length node) 2) '() (cadr node)))
(define (right node) (if (< (length node) 3) '() (caddr node)))

(define cache '())

(define (path parent)
    (if (not (assoc parent cache))
      (set! cache (cons (list parent (calc-path parent)) cache)))
    (cadr (assoc parent cache)))

(define (calc-path parent)
  (if (or (null? (left parent)) (null? (right parent)))
        (list (value parent))
        (cons (value parent) 
              (max-path (path (left parent)) (path (right parent))))))

(define (max-path left right)
    (if (> (apply + left) (apply + right))
          left
          right))

(letrec ((d1 '(6)) (d2 '(7)) (d3 '(1)) (d4 '(2))
          (c1 (list 2 d1 d2)) (c2 (list 4 d2 d3)) (c3 (list 3 d3 d4))
            (b1 (list 5 c1 c2)) (b2 (list 9 c2 c3))
              (root (list 1 b1 b2)))
  (path root))
