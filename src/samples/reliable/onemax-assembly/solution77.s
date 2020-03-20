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

    movl	$-31897, %eax
    movl	$-21514, %ebx
    movl	$10210, %ecx
    movl	$-1500, %edx

    jo n16
    jmp n20
    shl $184, %edx
    jne n9
    shr $69, %eax
    je n12
n9:
    shr $96, %eax
    shr $246, %ebx
    cmp %ebx, %edx
n12:
    cmp %ebx, %eax
    and %edx, %ebx
    or %edx, %eax
    jz n18
n16:
    jnz n24
    shl $241, %eax
n18:
    jo n23
    sub %ebx, %ecx
n20:
    shl $26, %ecx
    ja n22
n22:
    cmp %edx, %edx
n23:
    or %ecx, %eax
n24:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
