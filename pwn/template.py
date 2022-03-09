from pwn import *

# tmux split two have all in one window
context(terminal=['tmux', 'splitw', '-h'])

#set information level to debug
context.log_level = 'debug'

if args.REMOTE:
    io = remote("IP", 9999)
else:
    io = context.binary = ELF('ELF')
    if args.GDB:
            io = gdb.debug(io.path) 
    else:
            io =process(io.path)

payload = ""

io.sendline(payload)
io.interactive()
