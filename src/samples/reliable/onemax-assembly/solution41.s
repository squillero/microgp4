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

    movl	$-7630, %eax
    movl	$-20277, %ebx
    movl	$27647, %ecx
    movl	$6512, %edx

    jne n26
    xor %ebx, %ebx
    and %ebx, %eax
    xor %ecx, %edx
    add %eax, %ecx
    shl $122, %eax
    sub %eax, %eax
    shl $35, %ebx
    jnz n26
    shl $84, %ecx
    xor %edx, %ebx
    jno n21
    jne n26
    shl $224, %edx
    jz n25
    shr $32, %ecx
    ja n26
    shr $3, %eax
n21:
    cmp %eax, %ebx
    shr $16, %ecx
    shr $121, %ecx
    cmp %edx, %ebx
n25:
    jz n26
n26:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
