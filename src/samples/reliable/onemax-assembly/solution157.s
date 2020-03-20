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

    movl	$-20510, %eax
    movl	$22846, %ebx
    movl	$-11705, %ecx
    movl	$16795, %edx

    shr $83, %edx
    shl $211, %ecx
    shr $218, %ecx
    jc n14
    xor %eax, %ecx
    jne n21
    shr $33, %eax
    jz n18
    jc n12
n12:
    jmp n19
    jz n21
n14:
    add %eax, %ecx
    jmp n22
    shl $33, %ecx
    shl $10, %eax
n18:
    xor %eax, %ecx
n19:
    add %ebx, %eax
    xor %eax, %eax
n21:
    jc n24
n22:
    jne n23
n23:
    xor %ecx, %eax
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
