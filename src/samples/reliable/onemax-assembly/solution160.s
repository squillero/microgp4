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

    movl	$-10032, %eax
    movl	$7980, %ebx
    movl	$-11368, %ecx
    movl	$-14096, %edx

    shr $62, %edx
    jno n19
    add %edx, %ecx
    shr $92, %edx
    shl $222, %ecx
    jmp n17
    shr $166, %eax
    jno n22
    or %eax, %edx
    xor %edx, %eax
    shr $106, %eax
    jnz n26
    ja n51
    jo n37
n17:
    add %eax, %ebx
    xor %ebx, %ebx
n19:
    jz n36
    ja n23
    jz n38
n22:
    shl $186, %ebx
n23:
    shl $0, %ebx
    and %eax, %ecx
    shl $71, %edx
n26:
    cmp %ecx, %ecx
    jmp n45
    shr $50, %eax
    shr $18, %ebx
    sub %ecx, %ebx
    jnz n51
    jno n39
    jmp n45
    jne n39
    cmp %edx, %eax
n36:
    xor %ecx, %ecx
n37:
    or %ebx, %edx
n38:
    shl $42, %ecx
n39:
    shl $73, %ebx
    jz n51
    shl $98, %ecx
    shr $214, %ebx
    and %edx, %edx
    shr $126, %eax
n45:
    shl $63, %eax
    shl $33, %ecx
    jz n50
    and %ecx, %ebx
    shr $140, %eax
n50:
    add %edx, %ebx
n51:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
