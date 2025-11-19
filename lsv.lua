vim.keymap.set("n","<C-s>",function()
	local l=vim.fn.getline(".")
	if vim.fn.getline(1)==";1,55,51,1,45,37,51,2,77;" then
		local s1,s2=unpack(vim.api.nvim_win_get_cursor(0))
		local ps=l:sub(1,s2):find(".*;")
		local ds=l:sub(s2+2):find(";")
		if ps and ds then
			l=l:sub(ps,s2+2+ds)
		else return
		end
	else
		local s=tonumber(l:match("^([^;]+);"))
		if s and s>=1734424182 then
			vim.notify(os.date("%Y-%m-%d %H:%M:%S %Z",s))
		end
	end
	vim.fn.system("echo "..vim.fn.shellescape(l)..
	"|sed \"s/^[0-9\\/#]*\\;//g\"|sed \"s/\\;$//g\"|sed \"s/\\;/\\n/g\"|sed \"s/\\,/ /g\"|sksl|sox -t au - -d")
end)
