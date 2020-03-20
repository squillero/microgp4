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

    movl	$18978, %eax
    movl	$-23032, %ebx
    movl	$-11294, %ecx
    movl	$-16570, %edx

    add %ecx, %ebx
    shl $107, %eax
    jo n16
    shr $85, %edx
    jno n13
    jo n16
    shr $164, %ecx
    jno n16
    shl $253, %edx
    and %edx, %eax
n13:
    sub %ebx, %ebx
    shl $120, %edx
    shr $156, %edx
n16:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
