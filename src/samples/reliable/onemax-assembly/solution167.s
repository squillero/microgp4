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

    movl	$-21221, %eax
    movl	$-2312, %ebx
    movl	$29905, %ecx
    movl	$-11869, %edx

    jz n6
    jnc n10
    sub %edx, %edx
n6:
    xor %edx, %ebx
    add %ecx, %ecx
    xor %ebx, %edx
    or %edx, %edx
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
