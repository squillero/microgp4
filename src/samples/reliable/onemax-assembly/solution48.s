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

    movl	$-15517, %eax
    movl	$15305, %ebx
    movl	$25318, %ecx
    movl	$8298, %edx

    add %eax, %eax
    xor %eax, %edx
    jmp n12
    add %ecx, %edx
    cmp %ebx, %ecx
    shl $114, %ecx
    shr $237, %eax
    shl $186, %eax
    je n31
n12:
    jnz n29
    jnz n28
    sub %ebx, %ebx
    shl $183, %eax
    shr $249, %ebx
    jz n22
    jc n22
    ja n30
    je n29
    jc n28
n22:
    jo n30
    ja n24
n24:
    shl $52, %ecx
    cmp %ecx, %ebx
    or %edx, %ecx
    shr $128, %edx
n28:
    shr $207, %ecx
n29:
    and %edx, %edx
n30:
    jmp n31
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
