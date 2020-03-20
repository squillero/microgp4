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

    movl	$-30970, %eax
    movl	$-7435, %ebx
    movl	$-29515, %ecx
    movl	$-22092, %edx

    xor %ebx, %ebx
    shr $105, %ecx
    jnc n22
    ja n7
n7:
    jo n12
    cmp %ebx, %eax
    je n18
    xor %ecx, %ecx
    shl $192, %ecx
n12:
    or %ecx, %ebx
    shl $154, %edx
    shr $3, %ecx
    jno n26
    jmp n26
    and %ecx, %eax
n18:
    jo n20
    shl $141, %ecx
n20:
    jne n23
    cmp %ecx, %ebx
n22:
    sub %ebx, %eax
n23:
    jmp n27
    jc n27
    shr $13, %edx
n26:
    jne n27
n27:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
