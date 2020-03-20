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

    movl	$11482, %eax
    movl	$23712, %ebx
    movl	$-17354, %ecx
    movl	$-6307, %edx

    jz n22
    je n23
    jmp n7
    jmp n9
n7:
    jnc n29
    shl $133, %ebx
n9:
    cmp %ecx, %ebx
    and %edx, %ebx
    shl $234, %ecx
    add %eax, %edx
    xor %eax, %eax
    jno n21
    jno n24
    jnz n31
    and %eax, %ebx
    jc n23
    shr $224, %ecx
    xor %eax, %ecx
n21:
    cmp %eax, %ebx
n22:
    jne n24
n23:
    shr $79, %ecx
n24:
    jne n29
    je n31
    and %ebx, %ecx
    xor %edx, %ecx
    ja n29
n29:
    cmp %edx, %ecx
    add %eax, %ecx
n31:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
