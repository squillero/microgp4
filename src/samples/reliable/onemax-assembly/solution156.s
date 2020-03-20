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

    movl	$12243, %eax
    movl	$9114, %ebx
    movl	$-28999, %ecx
    movl	$32317, %edx

    and %ebx, %ebx
    sub %ebx, %ecx
    sub %ecx, %ecx
    cmp %eax, %edx
    je n10
    shr $46, %eax
    shl $238, %eax
n10:
    xor %eax, %ebx
    je n13
    shr $252, %ebx
n13:
    sub %edx, %ecx
    sub %eax, %edx
    ja n16
n16:
    add %edx, %ecx
    or %eax, %edx
    shl $4, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
