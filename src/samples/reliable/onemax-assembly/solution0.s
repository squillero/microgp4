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

    movl	$5069, %eax
    movl	$-20167, %ebx
    movl	$13406, %ecx
    movl	$-28210, %edx

    shr $116, %ecx
    shr $119, %eax
    jnc n14
    shl $186, %ebx
    shl $181, %ebx
    jne n20
    shr $87, %ebx
    jnz n18
    jnc n16
    cmp %ebx, %ecx
    ja n17
n14:
    shr $161, %edx
    and %eax, %ebx
n16:
    jmp n19
n17:
    sub %edx, %edx
n18:
    shl $73, %ecx
n19:
    jnz n20
n20:
    shl $219, %edx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
