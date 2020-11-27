*Examples*

*send one line*
io.sendline("")


*rec until* 
io.recvuntil("")


*output for debug*
info("")


*recv canary*
io.recvuntil("string")
io.sendline("%19$p")
canary = io.recvline().strip() 
*print canary for output*
info(f"canary = {canary}")
*send canary in payload*
io.sendline(("A"*88).encode()+p64(int(canary, base=16)))
