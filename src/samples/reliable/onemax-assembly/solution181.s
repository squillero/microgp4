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

    movl	$21271, %eax
    movl	$-6604, %ebx
    movl	$6871, %ecx
    movl	$20156, %edx

    je n7
    and %ecx, %eax
    jmp n12
    shr $39, %ecx
n7:
    or %ebx, %edx
    shr $153, %eax
    shl $40, %eax
    shl $178, %edx
    shl $61, %ebx
n12:
    shr $195, %eax
    jne n18
    ja n17
    jno n18
    sub %ecx, %ebx
n17:
    sub %eax, %edx
n18:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
