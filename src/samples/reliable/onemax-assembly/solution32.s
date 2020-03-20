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

    movl	$-29259, %eax
    movl	$-26132, %ebx
    movl	$-11070, %ecx
    movl	$-19298, %edx

    shr $209, %ecx
    jne n14
    je n9
    shr $201, %edx
    jnz n9
    shl $1, %edx
n9:
    jz n14
    cmp %edx, %ebx
    jz n12
n12:
    sub %ebx, %ecx
    jz n21
n14:
    shr $157, %edx
    or %edx, %ecx
    add %edx, %ebx
    shl $195, %ecx
    sub %edx, %eax
    jne n23
    shl $134, %ebx
n21:
    and %eax, %ebx
    jz n23
n23:
    cmp %ecx, %edx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
