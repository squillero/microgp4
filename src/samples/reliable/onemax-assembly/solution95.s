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

    movl	$15952, %eax
    movl	$-14035, %ebx
    movl	$3549, %ecx
    movl	$28153, %edx

    jo n4
n4:
    or %ebx, %edx
    jo n22
    jno n10
    jnc n8
n8:
    xor %ebx, %eax
    cmp %edx, %ecx
n10:
    shr $21, %edx
    jnz n22
    xor %ebx, %ebx
    shr $187, %ebx
    jno n20
    ja n22
    jo n23
    shr $191, %eax
    and %ebx, %eax
    shl $153, %edx
n20:
    shl $135, %ebx
    add %edx, %ebx
n22:
    shl $18, %edx
n23:
    shl $29, %ecx
    shr $235, %ecx
    and %ecx, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
