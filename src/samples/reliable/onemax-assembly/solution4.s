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

    movl	$27359, %eax
    movl	$22828, %ebx
    movl	$-24815, %ecx
    movl	$-2854, %edx

    shr $237, %ecx
    shl $218, %edx
    sub %edx, %edx
    and %ebx, %ecx
    jno n11
    cmp %ebx, %ecx
    or %eax, %ecx
    shr $139, %ecx
n11:
    shl $41, %ebx
    jnz n13
n13:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
