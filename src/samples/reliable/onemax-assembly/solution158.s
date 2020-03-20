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

    movl	$-27388, %eax
    movl	$-8041, %ebx
    movl	$-1624, %ecx
    movl	$21919, %edx

    shr $70, %edx
    or %edx, %ebx
    jc n6
n6:
    jmp n11
    or %edx, %ebx
    or %ecx, %eax
    shl $142, %eax
    sub %eax, %ecx
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
