vim.keymap.set("n","<C-s>",function()
	vim.fn.system("echo "..vim.fn.shellescape(vim.fn.getline("."))..
	"|sed \"s/^\\;//g\"|sed \"s/\\;$//g\"|sed \"s/\\;/\\n/g\"|sed \"s/\\,/ /g\"|sksl p.wav && play p.wav")
end)
