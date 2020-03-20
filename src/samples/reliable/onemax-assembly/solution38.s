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

    movl	$20781, %eax
    movl	$-17368, %ebx
    movl	$-27602, %ecx
    movl	$-2681, %edx

    or %edx, %eax
    shl $228, %ecx
    shr $254, %eax
    add %edx, %edx
    shr $0, %eax
    shl $105, %edx
    and %ecx, %eax
    je n14
    and %edx, %ecx
    jo n13
n13:
    jz n14
n14:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
