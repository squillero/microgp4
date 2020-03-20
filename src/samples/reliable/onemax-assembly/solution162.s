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

    movl	$6579, %eax
    movl	$15477, %ebx
    movl	$-12321, %ecx
    movl	$12258, %edx

    shl $115, %edx
    jne n29
    jnc n12
    add %edx, %ecx
    sub %eax, %edx
    cmp %eax, %edx
    jo n26
    shr $61, %ebx
    jnc n24
n12:
    cmp %eax, %ebx
    jz n25
    shr $83, %edx
    shl $211, %ecx
    shr $218, %ecx
    jc n25
    xor %eax, %ecx
    jne n29
    shr $33, %eax
    jz n29
    jc n23
n23:
    jmp n29
n24:
    jz n29
n25:
    add %eax, %ecx
n26:
    jmp n29
    shl $33, %ecx
    shl $230, %ecx
n29:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
