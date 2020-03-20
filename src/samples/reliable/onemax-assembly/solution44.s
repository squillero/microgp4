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

    movl	$-7268, %eax
    movl	$30446, %ebx
    movl	$8904, %ecx
    movl	$-32422, %edx

    jz n10
    shr $241, %edx
    add %eax, %ecx
    sub %ecx, %eax
    shr $196, %edx
    shl $29, %ebx
    shl $224, %eax
n10:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
