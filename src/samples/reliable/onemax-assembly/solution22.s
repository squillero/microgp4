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

    movl	$6319, %eax
    movl	$-23733, %ebx
    movl	$4902, %ecx
    movl	$-7622, %edx

    or %ebx, %edx
    shr $85, %edx
    and %ebx, %ebx
    and %edx, %eax
    shl $4, %edx
    jnz n9
n9:
    or %edx, %edx
    jo n11
n11:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
