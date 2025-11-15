vim.keymap.set("n","<C-s>",function()
	vim.fn.system("echo "..vim.fn.shellescape(vim.fn.getline("."))..
	"|sed \"s/^[0-9]*\\;//g\"|sed \"s/\\;$//g\"|sed \"s/\\;/\\n/g\"|sed \"s/\\,/ /g\"|sksl|sox -t au - -d")
end)
