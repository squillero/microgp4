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

    movl	$1999, %eax
    movl	$4147, %ebx
    movl	$-32213, %ecx
    movl	$7229, %edx

    shr $225, %ecx
    shr $77, %edx
    shl $111, %eax
    add %ebx, %eax
    shl $179, %edx
    and %ebx, %ebx
    jne n10
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