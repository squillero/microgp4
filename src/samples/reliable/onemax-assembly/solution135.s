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

    movl	$-3164, %eax
    movl	$16502, %ebx
    movl	$-26606, %ecx
    movl	$1564, %edx

    shl $10, %eax
    xor %eax, %ecx
    add %ebx, %eax
    xor %eax, %eax
    jc n14
    jne n9
n9:
    xor %ecx, %eax
    sub %ebx, %edx
    jnz n13
    jc n13
n13:
    cmp %ebx, %ecx
n14:
    shr $225, %ebx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
