    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$5069, %eax
    movl	$-20167, %ebx
    movl	$13406, %ecx
    movl	$-28210, %edx

    shr $116, %ecx
    shr $119, %eax
    jnc n20
    shl $186, %ebx
    shl $181, %ebx
    xor %eax, %eax
    jne n27
    shr $87, %ebx
    jnz n25
    jc n26
    jnz n28
    jnc n22
    cmp %ebx, %ecx
    shl $142, %eax
    ja n28
    sub %edx, %ebx
    shr $184, %eax
n20:
    jno n21
n21:
    jnc n35
n22:
    shl $22, %edx
    jc n28
    cmp %eax, %ecx
n25:
    add %ecx, %ebx
n26:
    jz n36
n27:
    jc n30
n28:
    ja n34
    jno n32
n30:
    cmp %ebx, %edx
    cmp %edx, %ebx
n32:
    jnz n33
n33:
    shl $18, %ecx
n34:
    shr $22, %ebx
n35:
    or %ecx, %edx
n36:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
