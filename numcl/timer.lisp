
(in-package :ros.script.benchmark)

(defconstant +trials+ 100)

(defparameter *header-width* 30)

(defun call-with-benchmark (trials fn &key (warmup 3))
  (let (user-run-time-us-s
        system-run-time-us-s
        real-time-ms-s
        gc-run-time-ms-s)
    (sb-ext:gc)
    (dotimes (i (+ warmup trials))
      (sb-ext:call-with-timing
       (lambda (&key
                  user-run-time-us
                  system-run-time-us
                  real-time-ms
                  gc-run-time-ms &allow-other-keys)
         (when (<= warmup i)
           (push user-run-time-us user-run-time-us-s)
           (push system-run-time-us system-run-time-us-s)
           (push real-time-ms real-time-ms-s)
           (push gc-run-time-ms gc-run-time-ms-s)))
       fn))
    (flet ((digits (x) (multiple-value-list (floor x 1000))))
      (list (list (digits (reduce #'+ real-time-ms-s))
                  (digits (+ (floor (reduce #'+ user-run-time-us-s)   1000)
                             (floor (reduce #'+ system-run-time-us-s) 1000)))
                  (digits (floor (reduce #'+ user-run-time-us-s) 1000))
                  (digits (floor (reduce #'+ system-run-time-us-s) 1000))
                  (digits (reduce #'+ gc-run-time-ms-s)))

            (list (digits (round (alexandria:median real-time-ms-s)))
                  (digits (round (+ (floor (alexandria:median user-run-time-us-s)   1000)
                                    (floor (alexandria:median system-run-time-us-s) 1000))))
                  (digits (floor (round (alexandria:median user-run-time-us-s)) 1000))
                  (digits (floor (round (alexandria:median system-run-time-us-s)) 1000))
                  (digits (round (alexandria:median gc-run-time-ms-s))))

            (list (digits (reduce #'max real-time-ms-s :initial-value 0))
                  (digits (+ (floor (reduce #'max user-run-time-us-s :initial-value 0)   1000)
                             (floor (reduce #'max system-run-time-us-s :initial-value 0) 1000)))
                  (digits (floor (reduce #'max user-run-time-us-s :initial-value 0) 1000))
                  (digits (floor (reduce #'max system-run-time-us-s :initial-value 0) 1000))
                  (digits (reduce #'max gc-run-time-ms-s :initial-value 0)))))))

(defmacro with-timing ((&key (trials +trials+) (name "N/A")) &body body)
  (when (< *header-width* (length name))
    (setf name (subseq name 0 *header-width*)))
  `(progn
     ;; the numbers are milliseconds so we just print 0 for the fourth digit below the dot
     (format *trace-output* "~va ~{~:{ ~4@a.~3,,,'0@a0  ~} ~}~%"
             ,*header-width*
             ,(cl:concatenate 'string (or (pathname-name *load-pathname*) "") "/" name)
             (call-with-benchmark ,trials (lambda () ,@body)))
     (finish-output *trace-output*)))

(defun banner ()
  (format *trace-output* "~va|~@{~30@a                              |~}~%"
          *header-width*
          "##"
          'sum
          'median
          'max)
  (format *trace-output* "~va|~{~{ ~9@a  ~}|~}~%"
          *header-width*
          "##"
          '((real total usr sys gc)
            (real total usr sys gc)
            (real total usr sys gc))))
