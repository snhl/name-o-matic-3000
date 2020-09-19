;; Generate and insert a random name for a namespace, class, function or
;; variable in your current buffer in Emacs.

(defun insert-name (type)
  "Generate and insert a random TYPE name in the current buffer at point."
  (interactive)
  (insert
   (shell-command-to-string
    (concat "~/name-o-matic-3000/name-o-matic-3000.py" " " type))))

(global-set-key (kbd "<f1>") '(lambda () (interactive) (insert-name "namespace")))
(global-set-key (kbd "<f2>") '(lambda () (interactive) (insert-name "class")))
(global-set-key (kbd "<f3>") '(lambda () (interactive) (insert-name "function")))
(global-set-key (kbd "<f4>") '(lambda () (interactive) (insert-name "variable")))
