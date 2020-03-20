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

    movl	$26771, %eax
    movl	$-3754, %ebx
    movl	$-13281, %ecx
    movl	$23603, %edx

    shl $156, %eax
    jmp n11
    sub %ebx, %ecx
    jz n17
    je n19
    shr $80, %eax
    or %edx, %edx
    shl $16, %ebx
n11:
    jne n30
    shl $36, %ebx
    and %ebx, %edx
    jz n49
    je n25
    shl $72, %eax
n17:
    add %ebx, %ecx
    xor %ecx, %edx
n19:
    add %edx, %ecx
    cmp %edx, %ecx
    xor %edx, %edx
    jz n42
    ja n37
    cmp %ecx, %ecx
n25:
    add %eax, %ebx
    jmp n45
    ja n49
    and %eax, %ebx
    or %edx, %ecx
n30:
    jnz n49
    shl $251, %eax
    shl $178, %edx
    shl $164, %eax
    jnz n40
    jnc n47
    jo n41
n37:
    shl $18, %edx
    add %ecx, %ecx
    jc n41
n40:
    jnc n49
n41:
    ja n49
n42:
    shl $27, %ebx
    xor %ecx, %edx
    shl $26, %ebx
n45:
    shl $67, %ecx
    shl $248, %eax
n47:
    ja n48
n48:
    shr $159, %eax
n49:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
