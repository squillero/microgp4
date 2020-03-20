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

    movl	$8590, %eax
    movl	$21540, %ebx
    movl	$-18632, %ecx
    movl	$-327, %edx

    jne n10
    ja n13
    jnz n9
    cmp %ebx, %eax
    jnz n12
    shl $153, %ebx
n9:
    shr $200, %edx
n10:
    jnc n11
n11:
    jo n13
n12:
    or %eax, %eax
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
