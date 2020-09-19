;; Generate and insert a random name for a namespace, class, function or
;; variable in your current buffer in Emacs.

(defun insert-name (type)
  "Generate and insert a random TYPE name in the current buffer at point."
  (interactive)
  (insert
   (shell-command-to-string
    (concat "~/name-o-matic-3000/name-o-matic-3000.py" " " type))))

(defun insert-namespace-name ()
  "Generate and insert a random namespace name in the current buffer at point."
  (interactive)
  (insert-name "namespace"))

(defun insert-class-name ()
  "Generate and insert a random class name in the current buffer at point."
  (interactive)
  (insert-name "class"))

(defun insert-function-name ()
  "Generate and insert a random function name in the current buffer at point."
  (interactive)
  (insert-name "function"))

(defun insert-variable-name ()
  "Generate and insert a random variable name in the current buffer at point."
  (interactive)
  (insert-name "variable"))

(global-set-key (kbd "<f1>") 'insert-namespace-name)
(global-set-key (kbd "<f2>") 'insert-class-name)
(global-set-key (kbd "<f3>") 'insert-function-name)
(global-set-key (kbd "<f4>") 'insert-variable-name)
