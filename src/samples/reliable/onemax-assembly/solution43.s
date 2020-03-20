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

    movl	$-9338, %eax
    movl	$25855, %ebx
    movl	$-4082, %ecx
    movl	$29824, %edx

    jmp n12
    jz n16
    and %ebx, %eax
    or %edx, %edx
    and %edx, %edx
    or %ebx, %eax
    jnz n21
    ja n13
    shr $213, %edx
n12:
    jmp n20
n13:
    jnz n20
    shl $14, %ebx
    or %edx, %eax
n16:
    or %edx, %eax
    add %ecx, %ecx
    add %ebx, %ecx
    xor %eax, %edx
n20:
    shr $246, %ecx
n21:
    shl $76, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
