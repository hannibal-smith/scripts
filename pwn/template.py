from pwn import *

# tmux split two have all in one window
context(terminal=['tmux', 'splitw', '-h'])

#set information level to debug
context.log_level = 'debug'

#TODO: replace <ELF-FILENMAE> with name of elf-file
io = context.binary = ELF('<ELF-FILENAME>')

# start in gdb or not
#io = gdb.debug(io.path)
io = process(io.path)

payload = ""

io.sendline(payload)
io.interactive()
