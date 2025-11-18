vim.keymap.set("n","<C-s>",function()
	local l=vim.fn.getline(".")
	local s=tonumber(l:match("^([^;]+);"))
	if s and s>=1734424182 then
		vim.notify(os.date("%Y-%m-%d %H:%M:%S %Z",s))
	end
	vim.fn.system("echo "..vim.fn.shellescape(l)..
	"|sed \"s/^[0-9\\/#]*\\;//g\"|sed \"s/\\;$//g\"|sed \"s/\\;/\\n/g\"|sed \"s/\\,/ /g\"|sksl|sox -t au - -d")
end)
