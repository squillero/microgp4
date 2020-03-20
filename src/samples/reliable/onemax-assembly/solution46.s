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

    movl	$3626, %eax
    movl	$-4443, %ebx
    movl	$23351, %ecx
    movl	$-7807, %edx

    sub %ebx, %ebx
    shl $4, %ebx
    or %edx, %ebx
    cmp %ecx, %edx
    and %ecx, %eax
    or %eax, %ebx
    add %ebx, %ecx
    jo n17
    shr $230, %ecx
    jne n15
    shl $131, %ecx
    shr $210, %eax
n15:
    jc n16
n16:
    jmp n17
n17:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
