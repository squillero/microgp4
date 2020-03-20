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

    movl	$-23551, %eax
    movl	$-11065, %ebx
    movl	$16078, %ecx
    movl	$-27669, %edx

    sub %ecx, %ecx
    jnz n15
    add %ecx, %edx
    add %ecx, %ebx
    shr $34, %ecx
    and %eax, %eax
    ja n13
    jo n14
    sub %edx, %edx
    shl $179, %edx
n13:
    add %edx, %ebx
n14:
    jnz n15
n15:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
