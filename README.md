# IMP_D valodas translators uz abstraktās mašīnas (AM) komandām
###### Autors: Pavels Ivanovs (st.apl.num.: pi19003)

Valodas IMP_D komandu translators uz AM komandām.

Piemēra ievads IMP_D valodā:
```text
while not(x=y) do 
    if x=<y then y:=y-x 
    else x:=x-y fi 
od
```
Atbilstoša izvade AM komandās:
```text
LOOP(FETCH(y) : FETCH(x) : EQ : NEG, FETCH(y) : FETCH(x) : LE : BRANCH(FETCH(y) : FETCH(x) : SUB : STORE(y), FETCH(x) : FETCH(y) : SUB : STORE(x)))
```