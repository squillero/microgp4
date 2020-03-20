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

    movl	$-15975, %eax
    movl	$20386, %ebx
    movl	$-13088, %ecx
    movl	$-26745, %edx

    xor %edx, %ebx
    cmp %eax, %ecx
    jo n11
    or %eax, %ecx
    shr $195, %eax
    ja n23
    shl $178, %edx
    shl $61, %ebx
n11:
    shr $195, %eax
    shl $21, %ecx
    shr $167, %ebx
    sub %eax, %edx
    or %eax, %ebx
    or %ecx, %edx
    jnz n19
    jc n19
n19:
    or %eax, %edx
    and %eax, %edx
    jno n23
    jnz n23
n23:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
