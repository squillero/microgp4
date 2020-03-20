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

    movl	$31072, %eax
    movl	$-2463, %ebx
    movl	$-19775, %ecx
    movl	$-15612, %edx

    ja n14
    shr $136, %ecx
    add %ecx, %edx
    jnz n14
    ja n12
    shr $153, %eax
    shl $40, %eax
    shl $178, %edx
    shl $61, %ebx
n12:
    shr $195, %eax
    jne n18
n14:
    ja n17
    jno n18
    sub %ecx, %ebx
n17:
    sub %eax, %edx
n18:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
